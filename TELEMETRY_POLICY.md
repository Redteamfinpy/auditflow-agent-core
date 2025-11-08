# Telemetry Policy

AuditFlow collects telemetry data only when you explicitly opt-in using the `--opt-in true` flag.

## What We Collect

- Sanitized failure trace logs (e.g., document ID, risk score, error type).
- No sensitive data such as file contents or personal information.

## Why We Collect It

To improve the agent by analyzing common failures and enhancing audit accuracy.

## Opt-Out

Simply use `--opt-in false` or omit the flag. No data is sent without your consent.
