# Release

- RELEASE_PROCEDURE.md
- VERSION
- MANIFEST.in
- .bumpversion.cfg


## Release a new version
See the complete instructions in the [RELEASE_PROCEDURE](./RELEASE_PROCEDURE.md).

### Make PyPI release:

First update version in setup.py, then:

```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
