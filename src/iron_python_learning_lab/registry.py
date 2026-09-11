from __future__ import annotations

from dataclasses import dataclass
from importlib import import_module
from typing import Any


@dataclass(frozen=True)
class StageInfo:
    number: int
    title: str
    java_compare: str
    module_name: str


STAGES: tuple[StageInfo, ...] = (
    StageInfo(1, "basics", "syntax, utility class, checked exception", "stage01_basics"),
    StageInfo(2, "object model", "reference variable, String, shallow copy", "stage02_object_model"),
    StageInfo(3, "type system", "interface, abstract class, generic, annotation", "stage03_type_system"),
    StageInfo(4, "functions and modules", "method, overload, Maven module", "stage04_functions_modules"),
    StageInfo(5, "OOP and dataclass", "POJO, record, Lombok, Spring DI", "stage05_oop_dataclass"),
    StageInfo(6, "collections and iterators", "Collections, Iterator, Stream", "stage06_collections_iterators"),
    StageInfo(7, "errors and context managers", "try/catch, try-with-resources", "stage07_errors_context"),
    StageInfo(8, "I/O and JSON", "Path, Jackson, configuration class", "stage08_io_json"),
    StageInfo(9, "async concurrency", "thread pool, CompletableFuture", "stage09_async_concurrency"),
    StageInfo(10, "mini component", "API/SPI/Core/Provider", "stage10_mini_component"),
)


def get_stage(number: int) -> StageInfo:
    for stage in STAGES:
        if stage.number == number:
            return stage
    raise ValueError(f"unknown stage: {number}")


def run_stage(number: int) -> dict[str, Any]:
    stage = get_stage(number)
    module = import_module(f"iron_python_learning_lab.stages.{stage.module_name}")
    result = module.demo()
    return {
        "stage": stage.number,
        "title": stage.title,
        "java_compare": stage.java_compare,
        "result": result,
    }


def run_all() -> dict[str, dict[str, Any]]:
    return {f"stage_{stage.number:02d}": run_stage(stage.number) for stage in STAGES}
