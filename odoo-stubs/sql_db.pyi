from datetime import datetime
from re import Pattern
from threading import Lock, RLock
from typing import Any, Callable, Generator, Iterable, Iterator, Literal, NoReturn, Sequence, TypeVar

import psycopg2.extensions
from decorator import decorator

from .api import Transaction
from .tools import Callbacks

_T = TypeVar('_T')
_CursorT = TypeVar('_CursorT', bound=Cursor)

real_time: Callable

def unbuffer(symb, cr: BaseCursor) -> str | None: ...
def undecimalize(symb, cr: BaseCursor) -> float | None: ...
def adapt_string(adapted: str) -> psycopg2.extensions.QuotedString: ...
def flush_env(cr: BaseCursor, *, clear: bool = ...) -> None: ...
def clear_env(cr: BaseCursor) -> None: ...

re_from: Pattern
re_into: Pattern
sql_counter: int

@decorator
def check(f: Callable[..., _T], self: Cursor, *args, **kwargs) -> _T: ...

class BaseCursor:
    precommit: Callbacks
    postcommit: Callbacks
    prerollback: Callbacks
    postrollback: Callbacks
    transaction: Transaction | None
    def __init__(self) -> None: ...
    def execute(self, query, *args, **kwargs): ...
    def commit(self): ...
    def rollback(self): ...
    def close(self): ...
    def flush(self) -> None: ...
    def clear(self) -> None: ...
    def reset(self) -> None: ...
    def savepoint(self, flush: bool = ...) -> Generator[None, None, None]: ...
    def __enter__(self: _CursorT) -> _CursorT: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class Cursor(BaseCursor):
    IN_MAX: int
    sql_from_log: dict
    sql_into_log: dict
    sql_log: bool
    sql_log_count: int
    _closed: bool
    __pool: ConnectionPool
    dbname: str
    _serialized: bool
    _cnx: PsycoConnection
    _obj: psycopg2.extensions.cursor
    __caller: tuple[str, int | str] | Literal[False]
    _default_log_exceptions: bool
    cache: dict
    _now: datetime | None
    def __init__(self, pool: ConnectionPool, dbname: str, dsn: dict, serialized: bool = ...) -> None: ...
    def __build_dict(self, row: Sequence) -> dict[str, Any]: ...
    def dictfetchone(self) -> dict[str, Any] | None: ...
    def dictfetchmany(self, size) -> list[dict[str, Any]]: ...
    def dictfetchall(self) -> list[dict[str, Any]]: ...
    def __del__(self) -> None: ...
    def _format(self, query, params: Any | None = ...): ...
    def execute(self, query, params: Any | None = ..., log_exceptions: Any | None = ...): ...
    def split_for_in_conditions(self, ids: Iterable, size: int | None = ...) -> Iterator[tuple]: ...
    def print_log(self): ...
    def close(self): ...
    def _close(self, leak: bool = ...) -> None: ...
    def autocommit(self, on: bool) -> None: ...
    def after(self, event: str, func: Callable) -> None: ...
    def commit(self): ...
    def rollback(self): ...
    def __getattr__(self, name: str): ...
    @property
    def closed(self) -> bool: ...
    def now(self) -> datetime: ...

class TestCursor(BaseCursor):
    _savepoint_seq: Iterator[int]
    _closed: bool
    _cursor: Cursor
    _lock: RLock
    _savepoint: str
    def __init__(self, cursor: Cursor, lock: RLock) -> None: ...
    def close(self) -> None: ...
    def autocommit(self, on: bool) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def __getattr__(self, name: str): ...

class PsycoConnection(psycopg2.extensions.connection): ...

class ConnectionPool:
    def locked(fun: Callable[..., _T]) -> Callable[..., _T]: ...
    _connections: list[tuple[psycopg2.extensions.connection, bool]]
    _maxconn: int
    _lock: Lock
    def __init__(self, maxconn: int = ...) -> None: ...
    def __repr__(self) -> str: ...
    def _debug(self, msg, *args) -> None: ...
    def borrow(self, connection_info: dict) -> PsycoConnection: ...
    def give_back(self, connection: PsycoConnection, keep_in_pool: bool = ...) -> None: ...
    def close_all(self, dsn: dict | None = ...) -> None: ...
    def _dsn_equals(self, dsn1, dsn2) -> bool: ...
    def _dsn_to_dict(self, dsn) -> dict: ...

class Connection:
    __dbname: str
    __dsn: dict
    __pool: ConnectionPool
    def __init__(self, pool: ConnectionPool, dbname: str, dsn: dict) -> None: ...
    @property
    def dsn(self) -> dict: ...
    @property
    def dbname(self) -> str: ...
    def cursor(self, serialized: bool = ...) -> Cursor: ...
    serialized_cursor = cursor
    def __bool__(self) -> NoReturn: ...

def connection_info_for(db_or_uri: str) -> tuple[str, dict]: ...

_Pool: ConnectionPool | None

def db_connect(to: str, allow_uri: bool = ...) -> Connection: ...
def close_db(db_name: str) -> None: ...
def close_all() -> None: ...
