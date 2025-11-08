import json
from typing import Any


def send_trace_log(trace_data: dict[str, Any], config_opt_in: bool) -> None:
    """
    Send trace log for telemetry.
    If opt_in is False, log a simple message.
    If True, print sanitized JSON trace (placeholder for server send).
    """
    if not config_opt_in:
        print("Telemetry disabled. Trace log not sent.")
        return

    # Placeholder: Strip sensitive data (e.g., remove user-specific info)
    sanitized_trace = {
        "document_id": trace_data.get("document_id", "unknown"),
        "risk_score": trace_data.get("risk_score", 0),
        "error_type": trace_data.get("error_type", "none"),
        # Add more sanitized fields as needed
    }

    # NOTE: In a real app, this is sent to the server
    print("Sending sanitized trace to server:", json.dumps(sanitized_trace, indent=2))
