import collections
import logging
import unittest
from itertools import count
from re import Pattern
from typing import Any, Callable, Generator, Generic, Iterator, Mapping, Match, TypeVar
from unittest.mock import Mock
from xmlrpc import client as xmlrpclib

import requests
from odoo.addons.base.models.res_users import Users
from websocket import WebSocket

from ..api import Environment
from ..http import OpenERPSession
from ..models import BaseModel
from ..modules.registry import Registry
from ..sql_db import BaseCursor, Cursor
from ..tools import profiler
from ..tools.profiler import Profiler

_T = TypeVar("_T")
_CallableT = TypeVar("_CallableT", bound=Callable)
_ModelT = TypeVar("_ModelT", bound=BaseModel)
_FormT = TypeVar("_FormT", bound=Form)

ADDONS_PATH: str
HOST: str
ADMIN_USER_ID: int

def get_db_name() -> str: ...

standalone_tests: collections.defaultdict[str, list]

def standalone(*tags: str) -> Callable[[_CallableT], _CallableT]: ...

DB: str

def new_test_user(
    env: Environment,
    login: str = ...,
    groups: str = ...,
    context: dict | None = ...,
    **kwargs
) -> Users: ...

class RecordCapturer:
    def __init__(self, model: BaseModel, domain: list) -> None: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, exc_type, exc_value, exc_traceback) -> None: ...
    @property
    def records(self) -> BaseModel: ...

class OdooSuite(unittest.suite.TestSuite):
    def __init__(self, *args, **kwargs) -> None: ...

class MetaCase(type):
    def __init__(cls, name, bases, attrs) -> None: ...

class BaseCase(unittest.TestCase, metaclass=MetaCase):
    tearDown_exceptions: list
    registry: Registry
    env: Environment
    cr: Cursor
    @classmethod
    def addClassCleanup(cls, function, *args, **kwargs) -> None: ...
    @classmethod
    def doClassCleanups(cls) -> None: ...
    longMessage: bool
    warm: bool
    def __init__(self, methodName: str = ...) -> None: ...
    def shortDescription(self) -> None: ...
    def cursor(self) -> Cursor: ...
    @property
    def uid(self) -> int: ...
    @uid.setter
    def uid(self, user) -> None: ...
    def ref(self, xid: str) -> int: ...
    def browse_ref(self, xid: str) -> BaseModel | None: ...
    def patch(self, obj, key, val) -> None: ...
    def with_user(self, login: str) -> None: ...
    def assertRaises(
        self, exception, func: Any | None = ..., *args, **kwargs
    ) -> Generator[Any, None, None] | None: ...
    def assertQueries(
        self, expected, flush: bool = ...
    ) -> Generator[list, None, None]: ...
    def assertQueryCount(
        self, default: int = ..., flush: bool = ..., **counters
    ) -> Generator[None, None, None]: ...
    def assertRecordValues(
        self, records: BaseModel, expected_values: list[dict[str, Any]]
    ) -> None: ...
    def assertItemsEqual(self, a, b, msg: str | None = ...) -> None: ...
    def assertTreesEqual(self, n1, n2, msg: str | None = ...) -> None: ...
    def assertXMLEqual(self, original: str, expected: str) -> None: ...
    def assertHTMLEqual(self, original: str, expected: str) -> None: ...
    profile_session: str
    def profile(self, description: str = ..., **kwargs) -> Profiler: ...
    def patch_requests(self) -> Mock: ...

savepoint_seq: count[int]

class TransactionCase(BaseCase):
    registry: Registry
    env: Environment
    cr: Cursor
    @classmethod
    def setUpClass(cls) -> None: ...
    def setUp(self): ...

class SavepointCase(TransactionCase):
    @classmethod
    def __init_subclass__(cls) -> None: ...

class SingleTransactionCase(BaseCase):
    @classmethod
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def setUpClass(cls) -> None: ...
    def setUp(self) -> None: ...

class ChromeBrowserException(Exception): ...

class ChromeBrowser:
    test_class: str
    devtools_port: int | None
    ws_url: str
    ws: WebSocket | None
    request_id: int
    user_data_dir: str
    chrome_pid: int | None
    screenshots_dir: str
    screencasts_dir: str | None
    screencast_frames: list
    window_size: str
    sigxcpu_handler: Any
    def __init__(
        self, logger: logging.Logger, window_size: str, test_class: str
    ) -> None: ...
    def signal_handler(self, sig, frame) -> None: ...
    def stop(self) -> None: ...
    @property
    def executable(self) -> str | None: ...
    def take_screenshot(self, prefix: str = ..., suffix: str | None = ...) -> None: ...
    screencasts_frames_dir: str
    def start_screencast(self) -> None: ...
    def set_cookie(self, name: str, value, path, domain) -> dict: ...
    def delete_cookie(self, name: str, **kwargs) -> dict: ...
    def navigate_to(self, url: str, wait_stop: bool = ...) -> None: ...
    def clear(self) -> None: ...
    LINE_PATTERN: str
    def console_formatter(self, args: list) -> Callable[[Match[str]], str]: ...

