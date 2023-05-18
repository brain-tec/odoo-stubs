from typing import Any

warn_msg: Any

class EmailParser:
    headers: Any
    dispatcher: Any
    def __init__(self, headers, dispatcher) -> None: ...
    def parse(self, msg) -> None: ...

class CommandDispatcher:
    receiver: Any
    def __init__(self, receiver) -> None: ...
    def __call__(self, request): ...

class RPCProxy:
    rpc: Any
    user_id: Any
    passwd: Any
    def __init__(
        self, uid, passwd, host: str = ..., port: int = ..., path: str = ...
    ) -> None: ...
    def __call__(self, request): ...

class ReceiverEmail2Event:
    email_re: Any
    project_re: Any
    rpc: Any
    def __init__(self, rpc) -> None: ...
    def get_addresses(self, headers, msg): ...
    def get_partners(self, headers, msg): ...
    def __call__(self, request) -> None: ...
    def save_mail(self, msg, subject, partners) -> None: ...
