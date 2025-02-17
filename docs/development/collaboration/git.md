# Git

## Branches

[Git Branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
are used to structure the developments and improvements. <br>
It is recommended to activate suitable GitHub Branch protection rules.

### Permanent Branches

- **production** - includes the current stable (latest) version
- **develop** - includes all current developments

### Temporary Branches

- **bug** - includes bugfixes and typos
- **enhance** - includes enhancements and improvements
- **feature** - includes a new feature that will be implemented
- **hotfix** - includes small improvements before a release, should be branched from a release branch
- **release** - includes the current version to be released

The majority of the development will be done in `enhance` and `feature` branches.

### Branch protection

Branch protection rules help safeguard the code by enforcing workflows and permissions on specific branches. <br>
The level of protection should correspond to the number of active developers and the importance of the package. <br>
The `production` branch should have <br>
- `Require a pull request before merging` with `Require approvals` and 1 other developer.
- `Require status checks to pass before merging`

## Gitignore

This file specifies intentionally untracked files to ignore. <br>
It is copied from [a collection of .gitignore templates](https://github.com/github/gitignore). <br>
For more information about how 📝 `.gitignore` files work, <br>
see the [Ignoring Files chapter](https://git-scm.com/book/en/v2/Git-Basics-Recording-Changes-to-the-Repository#_ignoring) of the Pro Git book.

## Issue Templates

[Issue Templates](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/configuring-issue-templates-for-your-repository)
offer specific functions and default configurations for new issues.

- [Feature Issue Template](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/.github/ISSUE_TEMPLATE/issue_template_feature.md)
- [Bug Issue Template](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/.github/ISSUE_TEMPLATE/issue_template_bug.md)
- [Release Issue Template](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/.github/ISSUE_TEMPLATE/issue_template_release.md)
- [User Kudos Issue Template](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/.github/ISSUE_TEMPLATE/issue_template_user_kudos.md)

## Pull Request (PR) Template

The [Pull Request Template](https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests/creating-a-pull-request-template-for-your-repository)
is used for all PR, because it is only possible to create a single one. <br>
It includes all needed information to merge branches and release new versions. <br>

- [Pull Request Template](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/.github/pull_request_template.md)

## GitHub Projects

[GitHub Projects](https://github.com/OpenEnergyPlatform/oemetadata/projects)
help to organise and manage the issues and PR across different repositories. <br>
It can be used for the release procedure, research projects, and complex developments.

## GitHub Labels

GitHub Labels are used to organize Issues and PR. <br>
Colours and emoticons improve presentation, see: <br>
    📝 [github-labels.json](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/docs/development/git/github-labels.json)

## GitHub Workflows (Actions)

[GitHub Actions](https://github.com/OpenEnergyPlatform/oemetadata/actions)
are used to automate processes of the repository. <br>
Main use-cases are building and publishing the documentation and run automated tests.

### Code coverage with codecov

Codecov is a code coverage and quality test for the repository. <br>
A login and token is needed to implement the codecov badge for the README.rst.

### Documentation with gh-pages

The `develop` branch is directly updated using `mike` and `mkdocs`.<br>
The included `git fetch` ensures that the released main versions are not deleted.

### Publish on Test PyPI

This workflow releases the package on PyPI using `build`.<br>
The token has to be added to the GitHUb Secrets.

### Publish on PyPI

This workflow releases the package on PyPI using `build`.<br>
The token has to be added to the GitHUb Secrets.

### License test with REUSE

The REUSE action does a full compliance check of all files of the repository.<br>
It uses the `REUSE.toml` and file headers and provides a badge.

### Automated tests with tox

Tox automates and standardizes testing for the repository.<br>
It builds the packages with different environments and versions.<br>
The file `tox.ini` configures tests: `pytest`, `coverage` and `ruff`.

## Pre-commit

**Pre-commit** is a tool to easily setup and run `pre-commit hooks` for your git repository.<br>
See the best-practice documentation of [pre-commit](https://github.com/pre-commit/pre-commit-hooks) or the
[official documentation](https://pre-commit.com/) for further information.<br>
It is used to improve auto-format code, do linting and run tests before every commit.

### Install

Install the required package in a python environment. <br>
    💻 `pip install pre-commit` Install pre-commit <br>
    💻 `pre-commit install` Install pre-commit

### Setup

The hooks are configured in the file 📝 `.pre-commit-config.yaml`.<br>
List of implemented hooks:

- [Pre-commit-hooks](https://github.com/pre-commit/pre-commit-hooks) - Out-of-the-box hooks
- [Black](https://github.com/psf/black) - Python code formatter
- [isort](https://github.com/pycqa/isort) - Sort Python imports
- [Ruff](https://github.com/astral-sh/ruff-pre-commit) - Fast Python linter, written in Rust
- [Flake8](https://github.com/pycqa/flake8) - Python linter with PyFlakes and pycodestyle
- [mypy mirror](https://github.com/pre-commit/mirrors-mypy) - Added static types to Python
- [mirrors-prettier](https://github.com/pre-commit/mirrors-prettier) - Formatting for other files then python scripts
- [reuse](https://github.com/fsfe/reuse-tool) - License and copyright information

### Use

All commits will trigger the hooks automatically. <br>
    💠 `git commit file -m "Commit message #IssueNr"` Commit with message

Commit without running the hooks. <br>
    💠 `git commit --no-verify file` Commit without hooks

!!! note "Line endings"
    There can be problems with file line endings on Windows, `CRLF` is used on Windows and `LF` is used on Linux.

To run the hooks on all files in your repository use: <br>
    💻 `pre-commit run --all-files` Run pre-commit hooks

!!! warning "Markdown files / Admonitions"
    If the hook is applied to markdown files that include special formatting,
    (for example 📝 `mkdocs.yml`), this can introduce incorrect changes.
    This effects [admonitions](https://squidfunk.github.io/mkdocs-material/reference/admonitions/) boxes for MkDocs.

!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
