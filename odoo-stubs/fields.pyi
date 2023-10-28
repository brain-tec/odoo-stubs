import datetime
import enum
from typing import (
    Any,
    Callable,
    Container,
    Generic,
    Iterator,
    Sequence,
    Type,
    TypeVar,
    Union,
    overload,
)

import psycopg2
from markupsafe import Markup

from .api import Environment, Registry
from .models import BaseModel
from .tools import date_utils, float_utils

_FieldT = TypeVar("_FieldT", bound=Field)
_FieldValueT = TypeVar("_FieldValueT")
_ModelT = TypeVar("_ModelT", bound=BaseModel)
_SeqIntT = TypeVar("_SeqIntT", bound=Sequence[int])

DATE_LENGTH: int
DATETIME_LENGTH: int
NO_ACCESS: str
IR_MODELS: tuple[str, ...]
NoneType: type[None]
Default: object

def first(records: _ModelT) -> _ModelT: ...
def resolve_mro(model: BaseModel, name: str, predicate: Callable[..., bool]): ...
def determine(needle: str | Callable, records: BaseModel, *args): ...

class MetaField(type):
    by_type: dict
    def __init__(cls: type[Field], name, bases, attrs) -> None: ...

class Field(Generic[_FieldValueT], metaclass=MetaField):
    type: str | None
    relational: bool
    translate: bool
    column_type: tuple[str, str] | None
    write_sequence: int
    args: dict[str, Any] | None
    automatic: bool
    inherited: bool
    inherited_field: Field | None
    name: str
    model_name: str
    comodel_name: str | None
    store: bool
    index: str | bool | None
    manual: bool
    copy: bool
    recursive: bool
    compute: str | Callable | None
    compute_sudo: bool
    precompute: bool
    inverse: str | Callable | None
    search: str | Callable | None
    related: str | None
    company_dependent: bool
    default: Any
    string: str | None
    help: str | None
    readonly: bool
    required: bool
    states: dict[str, list[tuple]] | None
    groups: str | None
    change_default: bool
    related_field: Field | None
    group_operator: str | None
    group_expand: str | None
    prefetch: bool
    default_export_compatible: bool
    exportable: bool
    related_attrs: list[tuple[str, str]]
    description_attrs: list[tuple[str, str]]
    def __init__(self, string: str = ..., **kwargs) -> None: ...
    def __set_name__(self, owner: Type[BaseModel], name: str) -> None: ...
    def prepare_setup(self) -> None: ...
    def setup(self, model: BaseModel) -> None: ...
    def setup_nonrelated(self, model: BaseModel) -> None: ...
    def get_depends(self, model: BaseModel) -> tuple: ...
    def setup_related(self, model: BaseModel) -> None: ...
    def traverse_related(self, record: _ModelT) -> tuple[_ModelT, Field]: ...
    @property
    def base_field(self) -> Field: ...
    @property
    def groupable(self) -> bool: ...
    def resolve_depends(self, registry: Registry) -> Iterator[tuple]: ...
    def get_description(
        self, env: Environment, attributes: Container[str] | None = ...
    ) -> dict[str, Any]: ...
    def is_editable(self) -> bool: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_record_multi(self, values, records: BaseModel): ...
    def convert_to_read(
        self, value, record: BaseModel, use_display_name: bool = ...
    ): ...
    def convert_to_write(self, value, record: BaseModel): ...
    def convert_to_onchange(self, value, record: BaseModel, names): ...
    def convert_to_export(self, value, record: BaseModel): ...
    def convert_to_display_name(self, value, record: BaseModel): ...
    @property
    def column_order(self) -> int: ...
    def update_db(self, model: BaseModel, columns: dict[str, Any]): ...
    def update_db_column(self, model: BaseModel, column: dict | None) -> None: ...
    def update_db_notnull(self, model: BaseModel, column: dict | None) -> None: ...
    def update_db_related(self, model: BaseModel) -> None: ...
    def read(self, records: BaseModel) -> None: ...
    def create(self, record_values: list[tuple[BaseModel, Any]]) -> None: ...
    def write(self, records: _ModelT, value) -> None: ...
    @overload
    def __get__(self, record: BaseModel, owner) -> _FieldValueT: ...
    @overload
    def __get__(self: _FieldT, records: None, owner) -> _FieldT: ...
    def mapped(self, records: BaseModel): ...
    def __set__(self, records: BaseModel, value): ...
    def recompute(self, records: BaseModel) -> None: ...
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
    group_operator: str
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> int: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> int | None: ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(
        self, value, record: BaseModel, use_display_name: bool = ...
    ): ...
    def convert_to_export(self, value, record): ...

class Float(Field[float]):
    type: str
    group_operator: str
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
    round = float_utils.float_round
    is_zero = float_utils.float_is_zero
    compare = float_utils.float_compare

