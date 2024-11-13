<!--
SPDX-FileCopyrightText: Ludwig Hülk <Ludee> © Reiner Lemoine Institut
SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut

SPDX-License-Identifier: CC0-1.0
-->

# OEMetadata Build Source

The OEMetadata uses the [JSON Schema](https://json-schema.org/) specification 
to define the structure of the metadata. <br>
It offers the possibility to make the `schema.json` more modular. <br>
For better maintenance the file is split into separate files. <br>
The `schema_structure.json` contains the overall pattern of the structure.

## Structure

The directory `build_source` contains two parts:

### Schemas `build_source/schemas/`

The schemas are the core of the OEMetadata specification. <br>
They are separated by category and follow the logic of OEMetadata structure.


### Scripts `build_source/scripts/`

- `create_schema.py` Creates the complete `schema.json` from `schemas`
- `create_template.py` Creates the `template.json` from `schema.json`
- `create_example.py` Creates the `example.json` from `schema.json`

## Usage

Create a python3 environment

    cd ../oemetadata/
    python3 -m venv env 

Install the requirements

    source env/bin/activate
    pip install -r requirements.txt

Create the OEMetadata json schema from schemas

    cd metadata/v2/v20/build_source/scripts/
    python metadata/v2/v20/build_source/scripts/create_schema.py

Create the OEMetadata template and example from json schema
    
    python metadata/v2/v20/build_source/scripts/create_example_from_schema.py
    python metadata/v2/v20/build_source/scripts/create_template_from_schema.py
