from logging import Logger
from typing import Any, Callable, Generator, TypeVar

import werkzeug
from odoo.addons.base.models.res_lang import Lang
from odoo.addons.website.models.website import Website
from werkzeug.exceptions import NotFound
from werkzeug.routing import Map

from .api import Environment
from .modules.registry import Registry
from .sql_db import Cursor
from .tools._vendor import sessions

_T = TypeVar("_T")

rpc_request: Logger
rpc_response: Logger
STATIC_CACHE: int
STATIC_CACHE_LONG: int
ALLOWED_DEBUG_MODES: list[str]
request: HttpRequest | JsonRequest

def replace_request_password(args) -> tuple: ...

NO_POSTMORTEM: tuple[type[Exception], ...]

def dispatch_rpc(service_name: str, method: str, params): ...
def local_redirect(
    path: str, query: dict | None = ..., keep_hash: bool = ..., code: int = ...
) -> werkzeug.Response: ...
def redirect_with_hash(url: str, code: int = ...) -> werkzeug.Response: ...

class WebRequest:
    httprequest: werkzeug.Request
    httpresponse: Response | None
    endpoint: EndPoint | None
    endpoint_arguments: Any
    auth_method: str | None
    website: Website
    website_routing: int
    is_frontend: bool
    is_frontend_multilang: bool
    lang: Lang
    def __init__(self, httprequest: werkzeug.Request) -> None: ...
    @property
    def cr(self) -> Cursor: ...
    @property
    def uid(self) -> int: ...
    @uid.setter
    def uid(self, val) -> None: ...
    @property
    def context(self) -> dict: ...
    @context.setter
    def context(self, val) -> None: ...
    @property
    def env(self) -> Environment: ...
    @property
    def session(self) -> OpenERPSession: ...
    def __enter__(self: _T) -> _T: ...
    def __exit__(self, exc_type, exc_value, traceback) -> None: ...
    def set_handler(self, endpoint: EndPoint, arguments, auth) -> None: ...
    def registry_cr(self) -> Generator[tuple[Registry, Cursor], None, None]: ...
    @property
    def registry(self) -> Registry: ...
    @property
    def db(self) -> str | None: ...
    def csrf_token(self, time_limit: int | None = ...): ...
    def validate_csrf(self, csrf) -> bool: ...

def route(
    route: str | list[str] | None = ...,
    type: str = ...,
    auth: str = ...,
    methods: list[str] = ...,
    cors: str = ...,
    csrf: bool = ...,
    **kw
): ...

class JsonRequest(WebRequest):
    params: dict
    jsonrequest: Any
    context: dict
    def __init__(self, *args) -> None: ...
    def dispatch(self) -> Response: ...

def serialize_exception(e: Exception) -> dict[str, Any]: ...

class HttpRequest(WebRequest):
    params: dict
    def __init__(self, *args) -> None: ...
    def dispatch(self): ...
    def make_response(
        self,
        data,
        headers: list[tuple[str, str]] | None = ...,
        cookies: dict | None = ...,
    ) -> Response: ...
    def render(
        self, template, qcontext: dict | None = ..., lazy: bool = ..., **kw
    ) -> Response: ...
    def not_found(self, description: str | Any | None = ...) -> NotFound: ...

addons_manifest: dict
controllers_per_module: dict[str, list]

class ControllerType(type):
    def __init__(cls, name: str, bases: tuple, attrs: dict) -> None: ...

Controller = ControllerType("Controller", (object,), {})

class EndPoint:
    method: Callable
    original: Callable
    routing: dict
    arguments: dict
    def __init__(self, method, routing) -> None: ...
    @property
    def first_arg_is_req(self) -> bool: ...
    def __call__(self, *args, **kw): ...
    def __eq__(self, other) -> bool: ...
    def __hash__(self) -> int: ...

class AuthenticationError(Exception): ...
class SessionExpiredException(Exception): ...

class OpenERPSession(sessions.Session):
    inited: bool
    modified: bool
    rotate: bool
    def __init__(self, *args, **kwargs) -> None: ...
    def __getattr__(self, attr): ...
    def __setattr__(self, k, v): ...
    pre_uid: int
    uid: int
    db: str | None
    login: str | None
    def authenticate(
        self, db: str, login: str | None = ..., password: str | None = ...
    ) -> int: ...
    session_token: str | None
    def finalize(self) -> None: ...
    def check_security(self) -> None: ...
    def logout(self, keep_db: bool = ...) -> None: ...
    context: dict
    def get_context(self) -> dict: ...
    def save_action(self, action) -> int: ...
    def get_action(self, key: int): ...

def session_gc(session_store: sessions.FilesystemSessionStore) -> None: ...

ODOO_DISABLE_SESSION_GC: bool

class Response(werkzeug.Response):
    default_mimetype: str
    def __init__(self, *args, **kw) -> None: ...
    template: Any
    qcontext: dict
    uid: int
    def set_default(
        self,
        template: Any | None = ...,
        qcontext: dict | None = ...,
        uid: int | None = ...,
    ) -> None: ...
    @property
    def is_qweb(self) -> bool: ...
    def render(self): ...
    def flatten(self) -> None: ...

class DisableCacheMiddleware:
    app: Callable
    def __init__(self, app: Callable) -> None: ...
    def __call__(self, environ: dict, start_response: Callable): ...

class Root:
    def __init__(self) -> None: ...
    @property
    def session_store(self) -> sessions.FilesystemSessionStore: ...
    @property
    def nodb_routing_map(self) -> Map: ...
    def __call__(self, environ: dict, start_response: Callable): ...
    def load_addons(self) -> None: ...
    def setup_session(self, httprequest: werkzeug.Request) -> bool: ...
    def setup_db(self, httprequest: werkzeug.Request) -> None: ...
    def setup_lang(self, httprequest: werkzeug.Request) -> None: ...
    def get_request(
        self, httprequest: werkzeug.Request
    ) -> HttpRequest | JsonRequest: ...
    def get_response(
        self, httprequest: werkzeug.Request, result, explicit_session: bool
    ) -> Any: ...
    def set_csp(self, response: werkzeug.Response) -> None: ...
    def dispatch(self, environ: dict, start_response: Callable): ...
    def get_db_router(self, db: str) -> Map: ...

def db_list(
    force: bool = ..., httprequest: werkzeug.Request | None = ...
) -> list[str]: ...
def db_filter(dbs, httprequest: werkzeug.Request | None = ...) -> list[str]: ...
def db_monodb(httprequest: werkzeug.Request | None = ...) -> str | None: ...
def send_file(
    filepath_or_fp,
    mimetype: str | None = ...,
    as_attachment: bool = ...,
    filename: str | None = ...,
    mtime: Any | None = ...,
    add_etags: bool = ...,
    cache_timeout: int = ...,
    conditional: bool = ...,
) -> Response: ...
def content_disposition(filename: str) -> str: ...
def set_safe_image_headers(headers, content): ...

root: Root
