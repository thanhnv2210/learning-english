# English for Vietnamese Tech Professionals — Learning & Recording Log

## Purpose
This repository helps Vietnamese engineers improve technical English by practicing, recording progress, and building reusable templates for real-world developer communication (PRs, standups, design discussions).

## Who this is for
- Vietnamese developers comfortable with code and logic.
- People who want practical, work-focused English: clear PR descriptions, concise standups, better code review comments, and confident spoken explanations.

## How to use
- Keep daily notes in `/daily/` using the Daily Log template located at `/templates/daily-template.md`.
- Add weekly summaries in `/weekly/` (create this folder if you need it).
- Save short voice recordings (30–90s) in `/recordings/` to track pronunciation and fluency.
- Store reusable prompts in `/prompts/` and common language problems in `/common-issues/` or `/special-issues/`.
- Keep PlantUML diagrams in `/diagrams/` to model conversational flows and PR structures.
- Open a PR when you add logs so teammates can give feedback.

## Repository structure (recommended)
- `prompts/` — Practice prompts and templates (chat prompts, role-plays).
- `common-issues/` — Frequent mistakes with examples and corrections.
- `special-issues/` — High-stakes or context-specific scripts (customer calls, interviews).
- `daily/` — Daily logs.
- `weekly/` — Weekly summaries.
- `monthly-notes/` — Monthly results and reflections (one file per month).
- `recordings/` — Short audio practice files.
- `diagrams/` — PlantUML files for conversational flows and PR explanations.
- `templates/` — Reusable Markdown and PlantUML templates.

(See `structure.md` for more detail.)

## Quick start
1. Copy `/templates/daily-template.md` to `daily/YYYY-MM-DD.md` and fill it after each practice session.
2. Pick a prompt from `/prompts/` and either role-play with a partner or paste it into a chat assistant.
3. Record a short voice note and drop it into `/recordings/`; link it from your daily log.
4. At the end of the month, create `monthly-notes/YYYY-MM.md` and summarize progress.

## PlantUML usage
- Keep `.puml` files in `/diagrams/`.
- Render locally (if you have plantuml installed):

  plantuml -tpng diagrams/*.puml

- Or using Docker:

  docker run --rm -v $(pwd):/workspace plantuml/plantuml -tpng diagrams/*.puml

- Include diagrams in Markdown by linking the generated PNGs, or use a PlantUML plugin in your editor.

## Templates and examples
- Daily template: `/templates/daily-template.md`
- Monthly template: `/templates/monthly-template.md` (create if you want a custom one)
- PR explanation prompt: see `/prompts/PROMPT_TEMPLATES.md`
- Conversation flow example: `/diagrams/conversation-flow.puml`

## Practical exercises
- Explain a recent PR in 3 sentences: Context → Change → Result.
- Write a PR description using the template: Motivation, What changed, How to test.
- Record a 60s explanation of a bug fix and compare pronunciation weekly.

## Contributing
- Add logs, prompts, or issues as small, focused files and open a PR.
- Tag files with `#speaking`, `#writing`, `#pr`, etc. for quick filtering.
- Give kind, actionable feedback on PRs; focus on 2–3 improvements per review.

## Resources
- Short technical talks (YouTube)
- Documentation writing guides
- Pronunciation apps and simple podcasts for devs


## License
This material is available under `MIT` — reuse and adapt for personal learning.