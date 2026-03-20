# Collocation Dictionary — quick lookup for natural phrases

Purpose

This folder stores collocations and short phrase cards that help Vietnamese tech professionals use natural English in speaking and writing without translating word-by-word.

How to use

- Look up a headword (e.g., "deploy", "optimize", "fix") and find common collocations and example sentences.
- Use examples in PRs, standups, and explanations. Practice speaking them aloud or recording short clips referencing the example sentences.
- Add new collocations using the `TEMPLATE.md` format and update `data.json` if you use the CLI.

Structure

- `TEMPLATE.md` — fields for adding a new collocation entry
- `common-collocations.md` — curated examples grouped by topic
- `speaking-use-cards.md` — short cues to practice in speaking drills
- `data.json` — machine-readable seed data for local search (edit carefully)
- `search.py` — small Python CLI to search collocations quickly

Guidelines for contributions

- Keep each entry focused: one collocation + 1–2 example sentences.
- Add tags for quick filtering: `#api`, `#deploy`, `#performance`, `#customer`, `#writing`, `#speaking`.
- Prefer natural, simple sentences and note register when needed (formal/informal).

Examples and quick workflow

1. During a standup, search for the verb you want (e.g., "optimize").
2. Pick a collocation like "optimize performance" and a prepared sentence: "We optimized DB queries to reduce latency by 25%."
3. Use it in your standup or PR; record yourself saying it, then save the recording under `/recordings/` and link it in your daily log.

