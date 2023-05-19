import ctypes
import os
from typing import Any, Optional

from odoo.release import nt_service_name as nt_service_name

def listdir(dir, recursive: bool = ...): ...
def walksymlinks(top, topdown: bool = ..., onerror: Optional[Any] = ...) -> None: ...
def tempdir() -> None: ...
def zip_dir(
    path, stream, include_dir: bool = ..., fnct_sort: Optional[Any] = ...
) -> None: ...

getppid = os.getppid
is_running_as_nt_service: Any
_TH32CS_SNAPPROCESS: int

class _PROCESSENTRY32(ctypes.Structure):
    _fields_: Any
