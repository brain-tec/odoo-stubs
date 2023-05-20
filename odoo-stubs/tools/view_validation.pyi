from ast import expr as _expr
from re import Pattern
from typing import Callable, TypeVar

from lxml.etree import RelaxNG, _Element

from ..api import Environment
from ..fields import Field

_CallableT = TypeVar("_CallableT", bound=Callable)

ATTRS_WITH_FIELD_NAMES: set[str]
READONLY: Pattern

def field_is_editable(field: Field, node: _Element) -> bool: ...
def get_attrs_field_names(
    env: Environment, arch: _Element, model, editable
) -> list: ...
def valid_view(arch: _Element, **kwargs) -> bool: ...
def validate(*view_types: str) -> Callable[[_CallableT], _CallableT]: ...
def relaxng(view_type: str) -> RelaxNG: ...
def schema_valid(arch: _Element, **kwargs) -> bool: ...
def valid_searchpanel(arch: _Element, **kwargs) -> bool: ...
def valid_searchpanel_domain_select(arch: _Element, **kwargs) -> bool: ...
def valid_searchpanel_domain_fields(arch: _Element, **kwargs) -> bool: ...
def valid_page_in_book(arch: _Element, **kwargs) -> bool: ...
def valid_field_in_graph(arch: _Element, **kwargs) -> bool: ...
def valid_field_in_tree(arch: _Element, **kwargs) -> bool: ...
def valid_att_in_field(arch: _Element, **kwargs) -> bool: ...
def valid_att_in_label(arch: _Element, **kwargs) -> bool: ...
def valid_att_in_form(arch: _Element, **kwargs) -> bool: ...
def valid_type_in_colspan(arch: _Element, **kwargs) -> bool: ...
def valid_type_in_col(arch: _Element, **kwargs) -> bool: ...
def valid_alternative_image_text(arch: _Element, **kwargs) -> bool: ...
def valid_simili_button(arch: _Element, **kwargs) -> bool: ...
def valid_simili_dropdown(arch: _Element, **kwargs) -> bool: ...
def valid_simili_progressbar(arch: _Element, **kwargs) -> bool: ...
def valid_dialog(arch: _Element, **kwargs) -> bool: ...
def valid_simili_tabpanel(arch: _Element, **kwargs) -> bool: ...
def valid_simili_tab(arch: _Element, **kwargs) -> bool: ...
def valid_simili_tablist(arch: _Element, **kwargs) -> bool: ...
def valid_focusable_button(arch: _Element, **kwargs) -> bool: ...
def valid_prohibited_none_role(arch: _Element, **kwargs) -> bool: ...
def valid_alerts(arch: _Element, **kwargs) -> bool: ...
