from typing import Any

from odoo.report.interface import report_int

class report_printscreen_list(report_int):
    def _parse_node(self, root_node): ...
    def _parse_string(self, view): ...
    title: Any
    def create(self, cr, uid, ids, datas, context: Any | None = ...): ...
    obj: Any
    def _create_table(
        self, uid, ids, fields, fields_order, results, context, title: str = ...
    ): ...
