..
  SPDX-FileCopyrightText: Ludwig Hülk <@Ludee> © Reiner Lemoine Institut

  SPDX-License-Identifier: CC0-1.0

.. figure:: https://user-images.githubusercontent.com/14353512/245271998-794e9d73-e728-4993-9ecf-4d0d08d96827.png
    :align: left
    :target: https://github.com/OpenEnergyPlatform/oemetadata
    :alt: Repo logo

=================================
Open Energy Metadata (OEMetadata)
=================================

**The energy metadata standard including a metadata schema, templates, and examples.**

.. list-table::
   :widths: auto

   * - License
     - |badge_license| |badge_reuse|
   * - Documentation
     - |badge_documentation|
   * - Publication
     - |badge_pypi| |badge_python| |badge_pypi_downloads|
   * - Development
     - |badge_issue_open| |badge_issue_closes| |badge_pr_open| |badge_pr_closes|
   * - Community
     - |badge_contributing| |badge_contributors| |badge_repo_counts|

.. contents::
    :depth: 2
    :local:
    :backlinks: top

Introduction
============
| Open Energy Metadata (OEMetadata) is a metadata standard for the energy domain.
| It is an extensive set of metadata based on the tabular data package specifications and the FAIR principles.
| The metadata contains multiple fields (keys) in a nested JSON structure.

You can find the latest version right here:

- `template.json <https://github.com/OpenEnergyPlatform/oemetadata/blob/production/metadata/latest/template.json>`_ contains an empty metadata string
- `example.json <https://github.com/OpenEnergyPlatform/oemetadata/blob/production/metadata/latest/example.json>`_ contains a basic metadata example
- `metadata_key_description.md <https://github.com/OpenEnergyPlatform/oemetadata/blob/production/metadata/latest/metadata_key_description.md>`_ contains a description of each metadata key

Documentation
=============
| The documentation is created with Markdown using `MkDocs <https://www.mkdocs.org/>`_.
| All files are stored in the ``docs`` folder of the repository.
| A **GitHub Actions** deploys the ``production`` branch on a **GitHub Page**.
| The documentation page is `openenergyplatform.github.io/oemetadata/ <https://openenergyplatform.github.io/oemetadata/>`_

Collaboration
=============
| Everyone is invited to develop this repository with good intentions.
| Please follow the workflow described in the `CONTRIBUTING.md <CONTRIBUTING.md>`_.
| Development work that aims to extend the oemetadata specification is added to the build_source/schemas/ directory for each release.
| To generate the schema, template & example JSON files see your script based `tooling <.metadata/latest/build_source/>`_ 

License and Citation
====================
| The code of this repository is licensed under the **MIT License** (MIT).
| See `LICENSE.txt <LICENSE.txt>`_ for rights and obligations.
| See the *Cite this repository* function or `CITATION.cff <CITATION.cff>`_ for citation of this repository.
| Copyright: `OEMetadata <https://github.com/OpenEnergyPlatform/oemetadata/>`_ © `Reiner Lemoine Institut <https://reiner-lemoine-institut.de/>`_ | `MIT <LICENSE.txt>`_
| The OEMetadata schema is licensed under `Creative Commons Zero v1.0 Universal <https://creativecommons.org/publicdomain/zero/1.0/>`_.
| The OEMetadata examples and templates are licensed under `Creative Commons Zero v1.0 Universal <https://creativecommons.org/publicdomain/zero/1.0/>`_.


.. |badge_license| image:: https://img.shields.io/github/license/OpenEnergyPlatform/oemetadata
    :target: https://github.com/OpenEnergyPlatform/oemetadata/blob/production/LICENSE.txt
    :alt: License

.. |badge_reuse| image:: https://api.reuse.software/badge/github.com/OpenEnergyPlatform/oemetadata
    :target: https://api.reuse.software/info/github.com/OpenEnergyPlatform/oemetadata
    :alt: REUSE

.. |badge_documentation| image:: https://img.shields.io/github/actions/workflow/status/OpenEnergyPlatform/oemetadata/gh-pages.yml?branch=release-v2.0.1
    :target: https://openenergyplatform.github.io/oemetadata/
    :alt: Documentation

.. |badge_pypi| image:: https://img.shields.io/pypi/v/oemetadata
    :target: https://pypi.org/project/oemetadata/
    :alt: PyPI Version

.. |badge_python| image:: https://img.shields.io/pypi/pyversions/oemetadata
    :target: https://pypi.org/project/oemetadata/
    :alt: PyPI Python Version

.. |badge_pypi_downloads| image:: https://img.shields.io/pypi/dm/oemetadata
    :target: https://openenergyplatform.github.io/oemetadata/
    :alt: PyPI Downloads

.. |badge_contributing| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
    :target: https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/CONTRIBUTING.md
    :alt: Contributions

.. |badge_repo_counts| image:: http://hits.dwyl.com/OpenEnergyPlatform/oemetadata.svg
    :alt: Counter

.. |badge_contributors| image:: https://img.shields.io/github/contributors/OpenEnergyPlatform/oemetadata
    :target: https://github.com/OpenEnergyPlatform/oemetadata/graphs/contributors
    :alt: Contributors

.. |badge_issue_open| image:: https://img.shields.io/github/issues-raw/OpenEnergyPlatform/oemetadata
    :target: https://github.com/OpenEnergyPlatform/oemetadata/issues
    :alt: Open issues

.. |badge_issue_closes| image:: https://img.shields.io/github/issues-closed-raw/OpenEnergyPlatform/oemetadata
    :target: https://github.com/OpenEnergyPlatform/oemetadata/issues?q=is%3Aissue+is%3Aclosed
    :alt: Closed issues

.. |badge_pr_open| image:: https://img.shields.io/github/issues-pr-raw/OpenEnergyPlatform/oemetadata
    :target: https://github.com/OpenEnergyPlatform/oemetadata/pulls
    :alt: Open PR

.. |badge_pr_closes| image:: https://img.shields.io/github/issues-pr-closed-raw/OpenEnergyPlatform/oemetadata
    :target: https://github.com/OpenEnergyPlatform/oemetadata/pulls?q=is%3Apr+is%3Aclosed
    :alt: Closed PR
