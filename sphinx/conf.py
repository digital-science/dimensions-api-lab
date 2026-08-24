# Configuration file for the Sphinx documentation builder.
# https://www.sphinx-doc.org/en/master/usage/configuration.html

from __future__ import annotations

import re
from typing import Any

project = "DSL"
copyright = "2026 Digital Science & Research Solutions, Inc. All Rights Reserved"
author = "Digital Science Dimensions API Team"

release = "0.3"

html_title = (
    "API Lab - reusable notebooks for research data analytics - "
    "powered by Dimensions Analytics API"
)
html_logo = "_static/img/dimensions-logo@2x.png"
html_favicon = "_static/img/favicon.ico"
html_show_sphinx = False
html_show_copyright = False

extensions = [
    "nbsphinx",
]

nbsphinx_allow_errors = True

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store", "**.ipynb_checkpoints"]

html_theme = "sphinx_book_theme"
html_static_path = ["_static"]
# PST 0.20 reads default_mode from html_context (not html_theme_options).
# An empty value becomes data-default-mode="" and logs
# "Got invalid theme mode: . Resetting to auto."
html_context = {
    "default_mode": "auto",
}
html_theme_options = {
    "repository_url": "https://github.com/digital-science/dimensions-api-lab",
    "repository_branch": "master",
    "path_to_docs": "sphinx",
    "use_repository_button": True,
    "use_issues_button": True,
    "use_download_button": True,
    "home_page_in_toc": True,
    "show_toc_level": 2,
    # Keep search in the primary sidebar (under the logo). PST 0.20 otherwise
    # injects a second search-button-field into the top navbar.
    "navbar_persistent": [],
    "footer_content_items": [
        "author.html",
        "copyright.html",
        "last-updated.html",
        "footer.html",
    ],
    "logo": {
        "image_light": "_static/img/dimensions-logo@2x.png",
        "image_dark": "_static/img/dimensions-logo@2x.png",
        "alt_text": "Dimensions API Lab",
    },
}

# Pin require.js so stored Plotly 4 cell outputs keep loading.
nbsphinx_requirejs_path = (
    "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.7/require.min.js"
)
nbsphinx_requirejs_options = {
    "integrity": "sha384-h+aUZRFA4igWfUQc/4swkXMaUbEGNjGfVnVDcfmHb62ZOq3vjMwLSDcGJcVlSLpY",
    "crossorigin": "anonymous",
}

nbsphinx_widgets_path = (
    "https://unpkg.com/@jupyter-widgets/html-manager@0.20.9/dist/embed-amd.js"
)
nbsphinx_widgets_options = {
    "integrity": "sha384-gpC61jTZJSrhKI1MNzGJkfhCMtImwPePhhwqr+/8prXCo6bfQANJovLOKeihv1zp",
    "crossorigin": "anonymous",
}

# Sphinx 9 defaults to MathJax 4. Do not pin MathJax 2 (CVE-2023-39663).
# Plotly 4 stored outputs still call MathJax.Hub; nbsphinx_prolog no-op-shims it.

# Plotly 4/5 notebook outputs call require(['plotly']) and expect a paths map.
# nbsphinx 0.9 / Sphinx 9 / sphinx-book-theme do not inject one. Pin plotly.js
# 2.8.3 (plotly.py 4/5 API) — not plotly.js 3 / plotly.py 6.
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

.. raw:: html

    <script>
    window.MathJax = window.MathJax || {};
    window.MathJax.Hub = window.MathJax.Hub || {
      Config: function () {},
      Queue: function () {},
      Register: { StartupHook: function () {} }
    };
    </script>
    <script crossorigin="anonymous" integrity="sha384-h+aUZRFA4igWfUQc/4swkXMaUbEGNjGfVnVDcfmHb62ZOq3vjMwLSDcGJcVlSLpY" src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.7/require.min.js"></script>
    <script>require=requirejs;</script>
    <script>
    require.config({
      paths: {
        plotly: 'https://cdn.plot.ly/plotly-2.8.3.min'
      }
    });
    </script>

.. image:: /_static/img/badge-colab.svg
   :target: https://colab.research.google.com/github/digital-science/dimensions-api-lab/blob/master/{{ docname }}

.. image:: /_static/img/badge-github-custom.svg
   :target: https://github.com/digital-science/dimensions-api-lab/blob/master/{{ docname }}

----

