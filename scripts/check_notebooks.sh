#!/usr/bin/env bash
# Lint and run every DATA 6900 marimo notebook headlessly, the way a student would open it.
# Usage: scripts/check_notebooks.sh [notebook.py ...]   (default: every notebook under course2027/notebooks)
# Uses the local mirror in ./data and Python 3.13 unless COURSE_DATA_LOCAL / UV_PYTHON are already set.
set -uo pipefail
cd "$(dirname "$0")/.."
export COURSE_DATA_LOCAL="${COURSE_DATA_LOCAL:-$PWD/data}"
export UV_PYTHON="${UV_PYTHON:-3.13}"

if [ $# -gt 0 ]; then
  files=("$@")
else
  files=()
  while IFS= read -r f; do files+=("$f"); done < <(
    find course2027/notebooks -name '*.py' -not -path '*/__marimo__/*' -not -name '_setup_cell.py' | sort)
fi

echo "== marimo check (${#files[@]} notebooks)"
marimo check "${files[@]}" || lint_failed=1

echo "== running each notebook (data: $COURSE_DATA_LOCAL, python: $UV_PYTHON)"
# Run from a throwaway copy: exporting rewrites the committed __marimo__/session snapshots
# next to each notebook, and the setup cell caches downloads in ./data of the working directory.
out="$(mktemp -d)"
repo="$PWD"
cd "$out"
failed=()
for f in "${files[@]}"; do
  mkdir -p "$(dirname "$f")" && cp "$repo/$f" "$f"
  if marimo export html --sandbox "$f" -o "$out/$(basename "$f" .py).html" >"$out/log" 2>&1; then
    echo "  ok    $f"
  else
    echo "  FAIL  $f"; tail -15 "$out/log" | sed 's/^/        /'
    failed+=("$f")
  fi
done
cd "$repo"
rm -rf "$out"

echo
if [ ${#failed[@]} -gt 0 ] || [ -n "${lint_failed:-}" ]; then
  echo "${#failed[@]} notebook(s) failed to run${lint_failed:+; marimo check reported problems}"
  exit 1
fi
echo "All ${#files[@]} notebooks passed."
