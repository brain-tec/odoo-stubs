import datetime
import pickle as pickle_
from collections.abc import Mapping, MutableMapping, MutableSet
from logging import Filter, LogRecord
from types import ModuleType
from typing import (
    IO,
    Any,
    AnyStr,
    Callable,
    Generic,
    ItemsView,
    Iterable,
    Iterator,
    NoReturn,
    TypeVar,
)

import xlsxwriter
import xlwt
from babel.core import Locale
from xlwt import Worksheet

from ..api import Environment
from ..loglevels import exception_to_unicode as exception_to_unicode
from ..loglevels import get_encodings as get_encodings
from ..sql_db import Cursor
from .cache import *
from .parse_version import parse_version as parse_version

_T = TypeVar("_T")
_T1 = TypeVar("_T1")
_KT = TypeVar("_KT")
_VT = TypeVar("_VT")
_CallableT = TypeVar("_CallableT", bound=Callable)

SKIPPED_ELEMENT_TYPES: tuple
NON_BREAKING_SPACE: str

def find_in_path(name: str) -> str: ...
def _exec_pipe(
    prog, args, env: Mapping[str, str] | None = ...
) -> tuple[IO[AnyStr] | None, IO[AnyStr] | None]: ...
def exec_command_pipe(
    name: str, *args
) -> tuple[IO[AnyStr] | None, IO[AnyStr] | None]: ...
def find_pg_tool(name: str) -> str: ...
def exec_pg_environ() -> dict[str, str]: ...
def exec_pg_command(name: str, *args) -> None: ...
def exec_pg_command_pipe(
    name: str, *args
) -> tuple[IO[AnyStr] | None, IO[AnyStr] | None]: ...
def file_open(
    name: str,
    mode: str = ...,
    subdir: str = ...,
    pathinfo: bool = ...,
    filter_ext: Any | None = ...,
): ...
def _fileopen(
    path: str,
    mode: str,
    basedir: str,
    pathinfo,
    basename: str | None = ...,
    filter_ext: Any | None = ...,
): ...
def flatten(list) -> list: ...
def reverse_enumerate(l): ...
def partition(
    pred: Callable[[_T], bool], elems: Iterable[_T]
) -> tuple[list[_T], list[_T]]: ...
def topological_sort(elems: dict[_T, Any]) -> list[_T]: ...
def merge_sequences(*iterables: Iterable[_T]) -> list[_T]: ...

class PatchedWorkbook(xlwt.Workbook):
    def add_sheet(self, name: str, cell_overwrite_ok: bool = ...) -> Worksheet: ...

class PatchedXlsxWorkbook(xlsxwriter.Workbook):
    def add_worksheet(self, name: str | None = ..., **kw) -> Worksheet: ...

def to_xml(s: str) -> str: ...
def get_iso_codes(lang: str) -> str: ...
def scan_languages() -> list[tuple[str, str]]: ...
def mod10r(number: str) -> str: ...
def str2bool(s: str, default: Any | None = ...) -> bool: ...
def human_size(sz) -> str: ...
def logged(f: _CallableT) -> _CallableT: ...

class profile:
    fname: str | None
    def __init__(self, fname: str | None = ...) -> None: ...
    def __call__(self, f: _CallableT) -> _CallableT: ...

def detect_ip_addr() -> str: ...

DEFAULT_SERVER_DATE_FORMAT: str
DEFAULT_SERVER_TIME_FORMAT: str
DEFAULT_SERVER_DATETIME_FORMAT: str
DATE_LENGTH: int
DATETIME_FORMATS_MAP: dict[str, str]
POSIX_TO_LDML: dict[str, str]

def posix_to_ldml(fmt: str, locale: Locale) -> str: ...
def split_every(
    n: int, iterable: Iterable[_T], piece_maker: Callable[[Iterable[_T]], _T1] = ...
) -> Iterator[_T1]: ...
def get_and_group_by_field(
    cr: Cursor, uid: int, obj, ids, field: str, context: dict | None = ...
) -> dict: ...
def get_and_group_by_company(
    cr: Cursor, uid: int, obj, ids, context: dict | None = ...
) -> dict: ...
def resolve_attr(obj, attr: str): ...
def attrgetter(*items): ...
def remove_accents(input_str: str) -> str: ...

class unquote(str):
    def __repr__(self) -> str: ...

class UnquoteEvalContext(defaultdict):
    def __init__(self, *args, **kwargs) -> None: ...
    def __missing__(self, key) -> unquote: ...

class mute_logger(Filter):
    loggers: tuple[str]
    def __init__(self, *loggers: str) -> None: ...
    def filter(self, record: LogRecord) -> int: ...
    def __enter__(self) -> None: ...
    def __exit__(
        self,
        exc_type: Any | None = ...,
        exc_val: Any | None = ...,
        exc_tb: Any | None = ...,
    ) -> None: ...
    def __call__(self, func: _CallableT) -> _CallableT: ...

_ph: Any

