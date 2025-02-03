# Documentation

## README

The repository contains a 📝 `README.rst` file with basic information. <br>
It gives a short introduction to the project and links to other relevant files.

## Changelog

The 📝 `CHANGELOG.md` is a record of all notable changes made to a project. <br>
It is structured by each release and divided by additions, changes, and removals. <br>

## Documentation with MkDocs

[MkDocs](https://www.mkdocs.org/) is a fast and simple static site generator that is used for documentation. <br>
The source files are written in [Markdown](https://www.markdownguide.org/cheat-sheet/), and configured with 📝 `mkdocs.yml`. <br>
[Material theme](https://squidfunk.github.io/mkdocs-material/) enables
additional features and an elegant design. <br>

### Install

Install the required packages in a python environment. <br>
    💻 `pip install mkdocs` Install MkDocs <br>
    💻 `pip install mkdocs-material` Install the material theme

### Build

Generate the documentation locally. <br>
    💻 `mkdocs serve` Start the local live version of the documentation <br>
    💻 `mkdocs build` Create a folder `site` with the documentation

### Publish

#### Manually publish mkdocs

Publish documentation on **GitHub Pages**. <br>
    💻 `mkdocs gh-deploy` Manually deploys the documentation files

!!! warning "Manually deploy documentation"
    This command overrides all manually deployed versions (mike). <br>

#### GitHub Action

🐙 Deploy the documentation with **GitHub Actions**. <br>
The file 📝 `.github\workflows\documentation.yml` creates an automated GitHub workflow. <br>
It is configured to be pushed to the branch `gh-page` and then deployed online. <br>
A commit on the `develop` branch starts the workflow.

#### Versioning with Mike

The package [mike](https://github.com/jimporter/mike) is used to deploy [multiple versions](https://squidfunk.github.io/mkdocs-material/setup/setting-up-versioning/?h=versioning) of the documentation.<br>
    💻 `pip install mike` Install mike <br>
    💻 `mike deploy --push --update-aliases 1.0 latest` Deploys the latest version <br>
    💻 `mike set-default --push latest` Set the default version to latest <br>
    💻 `mike deploy develop --push` Deploys the develop branch

!!! note "Mike Versions"
    Only use the **Minor Versions** (1.1) and exclude the **Patch Version** (1.1.1)!

When adding older versions, load the `Git Tags` used for the releases: <br>
    💠 `git checkout v1.0.0` <br>
    💻 `mike deploy 1.0 --push` Deploys the old version 0.1

When building mike locally, the branch `gh-pages` is modified locally. <br>
    💻 `error: gh-pages is unrelated to origin/gh-pages` <br>
    💠 `git branch -D gh-pages` Delete the local documentation branch

Other useful commands are: <br>
    💻 `mike serve` Test mike on [`http://localhost:8000`](http://localhost:8000) <br>
    💻 `mike list` List all versions <br>
    💻 `mike retitle 1.0.1 1.0.2 --push` Rename a version <br>
    💻 `mike delete 0.1 --push` Deletes a specific versions <br>
    💻 `mike delete --all --push` Deletes all versions

## Docstrings with mkdocstrings

[mkdocstrings](https://mkdocstrings.github.io/) generates automatic
documentation (autodocs) from [Google style docstrings](https://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html). <br>
    💻 `pip install mkdocstrings` Install mkdocstrings

!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