class Opener(requests.Session):
    cr: BaseCursor
    def __init__(self, cr: BaseCursor) -> None: ...
    def request(self, *args, **kwargs): ...

class Transport(xmlrpclib.Transport):
    cr: BaseCursor
    def __init__(self, cr: BaseCursor) -> None: ...
    def request(self, *args, **kwargs): ...

class HttpCase(TransactionCase):
    registry_test_mode: bool
    browser: ChromeBrowser
    browser_size: str
    @classmethod
    def setUpClass(cls) -> None: ...
    xmlrpc_common: xmlrpclib.ServerProxy
    xmlrpc_db: xmlrpclib.ServerProxy
    xmlrpc_object: xmlrpclib.ServerProxy
    opener: Opener
    def setUp(self) -> None: ...
    @classmethod
    def start_browser(cls) -> None: ...
    @classmethod
    def terminate_browser(cls) -> None: ...
    def url_open(
        self,
        url: str,
        data: Any | None = ...,
        files: Mapping | None = ...,
        timeout: int = ...,
        headers: Mapping | None = ...,
        allow_redirects: bool = ...,
        head: bool = ...,
    ) -> requests.Response: ...
    def logout(self, keep_db: bool = ...) -> None: ...
    session: OpenERPSession
    def authenticate(self, user, password) -> OpenERPSession: ...
    def browser_js(
        self,
        url_path: str,
        code: str,
        ready: str = ...,
        login: str | None = ...,
        timeout: int = ...,
        cookies: Any | None = ...,
        **kw
    ) -> None: ...
    @classmethod
    def base_url(cls) -> str: ...
    def start_tour(
        self, url_path: str, tour_name: str, step_delay: float | None = ..., **kwargs
    ) -> None: ...
    def profile(self, **kwargs) -> profiler.Nested: ...

class HttpSavepointCase(HttpCase):
    @classmethod
    def __init_subclass__(cls) -> None: ...

def users(*logins: str) -> Callable[[_CallableT], _CallableT]: ...
def warmup(func: _CallableT, *args, **kwargs) -> _CallableT: ...
def can_import(module: str) -> bool: ...

ref_re: Pattern

class Form(Generic[_ModelT]):
    def __init__(self, recordp: _ModelT, view: _ModelT | str | None = ...) -> None: ...
    def __getattr__(self, field: str): ...
    def __setattr__(self, field: str, value) -> None: ...
    def __enter__(self: _FormT) -> _FormT: ...
    def __exit__(self, etype, _evalue, _etb) -> None: ...
    def save(self) -> _ModelT: ...

class O2MForm(Form):
    def __init__(self, proxy: O2MProxy, index: int | None = ...) -> None: ...
    def save(self) -> None: ...

class UpdateDict(dict):
    def __init__(self, *args, **kwargs) -> None: ...
    def changed_items(self) -> Iterator[tuple[Any, Any]]: ...
    def update(self, *args, **kw) -> None: ...

class X2MProxy: ...

class O2MProxy(X2MProxy):
    def __init__(self, parent: Form, field: str) -> None: ...
    def __len__(self) -> int: ...
    def new(self) -> O2MForm: ...
    def edit(self, index: int): ...
    def remove(self, index: int) -> None: ...

class M2MProxy(X2MProxy, collections.Sequence):
    def __init__(self, parent: Form, field: str) -> None: ...
    def __getitem__(self, it) -> BaseModel: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[BaseModel]: ...
    def __contains__(self, record: BaseModel) -> bool: ...
    def add(self, record: BaseModel) -> None: ...
    def remove(self, id: int | None = ..., index: int | None = ...) -> None: ...
    def clear(self) -> None: ...

def record_to_values(fields: dict, record: BaseModel) -> dict: ...
def tagged(*tags: str) -> Callable[[_CallableT], _CallableT]: ...

class TagsSelector:
    filter_spec_re: Pattern
    exclude: set
    include: set
    def __init__(self, spec: str) -> None: ...
    def check(self, test) -> bool: ...
