# Repository Structure — learning-english

This file documents the recommended folders and where to keep material for learning technical English.

Top-level layout

- /prompts/              — Reusable prompt templates for practicing (chat prompts, role-plays, review prompts).
- /common-issues/        — Common issues Vietnamese techs face (phrases, corrections, examples).
- /special-issues/       — Edge or context-specific issues (eg. customer calls, interviews, system design talks).
- /monthly-notes/        — Monthly result notes and progress summaries (one file per month).
- /daily/                — Daily logs (one file per day; use the daily template in root ReadMe).
- /recordings/           — Short voice recordings (30–90s) for pronunciation and fluency tracking.
- /diagrams/             — PlantUML diagrams and templates illustrating conversational flows, PR process, etc.
- /templates/            — Markdown templates shared across the repo (issue, prompt, monthly note templates)

Guidelines

- Keep each item small and focused: 1 idea per file when possible.
- Name files with date or topic: e.g. `2026-03-20.md`, `pr-explanation-template.md`.
- Prefer versioned examples for prompts: include expected assistant responses and common mistakes.

Quick commands (if PlantUML is available):

- Render all diagrams to PNG (local plantuml):

  plantuml -tpng diagrams/*.puml

- Or using Docker (safe, no install):

  docker run --rm -v $(pwd):/workspace plantuml/plantuml -tpng diagrams/*.puml


