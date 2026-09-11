from __future__ import annotations

from dataclasses import dataclass
from datetime import UTC, datetime
from typing import Protocol


class Clock(Protocol):
    def now(self) -> datetime:
        ...


class SequenceRepository(Protocol):
    def next_sequence(self, biz_date: str) -> int:
        ...


class SystemClock:
    def now(self) -> datetime:
        return datetime.now(UTC)


class FixedClock:
    def __init__(self, value: datetime) -> None:
        self.value = value

    def now(self) -> datetime:
        return self.value


class InMemorySequenceRepository:
    def __init__(self) -> None:
        self._sequences: dict[str, int] = {}

    def next_sequence(self, biz_date: str) -> int:
        next_value = self._sequences.get(biz_date, 0) + 1
        self._sequences[biz_date] = next_value
        return next_value


@dataclass(frozen=True)
class OrderNumber:
    value: str
    biz_date: str
    sequence: int


class OrderNumberService:
    def __init__(self, clock: Clock, repository: SequenceRepository) -> None:
        self.clock = clock
        self.repository = repository

    def generate(self) -> OrderNumber:
        biz_date = self.clock.now().strftime("%Y%m%d")
        sequence = self.repository.next_sequence(biz_date)
        return OrderNumber(
            value=f"ORD{biz_date}{sequence:06d}",
            biz_date=biz_date,
            sequence=sequence,
        )


def demo() -> dict[str, object]:
    service = OrderNumberService(
        FixedClock(datetime(2026, 9, 11, tzinfo=UTC)),
        InMemorySequenceRepository(),
    )
    first = service.generate()
    second = service.generate()

    return {
        "first": first.value,
        "second": second.value,
        "same_biz_date": first.biz_date == second.biz_date,
    }
