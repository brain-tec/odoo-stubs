from collections.abc import Generator
from typing import Any
from unittest import TestCase as _TestCase

__unittest: bool
_subtest_msg_sentinel: object

class _Outcome:
    result: Any
    success: bool
    test: Any
    def __init__(self, test, result) -> None: ...
    def testPartExecutor(self, test_case, isTest: bool = ...) -> Generator[None, None, None]: ...
    def _complete_traceback(self, initial_tb): ...
    
class TestCase(_TestCase):
    _class_cleanups: list
    __unittest_skip__: bool
    __unittest_skip_why__: str
    _moduleSetUpFailed: bool
    _testMethodName: str
    _outcome: Any
    _cleanups: list
    _subtest: Any
    _type_equality_funcs: dict
    def __init__(self, methodName: str = ...) -> None: ...
    def addCleanup(self, function, *args, **kwargs) -> None: ...
    @classmethod
    def addClassCleanup(cls, function, *args, **kwargs) -> None: ...
    def shortDescription(self) -> None: ...
    def subTest(self, msg=..., **params) -> Generator[None, None, None]: ...
    def _addError(self, result, test, exc_info) -> None: ...
    def _callSetUp(self) -> None: ...
    def _callTestMethod(self, method) -> None: ...
    def _callTearDown(self) -> None: ...
    def _callCleanup(self, function, *args, **kwargs) -> None: ...
    def run(self, result): ...
    def doCleanups(self) -> None: ...
    @classmethod
    def doClassCleanups(cls) -> None: ...

class _SubTest(TestCase):
    _message: Any
    test_case: Any
    params: Any
    failureException: Any
    def __init__(self, test_case, message, params) -> None: ...
    def runTest(self) -> None: ...
    def _subDescription(self) -> str: ...
    def id(self) -> str: ...
    def __str__(self) -> str: ...
