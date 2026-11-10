# /// script
# requires-python = ">=3.11"
# dependencies = [
#     "marimo>=0.25",
#     "pandas>=2.2",
#     "duckdb>=1.1",
# ]
# ///
"""Save the week 10 course default layer as a DuckDB file, for querying it from Claude Code over MCP.

Runs week10_agent.py itself (no copy of its code), so the file always matches what students see:
tables `layer`, `column_info`, `provenance`, `build_log`, and `agent_brief` (the rules the agent follows).

    uv run scripts/build_week10_layer.py            # writes build/week10_layer.duckdb
"""
import importlib.util
import os
import tempfile
from pathlib import Path

import duckdb
import pandas as pd

REPO = Path(__file__).resolve().parents[1]
NOTEBOOK = REPO / "course2027" / "notebooks" / "week10_agent.py"
OUT = REPO / "build" / "week10_layer.duckdb"


def main() -> None:
    # Read the local mirror, and run from a temp folder so the setup cell's ./data cache lands there.
    os.environ.setdefault("COURSE_DATA_LOCAL", str(REPO / "data"))
    spec = importlib.util.spec_from_file_location("week10_agent", NOTEBOOK)
    nb = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(nb)
    cwd = os.getcwd()
    with tempfile.TemporaryDirectory() as tmp:
        os.chdir(tmp)
        try:
            _, defs = nb.app.run()
        finally:
            os.chdir(cwd)

    tables = {
        "layer": defs["layer"],
        "column_info": defs["column_info"],
        "provenance": defs["provenance_table"](),
        "build_log": defs["build_log"],
        "agent_brief": pd.DataFrame({"brief": [defs["agent_brief"]]}),
    }
    OUT.parent.mkdir(exist_ok=True)
    OUT.unlink(missing_ok=True)
    with duckdb.connect(str(OUT)) as con:
        for name, df in tables.items():
            con.register("_df", df)
            con.execute(f'CREATE TABLE "{name}" AS SELECT * FROM _df')
            con.unregister("_df")
            print(f"{name}: {len(df):,} rows")
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    main()
