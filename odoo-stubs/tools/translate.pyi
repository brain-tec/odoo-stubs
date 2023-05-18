import csv
from re import Match, Pattern
from tarfile import TarFile
from types import FrameType
from typing import IO, Any, BinaryIO, Callable, Container, Iterable, Iterator, NoReturn

from lxml.etree import HTMLParser, _Element
from polib import POFile

from ..sql_db import Connection, Cursor
from .pycompat import _CsvWriter

WEB_TRANSLATION_COMMENT: str
SKIPPED_ELEMENTS: tuple[str, ...]
_LOCALE2WIN32: dict[str, str]
ENGLISH_SMALL_WORDS: set[str]

class UNIX_LINE_TERMINATOR(csv.excel):
    lineterminator: str

def encode(s: str) -> str: ...

TRANSLATED_ELEMENTS: set[str]
TRANSLATED_ATTRS: set[str]
avoid_pattern: Pattern
node_pattern: Pattern

def translate_xml_node(
    node: _Element,
    callback: Callable[[str], str | None],
    parse: Callable[[str], _Element],
    serialize: Callable[[_Element], str],
) -> _Element: ...
def parse_xml(text: str) -> _Element: ...
def serialize_xml(node: _Element) -> str: ...

_HTML_PARSER: HTMLParser

def parse_html(text: str) -> _Element: ...
def serialize_html(node: _Element) -> str: ...
def xml_translate(callback: Callable[[str], str | None], value: str) -> str: ...
def html_translate(callback: Callable[[str], str | None], value: str) -> str: ...
def translate(
    cr: Cursor, name: str, source_type: str, lang: str, source: str | None = ...
) -> str: ...
def translate_sql_constraint(cr: Cursor, key: str, lang: str) -> str: ...

class GettextAlias:
    def _get_db(self) -> Connection | None: ...
    def _get_cr(
        self, frame: FrameType, allow_create: bool = ...
    ) -> tuple[Cursor, bool]: ...
    def _get_uid(self, frame: FrameType) -> int: ...
    def _get_lang(self, frame: FrameType) -> str: ...
    def __call__(self, source: str) -> str: ...
    def _get_translation(self, source: str) -> str: ...

class _lt:
    _source: str
    def __init__(self, source: str) -> None: ...
    def __str__(self) -> str: ...
    def __eq__(self, other) -> NoReturn: ...
    def __lt__(self, other) -> NoReturn: ...
    def __add__(self, other: str | _lt) -> str: ...
    def __radd__(self, other: str) -> str: ...

_: GettextAlias

def quote(s: str) -> str: ...

re_escaped_char: Pattern
re_escaped_replacements: dict[str, str]

def _sub_replacement(match_obj: Match) -> str: ...
def unquote(str: str) -> str: ...
def TranslationFileReader(
    source: IO, fileformat: str = ...
) -> CSVFileReader | PoFileReader: ...

class CSVFileReader:
    source: csv.DictReader
    prev_code_src: str
    def __init__(self, source: IO) -> None: ...
    def __iter__(self) -> Iterator[csv.DictReader]: ...

class PoFileReader:
    pofile: POFile
    def __init__(self, source: str | IO): ...
    def __iter__(self) -> Iterator[dict[str, Any]]: ...

def TranslationFileWriter(
    target,
    fileformat: str = ...,
    lang: str | None = ...,
    modules: Iterable[str] | None = ...,
) -> CSVFileWriter | PoFileWriter | TarFileWriter: ...

class CSVFileWriter:
    writer: _CsvWriter
    def __init__(self, target: BinaryIO) -> None: ...
    def write_rows(self, rows: Iterable) -> None: ...

class PoFileWriter:
    buffer: IO
    lang: str
    po: POFile
    def __init__(self, target: IO, modules: Iterable[str], lang: str) -> None: ...
    def write_rows(self, rows: Iterable) -> None: ...
    def add_entry(
        self, modules, tnrs, source, trad, comments: Iterable[str] | None = ...
    ) -> None: ...

class TarFileWriter:
    tar: TarFile
    lang: str
    def __init__(self, target: IO, lang: str) -> None: ...
    def write_rows(self, rows: Iterable) -> None: ...

def trans_export(
    lang: str, modules: list[str], buffer, format: str, cr: Cursor
) -> None: ...
def trans_parse_rml(de: Iterable) -> list[bytes]: ...
def _push(callback: Callable[[str, int], Any], term: str, source_line: int) -> None: ...
def in_modules(object_name: str, modules: Container[str]) -> bool: ...
def _extract_translatable_qweb_terms(
    element: _Element, callback: Callable[[str, int], Any]
) -> None: ...
def babel_extract_qweb(fileobj: IO, keywords, comment_tags, options) -> list[tuple]: ...
def trans_generate(lang: str, modules, cr: Cursor) -> list: ...
def trans_load(
    cr: Cursor,
    filename: str,
    lang: str,
    verbose: bool = ...,
    module_name: str | None = ...,
    context: dict | None = ...,
) -> None: ...
def trans_load_data(
    cr: Cursor,
    fileobj: IO,
    fileformat: str,
    lang_name: str | None = ...,
    verbose: bool = ...,
    module_name: str | None = ...,
    context: dict | None = ...,
) -> None: ...
def get_locales(lang: str | None = ...) -> None: ...
def resetlocale() -> str: ...
def load_language(cr: Cursor, lang: str) -> None: ...
