from __future__ import annotations

from iron_python_learning_lab.registry import run_stage


def test_stage03_type_system_demo() -> None:
    result = run_stage(3)["result"]

    assert result["protocol_result"] == "send email to dev@example.com"
    assert result["narrowed_upper"] == ["PYTHON", "TYPING"]


def test_stage07_error_context_demo() -> None:
    result = run_stage(7)["result"]

    assert result["cause"] == "ValueError"
    assert result["events"] == ["enter:parse", "error:ValueError", "exit:parse"]


def test_stage10_component_demo() -> None:
    result = run_stage(10)["result"]

    assert result["first"] == "ORD20260911000001"
    assert result["second"] == "ORD20260911000002"
    assert result["same_biz_date"] is True
