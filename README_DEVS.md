# DSL API Lab — developer notes

Tips for building the API Lab site locally.

## Setup

Use **Python 3.14** (`.python-version` pins it). The package floor is Python 3.12 because Sphinx 9.1 requires it; 3.15 is not stable yet.

Create a virtualenv, then install the project. Default dependencies are the notebook stack; the `docs` extra is needed to build the site:

```
python3.14 -m venv .venv
source .venv/bin/activate
pip install -e ".[docs]"
```

`pip install -e ".[notebooks]"` is the same notebook stack as the default install (dimcli, pandas, matplotlib, plotly, jupyter, gspread, google-auth).

Install [Pandoc](https://pandoc.org/installing.html) as a system dependency (`brew install pandoc`). nbsphinx needs it to convert notebooks.

Binder uses `runtime.txt` (`python-3.14`) plus this `pyproject.toml`.

## Workflow

### 1. Adding new notebooks

Put new notebooks in `cookbooks/`. Do not rename folders — that would break published URLs.

`backlog/` holds drafts that are not published yet.

### 2. Building the site

Sphinx + [nbsphinx](https://nbsphinx.readthedocs.io/) turn the notebooks into HTML.

```
make html
```

Output is `_build/html/` (gitignored). Open `_build/html/index.html`.

To try a subset of notebooks, copy them into `backlog/ACTIVE`, point `sphinx/index.rst` at those files (see `sphinx/index.rst.TEST`), and run:

```
make html_test
```

### 3. Publishing

Do **not** commit generated HTML. GitHub Actions (`.github/workflows/pages.yml`) builds on `master` and deploys to GitHub Pages.

**One-time repo setting:** Pages source = GitHub Actions (not `/docs`). After that is on, the committed `docs/` tree can be deleted.

Update [CHANGELOG.md](CHANGELOG.md) when notebooks are added or changed.

## vis.js / pyvis iframes

Network visualizations that live as sidecar `.html` files next to a notebook are copied into the build by `make extra-html` (run automatically from `make html`). Keep those HTML files in `cookbooks/` alongside the notebook.

## Plotly in static HTML

Stored notebook outputs still load Plotly via require.js. Keep the require.js pin and the `require.config({ paths: { plotly: ... } })` map in `sphinx/conf.py` (`nbsphinx_prolog`) or Plotly charts in existing cell output will fail to load. The map points at plotly.js 2.8.3 (`https://cdn.plot.ly/plotly-2.8.3.min.js`); do not switch stored cells to plotly.js 3 / plotly.py 6.

OneTrust AutoBlock lives at the end of `<body>` (`sphinx/_templates/layout.html`), not in `<head>`. Putting it in the head intercepts the Plotly CDN load and shows `Script error for "plotly"`.
