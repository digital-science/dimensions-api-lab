# DSL API Lab - DEVELOPERS information

Various useful tips for running the API LAB in development mode.

## Setup

Before trying to do any development work, you will need to create a `set-envs.sh` file in the `tools` folder.

The purpose of this file is to define the local directories you would like to use for building test and staging versions of site, to ensure the site renders as expected before pushing to production.

Example directories are given in `tools/set-envs-sample.sh`.

## Workflow

### 1. Adding new notebooks

New notebooks are added to the `cookbooks` folder. The folder structure should not be changed, so ensure legacy URLs and internal links doesn't break. 

PS The `backlog` folder contains various tutorials that are being considered for publication.

### 2. Development and Testing

The build process uses [sphinx](http://www.sphinx-doc.org/en/master/config) + [nbsphinx](https://nbsphinx.readthedocs.io/en/0.8.7/) to turn Python notebooks into HTML files. 

#### 2.1 Test selected notebooks

If you want to test building just a few notebooks another command is available, which processes only notebooks in `backlog/ACTIVE`:  

```
$ make html_test
```

The build directory is the same `tmp` location used for staging. 

> IMPORTANT: when testing, ensure that `/sphinx/index.rst` references the correct files! See `index.rst.TEST` for an example.

#### 2.2 Test full site in staging

```
$ make html_staging 
```

Both commands run in local and output everything to a `tmp` location. See the ([makefile](https://github.com/digital-science/dsl-api-lab-master/blob/master/Makefile)) for more details. 


### 3. Making a LIVE release

Running the `make html` command builds the site into the `docs` folder. This folder is publically available on the web, in the public clone of this project. So, first build and push for this project: 

```
$ make html 
$ git add -A
$ git commit
$ git push
```

#### 3.1 Update the CHANGELOG

The [CHANGELOG.md](CHANGELOG.md) file is publically available to end users. 

When notebooks are added or updated, changes are recorded in that file. 


## Tips and tricks

A few gotchas and related solutions.

### Dependencies

The notebook export functionality will work correctly with these library versions:

```
docutils==0.16 
nbconvert==6.0.0
markupsafe==1.1.1 
jinja2==2.11.3
sphinx==3.0.0 
sphinx_rtd_theme==0.5.0 
nbsphinx==0.8.3 
```

> TODO: update to most recent versions, dealing with css error dues to mathjax rendering [issue](https://github.com/spatialaudio/nbsphinx/issues/572#issuecomment-853389268) 

Pandoc is also needed: `brew install pandoc`


### Visualizations built with vis.js break!

For vis.js network visualizations, you need to **manually** put the HTML output in the right /docs folder. 

This is because the viz is embedded via an iFrame, so it does not get exported automatically via the ipynb file.

Relevant locations are:

```
docs/cookbooks/....
```

This needs to be done for both the STG export (in /tmp) and the PROD one (in the master repo itself), before the syncing step.


### Plotly library does not load

Discussed here  https://github.com/readthedocs/sphinx_rtd_theme/issues/788

Fix:

```
nbsphinx_prolog = r"""
{% set docname = env.doc2path(env.docname, base=None) %}

.. raw:: html

    <script src='http://cdnjs.cloudflare.com/ajax/libs/require.js/2.1.10/require.min.js'></script>
    <script>require=requirejs;</script>
...
```



### Navigation menu doesn't appear

Docs: https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html

Solution: you have to remove `titlesonly` in index.rst for that to work

```
.. toctree::
   :caption: Clinical Trials 
   :maxdepth: 5
   :glob:
   ####:titlesonly:####
```

Also, these settings:

```
    'collapse_navigation': False,
    'sticky_navigation': True,
    'navigation_depth': -1,
```

