from datetime import datetime
from threading import Thread
from types import FrameType
from typing import Any, Callable, ContextManager, Generic, Iterable, TypeVar

from ..sql_db import Cursor

_T = TypeVar("_T")

real_datetime_now: Callable[..., datetime]
real_time: Callable[[], float]

def get_current_frame(thread: Thread | None = ...) -> FrameType: ...
def stack_size() -> int: ...
def make_session(name: str = ...) -> str: ...
def force_hook() -> None: ...

class Collector:
    name: str | None
    @classmethod
    def __init_subclass__(cls) -> None: ...
    @classmethod
    def make(cls, name: str, *args, **kwargs): ...
    profiler: Profiler | None
    def __init__(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add(self, entry: dict | None = ..., frame: FrameType | None = ...) -> None: ...
    def post_process(self) -> None: ...
    @property
    def entries(self) -> list[dict]: ...

class SQLCollector(Collector):
    name: str
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def hook(self, cr: Cursor, query, params, query_start, query_time) -> None: ...

class PeriodicCollector(Collector):
    name: str
    active: bool
    frame_interval: float
    thread: Thread
    last_frame: FrameType | None
    def __init__(self, interval: float = ...) -> None: ...
    def run(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def add(self, entry: dict | None = ..., frame: FrameType | None = ...) -> None: ...

class SyncCollector(Collector):
    name: str
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def hook(self, _frame: FrameType, event: str, _arg: Any | None = ...): ...
    def post_process(self) -> None: ...

class QwebTracker:
    @classmethod
    def wrap_render(cls, method_render: _T) -> _T: ...
    @classmethod
    def wrap_compile(cls, method_compile: _T) -> _T: ...
    @classmethod
    def wrap_compile_directive(cls, method_compile_directive: _T) -> _T: ...
    execution_context_enabled: Any
    qweb_hooks: Iterable[Callable]
    context_stack: list[ExecutionContext]
    cr: Cursor
    view_id: Any
    def __init__(self, view_id, arch, cr) -> None: ...
    def enter_directive(self, directive, attrib, xpath) -> None: ...
    def leave_directive(self) -> None: ...

class QwebCollector(Collector):
    name: str
    events: list
    hook: Callable
    def __init__(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def post_process(self) -> None: ...

class ExecutionContext:
    context: dict
    previous_context: tuple | None
    def __init__(self, **context) -> None: ...
    def __enter__(self) -> None: ...
    def __exit__(self, *_args) -> None: ...

class Profiler:
    start_time: int
    duration: int
    profile_session: Any
    description: str | None
    init_frame: FrameType | None
    init_stack_trace: list[tuple[str, int, str, str]] | None
    init_thread: Thread | None
    disable_gc: bool
    filecache: dict
    params: Any
    profile_id: Any
    db: str | None
    collectors: list[Collector]
    def __init__(
        self,
        collectors: list[str | Collector] | None = ...,
        db: str | None = ...,
        profile_session: Any | None = ...,
        description: str | None = ...,
        disable_gc: bool = ...,
        params: Any | None = ...,
    ) -> None: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, *args) -> None: ...
    def entry_count(self) -> int: ...
    def format_path(self, path: str) -> str: ...
    def json(self) -> str: ...

class Nested(Generic[_T]):
    profiler: Profiler
    context_manager: ContextManager[_T]
    def __init__(
        self, profiler: Profiler, context_manager: ContextManager[_T]
    ) -> None: ...
    def __enter__(self) -> _T: ...
    def __exit__(self, exc_type, exc_value, traceback): ...
