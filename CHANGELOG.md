# Changelog

All notable changes to this project will be documented in this file.

The format is inspired from [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and the versioning aim to respect [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

Here is a template for new release sections

```
## Current

### Added
-
### Changed
-
### Removed
-

## [_._._] - 20XX-MM-DD

### Added
-
### Changed
-
### Removed
-
```
## [1.5.1] - 2022-02-15

## Current

### Added

### Changed

## [1.5.0] - Release 

### Added
- Add keys for linked data compatibility: ``@context``, ``@id``, ``subject``, ``is_about``, ``value_reference``
- Add context.json file 

### Changed
- Delete future directory
- Clarify instructions for dealing with non-applicable keys (null) and missing values ("todo")
- Make key 13.2 ``timeseries`` a list
- Relocate development information from README.md to CONTRIBUTING.md 
- Add licence information to README.md
- Update all .json files to v1.5.0
- reintroduce automated tests (CI) by switching form travis-ci to github actions [PR#63]
- Updated schema.json for v1.5.0 now includes the new key "title" which describes the title of the curent field [PR#56] adapted from [PR#43]

## [1.4.1] - Minor release 2021-01-14

### Added
- New directory for release version 1.4.1
- Added test for version 1.4.1
- Add Current section to Changelog, documenting all changes in current branch and stage for release
- Extend black options, COMMAND tox -v now shows exactly what code must be reformatted

### Changed
- Rename repository from "metadata" to "oemetadata"

## [1.0.1] Initial release

### Added

- v130 metadata schema, example, template
- v140 metadata schema, example, template
- Python implementation and tests for schema, example, template of v130
- Python implementation and tests for schema, example, template of v140
- Implementation of metaschema (draft07) and test of metaschema

