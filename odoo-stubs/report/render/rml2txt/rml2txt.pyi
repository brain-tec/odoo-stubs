from typing import Any

Font_size: float

def verbose(text) -> None: ...

class textbox:
    posx: Any
    posy: Any
    lines: Any
    curline: str
    endspace: bool
    def __init__(self, x: int = ..., y: int = ...) -> None: ...
    def newline(self) -> None: ...
    def fline(self) -> None: ...
    def appendtxt(self, txt) -> None: ...
    def rendertxt(self, xoffset: int = ...): ...
    def renderlines(self, pad: int = ...): ...
    def haplines(self, arr, offset, cc: str = ...) -> None: ...

class _flowable:
    _tags: Any
    template: Any
    doc: Any
    localcontext: Any
    nitags: Any
    tbox: Any
    def __init__(self, template, doc, localcontext) -> None: ...
    def warn_nitag(self, tag) -> None: ...
    def _tag_page_break(self, node): ...
    def _tag_next_template(self, node): ...
    def _tag_next_frame(self, node): ...
    def _tag_title(self, node): ...
    def _tag_spacer(self, node): ...
    tb: Any
    def _tag_table(self, node): ...
    def _tag_para(self, node) -> None: ...
    def _tag_section(self, node) -> None: ...
    def _tag_font(self, node) -> None: ...
    def rec_render_cnodes(self, node) -> None: ...
    def rec_render(self, node) -> None: ...
    def render(self, node): ...

class _rml_tmpl_tag:
    def __init__(self, *args) -> None: ...
    def tag_start(self): ...
    def tag_end(self): ...
    def tag_stop(self): ...
    def tag_mergeable(self): ...

class _rml_tmpl_frame(_rml_tmpl_tag):
    width: Any
    posx: Any
    def __init__(self, posx, width) -> None: ...
    def tag_start(self): ...
    def tag_end(self): ...
    def tag_stop(self): ...
    def tag_mergeable(self): ...
    def merge(self, frame) -> None: ...

class _rml_tmpl_draw_string(_rml_tmpl_tag):
    posx: Any
    posy: Any
    pos: Any
    def __init__(self, node, style) -> None: ...
    def tag_start(self): ...
    def merge(self, ds) -> None: ...

class _rml_tmpl_draw_lines(_rml_tmpl_tag):
    ok: bool
    posx: Any
    posy: Any
    width: Any
    style: Any
    def __init__(self, node, style) -> None: ...
    def tag_start(self): ...

class _rml_stylesheet:
    doc: Any
    attrs: Any
    _tags: Any
    result: Any
    def __init__(self, stylesheet, doc): ...
    def render(self): ...

class _rml_draw_style:
    style: Any
    _styles: Any
    def __init__(self): ...
    def update(self, node) -> None: ...
    def font_size_get(self, tag): ...
    def get(self, tag): ...

class _rml_template:
    localcontext: Any
    frame_pos: int
    frames: Any
    template_order: Any
    page_template: Any
    loop: int
    _tags: Any
    style: Any
    template: Any
    def __init__(
        self,
        localcontext,
        out,
        node,
        doc,
        images: Any | None = ...,
        path: str = ...,
        title: Any | None = ...,
    ) -> None: ...
    def _get_style(self): ...
    def set_next_template(self) -> None: ...
    def set_template(self, name) -> None: ...
    def frame_start(self): ...
    def frame_stop(self): ...
    def start(self): ...
    def end(self): ...

class _rml_doc:
    localcontext: Any
    etree: Any
    filename: Any
    result: str
    def __init__(
        self,
        node,
        localcontext: Any | None = ...,
        images: Any | None = ...,
        path: str = ...,
        title: Any | None = ...,
    ) -> None: ...
    def render(self, out) -> None: ...

def parseNode(
    rml,
    localcontext: Any | None = ...,
    fout: Any | None = ...,
    images: Any | None = ...,
    path: str = ...,
    title: Any | None = ...,
): ...
def parseString(
    rml,
    localcontext: Any | None = ...,
    fout: Any | None = ...,
    images: Any | None = ...,
    path: str = ...,
    title: Any | None = ...,
): ...
def trml2pdf_help() -> None: ...
