<!--
SPDX-FileCopyrightText: 2022 Ludwig Hülk <https://github.com/Ludee> © Reiner Lemoine Institut
SPDX-FileCopyrightText: super-repo v0.5.0 <https://github.com/rl-institut/super-repo>
SPDX-License-Identifier: MIT
-->

# Release Procedure

The release procedure is a process in which different parts of the repository are involved.<br>
These symbols help with orientation:

- 🐙 GitHub
- 💠 git (Bash)
- 📝 File
- 💻 Command Line (CMD)

## Version Numbers

This software follows the [Semantic Versioning (SemVer)](https://semver.org/).<br>
It always has the format `MAJOR.MINOR.PATCH`, for example `1.5.0`.

The data follows the [Calendar Versioning (CalVer)](https://calver.org/).<br>
It always has the format `YYYY-MM-DD`, for example `2022-05-16`.

## GitHub Release

Following the Semantic Versioning, different workflows for Major, Minor, or Patch
releases are possible. <br>
For Major and Minor releases, follow the complete workflow.<br>
For a **Patch Release** (Hotfix), start at [section 3](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/RELEASE_PROCEDURE.md#4--create-a-draft-github-release).

### 1. 🐙 Create a `GitHub Project`

- Create [New classic project](https://github.com/OpenEnergyPlatform/oemetadata/projects?type=classic)
- Use the project template _Automated kanban with reviews_
- Named `oemetadata-v0.1.0`
- Add a meaningful description
- Track project progress

▶️ It gives an overview of open and finished issues and Pull Requests!

### 2. 🐙 Finish all planned Developments

- Some days before the release, inform all developers
- Merge the open Pull Requests
- On release day, start the release early to ensure sufficient time for reviews
- Merge everything on the `develop` branch

▶️ Completion of the preparation of the planned release!

### 3. 🐙 Create a `GitHub Issue`

- Use [`📝issue_template_release`](https://github.com/OpenEnergyPlatform/oemetadata/issues/new?template=issue_template_release.md)
- Name `Release - Minor Version - 0.1.0`
- Complete the necessary details from the template

▶️ This issue documents the status of the release!

### 4. 🐙 Create a `Draft GitHub Release`

- Start here for a **Patch Release** (Hotfix)
- [Draft a new release](https://github.com/OpenEnergyPlatform/oemetadata/releases/new)
- Enter the release version number `0.1.0` as title
- Summarize key changes from changelog in the description

```
## [0.1.0] Minor Release - Name - Date
### Added
### Changed
### Removed

**Complete changelog:** [CHANGELOG.md](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/CHANGELOG.md)
**Compare versions:** [0.1.0 - 0.2.0](https://github.com/OpenEnergyPlatform/oemetadata/compare/v0.1.0...v0.2.0)
**Main developers:** @Ludee @jh-RLI
```

- Save draft

### 5. 💠 Create a `release` branch

- Change to `develop` branch: 💠`git checkout develop`
- Update with online version: 💠`git pull`
- Run [Pre-commit Hooks](https://https://openenergyplatform.github.io/oemetadata/latest//latest/development/best-practice/pre_commit_hooks/): 💻`pre-commit run --all-files`
- Create branch: 💠`git checkout -b release-v0.1.0`
- Push branch: 💠`git push --set-upstream origin release-v0.1.0`

### 6. 📝 Update the version files (bump version number)

- Run bumpversion: 💻 `bump-my-version bump --current-version 0.1.0 minor`
  - `📝CITATION.cff`
    - Update `version`
    - Update `date-released`
  - `📝pyproject.toml`
    - Update `version`
  - `📝uv.lock`
    - Update `version`
- Update the `📝CHANGELOG.md`
  - Check that all Pull Request are included
  - Rename `Unreleased` section with release title from issue
  - Follow `[0.0.0] Minor Release - Name of Release - 20YY-MM-DD`

▶️ Increase version numbers!

### 7. 🐙 Create a Release Pull Request

- Merge `release` into `production` branch
- Remove details from template
- Assign two reviewers to check the release
- Run all test
- Execute the software locally
- Wait for reviews and tests
- Merge Pull Request and delete `release` branch

▶️ Merge code on `production` branch!

### 8. 💠 Set the `Git Tag`

- Change to `production` branch: 💠`git checkout production`
- Update with online version: 💠`git pull`
- Check existing tags: 💠`git tag -n`
- Create new tag: 💠`git tag -a v0.1.0 -m "oemetadata Minor Release v0.1.0"`
- This commit will be the final version for the release, breath three times and check again
- Push tag: 💠`git push --tags`

If you messed up, remove tags and start again

- Delete local tag: 💠`git tag -d v0.1.0`
- Delete remote tag: 💠`git push --delete origin v0.1.0`

▶️ Git Tag for GitHub Release!

### 9. 🐙 Publish `GitHub Release`

- Navigate to releases and open the draft release
- Choose the correct `Git Tag`
- Choose the `production` branch
- Select `Set as the latest release`
- Select `Create a discussion for this release` in category `Announcements`
- **Publish release**

▶️ 🎉 Release on GitHub! 🚀

#### 🐙 Automated Release with GitHub Action

- Check [GitHub Action](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/publish_pypi.yml)
- The GitHub release starts the automated upload to PyPI
- Check on PyPI if release arrived
- If automated released failed, release manually

▶️ 🎉 Release on PyPI! 🚀

### 10. 💻 Update the documentation

- Change to `production` branch: 💠`git checkout production`
- Update with online version: 💠`git pull`
- Activate environment and enter repository: 💻`activate py310`
- Test version: 💻`mike serve`
- Publish new version: 💻`mike deploy --push --update-aliases 0.1 latest`

▶️ Update the documentation!

### 11. 🐙 Set up new development

- Create a [Pull Request](https://github.com/OpenEnergyPlatform/oemetadata/compare) from `production` to `develop`
- Named `Set up new development after release v0.1.0`
- Checkout `develop` branch and pull
- Create a new **Unreleased** section in the `📝CHANGELOG.md`

```
## [Unreleased]

### Added

### Changed

### Removed
```

- Close all solved issues and PR and set tags and status
- Create a new [GitHub Project](https://github.com/OpenEnergyPlatform/oemetadata/projects?query=is%3Aopen) by cloning the latest project

▶️ Continue the developments 🛠

## PyPi Release

### 🐙 Create and publish package on Test-PyPI

- Change to `develop` branch: 💠`git checkout develop`
- Update with online version: 💠`git pull`
- Create branch: 💠`git checkout -b deployment-test`
- Push branch: 💠`git push --set-upstream origin deployment-test`
- Check [GitHub Action](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/publish_testpypi.yml)
- Check [Test-PyPI](https://test.pypi.org/project/oemetadata/#history)
- Delete remote branch: 💠`git branch -d origin deployment-test`
- Delete local branch: 💠`git branch -D deployment-test`
- Note: Each version can only be released on Test-PyPI once. If needed, increment the Patch version
  - Run bumpversion: 💻 `bump-my-version bump --current-version 0.1.0 patch`

▶️ 🎉 Release on TestPyPI!

### 💻 Create and publish package on PyPI manually

- Change to `production` branch: 💠`git checkout production`
- Update with online version: 💠`git pull`
- Navigate to git folder: 💻`cd D:\git\github\USER\Repository\`
- Activate conda environment: 💻`activate py310`
- Create package using: 💻`python -m build`
- Check that files have been created in folder: 📝 `dist`
- Check build: 💻 `twine check dist/*`
- Upload to Test PyPI using: 💻 `twine upload -r testpypi dist/NAME_0.2.0.tar.gz`
- Upload to PyPI using: 💻 `twine upload dist/NAME_0.2.0.tar.gz`
- Enter `name` and `password`

▶️ 🎉 Release on PyPI! 🚁

## Sources:

- https://raw.githubusercontent.com/folio-org/stripes/master/doc/release-procedure.md

!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
