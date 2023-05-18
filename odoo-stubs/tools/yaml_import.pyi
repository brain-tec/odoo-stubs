from typing import Any, Optional

from odoo import SUPERUSER_ID as SUPERUSER_ID

from . import assertion_report as assertion_report
from . import pycompat as pycompat
from . import yaml_tag as yaml_tag
from .config import config as config
from .misc import DEFAULT_SERVER_DATE_FORMAT as DEFAULT_SERVER_DATE_FORMAT
from .misc import DEFAULT_SERVER_DATETIME_FORMAT as DEFAULT_SERVER_DATETIME_FORMAT
from .misc import file_open as file_open
from .safe_eval import safe_eval as safe_eval

unsafe_eval = eval
_logger: Any

class YamlImportException(Exception): ...
class YamlImportAbortion(Exception): ...

def _is_yaml_mapping(node, tag_constructor): ...
def is_comment(node): ...
def is_assert(node): ...
def is_record(node): ...
def is_python(node): ...
def is_menuitem(node): ...
def is_function(node): ...
def is_report(node): ...
def is_act_window(node): ...
def is_delete(node): ...
def is_context(node): ...
def is_url(node): ...
def is_eval(node): ...
def is_ref(node): ...
def is_string(node): ...

class RecordDictWrapper(dict):
    record: Any
    def __init__(self, record) -> None: ...
    def __getitem__(self, key): ...

class YamlInterpreter:
    cr: Any
    module: Any
    id_map: Any
    mode: Any
    filename: Any
    assertion_report: Any
    noupdate: Any
    loglevel: Any
    uid: Any
    context: Any
    eval_context: Any
    env: Any
    sudo_env: Any
    def __init__(
        self,
        cr,
        module,
        id_map,
        mode,
        filename,
        report: Optional[Any] = ...,
        noupdate: bool = ...,
        loglevel=...,
    ) -> None: ...
    def _log(self, *args, **kwargs) -> None: ...
    def validate_xml_id(self, xml_id) -> None: ...
    def get_id(self, xml_id): ...
    def get_record(self, xml_id): ...
    def get_context(self, node, eval_dict): ...
    def isnoupdate(self, node): ...
    def _get_first_result(self, results, default: bool = ...): ...
    def process_comment(self, node): ...
    def _log_assert_failure(self, msg, *args) -> None: ...
    def _get_assertion_id(self, assertion): ...
    def process_assert(self, node) -> None: ...
    def _coerce_bool(self, value, default: bool = ...): ...
    def create_osv_memory_record(self, record, fields): ...
    def process_record(self, node) -> None: ...
    _dict: Any
    def _create_record(
        self,
        model,
        fields,
        view_info: Optional[Any] = ...,
        parent=...,
        default: bool = ...,
        context: Optional[Any] = ...,
    ): ...
    def process_ref(self, node, field: Optional[Any] = ...): ...
    def process_eval(self, node): ...
    def _eval_field(
        self,
        model,
        field_name,
        expression,
        view_info: bool = ...,
        parent=...,
        default: bool = ...,
        context: Optional[Any] = ...,
    ): ...
    def process_context(self, node) -> None: ...
    def process_python(self, node) -> None: ...
    def _eval_params(self, model, params): ...
    def process_function(self, node): ...
    def _set_group_values(self, node, values) -> None: ...
    def process_menuitem(self, node) -> None: ...
    def process_act_window(self, node) -> None: ...
    def process_delete(self, node) -> None: ...
    def process_url(self, node) -> None: ...
    def process_report(self, node) -> None: ...
    def process_none(self) -> None: ...
    def process(self, yaml_string) -> None: ...
    def _process_node(self, node) -> None: ...
    def _log_node(self, node, is_preceded_by_comment): ...

def yaml_import(
    cr,
    module,
    yamlfile,
    kind,
    idref: Optional[Any] = ...,
    mode: str = ...,
    noupdate: bool = ...,
    report: Optional[Any] = ...,
) -> None: ...

convert_yaml_import = yaml_import