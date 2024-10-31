# Oemetadata build tooling

The OEMetaData uses the json schema specification to define the structure of the metadata. This specification is quite extensive and includes a lot of fields its development had to be supported by a simple tooling. It offers developers the possibility to edit the schema.json and its field groups in a more modular manner. This helps to keep an overview and to focus discussions on certain aspects of the OEMetData specification.

Over the years it also became an constant issue to keep all parts of the release consistent with all changes made to the schema.json. The tooling enables developers to only edit the schema.json and then generate the relevant example and template JSON files based on the OEMetaData specification and the example values available as part of the schema.json. 

## Structure

The structure of the OEMetaData release contents changed a bit. While the known schema, example and template json and python files are still available the new directory 'build_source' is now also part of each release. It contains two sub directories: `build_source/schemas/` includes the schema parts, if you want to extend the OEMetaData specification this is the directory you should maintain. The `build_source/scripts/` implements the tooling. There are 3 scripts for schema ref resolve and schema, example and template JSON file generation. The settings script is used to share common information across python modules, in this case it includes mainly the path´s.  

## Usage

Using bash terminal on wsl ubuntu distribution with Python >3.8 installed 

Create a python3 environment.

    #assuming you are currently in the oemetadata base directory.
    python3 -m venv env 

Install the requirements.

    source env/bin/activate
    pip install -r requirements.txt

Navigate to the tooling directory to ease usage and run the tooling as python script.

    #assuming you are currently in the oemetadata base directory.
    cd metadata/v20/build_source/scripts/
    # generate the oemetadata json schema based on json schemas in the schemas directory
    python metadata/v20/build_source/scripts/resolve_schema_refs.py
    # use option --debug to show additional logging information
    python metadata/v20/build_source/scripts/resolve_schema_refs.py --debug

Generate the example and template
    
    python metadata/v20/build_source/scripts/generate_example_from_schema.py
    python metadata/v20/build_source/scripts/generate_template_from_schema.py


