from typing import Any, Optional

def _quote(to_quote): ...

class Query:
    tables: Any
    where_clause: Any
    where_clause_params: Any
    joins: Any
    extras: Any
    def __init__(
        self,
        tables: Optional[Any] = ...,
        where_clause: Optional[Any] = ...,
        where_clause_params: Optional[Any] = ...,
        joins: Optional[Any] = ...,
        extras: Optional[Any] = ...,
    ) -> None: ...
    def _get_table_aliases(self): ...
    def _get_alias_mapping(self): ...
    def add_join(
        self,
        connection,
        implicit: bool = ...,
        outer: bool = ...,
        extra: Optional[Any] = ...,
        extra_params: Any = ...,
    ): ...
    def get_sql(self): ...
    def __str__(self): ...
