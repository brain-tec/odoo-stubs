from datetime import datetime
from re import Pattern
from threading import RLock
from typing import Any, Callable, Iterable, Iterator, NoReturn, TypeVar

import psycopg2.extensions

from .api import Transaction
from .tools import Callbacks

_T = TypeVar("_T")
_CursorT = TypeVar("_CursorT", bound=Cursor)
_SavepointT = TypeVar("_SavepointT", bound=Savepoint)

def undecimalize(symb, cr: Cursor) -> float | None: ...

DECIMAL_TO_FLOAT_TYPE: Any
real_time: Callable
re_from: Pattern
re_into: Pattern

def categorize_query(decoded_query: str) -> tuple[str, Any]: ...

sql_counter: int
MAX_IDLE_TIMEOUT: int

class Savepoint:
    name: str
    closed: bool
    def __init__(self, cr: BaseCursor) -> None: ...
    def __enter__(self: _SavepointT) -> _SavepointT: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def close(self, *, rollback: bool = ...) -> None: ...
    def rollback(self) -> None: ...

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
    def savepoint(self, flush: bool = ...) -> Savepoint: ...
    def __enter__(self: _CursorT) -> _CursorT: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...

class Cursor(BaseCursor):
    IN_MAX: int
    sql_from_log: dict
    sql_into_log: dict
    sql_log_count: int
    dbname: str
    cache: dict
    def __init__(self, pool: ConnectionPool, dbname: str, dsn: dict) -> None: ...
    def dictfetchone(self) -> dict[str, Any] | None: ...
    def dictfetchmany(self, size) -> list[dict[str, Any]]: ...
    def dictfetchall(self) -> list[dict[str, Any]]: ...
    def fetchall(self) -> list[tuple]: ...
    def __del__(self) -> None: ...
    def mogrify(self, query, params: Any | None = ...) -> str: ...
    def execute(self, query, params: Any | None = ..., log_exceptions: bool = ...): ...
    def execute_values(
        self,
        query,
        argslist,
        template: Any | None = ...,
        page_size: int = ...,
        fetch: bool = ...,
    ): ...
    def split_for_in_conditions(
        self, ids: Iterable[_T], size: int = ...
    ) -> Iterator[tuple[_T, ...]]: ...
    def print_log(self): ...
    def close(self): ...
    def commit(self): ...
    def rollback(self): ...
    def __getattr__(self, name: str): ...
    @property
    def closed(self) -> bool: ...
    @property
    def readonly(self) -> bool: ...
    def now(self) -> datetime: ...

class TestCursor(BaseCursor):
    readonly: bool
    def __init__(self, cursor: Cursor, lock: RLock, readonly: bool) -> None: ...
    def execute(self, *args, **kwargs): ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def __getattr__(self, name: str): ...
    def now(self) -> datetime: ...

class PsycoConnection(psycopg2.extensions.connection): ...

class ConnectionPool:
    def __init__(self, maxconn: int = ..., readonly: bool = ...) -> None: ...
    @property
    def readonly(self) -> bool: ...
    def borrow(self, connection_info: dict) -> PsycoConnection: ...
    def give_back(
        self, connection: PsycoConnection, keep_in_pool: bool = ...
    ) -> None: ...
    def close_all(self, dsn: dict | None = ...) -> None: ...

class Connection:
    def __init__(self, pool: ConnectionPool, dbname: str, dsn: dict) -> None: ...
    @property
    def dsn(self) -> dict: ...
    @property
    def dbname(self) -> str: ...
    def cursor(self) -> Cursor: ...
    def __bool__(self) -> NoReturn: ...

def connection_info_for(db_or_uri: str, readonly: bool = ...) -> tuple[str, dict]: ...
def db_connect(to: str, allow_uri: bool = ..., readonly: bool = ...) -> Connection: ...
def close_db(db_name: str) -> None: ...
def close_all() -> None: ...
