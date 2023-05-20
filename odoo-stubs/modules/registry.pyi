from collections import Mapping
from collections import defaultdict as defaultdict
from typing import Any, Optional

from ..sql_db import Cursor
from ..tools import table_exists as table_exists

class Registry(Mapping):
    model_cache: Any
    def registries(cls): ...
    def __new__(cls, db_name): ...
    @classmethod
    def new(
        cls,
        db_name,
        force_demo: bool = ...,
        status: Optional[Any] = ...,
        update_module: bool = ...,
    ): ...
    models: Any
    updated_modules: Any
    db_name: Any
    test_cr: Any
    loaded: bool
    ready: bool
    registry_sequence: Any
    cache_sequence: Any
    registry_invalidated: bool
    cache_invalidated: bool
    has_unaccent: Any
    def init(self, db_name) -> None: ...
    @classmethod
    def delete(cls, db_name) -> None: ...
    @classmethod
    def delete_all(cls) -> None: ...
    def __len__(self): ...
    def __iter__(self) -> Any: ...
    def __getitem__(self, model_name): ...
    def __call__(self, model_name): ...
    def __setitem__(self, model_name, model) -> None: ...
    def field_sequence(self): ...
    def do_parent_store(self, cr) -> None: ...
    def descendants(self, model_names, *kinds): ...
    def load(self, cr, module): ...
    def setup_models(self, cr) -> None: ...
    def post_init(self, func, *args, **kwargs) -> None: ...
    def init_models(self, cr, model_names, context) -> None: ...
    def check_tables_exist(self, cr) -> None: ...
    def cache(self): ...
    def clear_caches(self) -> None: ...
    def setup_signaling(self) -> None: ...
    def check_signaling(self): ...
    def signal_changes(self) -> None: ...
    def reset_changes(self) -> None: ...
    def manage_changes(self) -> None: ...
    def in_test_mode(self): ...
    def enter_test_mode(self) -> None: ...
    def leave_test_mode(self) -> None: ...
    def cursor(self) -> Cursor: ...

class DummyRLock:
    def acquire(self) -> None: ...
    def release(self) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, type, value, traceback) -> None: ...
