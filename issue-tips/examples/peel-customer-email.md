# PEEL Example — Customer-facing Email

Use a polite tone and reduce technical jargon.

Point

- We identified the cause of the failed transfer and implemented a fix.

Evidence

- The issue occurred when the beneficiary bank returned a malformed routing code; only 0.3% of transactions were affected.

Example

- Example: transaction ID `abc-123` failed with error `INVALID_ROUTING_CODE` on 2026-03-12 14:02 UTC; our fix added validation and a fallback path.

Link / Next step

- We retried affected transactions and notified customers through in-app messages.
- If you still see problems, please reply with the transaction ID and we will investigate immediately.
