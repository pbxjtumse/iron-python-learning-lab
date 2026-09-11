from __future__ import annotations

import pytest

from iron_python_learning_lab.registry import STAGES, get_stage, run_all, run_stage


def test_stage_count() -> None:
    assert len(STAGES) == 10


def test_run_single_stage() -> None:
    result = run_stage(1)

    assert result["stage"] == 1
    assert result["title"] == "basics"
    assert result["result"]["same_value_with_equals"] is True
    assert result["result"]["same_object_with_is"] is False


def test_run_all_stages() -> None:
    result = run_all()

    assert list(result.keys()) == [f"stage_{number:02d}" for number in range(1, 11)]


def test_unknown_stage() -> None:
    with pytest.raises(ValueError):
        get_stage(99)
