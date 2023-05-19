from typing import Any, Optional

def round(f): ...

round = round

def _float_check_precision(
    precision_digits: Optional[Any] = ..., precision_rounding: Optional[Any] = ...
): ...
def float_round(
    value,
    precision_digits: Optional[Any] = ...,
    precision_rounding: Optional[Any] = ...,
    rounding_method: str = ...,
): ...
def float_is_zero(
    value,
    precision_digits: Optional[Any] = ...,
    precision_rounding: Optional[Any] = ...,
): ...
def float_compare(
    value1,
    value2,
    precision_digits: Optional[Any] = ...,
    precision_rounding: Optional[Any] = ...,
): ...
def float_repr(value, precision_digits): ...

_float_repr = float_repr

def float_split_str(value, precision_digits): ...
def float_split(value, precision_digits): ...
