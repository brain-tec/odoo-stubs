from io import BytesIO
from re import Pattern
from typing import Any, BinaryIO, Iterable

from odoo.addons.base.models.ir_attachment import IrAttachment
from PyPDF2 import PdfFileReader, PdfFileWriter
from PyPDF2.generic import ArrayObject as ArrayObject
from PyPDF2.utils import b_ as b_

DEFAULT_PDF_DATETIME_FORMAT: str
REGEX_SUBTYPE_UNFORMATED: Pattern
REGEX_SUBTYPE_FORMATED: Pattern

class BrandedFileWriter(PdfFileWriter):
    def __init__(self) -> None: ...

PdfFileWriter = BrandedFileWriter

def merge_pdf(pdf_data: Iterable[bytes]) -> bytes: ...
def rotate_pdf(pdf: bytes) -> bytes: ...
def to_pdf_stream(attachment: "IrAttachment") -> BytesIO: ...
def add_banner(
    pdf_stream: str | BinaryIO,
    text: str | None = ...,
    logo: bool = ...,
    thickness: float = ...,
) -> BytesIO: ...

class OdooPdfFileReader(PdfFileReader):
    def getAttachments(self) -> Iterable[tuple[Any, Any]]: ...

class OdooPdfFileWriter(PdfFileWriter):
    is_pdfa: bool
    def __init__(self, *args, **kwargs):
        None
    def addAttachment(self, fname: str, fdata, subtype: str | None = ...) -> None: ...
    def embed_odoo_attachment(
        self, attachment: "IrAttachment", subtype: str | None = ...
    ) -> None: ...
    def cloneReaderDocumentRoot(self, reader: PdfFileReader) -> None: ...
    def convert_to_pdfa(self) -> None: ...
    def add_file_metadata(self, metadata_content: bytes) -> None: ...
