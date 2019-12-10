# Stubs for odoo.http (Python 3)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional, Union

from werkzeug.contrib.sessions import Session
import werkzeug.wrappers

from .api import Environment
from .sql_db import Cursor

rpc_request: Any
rpc_response: Any
STATIC_CACHE: Any
request: Union['HttpRequest', 'JsonRequest']

def replace_request_password(args: Any): ...

NO_POSTMORTEM: Any

def dispatch_rpc(service_name: Any, method: Any, params: Any): ...
def local_redirect(path: Any, query: Optional[Any] = ..., keep_hash: bool = ..., forward_debug: bool = ..., code: int = ...): ...
def redirect_with_hash(url: Any, code: int = ...): ...

class WebRequest:
    httprequest: werkzeug.wrappers.Request = ...
    httpresponse: Response = ...
    disable_db: bool = ...
    endpoint: Any = ...
    endpoint_arguments: Any = ...
    auth_method: Any = ...
    def __init__(self, httprequest: Any) -> None: ...
    @property
    def cr(self) -> Cursor: ...
    @property
    def uid(self) -> int: ...
    @uid.setter
    def uid(self, val: Any) -> None: ...
    @property
    def context(self): ...
    @context.setter
    def context(self, val: Any) -> None: ...
    @property
    def env(self) -> Environment: ...
    context: Any = ...
    @property
    def lang(self): ...
    @property
    def session(self) -> OpenERPSession: ...
    def __enter__(self): ...
    def __exit__(self, exc_type: Any, exc_value: Any, traceback: Any) -> None: ...
    def set_handler(self, endpoint: Any, arguments: Any, auth: Any) -> None: ...
    @property
    def debug(self): ...
    def registry_cr(self) -> None: ...
    @property
    def registry(self): ...
    @property
    def db(self): ...
    def csrf_token(self, time_limit: int = ...): ...
    def validate_csrf(self, csrf: Any): ...

def route(route: Optional[Any] = ..., **kw: Any): ...

class JsonRequest(WebRequest):
    jsonp_handler: Any = ...
    params: Any = ...
    jsonp: Any = ...
    jsonrequest: Any = ...
    context: Any = ...
    def __init__(self, *args: Any) -> None: ...
    def dispatch(self): ...

def serialize_exception(e: Any): ...

class HttpRequest(WebRequest):
    params: Any = ...
    def __init__(self, *args: Any) -> None: ...
    def dispatch(self): ...
    def make_response(self, data: Any, headers: Optional[Any] = ..., cookies: Optional[Any] = ...): ...
    def render(self, template: Any, qcontext: Optional[Any] = ..., lazy: bool = ..., **kw: Any): ...
    def not_found(self, description: Optional[Any] = ...): ...

addons_manifest: Any
controllers_per_module: Any

class ControllerType(type):
    def __init__(cls, name: Any, bases: Any, attrs: Any) -> None: ...

Controller: Any

class EndPoint:
    method: Any = ...
    original: Any = ...
    routing: Any = ...
    arguments: Any = ...
    def __init__(self, method: Any, routing: Any) -> None: ...
    @property
    def first_arg_is_req(self): ...
    def __call__(self, *args: Any, **kw: Any): ...

def routing_map(modules: Any, nodb_only: Any, converters: Optional[Any] = ...): ...

class AuthenticationError(Exception): ...
class SessionExpiredException(Exception): ...

class OpenERPSession(Session):
    inited: bool = ...
    modified: bool = ...
    rotate: bool = ...
    def __init__(self, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, attr: Any): ...
    def __setattr__(self, k: Any, v: Any): ...
    db: Any = ...
    uid: Any = ...
    login: Any = ...
    session_token: Any = ...
    def authenticate(self, db: Any, login: Optional[Any] = ..., password: Optional[Any] = ..., uid: Optional[Any] = ...): ...
    def check_security(self) -> None: ...
    def logout(self, keep_db: bool = ...) -> None: ...
    context: Any = ...
    def get_context(self): ...
    def save_action(self, action: Any): ...
    def get_action(self, key: Any): ...
    def save_request_data(self) -> None: ...
    def load_request_data(self) -> None: ...

def session_gc(session_store: Any) -> None: ...

class Response(werkzeug.wrappers.Response):
    default_mimetype: str = ...
    def __init__(self, *args: Any, **kw: Any) -> None: ...
    template: Any = ...
    qcontext: Any = ...
    uid: Any = ...
    def set_default(self, template: Optional[Any] = ..., qcontext: Optional[Any] = ..., uid: Optional[Any] = ...) -> None: ...
    @property
    def is_qweb(self): ...
    def render(self): ...
    def flatten(self) -> None: ...

class DisableCacheMiddleware:
    app: Any = ...
    def __init__(self, app: Any) -> None: ...
    def __call__(self, environ: Any, start_response: Any): ...

class Root:
    def __init__(self) -> None: ...
    def session_store(self): ...
    def nodb_routing_map(self): ...
    def __call__(self, environ: Any, start_response: Any): ...
    dispatch: Any = ...
    def load_addons(self) -> None: ...
    def setup_session(self, httprequest: Any): ...
    def setup_db(self, httprequest: Any) -> None: ...
    def setup_lang(self, httprequest: Any) -> None: ...
    def get_request(self, httprequest: Any): ...
    def get_response(self, httprequest: Any, result: Any, explicit_session: Any): ...
    def dispatch(self, environ: Any, start_response: Any): ...
    def get_db_router(self, db: Any): ...

def db_list(force: bool = ..., httprequest: Optional[Any] = ...): ...
def db_filter(dbs: Any, httprequest: Optional[Any] = ...): ...
def db_monodb(httprequest: Optional[Any] = ...): ...
def send_file(filepath_or_fp: Any, mimetype: Optional[Any] = ..., as_attachment: bool = ..., filename: Optional[Any] = ..., mtime: Optional[Any] = ..., add_etags: bool = ..., cache_timeout: Any = ..., conditional: bool = ...): ...
def content_disposition(filename: Any): ...

class CommonController(Controller):
    def gen_session_id(self): ...

root: Any
