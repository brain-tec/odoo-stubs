import unittest
from collections import defaultdict
from logging import Logger
from re import Pattern
from typing import Any, Generator, NamedTuple

stats_logger: Logger

class Stat(NamedTuple):
    time: float
    queries: int
    def __add__(self, other: Stat) -> Stat: ...

_TEST_ID: Pattern

class OdooTestResult(unittest.result.TestResult):
    time_start: float | None
    queries_start: int | None
    _soft_fail: bool
    had_failure: bool
    stats: defaultdict[Any, Stat]
    def __init__(self) -> None: ...
    def __str__(self) -> str: ...
    def soft_fail(self) -> Generator[None, None, None]: ...
    shouldStop: Any
    def update(self, other) -> None: ...
    def log(self, level, msg, *args, test: Any | None = ..., exc_info: Any | None = ..., extra: Any | None = ...,
            stack_info: bool = ..., caller_infos: Any | None = ...) -> None: ...
    def log_stats(self) -> None: ...
    def getDescription(self, test): ...
    def startTest(self, test) -> None: ...
    def stopTest(self, test) -> None: ...
    def collectStats(self, test_id) -> Generator[None, None, None]: ...
    def addError(self, test, err) -> None: ...
    def addFailure(self, test, err) -> None: ...
    def addSubTest(self, test, subtest, err) -> None: ...
    def addSkip(self, test, reason) -> None: ...
    def addUnexpectedSuccess(self, test) -> None: ...
    def logError(self, flavour, test, error) -> None: ...
    def getErrorCallerInfo(self, error, test): ...
