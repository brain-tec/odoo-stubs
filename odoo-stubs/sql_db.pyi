from datetime import datetime
from re import Pattern
from threading import Lock, RLock
from typing import Any, Callable, Generator, Iterable, Iterator, Literal, NoReturn, Sequence, TypeVar

import psycopg2.extensions
from psycopg2.sql import Identifier

from .api import Transaction
from .tools import Callbacks

_T = TypeVar('_T')
_CursorT = TypeVar('_CursorT', bound=Cursor)
_SavepointT = TypeVar('_SavepointT', bound=Savepoint)

def undecimalize(symb, cr: Cursor) -> float | None: ...

real_time: Callable
re_from: Pattern
re_into: Pattern
sql_counter: int
MAX_IDLE_TIMEOUT: int

class Savepoint:
    name: str
    _name: Identifier
    _cr: BaseCursor
    closed: bool
    def __init__(self, cr: BaseCursor) -> None: ...
    def __enter__(self: _SavepointT) -> _SavepointT: ...
    def __exit__(self, exc_type, exc_val, exc_tb) -> None: ...
    def close(self, *, rollback: bool = ...) -> None: ...
    def rollback(self) -> None: ...
    def _close(self, rollback: bool) -> None: ...

class _FlushingSavepoint(Savepoint):
    def __init__(self, cr: BaseCursor) -> None: ...
    def rollback(self) -> None: ...
    def _close(self, rollback: bool) -> None: ...

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
    _closed: bool
    __pool: ConnectionPool
    dbname: str
    _cnx: PsycoConnection
    _obj: psycopg2.extensions.cursor
    __caller: tuple[str, int | str] | Literal[False]
    cache: dict
    _now: datetime | None
    def __init__(self, pool: ConnectionPool, dbname: str, dsn: dict) -> None: ...
    def __build_dict(self, row: Sequence) -> dict[str, Any]: ...
    def dictfetchone(self) -> dict[str, Any] | None: ...
    def dictfetchmany(self, size) -> list[dict[str, Any]]: ...
    def dictfetchall(self) -> list[dict[str, Any]]: ...
    def __del__(self) -> None: ...
    def _format(self, query, params: Any | None = ...): ...
    def execute(self, query, params: Any | None = ..., log_exceptions: bool = ...): ...
    def split_for_in_conditions(self, ids: Iterable, size: int | None = ...) -> Iterator[tuple]: ...
    def print_log(self): ...
    def _enable_logging(self) -> Generator[None, None, None]: ...
    def close(self): ...
    def _close(self, leak: bool = ...) -> None: ...
    def commit(self): ...
    def rollback(self): ...
    def __getattr__(self, name: str): ...
    @property
    def closed(self) -> bool: ...
    def now(self) -> datetime: ...

class TestCursor(BaseCursor):
    _cursors_stack: list[TestCursor]
    _now: datetime | None
    _closed: bool
    _cursor: Cursor
    _lock: RLock
    _savepoint: Savepoint | None
    def __init__(self, cursor: Cursor, lock: RLock) -> None: ...
    def execute(self, *args, **kwargs): ...
    def close(self) -> None: ...
    def commit(self) -> None: ...
    def rollback(self) -> None: ...
    def __getattr__(self, name: str): ...
    def now(self) -> datetime: ...

class PsycoConnection(psycopg2.extensions.connection): ...

class ConnectionPool:
    _connections: list[tuple[psycopg2.extensions.connection, bool]]
    _maxconn: int
    _lock: Lock
    def __init__(self, maxconn: int = ...) -> None: ...
    def __repr__(self) -> str: ...
    def _debug(self, msg, *args) -> None: ...
    def borrow(self, connection_info: dict) -> PsycoConnection: ...
    def give_back(self, connection: PsycoConnection, keep_in_pool: bool = ...) -> None: ...
    def close_all(self, dsn: dict | None = ...) -> None: ...

class Connection:
    dbname: str
    dsn: dict
    __pool: ConnectionPool
    def __init__(self, pool: ConnectionPool, dbname: str, dsn: dict) -> None: ...
    def cursor(self) -> Cursor: ...
    def __bool__(self) -> NoReturn: ...

def connection_info_for(db_or_uri: str) -> tuple[str, dict]: ...

_Pool: ConnectionPool | None

def db_connect(to: str, allow_uri: bool = ...) -> Connection: ...
def close_db(db_name: str) -> None: ...
def close_all() -> None: ...
