<!--
SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut
SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut
SPDX-FileCopyrightText: Christian Hofmann <christian-rli> © Reiner Lemoine Institut

SPDX-License-Identifier: CC0-1.0

Title: Changelog of released versions
-->

# Changelog

All notable changes to this project will be documented in this file. <br>
For each version, important additions, changes and removals are listed here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).


## [Unreleased]

### Added
- Add REUSE Software compliance check [(#218)](https://github.com/OpenEnergyPlatform/oemetadata/pull/218)

### Changed
- Update documentation and README [(#209)](https://github.com/OpenEnergyPlatform/oemetadata/pull/209)
- Move old metadata versions to folder [(#209)](https://github.com/OpenEnergyPlatform/oemetadata/pull/209)
- Update JSON schema from (draft-07) to (Draft 2020-12) [(#212)](https://github.com/OpenEnergyPlatform/oemetadata/pull/212)
- Update all tests [(#212)](https://github.com/OpenEnergyPlatform/oemetadata/pull/212)
- Separate `timeseries - resolution` into `resolutionValue` and `resolutionUnit` [(#213)](https://github.com/OpenEnergyPlatform/oemetadata/pull/213)
- Rename URI from `path` to `@id` [(#214)](https://github.com/OpenEnergyPlatform/oemetadata/pull/214)
- Rename ``source``- ``licenses`` to ``sourceLicenses`` [(#215)](https://github.com/OpenEnergyPlatform/oemetadata/pull/215)
- Update create template [(#217)](https://github.com/OpenEnergyPlatform/oemetadata/pull/217)

### Removed
- [(#)]()


## [2.0.1] - Major Release - Refactor OEMetadata for NFDI

### Changed
- HotFix naming errors in some files related to the renaming of master to production [#202](https://github.com/OpenEnergyPlatform/oemetadata/issues/202)


## [2.0.0] - Major Release - Refactor OEMetadata for NFDI

### Added
- Add OEMetadata version 2.0: [#144](https://github.com/OpenEnergyPlatform/oemetadata/issues/144)
- Introduce a schema build system: [#105](https://github.com/OpenEnergyPlatform/oemetadata/pull/105)
  - The build files (schema & script) are maintained for each version (starting form v1.6.0) within the new directory called "metadata/(version)/build_source"  
  - The schema is rather long and complex. We split the long schema.json into modules. The modules are assembled in a json file that specifies the structure of the final schema.json, and it is called schema_structure.json.
  - It uses JSON schema $ref elements to reference the schema modules, and it provides code to resolve the reference´s and generate the complete schema.json.
- Add code to generate an example.json based on the schema.json. We read the example values for each of the fields specified in the schema and generate the example. [#105](https://github.com/OpenEnergyPlatform/oemetadata/pull/105)
- Add updated context.json [(#154)](https://github.com/OpenEnergyPlatform/oemetadata/pull/154)
- Add ``embargoPeriod`` section with keys ``start``, ``end``, ``isActive`` [(#155)](https://github.com/OpenEnergyPlatform/oemetadata/pull/155)
- Add ``path`` to ``contributors`` [(#157)](https://github.com/OpenEnergyPlatform/oemetadata/pull/157)
- Add organization to contributors [(#157)](https://github.com/OpenEnergyPlatform/oemetadata/pull/157)
- Add roles to contributors [(#157)](https://github.com/OpenEnergyPlatform/oemetadata/pull/157)
- Add section for ``Linked Data`` keys [(#159)](https://github.com/OpenEnergyPlatform/oemetadata/pull/159)
- Add mandatory fields to the json schema (Iron Badge) [(#160)](https://github.com/OpenEnergyPlatform/oemetadata/pull/160)
- Add key ``copyrightStatement`` to ``sources`` [(#162)](https://github.com/OpenEnergyPlatform/oemetadata/pull/162)
- Add key nullable to fields section (columns) [(#161)](https://github.com/OpenEnergyPlatform/oemetadata/pull/161)
- Add explicit json types [(#166)](https://github.com/OpenEnergyPlatform/oemetadata/pull/166)
- Add key ``topics`` to ``general`` [(#170)](https://github.com/OpenEnergyPlatform/oemetadata/pull/170)
- Add badge labels to documentation [(#175)](https://github.com/OpenEnergyPlatform/oemetadata/pull/175)
- Implement schema build system v1: Enhance the resolve and generation module [(#180)](https://github.com/OpenEnergyPlatform/oemetadata/pull/180)
- Add basic documentation with MkDocs [(#184)](https://github.com/OpenEnergyPlatform/oemetadata/pull/184)
- Add key ``publisher`` to ``context`` [(#191)](https://github.com/OpenEnergyPlatform/oemetadata/pull/191)
- Add array ``authors`` to ``sources``. [(#193)](https://github.com/OpenEnergyPlatform/oemetadata/pull/193)
- Add ``year`` to ``sources`` [(#194)](https://github.com/OpenEnergyPlatform/oemetadata/pull/194)
- Add key ``description`` to ``collection`` and update badges [(#195)](https://github.com/OpenEnergyPlatform/oemetadata/pull/195)
- Add mappings to DCAT-AP to the documentation [(#198)](https://github.com/OpenEnergyPlatform/oemetadata/pull/198)
- Add issue template for user kudos [(#199)](https://github.com/OpenEnergyPlatform/oemetadata/pull/199)

### Changed
- Remove comment field as it holds information on how to fill out the metadata and therefore should not be part of the actual oemetadata but the documentation. [#105](https://github.com/OpenEnergyPlatform/oemetadata/pull/105)
- Update the schema json file content (schema generation still broken, add desired output) and fix the schema path in the script for generating examples (it pointed to an incorrect directory and file name) [(#149)](https://github.com/OpenEnergyPlatform/oemetadata/pull/149)
- Update broken Link in key description example [(#159)](https://github.com/OpenEnergyPlatform/oemetadata/pull/159)
- Update ``resource/profile`` to ``resource/type`` [(#164)](https://github.com/OpenEnergyPlatform/oemetadata/pull/164)
- Update links in context.json and example.json for all versions [(#167)](https://github.com/OpenEnergyPlatform/oemetadata/pull/167)
- Restrict the version number to only major and minor versions since 2.0 [(#168)](https://github.com/OpenEnergyPlatform/oemetadata/pull/168)
- Update all descriptions and examples [(#175)](https://github.com/OpenEnergyPlatform/oemetadata/pull/175)
- Build scripts use a settings file to share variables [(#177)](https://github.com/OpenEnergyPlatform/oemetadata/pull/177)
- Refactor the ``spatial`` section and add new keys for location: ``address``, ``@id``, ``latitude``, ``longitude`` and for extent: ``name``, ``@id``, ``resolutionValue``, ``resolutionUnit``, ``boundingBox``, ``crs`` [(#179)](https://github.com/OpenEnergyPlatform/oemetadata/pull/179)
- Move ``linkedData`` keys to the top of the resource [(#183)](https://github.com/OpenEnergyPlatform/oemetadata/pull/183)
- Update order of keys in section context [(#191)](https://github.com/OpenEnergyPlatform/oemetadata/pull/191)

### Removed
- Remove email from contributors [(#157)](https://github.com/OpenEnergyPlatform/oemetadata/pull/157)
- Remove all additionalProperties is false [(#163)](https://github.com/OpenEnergyPlatform/oemetadata/pull/163)
- Remove duplicate keys from resources [(#165)](https://github.com/OpenEnergyPlatform/oemetadata/pull/165)
- Remove linkedData section and keys [(#176)](https://github.com/OpenEnergyPlatform/oemetadata/pull/176)


## [1.6.0] - Release - Introduce badges in json schema - 2023-05-30

### Added
- Add badge for all fields [PR#117](https://github.com/OpenEnergyPlatform/oemetadata/pull/117)
- Add CITATION.cff with list of authors [(#111)](https://github.com/OpenEnergyPlatform/oemetadata/pull/111)

### Changed
- Separate examples from description and put into its own key-value pair [(PR#117)](https://github.com/OpenEnergyPlatform/oemetadata/pull/117)
- Add issue and PR templates [(#116)](https://github.com/OpenEnergyPlatform/oemetadata/pull/116)
- Update context field [(PR#114)](https://github.com/OpenEnergyPlatform/oemetadata/pull/114)


## [1.5.2] - Release - Fix Repo and Package - 2022-11-18

### Added
- Add GitHub actions to automate package build and upload process on test and production pypi index

### Changed
- Fix missing json files in pypi oemetadata package
- Update context.json in latest & v151 to ensure ontologically annotated metadata can be sparkled #99


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
- Reintroduce automated tests (CI) by switching form travis-ci to GitHub actions [PR#63]
- Updated schema.json for v1.5.0 now includes the new key ``title`` which describes the title of the current field [PR#56] adapted from [PR#43]

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

