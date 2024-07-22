from typing import Iterable, Iterator

from ..api import Environment
from . import SQL

class Query:
    limit: int | None
    offset: int | None
    def __init__(
        self, env: Environment, alias: str, table: SQL | None = ...
    ) -> None: ...
    def make_alias(self, alias: str, link: str) -> str: ...
    def add_table(self, alias: str, table: SQL | None = ...) -> None: ...
    def add_join(
        self, kind: str, alias: str, table: str | SQL | None, condition: SQL
    ) -> None: ...
    def add_where(
        self, where_clause: str | SQL, where_params: Iterable = ...
    ) -> None: ...
    def join(
        self,
        lhs_alias: str,
        lhs_column: str,
        rhs_table: str | SQL,
        rhs_column: str,
        link: str,
    ) -> str: ...
    def left_join(
        self,
        lhs_alias: str,
        lhs_column: str,
        rhs_table: str,
        rhs_column: str,
        link: str,
    ) -> str: ...
    @property
    def order(self) -> SQL | None: ...
    @order.setter
    def order(self, value: SQL | str | None): ...
    @property
    def table(self) -> str: ...
    @property
    def from_clause(self) -> SQL: ...
    @property
    def where_clause(self) -> SQL: ...
    def is_empty(self) -> bool: ...
    def select(self, *args: str | SQL) -> SQL: ...
    def subselect(self, *args: str | SQL) -> SQL: ...
    def get_result_ids(self) -> tuple[int, ...]: ...
    def set_result_ids(self, ids, ordered: bool = ...) -> None: ...
    def __bool__(self) -> bool: ...
    def __len__(self) -> int: ...
    def __iter__(self) -> Iterator[int]: ...