"""

nbsphinx_epilog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

----

|

.. note::

   The `Dimensions Analytics API <https://www.dimensions.ai/dimensions-apis/>`_ allows to carry out sophisticated research data analytics tasks like the ones described on this website. Check out also the associated `Github repository <https://github.com/digital-science/dimensions-api-lab>`_ for examples, the source code of these tutorials and much more.

.. image:: /_static/img/badge-dimensions-api.svg
   :target: https://www.dimensions.ai/dimensions-apis/

"""

_MATHJAX2_SCRIPT = re.compile(
    r"""<script[^>]+src=["']https?://(?:cdnjs\.cloudflare\.com/ajax/libs/mathjax|cdn\.jsdelivr\.net/npm/mathjax@2)[^"']*["'][^>]*>\s*</script>""",
    re.IGNORECASE,
)
# Custom domain is an S3 website endpoint (HTTP only; :443 times out).
# Path-style S3 REST is the working HTTPS equivalent for this dotted bucket.
_INSECURE_SAMPLE_DATA = "http://api-sample-data.dimensions.ai"
_SECURE_SAMPLE_DATA = "https://s3.amazonaws.com/api-sample-data.dimensions.ai"

# Stored plotly.py 6 outputs request plotly.js 3.x. cdn.plot.ly/plotly-3.1.0.min
# (no .js) is not a JS file — require.js and ES module imports omit the
# extension and get application/xml (NS_ERROR_CORRUPTED_CONTENT). Pin 2.8.3
# (Plotly 4/5 API). plotly.js 2.x is UMD, so type=module imports become <script src>.
_PLOTLY_JS = "https://cdn.plot.ly/plotly-2.8.3.min.js"
_PLOTLY_REQUIRE = "https://cdn.plot.ly/plotly-2.8.3.min"
_PLOTLY_BAD_VERSION = r"(?:3[\w.-]*|latest)"
_PLOTLY_MODULE_IMPORT = re.compile(
    rf"""<script\s+type=["']module["']>\s*import\s+["']https://cdn\.plot\.ly/plotly-{_PLOTLY_BAD_VERSION}\.min(?:\.js)?["']\s*</script>""",
    re.IGNORECASE,
)
_PLOTLY_SCRIPT_SRC = re.compile(
    rf"""(<script\b)([^>]*\bsrc=["']https://cdn\.plot\.ly/plotly-{_PLOTLY_BAD_VERSION}\.min\.js["'][^>]*>)""",
    re.IGNORECASE,
)
_PLOTLY_BAD_SRC = re.compile(
    rf"https://cdn\.plot\.ly/plotly-{_PLOTLY_BAD_VERSION}\.min\.js",
    re.IGNORECASE,
)
_PLOTLY_BAD_REQUIRE = re.compile(
    rf"https://cdn\.plot\.ly/plotly-{_PLOTLY_BAD_VERSION}\.min(?!\.js)",
    re.IGNORECASE,
)
_INTEGRITY_ATTR = re.compile(r"""\s+integrity=["'][^"']*["']""", re.IGNORECASE)


def _rewrite_plotly_script_src(match: re.Match[str]) -> str:
    prefix, rest = match.group(1), match.group(2)
    rest = _INTEGRITY_ATTR.sub("", rest)
    rest = _PLOTLY_BAD_SRC.sub(_PLOTLY_JS, rest)
    return prefix + rest


def _rewrite_plotly_cdn(html: str) -> str:
    html = _PLOTLY_MODULE_IMPORT.sub(f'<script src="{_PLOTLY_JS}"></script>', html)
    html = _PLOTLY_SCRIPT_SRC.sub(_rewrite_plotly_script_src, html)
    return _PLOTLY_BAD_REQUIRE.sub(_PLOTLY_REQUIRE, html)


def _sanitize_html_body(
    app: Any,
    pagename: str,
    templatename: str,
    context: dict[str, Any],
    doctree: Any,
) -> None:
    body = context.get("body")
    if not isinstance(body, str):
        return
    if "mathjax" in body.lower():
        body = _MATHJAX2_SCRIPT.sub("", body)
    if _INSECURE_SAMPLE_DATA in body:
        body = body.replace(_INSECURE_SAMPLE_DATA, _SECURE_SAMPLE_DATA)
    if "cdn.plot.ly" in body:
        body = _rewrite_plotly_cdn(body)
    context["body"] = body


def setup(app: Any) -> None:
    app.add_css_file("css/custom.css")
    app.add_js_file("js/custom.js")
    app.connect("html-page-context", _sanitize_html_body)
