import datetime
from typing import (
    Any,
    Callable,
    Collection,
    Generic,
    Iterator,
    Sequence,
    TypeVar,
    Union,
    overload,
)

import psycopg2
from markupsafe import Markup

from .api import Environment
from .models import BaseModel
from .tools import date_utils, frozendict

_FieldT = TypeVar("_FieldT", bound=Field)
_FieldValueT = TypeVar("_FieldValueT")
_ModelT = TypeVar("_ModelT", bound=BaseModel)
_SeqIntT = TypeVar("_SeqIntT", bound=Sequence[int])

DATE_LENGTH: int
DATETIME_LENGTH: int
EMPTY_DICT: frozendict
RENAMED_ATTRS: list[tuple[str, str]]
DEPRECATED_ATTRS: list[tuple[str, str]]
Default: object

def first(records: _ModelT) -> _ModelT: ...
def resolve_mro(model: BaseModel, name: str, predicate: Callable[..., bool]): ...

class MetaField(type):
    by_type: dict
    def __new__(meta, name, bases, attrs): ...
    def __init__(cls: type[Field], name, bases, attrs) -> None: ...

class Field(Generic[_FieldValueT], metaclass=MetaField):
    type: str | None
    relational: bool
    translate: bool
    column_type: tuple[str, str] | None
    column_format: str
    column_cast_from: tuple[str, ...]
    args: dict[str, Any] | None
    automatic: bool
    inherited: bool
    inherited_field: Field | None
    name: str
    model_name: str
    comodel_name: str | None
    store: bool
    index: bool
    manual: bool
    copy: bool
    depends: Collection[str] | None
    depends_context: Collection[str] | None
    recursive: bool
    compute: str | Callable | None
    compute_sudo: bool
    inverse: str | Callable | None
    search: str | Callable | None
    related: str | Sequence[str] | None
    company_dependent: bool
    default: Any
    string: str | None
    help: str | None
    readonly: bool
    required: bool
    states: dict[str, list[tuple]] | None
    groups: str | None
    change_default: bool
    deprecated: bool | None
    related_field: Field | None
    group_operator: str | None
    group_expand: str | None
    prefetch: bool
    related_attrs: list[tuple[str, str]]
    description_attrs: list[tuple[str, str]]
    def __init__(self, string: str = ..., **kwargs) -> None: ...
    def new(self, **kwargs): ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value) -> None: ...
    def set_all_attrs(self, attrs) -> None: ...
    def __delattr__(self, name) -> None: ...
    def setup_base(self, model: BaseModel, name: str) -> None: ...
    def setup_full(self, model: BaseModel) -> None: ...
    def traverse_related(self, record: _ModelT) -> tuple[_ModelT, Field]: ...
    @property
    def base_field(self) -> Field: ...
    def cache_key(self, env: Environment) -> tuple: ...
    recursive: bool
    def resolve_depends(self, model: BaseModel) -> Iterator[tuple]: ...
    def get_description(self, env: Environment) -> dict[str, Any]: ...
    def null(self, record: BaseModel) -> bool: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(self, value, record: BaseModel, use_name_get: bool = ...): ...
    def convert_to_write(self, value, record: BaseModel): ...
    def convert_to_onchange(self, value, record: BaseModel, names): ...
    def convert_to_export(self, value, record: BaseModel): ...
    def convert_to_display_name(self, value, record: BaseModel): ...
    def update_db(self, model: BaseModel, columns: dict[str, Any]): ...
    def update_db_column(self, model: BaseModel, column: dict | None) -> None: ...
    def update_db_notnull(self, model: BaseModel, column: dict | None) -> None: ...
    def update_db_index(self, model: BaseModel, column: dict | None) -> None: ...
    def update_db_related(self, model: BaseModel) -> None: ...
    def read(self, records: BaseModel) -> None: ...
    def create(self, record_values: list[tuple[BaseModel, Any]]) -> None: ...
    def write(self, records: _ModelT, value) -> _ModelT: ...
    @overload
    def __get__(self, record: BaseModel, owner) -> _FieldValueT: ...
    @overload
    def __get__(self: _FieldT, records: None, owner) -> _FieldT: ...
    def __set__(self, records: BaseModel, value) -> None: ...
    def compute_value(self, records: BaseModel) -> None: ...
    def determine_inverse(self, records: BaseModel) -> None: ...
    def determine_domain(self, records: BaseModel, operator: str, value) -> list: ...

class Boolean(Field[bool]):
    type: str
    column_type: tuple[str, str]
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> bool: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> bool: ...
    def convert_to_export(self, value, record: BaseModel): ...

