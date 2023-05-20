from email.message import Message
from re import Pattern
from typing import Any, FrozenSet, Literal

from markupsafe import Markup

tags_to_kill: list[str]
tags_to_remove: list[str]
allowed_tags: FrozenSet
safe_attrs: FrozenSet

def html_sanitize(
    src: str,
    silent: bool = ...,
    sanitize_tags: bool = ...,
    sanitize_attributes: bool = ...,
    sanitize_style: bool = ...,
    strip_style: bool = ...,
    strip_classes: bool = ...,
    sanitize_form: bool = ...,
) -> Markup: ...
def html_keep_url(text: str) -> str: ...
def html2plaintext(
    html: str, body_id: str | None = ..., encoding: str = ...
) -> str: ...
def plaintext2html(text: str, container_tag: str = ...) -> Markup: ...
def append_content_to_html(
    html: str,
    content: str,
    plaintext: bool = ...,
    preserve: bool = ...,
    container_tag: str = ...,
) -> Markup: ...

email_re: Pattern
single_email_re: Pattern
mail_header_msgid_re: Pattern
email_addr_escapes_re: Pattern

def generate_tracking_message_id(res_id: str) -> str: ...
def email_send(
    email_from: str,
    email_to: str,
    subject: str,
    body: str,
    email_cc: str | None = ...,
    email_bcc: str | None = ...,
    reply_to: bool = ...,
    attachments: Any | None = ...,
    message_id: Any | None = ...,
    references: Any | None = ...,
    openobject_id: bool = ...,
    debug: bool = ...,
    subtype: str = ...,
    headers: Any | None = ...,
    smtp_server: Any | None = ...,
    smtp_port: Any | None = ...,
    ssl: bool = ...,
    smtp_user: Any | None = ...,
    smtp_password: Any | None = ...,
    cr: Any | None = ...,
    uid: Any | None = ...,
): ...
def email_split_tuples(text: str) -> list[str]: ...
def email_split(text: str) -> list[str]: ...
def email_split_and_format(text: str) -> list[str]: ...
def email_normalize(text: str) -> str | Literal[False]: ...
def email_escape_char(email_address: str) -> str: ...
def email_domain_extract(email: str) -> str | Literal[False]: ...
def decode_smtp_header(smtp_header, quoted: bool = ...) -> str: ...
def decode_message_header(
    message: Message, header: str, separator: str = ..., quoted: bool = ...
) -> str: ...
def formataddr(pair: tuple[str, str], charset: str = ...) -> str: ...
def encapsulate_email(old_email: str, new_email: str) -> str: ...
