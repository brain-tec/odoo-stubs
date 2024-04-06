from collections import MutableMapping
from typing import (
    Any,
    Callable,
    Dict,
    Generator,
    List,
    Literal,
    Optional,
    TypeVar,
    overload,
)

from . import api, fields
from .api import Environment
from .modules.registry import Registry
from .sql_db import Cursor

_T = TypeVar("_T")
_ModelT = TypeVar("_ModelT", bound=BaseModel)
_Model2T = TypeVar("_Model2T", bound=BaseModel)

regex_order: Any
regex_object_name: Any
regex_pg_name: Any
regex_field_agg: Any
AUTOINIT_RECALCULATE_STORED_FIELDS: int

def check_object_name(name): ...
def raise_on_invalid_object_name(name) -> None: ...
def check_pg_name(name) -> None: ...

regex_private: Any

def check_method_name(name) -> None: ...
def same_name(f, g): ...
def fix_import_export_id_paths(fieldname): ...

class MetaModel(api.Meta):
    module_to_models: Any
    def __init__(self, name, bases, attrs) -> None: ...

class NewId:
    ref: Any
    def __init__(self, ref: Optional[Any] = ...) -> None: ...
    def __bool__(self): ...
    __nonzero__: Any

IdType: Any
PREFETCH_MAX: int
LOG_ACCESS_COLUMNS: Any
MAGIC_COLUMNS: Any
VALID_AGGREGATE_FUNCTIONS: Any