class CountingStream(Generic[_T]):
    stream: Iterator[_T]
    index: int
    stopped: bool
    def __init__(self, stream: Iterable[_T], start: int = ...) -> None: ...
    def __iter__(self) -> CountingStream[_T]: ...
    def next(self) -> _T: ...
    __next__ = next

def stripped_sys_argv(*strip_args: str) -> list[str]: ...

class ConstantMapping(Mapping[_KT, _VT]):
    _value: _VT
    def __init__(self, val: _VT) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator: ...
    def __getitem__(self, item) -> _VT: ...

def dumpstacks(
    sig: Any | None = ..., frame: Any | None = ..., thread_idents: Any | None = ...
) -> None: ...
def freehash(arg) -> int: ...
def clean_context(context: dict[str, Any]) -> dict[str, Any]: ...

class frozendict(dict):
    def __delitem__(self, key) -> NoReturn: ...
    def __setitem__(self, key, val) -> NoReturn: ...
    def clear(self) -> NoReturn: ...
    def pop(self, key, default: Any | None = ...) -> NoReturn: ...
    def popitem(self) -> NoReturn: ...
    def setdefault(self, key, default: Any | None = ...) -> NoReturn: ...
    def update(self, *args, **kwargs) -> NoReturn: ...
    def __hash__(self) -> int: ...

class Collector(Mapping[_KT, _VT]):
    _map: dict
    def __init__(self) -> None: ...
    def add(self, key: _KT, val: _T) -> None: ...
    def __getitem__(self, key: _KT) -> tuple[_T]: ...
    def __iter__(self) -> Iterator[_KT]: ...
    def __len__(self) -> int: ...

class StackMap(MutableMapping):
    _maps: list[MutableMapping]
    def __init__(self, m: MutableMapping | None = ...) -> None: ...
    def __getitem__(self, key): ...
    def __setitem__(self, key, val) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def __str__(self) -> str: ...
    def pushmap(self, m: MutableMapping | None = ...) -> None: ...
    def popmap(self) -> MutableMapping: ...

class OrderedSet(MutableSet):
    _map: dict
    def __init__(self, elems: Iterable = ...) -> None: ...
    def __contains__(self, elem) -> bool: ...
    def __iter__(self) -> Iterator: ...
    def __len__(self) -> int: ...
    def add(self, elem) -> None: ...
    def discard(self, elem) -> None: ...

class LastOrderedSet(OrderedSet):
    def add(self, elem) -> None: ...

class IterableGenerator(Generic[_T]):
    func: Callable
    args: tuple
    def __init__(self, func: Callable[..., _T], *args) -> None: ...
    def __iter__(self) -> _T: ...

def groupby(
    iterable: Iterable[_T], key: Callable[..., _T1] | None = ...
) -> ItemsView[_T1, _T]: ...
def unique(it: Iterable[_T]) -> Iterator[_T]: ...

class Reverse:
    val: Any
    def __init__(self, val) -> None: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...

def ignore(*exc) -> None: ...
def html_escape(text: str) -> str: ...
def get_lang(env: Environment, lang_code: str = ...) -> "odoo.model.res_lang": ...
def babel_locale_parse(lang_code: str) -> Locale: ...
def formatLang(
    env: Environment,
    value,
    digits: int | None = ...,
    grouping: bool = ...,
    monetary: bool = ...,
    dp: bool = ...,
    currency_obj: "odoo.model.res_currency" = ...,
) -> str: ...
def format_date(
    env: Environment,
    value: datetime.date | datetime.datetime | str,
    lang_code: str = ...,
    date_format: str = ...,
) -> str: ...
def parse_date(env: Environment, value: str, lang_code: str = ...) -> datetime.date: ...
def format_datetime(
    env: Environment,
    value: str | datetime.datetime,
    tz: str = ...,
    dt_format: str = ...,
    lang_code: str = ...,
) -> str: ...
def format_time(
    env: Environment, value, tz: str = ..., time_format: str = ..., lang_code: str = ...
) -> str: ...
def _format_time_ago(
    env: Environment,
    time_delta: datetime.timedelta | int,
    lang_code: str = ...,
    add_direction: bool = ...,
) -> str: ...
def format_amount(
    env: Environment,
    amount: float,
    currency: "odoo.model.res_currency",
    lang_code: str = ...,
) -> str: ...
def format_duration(value: float) -> str: ...
def _consteq(str1: str, str2: str) -> bool: ...

consteq: Callable[[str, str], bool]

class Unpickler(pickle_.Unpickler):
    find_global: Any
    find_class: Any

def _pickle_load(
    stream: pickle_._ReadableFileobj, encoding: str = ..., errors: bool = ...
): ...

pickle: ModuleType

def wrap_values(d): ...

_missing: object
_cache: dict

def wrap_module(module, attr_list): ...

mods: list[str]
attribs: list

class DotDict(dict):
    def __getattr__(self, attrib): ...

def traverse_containers(val, type_) -> Iterator: ...