class Monetary(Field[float]):
    type: str
    write_sequence: int
    column_type: tuple[str, str]
    currency_field: str | None
    group_operator: str
    def __init__(
        self, string: str = ..., currency_field: str = ..., **kwargs
    ) -> None: ...
    def get_currency_field(self, model: BaseModel) -> str: ...
    def setup_nonrelated(self, model: BaseModel) -> None: ...
    def setup_related(self, model: BaseModel) -> None: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> float: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> float: ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(
        self, value, record: BaseModel, use_display_name: bool = ...
    ): ...
    def convert_to_write(self, value, record: BaseModel): ...

class _String(Field[str]):
    translate: Callable | bool
    unaccent: bool
    def __init__(self, string: str = ..., **kwargs) -> None: ...
    def get_trans_terms(self, value) -> list: ...
    def get_text_content(self, term): ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_write(self, value, record: BaseModel): ...
    def get_translation_dictionary(
        self, from_lang_value: str, to_lang_values: dict
    ) -> dict: ...
    def get_translation_fallback_langs(self, env: Environment) -> tuple[str, ...]: ...
    def write(self, records: _ModelT, value) -> None: ...

class Char(_String):
    type: str
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
    @property
    def column_type(self) -> tuple[str, str]: ...
    def convert_to_cache(self, value, record, validate: bool = ...) -> str | None: ...

class Html(_String):
    type: str
    sanitize: bool
    sanitize_overridable: bool
    sanitize_tags: bool
    sanitize_attributes: bool
    sanitize_style: bool
    sanitize_form: bool
    strip_style: bool
    strip_classes: bool
    @property
    def column_type(self) -> tuple[str, str]: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ) -> Markup | None: ...
    def convert_to_cache(
        self, value, record: BaseModel, validate: bool = ...
    ) -> Markup | None: ...
    def convert_to_record(self, value, record: BaseModel) -> Markup | None: ...
    def convert_to_read(
        self, value, record: BaseModel, use_display_name: bool = ...
    ) -> Markup | None: ...
    def get_trans_terms(self, value) -> list: ...

class Date(Field[datetime.date]):
    type: str
    column_type: tuple[str, str]
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
    def write(self, records: _ModelT, value) -> None: ...

class Image(Binary):
    max_width: int
    max_height: int
    verify_resolution: bool
    def setup(self, model: BaseModel) -> None: ...
    def create(self, record_values: list[tuple[BaseModel, Any]]) -> None: ...
    def write(self, records: BaseModel, value) -> None: ...

class Selection(Field[str]):
    type: str
    column_type: tuple[str, str]
    selection: list | Callable | str
    validate: bool
    ondelete: dict[str, Any] | None
    def __init__(
        self, selection: list | Callable | str = ..., string: str = ..., **kwargs
    ) -> None: ...
    def setup_nonrelated(self, model: BaseModel) -> None: ...
    def setup_related(self, model: BaseModel): ...
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
        self, value, record: BaseModel, use_display_name: bool = ...
    ) -> str | bool: ...
    def convert_to_export(self, value, record: BaseModel) -> str: ...
    def convert_to_display_name(self, value, record: BaseModel) -> str: ...

class _Relational(Field[BaseModel]):
    relational: bool
    domain: list | Callable
    context: dict
    check_company: bool
    comodel_name: str
    def setup_nonrelated(self, model: BaseModel) -> None: ...
    def get_domain_list(self, model: BaseModel) -> list: ...

class Many2one(_Relational):
    type: str
    column_type: tuple[str, str]
    ondelete: str | None
    auto_join: bool
    delegate: bool
    def __init__(
        self, comodel_name: str = ..., string: str = ..., **kwargs
    ) -> None: ...
    def setup_nonrelated(self, model: BaseModel) -> None: ...
    def update_db(self, model: BaseModel, columns): ...
    def update_db_column(self, model: BaseModel, column) -> None: ...
    def update_db_foreign_key(self, model: BaseModel, column) -> None: ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_record_multi(self, values, records: BaseModel): ...
    def convert_to_read(
        self, value, record: BaseModel, use_display_name: bool = ...
    ): ...
    def convert_to_write(self, value, record: BaseModel): ...
    def convert_to_export(self, value, record: BaseModel) -> str: ...
    def convert_to_display_name(self, value, record: BaseModel) -> str: ...
    def convert_to_onchange(self, value, record: BaseModel, names): ...
    def write(self, records: _ModelT, value) -> None: ...

class Many2oneReference(Integer):
    type: str
    model_field: str | None
    group_operator: str | None
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...

class Json(Field):
    type: str
    column_type: tuple[str, str]
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_export(self, value, record: BaseModel): ...

