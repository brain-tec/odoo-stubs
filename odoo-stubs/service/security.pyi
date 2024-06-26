from typing import Literal

from ..api import Environment
from ..http import OpenERPSession

def check(db: str, uid: int, passwd: str) -> None: ...
def compute_session_token(
    session: OpenERPSession, env: Environment
) -> str | Literal[False]: ...
def check_session(session: OpenERPSession, env: Environment) -> bool: ...
