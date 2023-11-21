from collections import defaultdict
from typing import (
    Any,
    Callable,
    Collection,
    Generator,
    Iterable,
    Iterator,
    KeysView,
    Mapping,
    Optional,
    Sequence,
    TypeVar,
)
from weakref import WeakSet

from odoo.addons.base.models.res_company import Company
from odoo.addons.base.models.res_users import Users

from .fields import Field
from .models import BaseModel
from .modules.registry import Registry
from .sql_db import Cursor
from .tools import StackMap, frozendict

_T = TypeVar("_T")
_ModelT = TypeVar("_ModelT", bound=BaseModel)
_CallableT = TypeVar("_CallableT", bound=Callable)

INHERITED_ATTRS: tuple[str, ...]

class Params:
    args: tuple
    kwargs: dict
    def __init__(self, args: tuple, kwargs: dict) -> None: ...

class Meta(type):
    def __new__(meta, name: str, bases: tuple, attrs: dict): ...

def attrsetter(attr, value) -> Callable[[_T], _T]: ...
def propagate(method1: Callable, method2: _CallableT) -> _CallableT: ...
def constrains(
    *args: str | Callable[[_ModelT], Sequence[str]]
) -> Callable[[_T], _T]: ...
def ondelete(*, at_uninstall: bool) -> Callable[[_T], _T]: ...
def onchange(*args: str) -> Callable[[_T], _T]: ...
def depends(*args: str | Callable[[_ModelT], Sequence[str]]) -> Callable[[_T], _T]: ...
def depends_context(*args: str) -> Callable[[_T], _T]: ...
def returns(
    model: str | None, downgrade: Callable | None = ..., upgrade: Callable | None = ...
) -> Callable[[_T], _T]: ...
def downgrade(method: Callable, value, self, args, kwargs): ...
def autovacuum(method: _CallableT) -> _CallableT: ...
def model(method: _CallableT) -> _CallableT: ...
def model_create_single(method: _CallableT) -> _CallableT: ...
def model_create_multi(method: _CallableT) -> _CallableT: ...
def call_kw(model: BaseModel, name: str, args, kwargs): ...

class Environment(Mapping[str, BaseModel]):
    cr: Cursor = ...
    uid: int = ...
    context: dict[str, Any] = ...
    su: bool = ...
    args: tuple[Cursor, int, dict, bool]
    def reset(self) -> None: ...
    all: Transaction
    transaction: Transaction
    registry: Registry
    cache: Cache
    def __new__(
        cls, cr: Cursor, uid: int | None, context: dict, su: bool = ...
    ) -> Environment: ...
    def __contains__(self, model_name) -> bool: ...
    def __getitem__(self, model_name: str) -> BaseModel: ...
    def __iter__(self) -> Iterator[str]: ...
    def __len__(self) -> int: ...
    def __eq__(self, other) -> bool: ...
    def __ne__(self, other) -> bool: ...
    def __hash__(self) -> int: ...
    def __call__(
        self,
        cr: Cursor | None = ...,
        user: Users | int | None = ...,
        context: dict | None = ...,
        su: bool | None = ...,
    ) -> Environment: ...
    def ref(
        self, xml_id: str, raise_if_not_found: bool = ...
    ) -> Optional[BaseModel]: ...
    def is_superuser(self) -> bool: ...
    def is_admin(self) -> bool: ...
    def is_system(self) -> bool: ...
    @property
    def user(self) -> Users: ...
    @property
    def company(self) -> Company: ...
    @property
    def companies(self) -> Company: ...
    @property
    def lang(self) -> str: ...
    def clear(self) -> None: ...
    def invalidate_all(self, flush: bool = ...) -> None: ...
    def flush_all(self) -> None: ...
    def is_protected(self, field: Field, record: BaseModel) -> bool: ...
    def protected(self, field: Field) -> BaseModel: ...
    def protecting(
        self, what, records: Optional[BaseModel] = ...
    ) -> Generator[None, None, None]: ...
    def fields_to_compute(self) -> KeysView[Field]: ...
    def records_to_compute(self, field: Field) -> BaseModel: ...
    def is_to_compute(self, field: Field, record: BaseModel) -> bool: ...
    def not_to_compute(self, field: Field, records: _ModelT) -> _ModelT: ...
    def add_to_compute(self, field: Field, records: BaseModel): ...
    def remove_to_compute(self, field: Field, records: BaseModel) -> None: ...
    def cache_key(self, field: Field): ...

class Transaction:
    registry: Registry
    envs: WeakSet[Environment]
    cache: Cache
    protected: StackMap[Field, set[int]]
    tocompute: defaultdict[Field, set[int]]
    def __init__(self, registry: Registry) -> None: ...
    def flush(self) -> None: ...
    def clear(self) -> None: ...
    def reset(self) -> None: ...

NOTHING: object
EMPTY_DICT: frozendict

class Cache:
    def __init__(self) -> None: ...
    def contains(self, record: BaseModel, field: Field) -> bool: ...
    def contains_field(self, field: Field) -> bool: ...
    def get(self, record: BaseModel, field: Field, default=...): ...
    def set(
        self,
        record: BaseModel,
        field: Field,
        value,
        dirty: bool = ...,
        check_dirty: bool = ...,
    ) -> None: ...
    def update(
        self,
        records: BaseModel,
        field: Field,
        values,
        dirty: bool = ...,
        check_dirty: bool = ...,
    ) -> None: ...
    def update_raw(
        self,
        records: BaseModel,
        field: Field,
        values,
        dirty: bool = ...,
        check_dirty: bool = ...,
    ) -> None: ...
    def insert_missing(self, records: BaseModel, field: Field, values) -> None: ...
    def remove(self, record: BaseModel, field: Field) -> None: ...
    def get_values(self, records: BaseModel, field: Field) -> Iterator: ...
    def get_until_miss(self, records: BaseModel, field: Field) -> list: ...
    def get_records_different_from(
        self, records: _ModelT, field: Field, value
    ) -> _ModelT: ...
    def get_fields(self, record: BaseModel) -> Iterator[Field]: ...
    def get_records(self, model: _ModelT, field: Field) -> _ModelT: ...
    def get_missing_ids(self, records: BaseModel, field: Field) -> Iterator[int]: ...
    def get_dirty_fields(self) -> "set[Field]": ...
    def get_dirty_records(self, model: _ModelT, field: Field) -> _ModelT: ...
    def has_dirty_fields(
        self, records: BaseModel, fields: Iterable[Field] | None = ...
    ) -> bool: ...
    def clear_dirty_field(self, field: Field) -> Collection[int]: ...
    def invalidate(
        self, spec: list[tuple[Field, Iterable | None]] | None = ...
    ) -> None: ...
    def clear(self) -> None: ...
    def check(self, env: Environment) -> None: ...

class Starred:
    value: Any
    def __init__(self, value) -> None: ...
