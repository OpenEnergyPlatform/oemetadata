[![Automated tests](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/metadata-test.yml/badge.svg)](https://github.com/OpenEnergyPlatform/oemetadata/actions/workflows/metadata-test.yml)

<a href="https://github.com/OpenEnergyPlatform/oemetadata/"><img align="right" width="100" height="100" src="https://raw.githubusercontent.com/OpenEnergyPlatform/organisation/master/logo/OpenEnergyFamily_Logo_OEMetadata.png" alt="OpenEnergyMetadata"></a>
<a href="https://openenergy-platform.org/"><img align="right" width="100" height="100" src="https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4" alt="OpenEnergyPlatform"></a>

# Open Energy Family - Open Energy Metadata (OEMetadata)

Open Energy Metadata (OEMetadata) is an energy metadata standard including a template, examples and a metadata schema.
It is an extensive set of metadata based on the tabular data package specifications and the FAIR principles.
The metadata contains multiple fields (keys) in a nested JSON structure.

You can find the latest version right here:
* [template.json](./metadata/latest/template.json) contains an empty metadata string
* [metadata_key_description.md](./metadata/latest/metadata_key_description.md) contains a description of each metadata key
* [example.json](./metadata/latest/example.json) contains a basic metadata example


## License / Copyright

This repository is licensed under [MIT License (MIT)](https://spdx.org/licenses/MIT.html) <br>
The oemetadata is licensed under [Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/) <br>
The oemetadata example and oemetadata template are licensed under [Creative Commons Zero v1.0 Universal](https://creativecommons.org/publicdomain/zero/1.0/)

## Installation

`pip install oep-metadata`

## Usage Examples

```
from metadata.latest.example import OEMETADATA_v150_EXAMPLE

print(OEMETADATA_LATEST_EXAMPLE)
```

```
from metadata.latest.schema import OEMETADATA_v150_SCHEMA

print(OEMETADATA_LATEST_SCHEMA)
```

```
from metadata.latest.template import OEMETADATA_v150_TEMPLATE

print(OEMETADATA_LATEST_TEMPLATE)
```

## Contributing

For further contributing infos and conventions see: [CONTRIBUTING.md](./CONTRIBUTING.md)

## Make PyPI release:

First bump version in setup.py, then:

```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
