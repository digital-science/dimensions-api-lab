# ----------------------------------------------------------------------------
# Configuration file for the Sphinx documentation builder.
# # http://www.sphinx-doc.org/en/master/config


# -- Project information -----------------------------------------------------
project = 'DSL'
copyright = '2026 Digital Science & Research Solutions, Inc. All Rights Reserved'
author = 'Digital Science Dimensions API Team (Michele Pasin)'

# The full version, including alpha/beta/rc tags
release = '0.3'

html_title = """API Lab - reusable notebooks for research data analytics - powered by Dimensions Analytics API"""

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_logo = "_static/img/dimensions-logo@2x.png"

html_show_sphinx = False
# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = False # footer.html used instead

html_favicon = "_static/img/favicon.ico"



# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'nbsphinx',
    'sphinx_rtd_theme'
]


nbsphinx_allow_errors = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']


# -- Options for HTML output -------------------------------------------------

html_theme = 'sphinx_rtd_theme' 

# MORE NICE THEMES
# https://nbsphinx.readthedocs.io/en/typlog-theme/prolog-and-epilog.html
# https://schettino72.github.io/sphinx_press_site/

# used with 'nature' theme
# html_sidebars = { '**': ['localtoc.html', 'relations.html', 'sidebar_github.html', 'searchbox.html'] }

# opts for sphinx_rtd_theme 
html_theme_options = {
   #  'canonical_url': '',
   #  'analytics_id': 'UA-XXXXXXX-1',  #  Provided by Google in your dashboard
   #  'logo_only': False,
   #  'display_version': True,
    'prev_next_buttons_location': None,
   #  'style_external_links': False,
   #  'vcs_pageview_mode': '',
   #  'style_nav_header_background': 'white',
   #  # Toc options
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
    'includehidden': True,
   #  'titles_only': False
}


# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

def setup(app):
    app.add_css_file('css/custom.css')  # may also be an URL
    app.add_js_file('js/custom.js')  # may also be an URL


# html_js_files = [
#     'js/ga.js',
# ]

# /Then put the file into the _static/css/ folder.


# -- pinned CDN assets (security) ------------------------------------------
# Pin exact versions + SRI integrity hashes so a compromised or hijacked CDN
# release cannot inject code into the published site. Keep these in sync with
# the script tags in the published /docs HTML. When bumping a version,
# recompute the hash:  curl -sL <url> | openssl dgst -sha384 -binary | base64
# NOTE: MathJax is still on the (EOL) v2 line because the plotly.js 4.x
# bundles embedded in notebook outputs only support the MathJax v2 API.
# Migrate to MathJax v3+ together with the sphinx/nbsphinx/plotly upgrade.

nbsphinx_requirejs_path = "https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.7/require.min.js"
nbsphinx_requirejs_options = {
    "integrity": "sha384-h+aUZRFA4igWfUQc/4swkXMaUbEGNjGfVnVDcfmHb62ZOq3vjMwLSDcGJcVlSLpY",
    "crossorigin": "anonymous",
}

nbsphinx_widgets_path = "https://unpkg.com/@jupyter-widgets/html-manager@0.20.9/dist/embed-amd.js"
nbsphinx_widgets_options = {
    "integrity": "sha384-gpC61jTZJSrhKI1MNzGJkfhCMtImwPePhhwqr+/8prXCo6bfQANJovLOKeihv1zp",
    "crossorigin": "anonymous",
}

mathjax_path = "https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.9/MathJax.js?config=TeX-AMS-MML_HTMLorMML"


# -- prolog and epilog ---------------------------------------------------
# https://nbsphinx.readthedocs.io/en/0.4.3/prolog-and-epilog.html


nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

.. raw:: html

    <script crossorigin="anonymous" integrity="sha384-h+aUZRFA4igWfUQc/4swkXMaUbEGNjGfVnVDcfmHb62ZOq3vjMwLSDcGJcVlSLpY" src="https://cdnjs.cloudflare.com/ajax/libs/require.js/2.3.7/require.min.js"></script>
    <script>require=requirejs;</script>

.. image:: /_static/img/badge-colab.svg
   :target: https://colab.research.google.com/github/digital-science/dimensions-api-lab/blob/master/{{ docname }}

.. image:: /_static/img/badge-github-custom.svg
   :target: https://github.com/digital-science/dimensions-api-lab/blob/master/{{ docname }}

----



"""

# .. image:: /_static/img/badge-dimensions-api.svg
#    :target: https://www.dimensions.ai/dimensions-apis/

# .. seealso:: 

#     Learn how to access the `Dimensions Analytics API <https://www.dimensions.ai/dimensions-apis/>`_.   

# ----



nbsphinx_epilog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

----

|

.. note:: 

   The `Dimensions Analytics API <https://www.dimensions.ai/dimensions-apis/>`_ allows to carry out sophisticated research data analytics tasks like the ones described on this website. Check out also the associated `Github repository <https://github.com/digital-science/dimensions-api-lab>`_ for examples, the source code of these tutorials and much more. 

.. image:: /_static/img/badge-dimensions-api.svg
   :target: https://www.dimensions.ai/dimensions-apis/

"""

