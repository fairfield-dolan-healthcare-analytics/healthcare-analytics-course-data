# Week 13: Mock hand-off

**No notebook this week:** [hand-off template](../templates/handoff.md) · [Course home](../README.md)

## Why this week matters

An app that only its builder can use isn't finished. Suppose you've built a readmissions dashboard for a clinic. The day you hand it over, someone else has to read it correctly, know what it can't answer, and keep it current when CMS posts a new release, without calling you. Most analytics work that fails in practice fails here: the numbers were right, but nobody else knew how to use them, refresh them, or tell when they had gone stale.

## The idea

A **hand-off package** is everything the person taking over needs, and nothing they don't:

1. **The app**, as a link that opens.
2. **How to use it**: who it's for, the one question it answers, how to read the main screen, and what it can't answer.
3. **The run-book**: where each number comes from, when each source updates, how to refresh, which checks to rerun, and what to do if one fails.
4. **Who owns what** after you leave: refreshing, checking, approving, and the known issues.

You've already written most of it this term. Your data card, compliance checklist, week 12 change report and test questions are the raw material.

## In class

- Show and explain: four or five of you show your week 12 change report.
- You're paired with a classmate who plays your **client**, for example a clinic operations manager, a health department program lead, or a hospital quality director. You play theirs.
- **Cold start (10 minutes):** your client opens your app with only your package in hand and tries to answer its one question. You stay silent. They log every question they would have had to ask you.
- **Hand-off meeting (10 minutes):** go through the log together. Then swap roles.

## Your one required deliverable

1. Your **hand-off package**, sections 1–3 of the [hand-off template](../templates/handoff.md) (the app, what it can't tell you, how to keep it current). Section 4, who owns what, is optional.
2. The **hand-off log** you kept as your partner's client (section 5 of the template, filled in for their app).

## Steps

1. Copy the [hand-off template](../templates/handoff.md) and fill in sections 1–3 for your own app before class (section 4 is optional). Reuse your data card ("Not for"), your week 12 refresh notes, your compliance checklist and your test questions. Don't rewrite them.
2. Ask your AI tool to find the gaps, but decide yourself what goes in:
   > Here is my hand-off package for a healthcare data app: [paste]. Read it as a clinic manager who has never seen the app and can't call me. List every question you would still need answered. Don't rewrite the package.
3. In class, run the cold start and the meeting, then swap.
4. After class, fix the **top two** problems your client hit, before the week 14 showcase. Note what you changed.

## The check to run before you submit

Hand your package to someone who has never seen your app, with no explanation. Can they open the link, answer the app's one question, and say what it **can't** tell them? If they can't, the package isn't done.

## Human sign-off

- What I checked myself:
- What I'm trusting the AI on:
- What I won't sign:

## Power-ups (optional)

- Write the refresh steps so plainly that your client could run them without you, then have them try.
- Add a "data as of" line and a "next refresh due" date to your app's provenance panel.

## Reading

None this week.
