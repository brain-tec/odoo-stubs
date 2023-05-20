from collections.abc import Generator
from logging import Logger
from typing import Any, NamedTuple

STDOUT_LINE: str
STDERR_LINE: str
stats_logger: Logger

class Stat(NamedTuple):
    time: float
    queries: int
    def __add__(self, other: Stat) -> Stat: ...

class OdooTestResult:
    failures_count: int
    errors_count: int
    testsRun: int
    skipped: int
    tb_locals: bool
    time_start: float | None
    queries_start: int | None
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
