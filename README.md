| Workflow                                       | Badge                                                                                                      |
| ---------------------------------------------- | ---------------------------------------------------------------------------------------------------------- |
| Automated tests                                | [![Automated tests](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/metadata-test.yml/badge.svg)](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/metadata-test.yml) |
| PyPI Publish                                   | [![](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/pypi-publish.yml/badge.svg)](https://pypi.org/project/oemetadata/) |
| Docs                                           | [![Docs](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/pages/pages-build-deployment/badge.svg)](https://openenergyplatform.github.io/oemetadata/) |


<a href="https://github.com/OpenEnergyPlatform/oemetadata/"><img align="right" width="100" height="100" src="https://raw.githubusercontent.com/OpenEnergyPlatform/organisation/master/logo/OpenEnergyFamily_Logo_OEMetadata.png" alt="OpenEnergyMetadata"></a>
<a href="https://openenergy-platform.org/"><img align="right" width="100" height="100" src="https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4" alt="OpenEnergyPlatform"></a>

# Open Energy Family - Open Energy Metadata (OEMetadata)

Open Energy Metadata (OEMetadata) is an energy metadata standard including a template, examples and a metadata schema.
It is an extensive set of metadata based on the tabular data package specifications and the FAIR principles.
The metadata contains multiple fields (keys) in a nested JSON structure.

You can find the latest version right here:
* [template.json](https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/template.json) contains an empty metadata string
* [metadata_key_description.md](https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/metadata_key_description.md) contains a description of each metadata key
* [example.json](https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/metadata/latest/example.json) contains a basic metadata example


## License / Copyright

This repository is licensed under [MIT License (MIT)](https://spdx.org/licenses/MIT.html) <br>
The oemetadata is licensed under [Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) <br>
The oemetadata example and oemetadata template are licensed under [Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

## Installation

`pip install oemetadata`

## Usage Examples

```
from metadata.latest.example import OEMETADATA_LATEST_EXAMPLE

print(OEMETADATA_LATEST_EXAMPLE)
```

```
from metadata.latest.schema import OEMETADATA_LATEST_SCHEMA

print(OEMETADATA_LATEST_SCHEMA)
```

```
from metadata.latest.template import OEMETADATA_LATEST_TEMPLATE

print(OEMETADATA_LATEST_TEMPLATE)
```

## Contributing

For further contributing infos and conventions see: [CONTRIBUTING.md](https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/CONTRIBUTING.md)

## Release a new version
See the complete instructions in the [RELEASE_PROCEDURE](https://github.com/OpenEnergyPlatform/oemetadata/blob/develop/RELEASE_PROCEDURE.md).

### Make PyPI release:

1. Update the version in the setup.py file to reflect the new version number.
2. Follow these steps to utilize the release automation workflow:

Testing Stage:

- Create a new branch named "release/branch-name" to test your changes.
- Make sure all your changes are included in a single commit (until a more efficient workflow is determined).
- The release automation workflow is automatically exceuted, which will attempt to upload the package to the test.PyPI repository.
- If the upload is successful, the workflow will fail on subsequent attempts (as it should only be uploaded once successfully).

Deployment Stage:

- Merge the release branch into the "master" or "main" branch, depending on your repository's default branch.
- Publish a release on GitHub, documenting the changes made in this version.
- This action will trigger the automated workflow to release the new version to the official PyPI repository.


Manual steps are:

```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
