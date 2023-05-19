import threading
from collections import defaultdict, deque
from collections.abc import Mapping
from threading import RLock
from typing import Any, Callable, ClassVar, Iterable, Iterator
from weakref import WeakValueDictionary

from ..models import BaseModel
from ..sql_db import Connection, Cursor
from ..tools.assertion_report import assertion_report
from ..tools.lru import LRU
from .graph import Node

class Registry(Mapping[str, type[BaseModel]]):
    _lock: RLock
    _saved_lock: RLock | None
    model_cache: WeakValueDictionary
    registries: ClassVar[LRU]
    def __new__(cls, db_name: str) -> Registry: ...
    @classmethod
    def new(
        cls,
        db_name: str,
        force_demo: bool = ...,
        status: Any | None = ...,
        update_module: bool = ...,
    ) -> Registry: ...
    models: dict[str, type[BaseModel]]
    _sql_constraints: set
    _init: bool
    _assertion_report: assertion_report
    _fields_by_model: Any
    _post_init_queue: deque
    _constraint_queue: deque
    _init_modules: set[str]
    updated_modules: list[str]
    loaded_xmlids: set
    db_name: str
    _db: Connection
    test_cr: Cursor | None
    test_lock: RLock | None
    loaded: bool
    ready: bool
    registry_sequence: int | None
    cache_sequence: int | None
    _invalidation_flags: threading.local
    has_unaccent: bool
    populated_models: dict[str, list[int]]
    def init(self, db_name: str) -> None: ...
    @classmethod
    def delete(cls, db_name: str) -> None: ...
    @classmethod
    def delete_all(cls) -> None: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[str]: ...
    def __getitem__(self, model_name: str) -> type[BaseModel]: ...
    def __call__(self, model_name: str) -> type[BaseModel]: ...
    def __setitem__(self, model_name: str, model: type[BaseModel]) -> None: ...
    def descendants(self, model_names: Iterable[str], *kinds) -> set[str]: ...
    def load(self, cr: Cursor, module: Node) -> set[str]: ...
    _m2m: defaultdict[Any, list]
    def setup_models(self, cr: Cursor) -> None: ...
    def post_init(self, func: Callable, *args, **kwargs) -> None: ...
    def post_constraint(self, func: Callable, *args, **kwargs) -> None: ...
    def finalize_constraints(self) -> None: ...
    _is_install: bool
    def init_models(
        self, cr: Cursor, model_names: Iterable[str], context: dict, install: bool = ...
    ) -> None: ...
    def check_tables_exist(self, cr: Cursor) -> None: ...
    @property
    def cache(self) -> LRU: ...
    def _clear_cache(self) -> None: ...
    def clear_caches(self) -> None: ...
    @property
    def registry_invalidated(self) -> bool: ...
    @registry_invalidated.setter
    def registry_invalidated(self, value: bool) -> None: ...
    @property
    def cache_invalidated(self) -> bool: ...
    @cache_invalidated.setter
    def cache_invalidated(self, value: bool) -> None: ...
    def setup_signaling(self) -> None: ...
    def check_signaling(self) -> Registry: ...
    def signal_changes(self) -> None: ...
    def reset_changes(self) -> None: ...
    def manage_changes(self) -> None: ...
    def in_test_mode(self) -> bool: ...
    def enter_test_mode(self, cr: Cursor) -> None: ...
    def leave_test_mode(self) -> None: ...
    def cursor(self) -> Cursor: ...

class DummyRLock:
    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type, value, traceback) -> None: ...
