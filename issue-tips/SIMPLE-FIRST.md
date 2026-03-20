# SIMPLE-FIRST — Minimal rapid-response template

Use this when you need to respond fast (chat, Slack, on-call).

Template (3 lines):
1. Situation (1 short sentence): what happened / what you changed.
2. Action (1 short sentence): what you did or will do.
3. Result / Next step (1 short sentence): outcome or what you need from the reader.

Example — PR quick reply:
- Situation: "I noticed the API client throws an NPE when header `X` is missing."
- Action: "I added a null-check and improved the test coverage."
- Result / Next step: "Please re-run the failing test and let me know if you still see it."

Why it works

- Short structure forces clarity.
- Good for chat where readers prefer brief and actionable lines.
