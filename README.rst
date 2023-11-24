
.. figure:: https://user-images.githubusercontent.com/14353512/185425447-85dbcde9-f3a2-4f06-a2db-0dee43af2f5f.png
    :align: left
    :target: https://github.com/rl-institut/super-repo/
    :alt: Repo logo

.. list-table::
   :widths: 50 50

   * - License
     - |badge_license|
   * - Workflow
     - Badge
   * - Automated tests
     - `|Automated tests|`
   * - PyPI Publish
     - `|PyPI Publish|`
   * - Docs
     - `|Docs|`
   * - Development
     - |badge_issue_open| |badge_issue_closes| |badge_pr_open| |badge_pr_closes|
   * - Community
     - |badge_contributing| |badge_contributors| |badge_repo_counts|

.. |Automated tests| image:: https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/metadata-test.yml/badge.svg
   :target: https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/metadata-test.yml
   :alt: Automated tests

.. |PyPI Publish| image:: https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/pypi-publish.yml/badge.svg
   :target: https://pypi.org/project/oemetadata/
   :alt: PyPI Publish

.. |Docs| image:: https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/pages/pages-build-deployment/badge.svg
   :target: https://openenergyplatform.github.io/oemetadata/
   :alt: Docs

.. image:: https://raw.githubusercontent.com/OpenEnergyPlatform/organisation/master/logo/OpenEnergyFamily_Logo_OEMetadata.png
   :align: right
   :width: 100
   :height: 100
   :alt: OpenEnergyMetadata
   :target: https://github.com/OpenEnergyPlatform/oemetadata/

.. image:: https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4
   :align: right
   :width: 100
   :height: 100
   :alt: OpenEnergyPlatform
   :target: https://openenergy-platform.org/

======================================================
Open Energy Family - Open Energy Metadata (OEMetadata)
======================================================

.. contents::
    :depth: 2
    :local:
    :backlinks: top

Open Energy Metadata (OEMetadata) is an energy metadata standard including a template, examples and a metadata schema. It is an extensive set of metadata based on the tabular data package specifications and the FAIR principles. The metadata contains multiple fields (keys) in a nested JSON structure.

You can find the latest version right here:

- `template.json <https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/template.json>`_ contains an empty metadata string
- `metadata_key_description.md <https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/metadata_key_description.md>`_ contains a description of each metadata key
- `example.json <https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/example.json>`_ contains a basic metadata example

License / Copyright
=====================

This repository is licensed under `MIT License (MIT) <https://spdx.org/licenses/MIT.html>`_.
The oemetadata is licensed under `Creative Commons Zero v1.0 Universal <https://creativecommons.org/publicdomain/zero/1.0/>`_. The oemetadata example and oemetadata template are licensed under `Creative Commons Zero v1.0 Universal <https://creativecommons.org/publicdomain/zero/1.0/>`_.

Installation
=====================

.. code-block:: bash

    pip install oemetadata

Usage Examples
=====================

.. code-block:: python

    from metadata.latest.example import OEMETADATA_LATEST_EXAMPLE

    print(OEMETADATA_LATEST_EXAMPLE)

.. code-block:: python

    from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA

    print(OEMETADATA_LATEST_SCHEMA)

.. code-block:: python

    from metadata.latest.template import OEMETADATA_LATEST_TEMPLATE

    print(OEMETADATA_LATEST_TEMPLATE)

Contributing
=====================

For further contributing infos and conventions see: `CONTRIBUTING.md <https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/CONTRIBUTING.md>`_.

Release a New Version
=====================
See the complete instructions in the `RELEASE_PROCEDURE <https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/RELEASE_PROCEDURE.md>`_.

Make PyPI Release:
------------------

1. Update the version in the setup.py file to reflect the new version number.
2. Follow these steps to utilize the release automation workflow:

   Testing Stage:

   - Create a new branch named "release/branch-name" to test your changes.
   - Make sure all your changes are included in a single commit (until a more efficient workflow is determined).
   - The release automation workflow is automatically executed, which will attempt to upload the package to the test.PyPI repository.
   - If the upload is successful, the workflow will fail on subsequent attempts (as it should only be uploaded once successfully).

   Deployment Stage:

   - Merge the release branch into the "master" or "main" branch, depending on your repository's default branch.
   - Publish a release on GitHub, documenting the changes made in this version.
   - This action will trigger the automated workflow to release the new version to the official PyPI repository.

   Manual steps are:

   .. code-block:: bash

       python3 setup.py sdist bdist_wheel
       twine upload dist/*



.. |badge_license| image:: https://img.shields.io/github/license/OpenEnergyPlatform/oemetadata
    :target: LICENSE.txt
    :alt: License
.. |badge_contributing| image:: https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat
    :alt: contributions

.. |badge_repo_counts| image:: http://hits.dwyl.com/OpenEnergyPlatform/oemetadata.svg
    :alt: counter

.. |badge_contributors| image:: https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square
    :alt: contributors

.. |badge_issue_open| image:: https://img.shields.io/github/issues-raw/OpenEnergyPlatform/oemetadata
    :alt: open issues

.. |badge_issue_closes| image:: https://img.shields.io/github/issues-closed-raw/OpenEnergyPlatform/oemetadata
    :alt: closes issues

.. |badge_pr_open| image:: https://img.shields.io/github/issues-pr-raw/OpenEnergyPlatform/oemetadata
    :alt: closes issues

.. |badge_pr_closes| image:: https://img.shields.io/github/issues-pr-closed-raw/OpenEnergyPlatform/oemetadata
    :alt: closes issues
