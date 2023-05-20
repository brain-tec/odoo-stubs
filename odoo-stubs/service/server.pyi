from typing import Any, Optional

import werkzeug.serving

INOTIFY_LISTEN_EVENTS: Any
SLEEP_INTERVAL: int

def memory_info(process): ...
def empty_pipe(fd) -> None: ...

class LoggingBaseWSGIServerMixIn:
    def handle_error(self, request, client_address) -> None: ...

class BaseWSGIServerNoBind(LoggingBaseWSGIServerMixIn, werkzeug.serving.BaseWSGIServer):
    def __init__(self, app) -> None: ...
    def server_activate(self) -> None: ...

class RequestHandler(werkzeug.serving.WSGIRequestHandler):
    def setup(self) -> None: ...

class ThreadedWSGIServerReloadable(
    LoggingBaseWSGIServerMixIn, werkzeug.serving.ThreadedWSGIServer
):
    max_http_threads: Any
    http_threads_sem: Any
    def __init__(self, host, port, app) -> None: ...
    reload_socket: bool
    socket: Any
    def server_bind(self) -> None: ...
    def server_activate(self) -> None: ...
    def shutdown_request(self, request) -> None: ...

class FSWatcherBase:
    def handle_file(self, path): ...

class FSWatcherWatchdog(FSWatcherBase):
    observer: Any
    def __init__(self) -> None: ...
    def dispatch(self, event) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...

class FSWatcherInotify(FSWatcherBase):
    started: bool
    watcher: Any
    def __init__(self) -> None: ...
    def run(self) -> None: ...
    thread: Any
    def start(self) -> None: ...
    def stop(self) -> None: ...

class CommonServer:
    app: Any
    interface: Any
    port: Any
    pid: Any
    def __init__(self, app) -> None: ...
    def close_socket(self, sock) -> None: ...

class ThreadedServer(CommonServer):
    main_thread_id: Any
    quit_signals_received: int
    httpd: Any
    def __init__(self, app) -> None: ...
    def signal_handler(self, sig, frame) -> None: ...
    def cron_thread(self, number) -> None: ...
    def cron_spawn(self) -> None: ...
    def http_thread(self): ...
    def http_spawn(self) -> None: ...
    def start(self, stop: bool = ...): ...
    def stop(self) -> None: ...
    def run(self, preload: Optional[Any] = ..., stop: bool = ...): ...
    def reload(self) -> None: ...

class GeventServer(CommonServer):
    port: Any
    httpd: Any
    def __init__(self, app) -> None: ...
    def process_limits(self) -> None: ...
    ppid: Any
    def watchdog(self, beat: int = ...) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def run(self, preload, stop) -> None: ...

class PreforkServer(CommonServer):
    address: Any
    population: Any
    timeout: Any
    limit_request: Any
    cron_timeout: Any
    beat: int
    app: Any
    pid: Any
    socket: Any
    workers_http: Any
    workers_cron: Any
    workers: Any
    generation: int
    queue: Any
    long_polling_pid: Any
    def __init__(self, app) -> None: ...
    def pipe_new(self): ...
    def pipe_ping(self, pipe) -> None: ...
    def signal_handler(self, sig, frame) -> None: ...
    def worker_spawn(self, klass, workers_registry): ...
    def long_polling_spawn(self) -> None: ...
    def worker_pop(self, pid) -> None: ...
    def worker_kill(self, pid, sig) -> None: ...
    def process_signals(self) -> None: ...
    def process_zombie(self) -> None: ...
    def process_timeout(self) -> None: ...
    def process_spawn(self) -> None: ...
    def sleep(self) -> None: ...
    pipe: Any
    def start(self) -> None: ...
    def stop(self, graceful: bool = ...) -> None: ...
    def run(self, preload, stop): ...

class Worker:
    multi: Any
    watchdog_time: Any
    watchdog_pipe: Any
    eintr_pipe: Any
    watchdog_timeout: Any
    ppid: Any
    pid: Any
    alive: bool
    request_max: Any
    request_count: int
    def __init__(self, multi) -> None: ...
    def setproctitle(self, title: str = ...) -> None: ...
    def close(self) -> None: ...
    def signal_handler(self, sig, frame) -> None: ...
    def signal_time_expired_handler(self, n, stack) -> None: ...
    def sleep(self) -> None: ...
    def check_limits(self) -> None: ...
    def process_work(self) -> None: ...
    def start(self) -> None: ...
    def stop(self) -> None: ...
    def run(self) -> None: ...

class WorkerHTTP(Worker):
    sock_timeout: Any
    def __init__(self, multi) -> None: ...
    def process_request(self, client, addr) -> None: ...
    def process_work(self) -> None: ...
    server: Any
    def start(self) -> None: ...

class WorkerCron(Worker):
    db_index: int
    watchdog_timeout: Any
    def __init__(self, multi) -> None: ...
    def sleep(self) -> None: ...
    def process_work(self) -> None: ...
    def start(self) -> None: ...

server: Any

def load_server_wide_modules() -> None: ...
def load_test_file_yml(registry, test_file) -> None: ...
def load_test_file_py(registry, test_file) -> None: ...
def preload_registries(dbnames): ...
def start(preload: Optional[Any] = ..., stop: bool = ...): ...
def restart() -> None: ...
