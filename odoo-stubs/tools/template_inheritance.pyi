from typing import Any, Callable

from lxml.etree import _Element

def add_text_before(node: _Element, text: str | None) -> None: ...
def add_text_inside(node: _Element, text: str | None) -> None: ...
def remove_element(node: _Element) -> None: ...
def locate_node(arch: _Element, spec: _Element) -> _Element: ...
def apply_inheritance_specs(
    source: _Element,
    specs_tree: _Element,
    inherit_branding: bool = ...,
    pre_locate: Callable[[_Element], Any] = ...,
) -> _Element: ...
