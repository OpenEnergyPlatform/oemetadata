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

## [0.0.0] - Release - Name of Release - 20YY-MM-DD

### Added
-
### Changed
-
### Removed
-
```

## Current

### Added
- Add badge for all fields [PR#117]

### Changed
- Separate examples from descripton and put into its own key-value pair [PR#117]

### Removed
-

## [1.5.2] - Release - Fix missing json files in pypi package, Improve context.jsonld - 2022-11-18

- Fix missing json files in pypi oemetadata package
- Add github actions/workflwos to automate package build and upload process on test and production pypi index

### Added

### Changed
- Update context.json in latest & v151 to ensure ontologically annotated metadata can be sparqled #99

## [1.5.1] - Release - Ontology-Ready - 2022-02-21

### Added
- Use  [GitHub projects](https://github.com/OpenEnergyPlatform/oemetadata/projects) to organise releases
- Add new example table to show connection to OEO
- Add test for latest directory to CI [PR#74]
- Add tests for v151 [PR#81]
- Add release version directory for oem-v151

### Changed
- Update ``subject`` to work with OEO
- Rename and update ``isAbout`` to work with OEO
- Rename and update ``valueReference`` to work with OEO
- Improve documentation
- Update schema.json
- Update CHANGELOG.md and give names to releases
- Update CONTRIBUTING.md

## [1.5.0] - Release - Get Some Semantics - 2021-11-18

### Added
- Add keys for linked data compatibility: ``@context``, ``@id``, ``subject``, ``is_about``, ``value_reference``
- Add context.json file 
- Add licence information to README.md

### Changed
- Clarify instructions for dealing with non-applicable keys (null) and missing values ("todo")
- Make key 13.2 ``timeseries`` a list
- Relocate development information from README.md to CONTRIBUTING.md 
- Update all .json files to v1.5.0
- Reintroduce automated tests (CI) by switching form travis-ci to github actions [PR#63]
- Updated schema.json for v1.5.0 now includes the new key ``title`` which describes the title of the curent field [PR#56] adapted from [PR#43]

### Removed
- Delete future directory

## [1.4.1] Minor Release - Repo Upgrade - 2021-01-18

### Added
- Add directory for v1.4.1
- Add tests for v1.4.1
- Add current section to Changelog, documenting all changes in current branch and stage for release
- Extend black options, COMMAND tox -v now shows exactly what code must be reformatted

### Changed
- Rename repository from "metadata" to "oemetadata"

## [1.4.0] Release - It'll be a standard - 2021-01-11

### Added
- Add ``timeseries`` to ``temporal``
- Add ``context`` object for project information
- Add ``object`` to ``contributors`` to decide between data and metadata
- Add ``profile`` to ``resources`` according to datapackage standard
- Add ``encoding`` to ``resources`` according to datapackage standard
- Add ``schema`` to ``resources`` according to datapackage standard
- Add ``type`` to ``fields`` for data types
- Add ``primaryKey``
- Add ``foreignKeys``
- Add ``dialect``
- Add ``review``
- Add ``metaMetadata``
- Add ``_comment``

### Changed
- Rename ``url`` to ``path`` according to datapackage standard

## [1.0.1] Initial Release - Hello OEMetadata - 2019-11-07

### Added

- OEMetadata version v1.3.0 metadata schema, example, template
- OEMetadata version v1.4.0 metadata schema, example, template
- Python implementation and tests for schema, example, template of v1.3.0
- Python implementation and tests for schema, example, template of v1.4.0
- Implementation of metaschema (draft07) and test of metaschema

