# Build the API Lab site from cookbooks/ via sphinx/ + nbsphinx.
# Generated HTML goes to _build/html (not committed). GitHub Actions deploys it.

SPHINXOPTS   ?=
SPHINXBUILD  ?= python -m sphinx
SOURCEDIR     = sphinx
BUILDDIR      = _build/html
BUILDDIR_TEST = _build/html-test
NOTEBOOKS_FOLDER = cookbooks
NOTEBOOKS_FOLDER_TEST = backlog/ACTIVE

.PHONY: help html html_test clean extra-html extra-html-test

help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

html:
	@echo "==== Building documentation ===="
	rm -rf "$(SOURCEDIR)/$(NOTEBOOKS_FOLDER)"
	cp -r "$(NOTEBOOKS_FOLDER)" "$(SOURCEDIR)/$(NOTEBOOKS_FOLDER)"
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)
	@$(MAKE) extra-html
	@if [ -z "$$CI" ]; then open "$(BUILDDIR)/index.html" || true; fi
	@echo "==== Built $(BUILDDIR)/index.html ===="

# IMPORTANT: when testing, ensure sphinx/index.rst references the files
# you want. See sphinx/index.rst.TEST for an example.
html_test:
	@echo "==== TEST documentation for selected notebooks only ===="
	rm -rf "$(SOURCEDIR)/$(NOTEBOOKS_FOLDER)"
	cp -r "$(NOTEBOOKS_FOLDER_TEST)" "$(SOURCEDIR)/$(NOTEBOOKS_FOLDER)"
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" "$(BUILDDIR_TEST)" $(SPHINXOPTS) $(O)
	@$(MAKE) extra-html-test
	@if [ -z "$$CI" ]; then open "$(BUILDDIR_TEST)/index.html" || true; fi
	@echo "==== Built $(BUILDDIR_TEST)/index.html ===="

# vis.js / pyvis iframe pages are not emitted by nbsphinx.
# Prepend <!DOCTYPE html> when missing so copied pages are not in Quirks Mode.
COPY_HTML = python -c 'from pathlib import Path; import sys; src, dest = Path(sys.argv[1]), Path(sys.argv[2]); text = src.read_text(encoding="utf-8"); dest.parent.mkdir(parents=True, exist_ok=True); dest.write_text(text if text.lstrip().lower().startswith("<!doctype") else "<!DOCTYPE html>\n" + text, encoding="utf-8")'

extra-html:
	@mkdir -p "$(BUILDDIR)"
	@find "$(NOTEBOOKS_FOLDER)" -name '*.html' | while read -r f; do \
		dest="$(BUILDDIR)/$$f"; \
		$(COPY_HTML) "$$f" "$$dest"; \
	done
	@echo "api-lab.dimensions.ai" > "$(BUILDDIR)/CNAME"

extra-html-test:
	@mkdir -p "$(BUILDDIR_TEST)"
	@if [ -d "$(NOTEBOOKS_FOLDER_TEST)" ]; then \
		find "$(NOTEBOOKS_FOLDER_TEST)" -name '*.html' | while read -r f; do \
			rel="$${f#$(NOTEBOOKS_FOLDER_TEST)/}"; \
			dest="$(BUILDDIR_TEST)/$(NOTEBOOKS_FOLDER)/$$rel"; \
			$(COPY_HTML) "$$f" "$$dest"; \
		done; \
	fi

clean:
	rm -rf _build "$(SOURCEDIR)/$(NOTEBOOKS_FOLDER)"
