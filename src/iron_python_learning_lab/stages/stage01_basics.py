from __future__ import annotations


def normalize_status(raw_status: str) -> str:
    status = raw_status.strip().lower()
    if status in {"ok", "success"}:
        return "SUCCESS"
    if status in {"fail", "failed", "error"}:
        return "FAILED"
    return "UNKNOWN"


def divide(left: int, right: int) -> float:
    try:
        return left / right
    except ZeroDivisionError as exc:
        raise ValueError("right must not be zero") from exc


def demo() -> dict[str, object]:
    left = ["order-1"]
    right = ["order-1"]

    try:
        divide(10, 0)
    except ValueError as exc:
        wrapped_error = str(exc)
        cause = type(exc.__cause__).__name__ if exc.__cause__ else None

    return {
        "same_value_with_equals": left == right,
        "same_object_with_is": left is right,
        "normalized_statuses": [normalize_status(item) for item in [" ok ", "FAILED", "missing"]],
        "wrapped_error": wrapped_error,
        "cause": cause,
    }