class Integer(Field[int]):
    type: str
    column_type: tuple[str, str]
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> int: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> int | None: ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(self, value, record: BaseModel, use_name_get: bool = ...): ...
    def convert_to_export(self, value, record): ...

class Float(Field[float]):
    type: str
    column_cast_from: tuple[str, str, str]
    def __init__(
        self, string: str = ..., digits: tuple[int, int] | str | None = ..., **kwargs
    ) -> None: ...
    @property
    def column_type(self): ...
    def get_digits(self, env: Environment) -> tuple[int, int]: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> float: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> float: ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_export(self, value, record: BaseModel): ...

class Monetary(Field[float]):
    type: str
    column_type: tuple[str, str]
    column_cast_from: tuple[str]
    currency_field: str | None
    group_operator: str
    def __init__(
        self, string: str = ..., currency_field: str = ..., **kwargs
    ) -> None: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> float: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> float: ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(self, value, record: BaseModel, use_name_get: bool = ...): ...
    def convert_to_write(self, value, record: BaseModel): ...

class _String(Field[str]):
    translate: Callable | bool
    prefetch: Any
    def __init__(self, string: str = ..., **kwargs) -> None: ...
    def get_trans_terms(self, value) -> list: ...
    def get_trans_func(self, records: BaseModel) -> Callable: ...
    def check_trans_value(self, value): ...
    def write(self, records: _ModelT, value) -> _ModelT: ...

class Char(_String):
    type: str
    column_cast_from: tuple[str]
    size: int | None
    trim: bool
    @property
    def column_type(self) -> tuple[str, str]: ...
    def update_db_column(self, model: BaseModel, column: dict | None) -> None: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> str | None: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> str | None: ...

class Text(_String):
    type: str
    column_type: tuple[str, str]
    column_cast_from: tuple[str]
    def convert_to_cache(self, value, record, validate: bool = ...) -> str | None: ...

class Html(_String):
    type: str
    column_type: tuple[str, str]
    sanitize: bool
    sanitize_tags: bool
    sanitize_attributes: bool
    sanitize_style: bool
    sanitize_form: bool
    strip_style: bool
    strip_classes: bool
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> Markup | None: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> Markup | None: ...

class Date(Field[datetime.date]):
    type: str
    column_type: tuple[str, str]
    column_cast_from: tuple[str]
    start_of = date_utils.start_of
    end_of = date_utils.end_of
    add = date_utils.add
    subtract = date_utils.subtract
    @staticmethod
    def today(*args) -> datetime.date: ...
    @staticmethod
    def context_today(
        record: BaseModel, timestamp: datetime.datetime | None = ...
    ) -> datetime.date: ...
    @staticmethod
    def to_date(value) -> datetime.date | None: ...
    from_string = to_date
    @staticmethod
    def to_string(value: datetime.datetime | datetime.date) -> str: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> datetime.date | None: ...
    def convert_to_export(self, value, record: BaseModel): ...

class Datetime(Field[datetime.datetime]):
    type: str
    column_type: tuple[str, str]
    column_cast_from: tuple[str]
    start_of = date_utils.start_of
    end_of = date_utils.end_of
    add = date_utils.add
    subtract = date_utils.subtract
    @staticmethod
    def now(*args) -> datetime.datetime: ...
    @staticmethod
    def today(*args) -> datetime.datetime: ...
    @staticmethod
    def context_timestamp(
        record: BaseModel, timestamp: datetime.datetime
    ) -> datetime.datetime: ...
    @staticmethod
    def to_datetime(value) -> datetime.datetime | None: ...
    from_string = to_datetime
    @staticmethod
    def to_string(value: datetime.datetime | datetime.date) -> str: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> datetime.datetime | None: ...
    def convert_to_export(self, value, record: BaseModel): ...
    def convert_to_display_name(self, value, record: BaseModel) -> str: ...

class Binary(Field[bytes]):
    type: str
    prefetch: bool
    depends_context: tuple[str]
    attachment: bool
    @property
    def column_type(self) -> tuple[str, str] | None: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> psycopg2.Binary | None: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> bytes | None: ...
    def convert_to_record(self, value, record: BaseModel) -> bytes: ...
    def compute_value(self, records: BaseModel) -> None: ...
    def read(self, records: BaseModel) -> None: ...
    def create(self, record_values: list[tuple[BaseModel, Any]]) -> None: ...
    def write(self, records: _ModelT, value) -> _ModelT: ...

