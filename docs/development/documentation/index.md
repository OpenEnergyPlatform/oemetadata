# Documentation

- README.rst
- CHANGELOG.md
- docs/
- MkDocs
- mkdocstrings


## MkDocs
[MkDocs](https://www.mkdocs.org/) is a fast and simple static site generator that is used for documentation. <br>
The source files are written in Markdown, and configured with a single YAML configuration file `mkdocs.yml`. <br>
[Material theme](https://squidfunk.github.io/mkdocs-material/) enables 
additional features and an elegant design.

### Install
Install the required packages in a python environment. <br>
`pip install mkdocs` install MkDocs <br>
`pip install mkdocs-material` install the material theme

### Build
Generate the documentation. <br>
`mkdocs serve` start the local live version of the documentation <br>
`mkdocs build` create a folder `site` with the documentation

### Publish

#### Manually
Publish documentation on **GitHub Pages**. <br>
`mkdocs gh-deploy` manually deploys the documentation files

#### GitHub Action
Deploy the documentation with **GitHub Actions**. <br>
The file `.github\workflows\gh-pages.yml` creates an automated GitHub workflow. <br>
It is configured to be pushed to the branch `gh-page` and then deployed online. <br>
A commit on the `production` branch triggers the workflow. 
