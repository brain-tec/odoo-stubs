from typing import Any, Optional

_logger: Any
PG_CONCURRENCY_ERRORS_TO_RETRY: Any
MAX_TRIES_ON_CONCURRENCY_FAILURE: int

def dispatch(method, params): ...
def check(f): ...
def execute_cr(cr, uid, obj, method, *args, **kw): ...
def execute_kw(db, uid, obj, method, args, kw: Optional[Any] = ...): ...
def execute(db, uid, obj, method, *args, **kw): ...
