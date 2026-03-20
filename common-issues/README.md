# Common Issues — frequent problems and patterns

Purpose: a quick catalog of repeated problems Vietnamese engineers encounter and clear corrections.

Structure

- Each file documents one issue (example: `tense-in-commit-messages.md`, `polite-phrases-for-review.md`).
- Include: original example, corrected example, explanation (short), and practice prompt.

Example entry format

Title: Using simple past vs present in commit messages

- Original: "Fix bug that causes crash"
- Better: "Fix bug that caused a crash" or "Fix crash when X happens"
- Why: commit messages usually describe what the change does or what it fixed — choose consistent tense.
- Practice prompt: "Rewrite the commit message for this change: ..."

How to contribute

- Add a new markdown file under this folder for each issue.
- Keep examples minimal and add a quick practice prompt.
