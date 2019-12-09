# Stubs for odoo.tools.func (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

class lazy_property:
    fget: Any = ...
    def __init__(self, fget: Any) -> None: ...
    def __get__(self, obj: Any, cls: Any): ...
    @property
    def __doc__(self): ...
    @staticmethod
    def reset_all(obj: Any) -> None: ...

class lazy_classproperty(lazy_property):
    def __get__(self, obj: Any, cls: Any): ...

def conditional(condition: Any, decorator: Any): ...
def synchronized(lock_attr: str = ...): ...

class _ClassProperty(property):
    def __get__(self, cls: Any, owner: Any): ...

def classproperty(func: Any): ...

class lazy:
    def __init__(self, func: Any, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, name: Any): ...
    def __setattr__(self, name: Any, value: Any): ...
    def __delattr__(self, name: Any): ...
    def __bytes__(self): ...
    def __format__(self, format_spec: Any): ...
    def __lt__(self, other: Any): ...
    def __le__(self, other: Any): ...
    def __eq__(self, other: Any): ...
    def __ne__(self, other: Any): ...
    def __gt__(self, other: Any): ...
    def __ge__(self, other: Any): ...
    def __hash__(self): ...
    def __bool__(self): ...
    def __call__(self, *args: Any, **kwargs: Any): ...
    def __len__(self): ...
    def __getitem__(self, key: Any): ...
    def __missing__(self, key: Any): ...
    def __setitem__(self, key: Any, value: Any) -> None: ...
    def __delitem__(self, key: Any) -> None: ...
    def __iter__(self): ...
    def __reversed__(self): ...
    def __contains__(self, key: Any): ...
    def __add__(self, other: Any): ...
    def __sub__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def __matmul__(self, other: Any): ...
    def __truediv__(self, other: Any): ...
    def __floordiv__(self, other: Any): ...
    def __mod__(self, other: Any): ...
    def __divmod__(self, other: Any): ...
    def __pow__(self, other: Any): ...
    def __lshift__(self, other: Any): ...
    def __rshift__(self, other: Any): ...
    def __and__(self, other: Any): ...
    def __xor__(self, other: Any): ...
    def __or__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __rsub__(self, other: Any): ...
    def __rmul__(self, other: Any): ...
    def __rmatmul__(self, other: Any): ...
    def __rtruediv__(self, other: Any): ...
    def __rfloordiv__(self, other: Any): ...
    def __rmod__(self, other: Any): ...
    def __rdivmod__(self, other: Any): ...
    def __rpow__(self, other: Any): ...
    def __rlshift__(self, other: Any): ...
    def __rrshift__(self, other: Any): ...
    def __rand__(self, other: Any): ...
    def __rxor__(self, other: Any): ...
    def __ror__(self, other: Any): ...
    def __iadd__(self, other: Any): ...
    def __isub__(self, other: Any): ...
    def __imul__(self, other: Any): ...
    def __imatmul__(self, other: Any): ...
    def __itruediv__(self, other: Any): ...
    def __ifloordiv__(self, other: Any): ...
    def __imod__(self, other: Any): ...
    def __ipow__(self, other: Any): ...
    def __ilshift__(self, other: Any): ...
    def __irshift__(self, other: Any): ...
    def __iand__(self, other: Any): ...
    def __ixor__(self, other: Any): ...
    def __ior__(self, other: Any): ...
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
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any): ...
    def __await__(self): ...
    def __aiter__(self): ...
    def __anext__(self): ...
    def __aenter__(self): ...
    def __aexit__(self, exc_type: Any, exc_value: Any, traceback: Any): ...
