from typing import Any
from zipfile import ZIP_DEFLATED as ZIP_DEFLATED
from zipfile import PyZipFile as PyZipFile

from ..tools.translate import _ as _

class Graph(dict):
    def add_node(self, name, info): ...
    def update_from_db(self, cr) -> None: ...
    def add_module(self, cr, module, force: Any | None = ...) -> None: ...
    def add_modules(self, cr, module_list, force: Any | None = ...): ...
    def __iter__(self): ...

class Node:
    def __new__(cls, name, graph, info): ...
    name: Any
    graph: Any
    info: Any
    children: Any
    depth: int
    def __init__(self, name, graph, info) -> None: ...
    @property
    def data(self): ...
    def add_child(self, name, info): ...
    def __setattr__(self, name, value) -> None: ...
    def __iter__(self): ...
