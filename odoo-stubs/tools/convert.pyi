from io import BufferedReader
from typing import Any, Callable, TextIO

from lxml.etree import _Element

from ..api import Environment
from ..sql_db import Cursor
from .misc import ustr as ustr

__all__ = [
    "convert_file",
    "convert_sql_import",
    "convert_csv_import",
    "convert_xml_import",
]

safe_eval: Callable

class ParseError(Exception): ...

class RecordDictWrapper(dict):
    record: Any
    def __init__(self, record) -> None: ...
    def __getitem__(self, key): ...

def _get_idref(self, env: Environment, model_str: str, idref: dict) -> dict: ...
def _fix_multiple_roots(node: _Element) -> None: ...
def _eval_xml(self, node: _Element, env: Environment): ...
def str2bool(value) -> bool: ...
def nodeattr2bool(node: _Element, attr, default: bool = ...) -> bool: ...

class xml_import:
    def get_env(
        self, node: _Element, eval_context: dict | None = ...
    ) -> Environment: ...
    def make_xml_id(self, xml_id: str) -> str: ...
    def _test_xml_id(self, xml_id: str) -> None: ...
    def _tag_delete(self, rec: _Element) -> None: ...
    def _tag_function(self, rec: _Element) -> None: ...
    def _tag_menuitem(self, rec: _Element, parent: Any | None = ...) -> None: ...
    def _tag_record(
        self, rec: _Element, extra_vals: dict | None = ...
    ) -> tuple[str, int] | None: ...
    def _tag_template(self, el: _Element) -> tuple[str, int] | None: ...
    def id_get(self, id_str: str, raise_if_not_found: bool = ...) -> int | None: ...
    def model_id_get(
        self, id_str: str, raise_if_not_found: bool = ...
    ) -> tuple[Any, Any]: ...
    def _tag_root(self, el: _Element) -> None: ...
    @property
    def env(self) -> Environment: ...
    @property
    def noupdate(self) -> bool: ...
    mode: str
    module: str
    envs: list[Environment]
    idref: dict
    _noupdate: list[bool]
    xml_filename: str
    _tags: dict[str, Callable]
    def __init__(
        self,
        env: Environment,
        module: str,
        idref: dict,
        mode: str,
        noupdate: bool = ...,
        xml_filename: str | None = ...,
    ) -> None: ...
    def parse(self, de: _Element) -> None: ...
    DATA_ROOTS: list[str]

def convert_file(
    env: Environment,
    module: str,
    filename: str,
    idref: dict,
    mode: str = ...,
    noupdate: bool = ...,
    kind: str | None = ...,
    pathname: str | None = ...,
) -> None: ...
def convert_sql_import(env: Environment, fp: TextIO) -> None: ...
def convert_csv_import(
    env: Environment,
    module: str,
    fname: str,
    csvcontent: bytes,
    idref: dict | None = ...,
    mode: str = ...,
    noupdate: bool = ...,
) -> None: ...
def convert_xml_import(
    env: Environment,
    module: str,
    xmlfile: str | BufferedReader,
    idref: dict | None = ...,
    mode: str = ...,
    noupdate: bool = ...,
    report: Any | None = ...,
) -> None: ...