class BaseModel(metaclass=MetaModel):
    _auto: bool
    _register: bool
    _abstract: bool
    _transient: bool
    _name: str
    _description: str
    _custom: bool
    _inherit: Any
    _inherits: Dict[str, str]
    _constraints: Any
    _table: str
    _sequence: Any
    _sql_constraints: list
    _rec_name: str
    _order: str
    _parent_name: str
    _parent_store: bool
    _date_name: str
    _fold_name: str
    _needaction: bool
    _translate: bool
    _depends: Any
    _transient_check_count: int
    _transient_max_count: Any
    _transient_max_hours: Any
    _fields: Dict[str, fields.Field]
    _ids: tuple
    env: Environment
    pool: Registry
    id = fields.Id()
    display_name = fields.Char()
    create_uid = fields.Many2one("res.users")
    create_date = fields.Datetime()
    write_uid = fields.Many2one("res.users")
    write_date = fields.Datetime()
    CONCURRENCY_CHECK_FIELD: str
    def view_init(self, fields_list) -> None: ...
    def _reflect(self) -> None: ...
    def _add_field(self, name, field) -> None: ...
    def _pop_field(self, name): ...
    def _add_magic_fields(self) -> None: ...
    def compute_concurrency_field(self) -> None: ...
    def compute_concurrency_field_with_access(self) -> None: ...
    @classmethod
    def _build_model(cls, pool, cr): ...
    @classmethod
    def _build_model_check_base(model_class, cls) -> None: ...
    @classmethod
    def _build_model_check_parent(model_class, cls, parent_class) -> None: ...
    @classmethod
    def _build_model_attributes(cls, pool) -> None: ...
    @classmethod
    def _init_constraints_onchanges(cls) -> None: ...
    @property
    def _constraint_methods(self): ...
    @property
    def _onchange_methods(self): ...
    def __new__(cls) -> None: ...
    def __init__(self, pool, cr) -> None: ...
    def _is_an_ordinary_table(self): ...
    def _export_rows(self, fields, *, _is_toplevel_call: bool = ...): ...
    def export_data(self, fields_to_export, raw_data: bool = ...): ...
    def load(self, fields, data): ...
    def _add_fake_fields(self, fields): ...
    def _extract_records(self, fields_, data, log: Any = ...): ...
    def _convert_records(self, records, log: Any = ...) -> None: ...
    def _validate_fields(self, field_names) -> None: ...
    def default_get(self, fields_list): ...
    def fields_get_keys(self): ...
    def _rec_name_fallback(self): ...
    def view_header_get(self, view_id: Optional[Any] = ..., view_type: str = ...): ...
    def user_has_groups(self, groups): ...
    def _get_default_form_view(self): ...
    def _get_default_search_view(self): ...
    def _get_default_tree_view(self): ...
    def _get_default_activity_view(self): ...
    def _get_default_pivot_view(self): ...
    def _get_default_kanban_view(self): ...
    def _get_default_graph_view(self): ...
    def _get_default_calendar_view(self): ...
    def load_views(self, views, options: Optional[Any] = ...): ...
    def _fields_view_get(
        self,
        view_id: Optional[Any] = ...,
        view_type: str = ...,
        toolbar: bool = ...,
        submenu: bool = ...,
    ): ...
    def fields_view_get(
        self,
        view_id: Optional[Any] = ...,
        view_type: str = ...,
        toolbar: bool = ...,
        submenu: bool = ...,
    ): ...
    def get_formview_id(self, access_uid: Optional[Any] = ...): ...
    def get_formview_action(self, access_uid: Optional[Any] = ...): ...
    def get_access_action(self, access_uid: Optional[Any] = ...): ...
    def search_count(self, args) -> int: ...
    @overload
    def search(
        self: _ModelT,
        args,
        offset: int = ...,
        limit: Optional[int] = ...,
        order: Optional[str] = ...,
        count: Literal[False] = ...,
    ) -> _ModelT: ...
    @overload
    def search(
        self,
        args,
        offset: int = ...,
        limit: Optional[int] = ...,
        order: Optional[str] = ...,
        count: Literal[True] = ...,
    ) -> int: ...
    @overload
    def search(
        self: _ModelT,
        args,
        offset: int = ...,
        limit: Optional[int] = ...,
        order: Optional[str] = ...,
        count: bool = ...,
    ) -> int | _ModelT: ...
    def _compute_display_name(self) -> None: ...
    def name_get(self): ...
    def name_create(self, name): ...
    def name_search(
        self,
        name: str = ...,
        args: Optional[Any] = ...,
        operator: str = ...,
        limit: int = ...,
    ): ...
    def _name_search(
        self,
        name: str = ...,
        args: Optional[Any] = ...,
        operator: str = ...,
        limit: int = ...,
        name_get_uid: Optional[Any] = ...,
    ): ...
    def _add_missing_default_values(self, values): ...
    @classmethod
    def clear_caches(cls) -> None: ...
    def _read_group_fill_results(
        self,
        domain,
        groupby,
        remaining_groupbys,
        aggregated_fields,
        count_field,
        read_group_result,
        read_group_order: Optional[Any] = ...,
    ): ...
    def _read_group_fill_temporal(
        self, data, groupby, aggregated_fields, annotated_groupbys, interval: Any = ...
    ): ...
    def _read_group_prepare(
        self, orderby, aggregated_fields, annotated_groupbys, query
    ): ...
    def _read_group_process_groupby(self, gb, query): ...
    def _read_group_prepare_data(self, key, value, groupby_dict): ...
    def _read_group_format_result(self, data, annotated_groupbys, groupby, domain): ...
    def read_group(
        self,
        domain,
        fields,
        groupby,
        offset: int = ...,
        limit: Optional[Any] = ...,
        orderby: bool = ...,
        lazy: bool = ...,
    ): ...
    def _read_group_raw(
        self,
        domain,
        fields,
        groupby,
        offset: int = ...,
        limit: Optional[Any] = ...,
        orderby: bool = ...,
        lazy: bool = ...,
    ): ...
    def _read_group_resolve_many2one_fields(self, data, fields) -> None: ...
    def _inherits_join_add(self, current_model, parent_model_name, query): ...
    def _inherits_join_calc(
        self, alias, fname, query, implicit: bool = ..., outer: bool = ...
    ): ...
    def _parent_store_compute(self): ...
    def _check_removed_columns(self, log: bool = ...) -> None: ...
    def _init_column(self, column_name) -> None: ...
    def _table_has_rows(self): ...
    def _auto_init(self) -> None: ...
    def init(self) -> None: ...
    def _create_parent_columns(self) -> None: ...
    def _add_sql_constraints(self) -> None: ...
    def _execute_sql(self) -> None: ...
    def _add_inherited_fields(self) -> None: ...
    def _inherits_check(self) -> None: ...
    def _prepare_setup(self) -> None: ...
    def _setup_base(self): ...
    def _setup_fields(self) -> None: ...
    def _setup_complete(self) -> None: ...
    def fields_get(
        self, allfields: Optional[Any] = ..., attributes: Optional[Any] = ...
    ): ...
    def get_empty_list_help(self, help): ...
    def check_field_access_rights(self, operation, fields): ...
    def read(
        self, fields: Optional[list[str]] = ..., load: str = ...
    ) -> list[dict[str, Any]]: ...
    def _prefetch_field(self, field) -> None: ...
    def _read_from_database(self, field_names, inherited_field_names: Any = ...): ...
    def get_metadata(self): ...
    def _check_concurrency(self) -> None: ...
    def check_access_rights(self, operation, raise_exception: bool = ...): ...
    def check_access_rule(self, operation) -> None: ...
    def _filter_access_rules(self, operation): ...
    def unlink(self): ...
    def write(self, vals: dict[str, Any]): ...
    def _write(self, vals: dict[str, Any]): ...
    @overload
    def create(self: _ModelT, vals_list: list[dict[str, Any]]) -> _ModelT: ...
    @overload
    def create(self: _ModelT, vals_list: dict[str, Any]) -> _ModelT: ...
    def _create(self: _ModelT, data_list: list[dict[str, Any]]) -> _ModelT: ...
    def _parent_store_create(self) -> None: ...
    def _parent_store_update_prepare(self, vals): ...
    def _parent_store_update(self) -> None: ...
    def _load_records_write(self, values) -> None: ...
    def _load_records_create(self, values): ...
    def _load_records(self, data_list, update: bool = ...): ...
    def _where_calc(self, domain, active_test: bool = ...): ...
    def _check_qorder(self, word): ...
    def _apply_ir_rules(self, query, mode: str = ...) -> None: ...
    def _generate_translated_field(self, table_alias, field, query): ...
    def _generate_m2o_order_by(
        self, alias, order_field, query, reverse_direction, seen
    ): ...
    def _generate_order_by_inner(
        self,
        alias,
        order_spec,
        query,
        reverse_direction: bool = ...,
        seen: Optional[Any] = ...,
    ): ...
    def _generate_order_by(self, order_spec, query): ...
    def _search(
        self,
        args,
        offset: int = ...,
        limit: Optional[Any] = ...,
        order: Optional[Any] = ...,
        count: bool = ...,
        access_rights_uid: Optional[Any] = ...,
    ): ...
    def copy_data(self, default: Optional[Any] = ...): ...
    def copy_translations(old, new, excluded: Any = ...): ...
    def copy(self: _ModelT, default: Optional[Any] = ...) -> _ModelT: ...
    def exists(self: _ModelT) -> _ModelT: ...
    def _check_recursion(self, parent: Optional[Any] = ...): ...
    def _check_m2m_recursion(self, field_name): ...
    def _get_external_ids(self): ...
    def get_external_id(self): ...
    get_xml_id: Any
    _get_xml_ids: Any
    @classmethod
    def is_transient(cls): ...
    def _transient_clean_rows_older_than(self, seconds) -> None: ...
    def _transient_clean_old_rows(self, max_count) -> None: ...
    def _transient_vacuum(self, force: bool = ...): ...
    def resolve_2many_commands(
        self, field_name, commands, fields: Optional[Any] = ...
    ): ...
    resolve_o2m_commands_to_record_dicts: Any
    def search_read(
        self,
        domain: Optional[Any] = ...,
        fields: Optional[Any] = ...,
        offset: int = ...,
        limit: Optional[Any] = ...,
        order: Optional[Any] = ...,
    ): ...
    def toggle_active(self) -> None: ...
    def _register_hook(self) -> None: ...
    @classmethod
    def _patch_method(cls, name, method) -> None: ...
    @classmethod
    def _revert_method(cls, name) -> None: ...
    @classmethod
    def _browse(
        cls, ids, env, prefetch: Optional[Any] = ..., add_prefetch: bool = ...
    ): ...
    def browse(
        self: _ModelT, arg: Optional[Any] = ..., prefetch: Optional[Any] = ...
    ) -> _ModelT: ...
    @property
    def ids(self) -> List[int]: ...
    _cr: Cursor
    _uid: int
    _context: dict
    def ensure_one(self): ...
    def with_env(self: _ModelT, env) -> _ModelT: ...
    def sudo(self: _ModelT, user: Any = ...) -> _ModelT: ...
    def with_context(self: _ModelT, *args, **kwargs) -> _ModelT: ...
    def with_prefetch(self: _ModelT, prefetch: Optional[Any] = ...) -> _ModelT: ...
    def _convert_to_cache(self, values, update: bool = ..., validate: bool = ...): ...
    def _convert_to_record(self, values): ...
    def _convert_to_write(self, values: dict[str, Any]) -> dict[str, Any]: ...
    def _mapped_func(self, func): ...
    @overload
    def mapped(self: _ModelT, func: Callable[[_ModelT], _Model2T]) -> _Model2T: ...
    @overload
    def mapped(self: _ModelT, func: Callable[[_ModelT], _T]) -> list[_T]: ...
    @overload
    def mapped(self, func: str) -> Any: ...
    def _mapped_cache(self, name_seq): ...
    @overload
    def filtered(self: _ModelT, func: Callable[[_ModelT], Any]) -> _ModelT: ...
    @overload
    def filtered(self: _ModelT, func: str) -> _ModelT: ...
    @overload
    def sorted(
        self: _ModelT, key: Callable[[_ModelT], Any] = ..., reverse: bool = ...
    ) -> _ModelT: ...
    @overload
    def sorted(
        self: _ModelT, key: str | None = ..., reverse: bool = ...
    ) -> _ModelT: ...
    def update(self, values) -> None: ...
    def new(self: _ModelT, values=..., ref: Optional[Any] = ...) -> _ModelT: ...
    def _is_dirty(self): ...
    def _get_dirty(self): ...
    def _set_dirty(self, field_name) -> None: ...
    def __bool__(self) -> bool: ...
    __nonzero__: Any
    def __len__(self) -> int: ...
    def __iter__(self: _ModelT) -> Generator[_ModelT]: ...
    def __contains__(self, item) -> bool: ...
    def __add__(self: _ModelT, other) -> _ModelT: ...
    def concat(self: _ModelT, *args) -> _ModelT: ...
    def __sub__(self: _ModelT, other) -> _ModelT: ...
    def __and__(self: _ModelT, other) -> _ModelT: ...
    def __or__(self: _ModelT, other) -> _ModelT: ...
    def union(self: _ModelT, *args) -> _ModelT: ...
    def __eq__(self, other) -> bool: ...
    def __lt__(self, other) -> bool: ...
    def __le__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __ge__(self, other) -> bool: ...
    def __int__(self): ...
    def __str__(self): ...
    def __repr__(self): ...
    def __hash__(self) -> Any: ...
    @overload
    def __getitem__(self: _ModelT, key: int | slice) -> _ModelT: ...
    @overload
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key, value): ...
    def _cache(self): ...
    def _in_cache_without(self, field, limit: Any = ...): ...
    def refresh(self) -> None: ...
    def invalidate_cache(
        self, fnames: Optional[Any] = ..., ids: Optional[Any] = ...
    ): ...
    def modified(self, fnames) -> None: ...
    def _recompute_check(self, field): ...
    def _recompute_todo(self, field) -> None: ...
    def _recompute_done(self, field) -> None: ...
    def recompute(self) -> None: ...
    def _has_onchange(self, field, other_fields): ...
    def _onchange_spec(self, view_info: Optional[Any] = ...): ...
    def _onchange_eval(self, field_name, onchange, result) -> None: ...
    def onchange(self, values, field_name, field_onchange): ...

class RecordCache(MutableMapping):
    def __init__(self, record) -> None: ...
    def __contains__(self, name): ...
    def __getitem__(self, name): ...
    def __setitem__(self, name, value) -> None: ...
    def __delitem__(self, name) -> None: ...
    def __iter__(self) -> Any: ...
    def __len__(self): ...
    def has_value(self, name): ...
    def get_value(self, name, default: Optional[Any] = ...): ...
    def set_special(self, name, getter) -> None: ...
    def set_failed(self, names, exception) -> None: ...

AbstractModel = BaseModel

class Model(AbstractModel):
    _auto: bool
    _register: bool
    _abstract: bool
    _transient: bool

class TransientModel(Model):
    _auto: bool
    _register: bool
    _abstract: bool
    _transient: bool

def itemgetter_tuple(items): ...
def convert_pgerror_not_null(model, fields, info, e): ...
def convert_pgerror_unique(model, fields, info, e): ...

PGERROR_TO_OE: Any

def lazy_name_get(self): ...