class Image(Binary):
    max_width: int
    max_height: int
    verify_resolution: bool
    def create(self, record_values: list[tuple[BaseModel, Any]]) -> None: ...
    def write(self, records: BaseModel, value) -> None: ...

class Selection(Field[str]):
    type: str
    column_type: tuple[str, str]
    selection: list | Callable | str
    validate: bool
    def __init__(
        self, selection: list | Callable | str = ..., string: str = ..., **kwargs
    ) -> None: ...
    def get_values(self, env: Environment) -> list[str]: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_export(self, value, record: BaseModel): ...

class Reference(Selection):
    type: str
    @property
    def column_type(self) -> tuple[str, str]: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> str | None: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> str | None: ...
    def convert_to_record(self, value, record: BaseModel) -> Union[BaseModel, None]: ...
    def convert_to_read(
        self, value, record: BaseModel, use_name_get: bool = ...
    ) -> str | bool: ...
    def convert_to_export(self, value, record: BaseModel) -> str: ...
    def convert_to_display_name(self, value, record: BaseModel) -> str: ...

class _Relational(Field[BaseModel]):
    relational: bool
    domain: list | Callable
    context: dict
    check_company: bool
    comodel_name: str
    def get_domain_list(self, model: BaseModel) -> list: ...
    def null(self, record: BaseModel) -> BaseModel: ...

class Many2one(_Relational):
    type: str
    column_type: tuple[str, str]
    ondelete: str | None
    auto_join: bool
    delegate: bool
    def __init__(
        self, comodel_name: str = ..., string: str = ..., **kwargs
    ) -> None: ...
    def update_db(self, model: BaseModel, columns): ...
    def update_db_column(self, model: BaseModel, column) -> None: ...
    def update_db_foreign_key(self, model: BaseModel, column) -> None: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(self, value, record: BaseModel, use_name_get: bool = ...): ...
    def convert_to_write(self, value, record: BaseModel): ...
    def convert_to_export(self, value, record: BaseModel) -> str: ...
    def convert_to_display_name(self, value, record: BaseModel) -> str: ...
    def convert_to_onchange(self, value, record: BaseModel, names): ...
    def write(self, records: _ModelT, value) -> _ModelT: ...

class Many2oneReference(Integer):
    type: str
    model_field: str | None
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...

class _RelationalMulti(_Relational):
    write_sequence: int
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(self, value, record: BaseModel, use_name_get: bool = ...): ...
    def convert_to_write(self, value, record: BaseModel): ...
    def convert_to_export(self, value, record: BaseModel) -> str: ...
    def convert_to_display_name(self, value, record: BaseModel) -> None: ...
    def create(self, record_values: list[tuple[BaseModel, Any]]) -> None: ...
    def write(self, records: BaseModel, value): ...
    def write_batch(self, records_commands_list: list, create: bool = ...): ...

class One2many(_RelationalMulti):
    type: str
    inverse_name: str | None
    auto_join: bool
    limit: int | None
    copy: bool
    def __init__(
        self,
        comodel_name: str = ...,
        inverse_name: str = ...,
        string: str = ...,
        **kwargs
    ) -> None: ...
    def update_db(self, model: BaseModel, columns) -> None: ...
    def get_domain_list(self, records: BaseModel): ...
    def read(self, records: BaseModel): ...
    def write_real(self, records_commands_list: list, create: bool = ...): ...
    def write_new(self, records_commands_list: list): ...

class Many2many(_RelationalMulti):
    type: str
    relation: str | None
    column1: str | None
    column2: str | None
    auto_join: bool
    limit: int | None
    ondelete: str
    def __init__(
        self,
        comodel_name: str = ...,
        relation: str = ...,
        column1: str = ...,
        column2: str = ...,
        string: str = ...,
        **kwargs
    ) -> None: ...
    def update_db(self, model: BaseModel, columns) -> None: ...
    def update_db_foreign_keys(self, model: BaseModel) -> None: ...
    def read(self, records: BaseModel) -> None: ...
    def write_real(self, records_commands_list: list, create: bool = ...): ...
    def write_new(self, records_commands_list: list): ...

class Id(Field[int]):
    type: str
    column_type: tuple[str, str]
    string: str
    store: bool
    readonly: bool
    prefetch: bool
    def update_db(self, model: BaseModel, columns) -> None: ...
    def __set__(self, record: BaseModel, value) -> None: ...

def prefetch_many2one_ids(record: BaseModel, field: Field) -> Iterator: ...
def prefetch_x2many_ids(record: BaseModel, field: Field) -> Iterator: ...
def apply_required(model: BaseModel, field_name: str) -> None: ...
