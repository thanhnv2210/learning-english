# PEEL Example — Incident Response (short then expanded)

Short reply (use first during an incident)

- Situation: "Payment microservice returned 500 for a subset of requests starting 2026-03-18 09:12 UTC."
- Action: "We rolled back the latest deploy and scaled up the service to relieve pressure."
- Result / Next step: "Error rate dropped to baseline; we are collecting logs for root cause and will post a full update in 60 minutes."

Expanded PEEL (for the post-incident note)

Point

- The rollback resolved the immediate outage; the root cause is a race condition in session cleanup.

Evidence

- Error traces show NPE in `SessionCleaner` (stack trace excerpt) and memory churn in GC logs between 09:10–09:20 UTC.

Example

- Reproduction: workload with many short-lived sessions triggers concurrent cleanup.
- Patch: added a guarded boolean to `SessionCleaner` and added an integration test.

Link / Next step

- Issue: https://your.git/repo/issues/456
- Next step: add a canary deployment for the fix and schedule a retro to improve deploy validation.
