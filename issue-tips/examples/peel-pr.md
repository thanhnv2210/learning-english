# PEEL Example — PR Explanation

Context: Use this to write the PR description or an explanation in a review.

Point

- Fixes a race condition in `CacheManager` that caused stale reads under high load.

Evidence

- Observed failure rates increased by 12% in `service-A` on 2026-03-10 (see Sentry: event IDs ...).
- Unit tests `CacheManagerTest#concurrentAccess` previously flaked.

Example

- Reproduction steps: run `./gradlew :service-A:test --tests CacheManagerTest#concurrentAccess` with 8 parallel workers.
- Code change: added synchronized block and replaced lazy-init with double-checked locking.

Link / Next step

- PR: https://your.git/repo/pull/123 — please review the synchronized block and suggest improvements.
- Deploy plan: canary to 10% for 24h, monitor error-rate and latency.
