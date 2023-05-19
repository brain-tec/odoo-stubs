from collections.abc import Generator
from logging import Logger
from re import Pattern
from typing import Any, NamedTuple

__unittest: bool
STDOUT_LINE: str
STDERR_LINE: str
stats_logger: Logger

class Stat(NamedTuple):
    time: float
    queries: int
    def __add__(self, other: Stat) -> Stat: ...

_TEST_ID: Pattern

class OdooTestResult:
    _previousTestClass: Any
    _moduleSetUpFailed: bool
    failures_count: int
    errors_count: int
    testsRun: int
    skipped: int
    tb_locals: bool
    time_start: float | None
    queries_start: int | None
    _soft_fail: bool
    had_failure: bool
    stats: dict[str, Stat]
    def __init__(
        self,
        stream: Any | None = ...,
        descriptions: Any | None = ...,
        verbosity: Any | None = ...,
    ) -> None: ...
    def printErrors(self) -> None: ...
    def startTest(self, test) -> None: ...
    def stopTest(self, test) -> None: ...
    def addError(self, test, err) -> None: ...
    def addFailure(self, test, err) -> None: ...
    def addSubTest(self, test, subtest, err) -> None: ...
    def addSuccess(self, test) -> None: ...
    def addSkip(self, test, reason) -> None: ...
    def wasSuccessful(self) -> bool: ...
    def _exc_info_to_string(self, err, test) -> str: ...
    def _is_relevant_tb_level(self, tb) -> bool: ...
    def _count_relevant_tb_levels(self, tb) -> int: ...
    def __repr__(self) -> str: ...
    def __str__(self) -> str: ...
    def soft_fail(self) -> Generator[None, None, None]: ...
    def update(self, other) -> None: ...
    def log(
        self,
        level,
        msg,
        *args,
        test: Any | None = ...,
        exc_info: Any | None = ...,
        extra: Any | None = ...,
        stack_info: bool = ...,
        caller_infos: Any | None = ...
    ) -> None: ...
    def log_stats(self) -> None: ...
    def getDescription(self, test) -> str: ...
    def collectStats(self, test_id) -> Generator[None, None, None]: ...
    def logError(self, flavour, test, error) -> None: ...
    def getErrorCallerInfo(self, error, test) -> tuple | None: ...
