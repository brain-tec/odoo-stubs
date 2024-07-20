from re import Pattern
from threading import RLock
from typing import Any, Callable, Generator, Iterable, Iterator, NoReturn, TypeVar

import psycopg2.extensions

_T = TypeVar("_T")
_CallableT = TypeVar("_CallableT", bound=Callable)
_CursorT = TypeVar("_CursorT", bound=Cursor)

def unbuffer(symb, cr) -> str | None: ...
def undecimalize(symb, cr) -> float | None: ...
def adapt_string(adapted: str) -> psycopg2.extensions.QuotedString: ...
def flush_env(cr, *, clear: bool = ...) -> None: ...
def clear_env(cr) -> None: ...

re_from: Pattern
re_into: Pattern
sql_counter: int

class Cursor:
    IN_MAX: int
    def check(f: _CallableT) -> _CallableT: ...
    sql_from_log: dict
    sql_into_log: dict
    sql_log: bool
    sql_log_count: int
    dbname: str
    cache: dict
    def __init__(
        self, pool: ConnectionPool, dbname: str, dsn: dict, serialized: bool = ...
    ) -> None: ...
    def dictfetchone(self) -> dict[str, Any] | None: ...
    def dictfetchmany(self, size) -> list[dict[str, Any]]: ...
    def dictfetchall(self) -> list[dict[str, Any]]: ...
    def fetchall(self) -> list[tuple]: ...
    def __del__(self) -> None: ...
    def execute(
        self, query, params: Any | None = ..., log_exceptions: Any | None = ...
    ): ...
    def split_for_in_conditions(
        self, ids: Iterable, size: int | None = ...
    ) -> Iterator[tuple]: ...
    def print_log(self): ...
    def close(self): ...
    def autocommit(self, on: bool) -> None: ...
    def after(self, event: str, func: Callable) -> None: ...
    def commit(self): ...
    def rollback(self): ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def savepoint(self, flush: bool = ...) -> Generator[None, None, None]: ...
    def __getattr__(self, name: str): ...
    @property
    def closed(self) -> bool: ...

class TestCursor:
    def __init__(self, cursor: Cursor, lock: RLock) -> None: ...
    def close(self) -> None: ...
    def autocommit(self, on: bool) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def __getattr__(self, name: str): ...

class PsycoConnection(psycopg2.extensions.connection): ...

class ConnectionPool:
    def locked(fun: Callable[..., _T]) -> Callable[..., _T]: ...
    def __init__(self, maxconn: int = ...) -> None: ...
    def borrow(self, connection_info: dict) -> PsycoConnection: ...
    def give_back(
        self, connection: PsycoConnection, keep_in_pool: bool = ...
    ) -> None: ...
    def close_all(self, dsn: dict | None = ...) -> None: ...

class Connection:
    dbname: str
    dsn: dict
    def __init__(self, pool: ConnectionPool, dbname: str, dsn: dict) -> None: ...
    def cursor(self, serialized: bool = ...) -> Cursor: ...
    serialized_cursor = cursor
    def __bool__(self) -> NoReturn: ...

def connection_info_for(db_or_uri: str) -> tuple[str, dict]: ...
def db_connect(to: str, allow_uri: bool = ...) -> Connection: ...
def close_db(db_name: str) -> None: ...
def close_all() -> None: ...
