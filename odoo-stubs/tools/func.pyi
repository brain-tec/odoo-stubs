from json import JSONEncoder as JSONEncoder
from typing import Any

class lazy_property:
    fget: Any
    def __init__(self, fget) -> None: ...
    def __get__(self, obj, cls): ...
    @property
    def __doc__(self): ...
    @staticmethod
    def reset_all(obj) -> None: ...

class lazy_classproperty(lazy_property):
    def __get__(self, obj, cls): ...

def conditional(condition, decorator): ...
def synchronized(lock_attr: str = ...): ...
def frame_codeinfo(fframe, back: int = ...): ...
def compose(a, b): ...

class _ClassProperty(property):
    def __get__(self, cls, owner): ...

def classproperty(func): ...

class lazy:
    def __init__(self, func, *args, **kwargs) -> None: ...
    def __getattr__(self, name): ...
    def __setattr__(self, name, value): ...
    def __delattr__(self, name): ...
    def __bytes__(self): ...
    def __format__(self, format_spec): ...
    def __lt__(self, other) -> Any: ...
    def __le__(self, other) -> Any: ...
    def __eq__(self, other) -> Any: ...
    def __ne__(self, other) -> Any: ...
    def __gt__(self, other) -> Any: ...
    def __ge__(self, other) -> Any: ...
    def __hash__(self) -> Any: ...
    def __bool__(self): ...
    def __call__(self, *args, **kwargs): ...
    def __len__(self): ...
    def __getitem__(self, key): ...
    def __missing__(self, key): ...
    def __setitem__(self, key, value) -> None: ...
    def __delitem__(self, key) -> None: ...
    def __iter__(self) -> Any: ...
    def __reversed__(self): ...
    def __contains__(self, key): ...
    def __add__(self, other): ...
    def __sub__(self, other): ...
    def __mul__(self, other): ...
    def __matmul__(self, other): ...
    def __truediv__(self, other): ...
    def __floordiv__(self, other): ...
    def __mod__(self, other): ...
    def __divmod__(self, other): ...
    def __pow__(self, other): ...
    def __lshift__(self, other): ...
    def __rshift__(self, other): ...
    def __and__(self, other): ...
    def __xor__(self, other): ...
    def __or__(self, other): ...
    def __radd__(self, other): ...
    def __rsub__(self, other): ...
    def __rmul__(self, other): ...
    def __rmatmul__(self, other): ...
    def __rtruediv__(self, other): ...
    def __rfloordiv__(self, other): ...
    def __rmod__(self, other): ...
    def __rdivmod__(self, other): ...
    def __rpow__(self, other): ...
    def __rlshift__(self, other): ...
    def __rrshift__(self, other): ...
    def __rand__(self, other): ...
    def __rxor__(self, other): ...
    def __ror__(self, other): ...
    def __iadd__(self, other): ...
    def __isub__(self, other): ...
    def __imul__(self, other): ...
    def __imatmul__(self, other): ...
    def __itruediv__(self, other): ...
    def __ifloordiv__(self, other): ...
    def __imod__(self, other): ...
    def __ipow__(self, other): ...
    def __ilshift__(self, other): ...
    def __irshift__(self, other): ...
    def __iand__(self, other): ...
    def __ixor__(self, other): ...
    def __ior__(self, other): ...
    def __neg__(self): ...
    def __pos__(self): ...
    def __abs__(self): ...
    def __invert__(self): ...
    def __complex__(self): ...
    def __int__(self): ...
    def __float__(self): ...
    def __index__(self): ...
    def __round__(self): ...
    def __trunc__(self): ...
    def __floor__(self): ...
    def __ceil__(self): ...
    def __enter__(self): ...
    def __exit__(self, exc_type, exc_value, traceback): ...
    def __await__(self): ...
    def __aiter__(self): ...
    def __anext__(self): ...
    def __aenter__(self): ...
    def __aexit__(self, exc_type, exc_value, traceback): ...
