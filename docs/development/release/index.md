# Release

The software release has four main goals:

1. Merge the new features to the `production` branch
2. Create a [GitHub Release](https://github.com/OpenEnergyPlatform/oemetadata/releases)
3. Update the documentation
4. Publish a new version of the package at PyPI

The 📝 [RELEASE_PROCEDURE.md](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/RELEASE_PROCEDURE.md)
contains detailed instructions to do a release.

## Automated Versioning with Bumpversion

**Bumpversion** is a tool for automated version management in software projects. <br>
It ensures consistent version updates across files and documentation <br>
by specifying a part to increment (major, minor, or patch). <br>
This streamlines release workflows and keeps project versioning synchronized.

Install package:  
    💻 `pip install --upgrade bump-my-version` <br>
    📝 `.bumpversion.toml` Configuration file for versioning rules and affected files

Test bumpversion: <br>
    💻 `bump-my-version show-bump` Preview next possible versions <br>
    💻 `bump-my-version bump minor --dry-run -vv` Sandbox bump

Use bumpversion: <br>
    💻 `bump-my-version bump --current-version 0.2.0 minor` <br> Run bumpversion
    💠 `git push` Push bumpversion changes

!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
