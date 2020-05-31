from odoo.exceptions import UserError as UserError
from odoo.tools.misc import file_open as file_open
from typing import Any, Optional

def check_with_xsd(tree_or_str: Any, stream: Any) -> None: ...
def _check_with_xsd(tree_or_str: Any, stream: Any) -> None: ...
def create_xml_node_chain(first_parent_node: Any, nodes_list: Any, last_node_value: Optional[Any] = ...): ...
def create_xml_node(parent_node: Any, node_name: Any, node_value: Optional[Any] = ...): ...