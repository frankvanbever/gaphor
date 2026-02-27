"""HTML, CSS, and JavaScript templates for the HTML model report."""

from pathlib import Path

_TEMPLATE_DIR = Path(__file__).parent

VENDOR_SVG_PAN_ZOOM_PATH = _TEMPLATE_DIR / "vendor_svg_pan_zoom.js"

HTML_TEMPLATE = (_TEMPLATE_DIR / "report.html").read_text(encoding="utf-8")
CSS_TEMPLATE = (_TEMPLATE_DIR / "report.css").read_text(encoding="utf-8")
JS_TEMPLATE = (_TEMPLATE_DIR / "report.js").read_text(encoding="utf-8")
