from typing import Any, Optional

def existing_tables(cr, tablenames): ...
def table_exists(cr, tablename): ...
def table_kind(cr, tablename): ...
def create_model_table(cr, tablename, comment: Optional[Any] = ...) -> None: ...
def table_columns(cr, tablename): ...
def column_exists(cr, tablename, columnname): ...
def create_column(
    cr, tablename, columnname, columntype, comment: Optional[Any] = ...
) -> None: ...
def rename_column(cr, tablename, columnname1, columnname2) -> None: ...
def convert_column(cr, tablename, columnname, columntype) -> None: ...
def set_not_null(cr, tablename, columnname) -> None: ...
def drop_not_null(cr, tablename, columnname) -> None: ...
def constraint_definition(cr, tablename, constraintname): ...
def add_constraint(cr, tablename, constraintname, definition) -> None: ...
def drop_constraint(cr, tablename, constraintname) -> None: ...
def add_foreign_key(cr, tablename1, columnname1, tablename2, columnname2, ondelete): ...
def fix_foreign_key(cr, tablename1, columnname1, tablename2, columnname2, ondelete): ...
def index_exists(cr, indexname): ...
def create_index(cr, indexname, tablename, expressions) -> None: ...
def create_unique_index(cr, indexname, tablename, expressions) -> None: ...
def drop_index(cr, indexname, tablename) -> None: ...
def drop_view_if_exists(cr, viewname) -> None: ...
def escape_psql(to_escape): ...
def pg_varchar(size: int = ...): ...
def reverse_order(order): ...
