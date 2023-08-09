# == APILAB build logic Sphinx ==============================================
#
#
# * `cookbooks` ipynb source is at top level 
# * `sphinx` folder contains all that's needed to build the api-lab website 
# * `cookbooks` are copied there at runtime when building the docs
#  * same folder will be created in corresponding html output
# * resulting docs are saved either in `docs` or `private/docs-staging` (staging or live)
# * when syncing with the live github repo, the `sphinx` folder gets omitted
#
# ===========================================================================

SPHINXOPTS    =
SPHINXBUILD   = sphinx-build
SOURCEDIR     = sphinx

### MEMO - white space at the end of variables matters!

# src of ipynb
NOTEBOOKS_FOLDER="cookbooks"
# src of ipynb for only selected notebooks testing
NOTEBOOKS_FOLDER_TEST="backlog/ACTIVE"

# update as needed locally - full path
BUILDDIR_STAGING:= $(shell source ./tools/set-envs.sh && echo $$STGDIR)
# folder for github docs
BUILDDIR_LIVE="docs"



# Put it first so that "make" without argument is like "make help".
help:
	@$(SPHINXBUILD) -M help "$(SOURCEDIR)" "$(BUILDDIR)" $(SPHINXOPTS) $(O)

.PHONY: help Makefile


# 

html_test:
	@echo "==== TEST documentation for selected notebooks only ===="
	@echo "==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ==== ="
	rm -rf $(SOURCEDIR)/$(NOTEBOOKS_FOLDER)
	cp -r $(NOTEBOOKS_FOLDER_TEST)  $(SOURCEDIR)/$(NOTEBOOKS_FOLDER)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" $(BUILDDIR_STAGING)
	open "$(BUILDDIR_STAGING)/index.html"
	@echo "==== TEST documentation generated in private/docs folder run ===="

html_staging:
	@echo "==== STAGING documentation for entire docs ===="
	@echo "==== ==== ==== ==== ==== ==== ==== ==== ==== =="
	rm -rf $(SOURCEDIR)/$(NOTEBOOKS_FOLDER)
	cp -r $(NOTEBOOKS_FOLDER)  $(SOURCEDIR)/$(NOTEBOOKS_FOLDER)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" $(BUILDDIR_STAGING)
	open "$(BUILDDIR_STAGING)/index.html"
	@echo "==== Staging documentation generated in private/docs folder run - TIP use *make html* to finalize ===="

html:
	@echo "==== LIVE documentation ===="
	@echo "==== ==== ==== ==== ==== ==="
	rm -rf $(SOURCEDIR)/$(NOTEBOOKS_FOLDER)
	cp -r $(NOTEBOOKS_FOLDER)  $(SOURCEDIR)/$(NOTEBOOKS_FOLDER)
	@$(SPHINXBUILD) -b html "$(SOURCEDIR)" $(BUILDDIR_LIVE)
	open "$(BUILDDIR_LIVE)/index.html"
	@echo "==== LIVE documentation generated - in main /docs folder - TIP use *./tools/run-sync-and-push.sh* to finalize===="




