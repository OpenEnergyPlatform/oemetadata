<a href="http://oep.iks.cs.ovgu.de/"><img align="right" width="200" height="200" src="https://avatars2.githubusercontent.com/u/37101913?s=400&u=9b593cfdb6048a05ea6e72d333169a65e7c922be&v=4" alt="OpenEnergyPlatform"></a>

# OpenEnergyPlatform - Metadata

OEP metadata schemata, examples and templates package

[![Build Status](https://travis-ci.org/OpenEnergyPlatform/metadata.svg?branch=develop)](https://travis-ci.org/OpenEnergyPlatform/metadata)

## License / Copyright

This repository is licensed under [MIT License (MIT)](https://spdx.org/licenses/MIT.html)

## Installation

`pip install oep-metadata`

## Usage Examples

```
from metadata.v140.example import METADATA_V140_EXAMPLE

print(METADATA_V140_EXAMPLE)
```

```
from metadata.v140.schema import METADATA_V140_SCHEMA

print(METADATA_V140_SCHEMA)
```

```
from metadata.v140.template import METADATA_V140_TEMPLATE

print(METADATA_V140_TEMPLATE)
```

## Development

### Example for activating virtualenv and install development dependencies:

1. Create virtualenv in root folder of repo

`python -m venv venv`

2. Activate virtualenv

    Linux:

    `. venv/bin/activate`

    Windows:

    `. venv/scripts/activate`

3. Install requirements

`pip install -r requirements.txt`

### Run tests locally (after above steps):

Short:

`pytest`

Complete:

`tox -v`

### If a Python interpreter version is missing:

Linux (Ubuntu):

```
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt-get update
# Install only missing interpreters:
sudo apt-get install python3.6
sudo apt-get install python3.7
```

### Make PyPI release:

First bump version in setup.py, then:

```
python3 setup.py sdist bdist_wheel
twine upload dist/*
```