class Properties(Field):
    type: str
    column_type: tuple[str, str]
    copy: bool
    prefetch: bool
    unaccent: bool
    write_sequence: int
    store: bool
    readonly: bool
    precompute: bool
    definition: str | None
    definition_record: str | None
    definition_record_field: str | None
    ALLOWED_TYPES: tuple[str, ...]
    compute: Callable
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(
        self, value, record: BaseModel, use_display_name: bool = ...
    ): ...
    def convert_to_read_multi(self, values, records: BaseModel): ...
    def convert_to_write(self, value, record: BaseModel): ...
    def convert_to_onchange(self, value, record: BaseModel, names): ...
    def write(self, records: _ModelT, value) -> None: ...

class PropertiesDefinition(Field):
    type: str
    column_type: tuple[str, str]
    copy: bool
    readonly: bool
    prefetch: bool
    REQUIRED_KEYS: tuple[str, ...]
    ALLOWED_KEYS: tuple[str, ...]
    PROPERTY_PARAMETERS_MAP: dict[str, set[str]]
    def convert_to_column(
        self, value, record: BaseModel, values: Any | None = ..., validate: bool = ...
    ): ...
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_read(
        self, value, record: BaseModel, use_display_name: bool = ...
    ): ...

class Command(enum.IntEnum):
    CREATE: int
    UPDATE: int
    DELETE: int
    UNLINK: int
    LINK: int
    CLEAR: int
    SET: int
    @classmethod
    def create(cls, values: dict) -> tuple[int, int, dict]: ...
    @classmethod
    def update(cls, id: int, values: dict) -> tuple[int, int, dict]: ...
    @classmethod
    def delete(cls, id: int) -> tuple[int, int, int]: ...
    @classmethod
    def unlink(cls, id: int) -> tuple[int, int, int]: ...
    @classmethod
    def link(cls, id: int) -> tuple[int, int, int]: ...
    @classmethod
    def clear(cls) -> tuple[int, int, int]: ...
    @classmethod
    def set(cls, ids: _SeqIntT) -> tuple[int, int, _SeqIntT]: ...

class _RelationalMulti(_Relational):
    write_sequence: int
    def convert_to_cache(self, value, record: BaseModel, validate: bool = ...): ...
    def convert_to_record(self, value, record: BaseModel): ...
    def convert_to_record_multi(self, values, records: BaseModel): ...
    def convert_to_read(
        self, value, record: BaseModel, use_display_name: bool = ...
    ): ...
    def convert_to_write(self, value, record: BaseModel): ...
    def convert_to_export(self, value, record: BaseModel) -> str: ...
    def convert_to_display_name(self, value, record: BaseModel) -> None: ...
    def get_depends(self, model: BaseModel): ...
    def create(self, record_values: list[tuple[BaseModel, Any]]) -> None: ...
    def write(self, records: BaseModel, value) -> None: ...
    def write_batch(self, records_commands_list: list, create: bool = ...) -> None: ...

class One2many(_RelationalMulti):
    type: str
    inverse_name: str | None
    auto_join: bool
    copy: bool
    def __init__(
        self,
        comodel_name: str = ...,
        inverse_name: str = ...,
        string: str = ...,
        **kwargs
    ) -> None: ...
    def setup_nonrelated(self, model: BaseModel) -> None: ...
    def update_db(self, model: BaseModel, columns) -> None: ...
    def get_domain_list(self, records: BaseModel): ...
    def read(self, records: BaseModel): ...
    def write_real(self, records_commands_list: list, create: bool = ...) -> None: ...
    def write_new(self, records_commands_list: list): ...

class Many2many(_RelationalMulti):
    type: str
    relation: str | None
    column1: str | None
    column2: str | None
    auto_join: bool
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
    def setup_nonrelated(self, model: BaseModel) -> None: ...
    def update_db(self, model: BaseModel, columns) -> None: ...
    def update_db_foreign_keys(self, model: BaseModel) -> None: ...
    @property
    def groupable(self) -> bool: ...
    def read(self, records: BaseModel) -> None: ...
    def write_real(self, records_commands_list: list, create: bool = ...) -> None: ...
    def write_new(self, records_commands_list: list) -> None: ...

class Id(Field[int]):
    type: str
    column_type: tuple[str, str]
    string: str
    store: bool
    readonly: bool
    prefetch: bool
    def update_db(self, model: BaseModel, columns) -> None: ...
    def __set__(self, record: BaseModel, value) -> None: ...

class PrefetchMany2one:
    record: BaseModel
    field: Field
    def __init__(self, record: BaseModel, field: Field) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __reversed__(self) -> Iterator[int]: ...

class PrefetchX2many:
    record: BaseModel
    field: Field
    def __init__(self, record: BaseModel, field: Field) -> None: ...
    def __iter__(self) -> Iterator[int]: ...
    def __reversed__(self) -> Iterator[int]: ...

def apply_required(model: BaseModel, field_name: str) -> None: ...
