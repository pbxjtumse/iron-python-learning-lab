from __future__ import annotations

import argparse
from pprint import pprint

from iron_python_learning_lab.registry import run_all, run_stage


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="iron-python-learning-lab",
        description="Run Python learning stage demos.",
    )
    parser.add_argument(
        "stage",
        nargs="?",
        help="Stage number from 1 to 10. Omit it to run all stages.",
    )
    args = parser.parse_args(argv)

    if args.stage is None or args.stage == "all":
        pprint(run_all(), sort_dicts=False)
        return 0

    try:
        stage_number = int(args.stage)
    except ValueError:
        parser.error("stage must be a number from 1 to 10, or 'all'")
        return 2

    pprint(run_stage(stage_number), sort_dicts=False)
    return 0
