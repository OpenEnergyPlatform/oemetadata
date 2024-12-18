<!--
SPDX-FileCopyrightText: Ludwig Hülk <Ludee> © Reiner Lemoine Institut
SPDX-FileCopyrightText: Jonas Huber <jh-RLI> © Reiner Lemoine Institut

SPDX-License-Identifier: CC0-1.0
-->

# OEMetadata - Key Description

This pages describes the key of **OEMetadata version 2.0 .** <br>
You can have a look at an empty [template](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/metadata/latest/template.json) and a filled out [example](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/metadata/latest/example.json) of the metadata string.<br>
[`schema.json`](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/metadata/latest/schema.json) contains the complete schema.

## JSON Format

The JSON format offers different formats:

* key-value pair: 
    ```JSON
    {"key":"value"}
    ```
* array: 
    ```JSON
    {"key":
        ["value","value"]}
    ```
* object {nested key}:
    ```JSON
    {"key": {
        "key_a":"value",
        "key_b":"value"}}
    ```
* array of objects {nested array}:
    ```JSON
    {"key": [
        {"key_a":"value"},
        {"key_a":"value"}]}
    ```


## Metadata keys with a description and example

If a field is not applicable use: `null`.<br>
If a value is not yet available, use: `ToDo`.

### Collection Keys
| # | Key         | Description                                                                                 | Example                                                     | Badge  |
|---|-------------|---------------------------------------------------------------------------------------------|-------------------------------------------------------------|--------|
| 1 | name        | A filename or database conform collection name.                                             | oep_oemetadata                                              | Iron   |
| 2 | title       | A human readable collection name.                                                           | OEP OEMetadata                                              | Bronze |
| 3 | description | A free text description of the collection.                                                  | A collection of tables for the OEMetadata examples.         | Bronze |
| 4 | id          | A unique identifier (UUID/DOI) for the collection.                                          | https://databus.openenergyplatform.org/oeplatform/reference | Silver |
| 5 | resources   | An array of objects of the resources. The collection can contain several (database) tables. |                                                             |        |

### Resource - Linked Data Keys
| # | Key      | Description                                                                                              | Example                                                                                                 | Badge    |
|---|----------|----------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------|----------|
| 1 | @id      | A Uniform Resource Identifier (URI) that links the resource via the OpenEnergyDatabus (DBpedia Databus). | https://databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/2022-11-07     | Platinum |
| 2 | @context | Explanation of metadata keys in ontology terms.                                                          | https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/metadata/latest/context.json | Platinum |

### Resource - General Keys
| #    | Key               | Description                                                                                                                                                                      | Example                                                                              | Badge    |
|------|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|----------|
| 1    | name              | A filename or database conform table name.                                                                                                                                       | oep_oemetadata_table_example                                                         | Iron     |
| 2    | topics            | An array of predefined topics that correspond to the database schemas of the OEP.                                                                                                | model_draft, reference                                                               | Bronze   |
| 3    | title             | A human readable table name.                                                                                                                                                     | OEP OEMetadata Example Table                                                         | Silver   |
| 4    | path              | A unique identifier (URI/UUID/DOI) for the table or file.                                                                                                                        | http://openenergyplatform.org/dataedit/view/model_draft/oep_oemetadata_table_example | Bronze   |
| 5    | description       | A description of the table. It should be usable as summary information for the table that is described by the metadata.                                                          | Example table used to illustrate the OEMetadata structure and meaning.               | Silver   |
| 6    | languages         | An array of languages used within the described data structures (e.g. titles, descriptions). The language key can be repeated if more languages are used. Standard: IETF (BCP47) | en-GB, de-DE, fr-FR                                                                  | Gold     |
| 7    | **subject**       | An array of objects that references to the subjects of the resource in ontology terms.                                                                                           |                                                                                      |
| 7.1  | name              | A class label of the ontology term.                                                                                                                                              | energy                                                                               | Platinum |
| 7.2  | path              | A unique identifier (URI/IRI) of the ontology class.                                                                                                                             | https://openenergyplatform.org/ontology/oeo/OEO_00000150                             | Platinum |
| 8    | keywords          | An array of freely selectable keywords that help with searching and structuring. The keyword are used and managed in the OEP as table tags.                                      | example, ODbL-1.0, NFDI4Energy                                                       | Silver   |
| 9    | publicationDate   | A date of publication of the data or metadata. The date format is ISO 8601 (YYYY-MM-DD).                                                                                         | 2024-10-15                                                                           | Bronze   |
| 10   | **embargoPeriod** | An object that describes the embargo period during which public access to the data is not allowed.                                                                               |
| 10.1 | start             | The start date of the embargo period. The date of the data (metadata) upload.                                                                                                    | 2024-10-11                                                                           | Bronze   |
| 10.2 | end               | The end date of the embargo period. This is the envisioned publication date.                                                                                                     | 2025-01-01                                                                           | Bronze   |
| 10.3 | isActive          | A boolean key that indicates if the embargo period is currently active. Must be changed to False on the embargo period end date.                                                 | True                                                                                 | Bronze   |

### Resource - Context Keys
| #    | Key               | Description                                                                                                                                                                   | Example                                                                                                              | Badge |
|------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|-------|
| 1    | **context**       | An object that describes the general setting, environment, or project leading to the creation or maintenance of this dataset. In science this is can be the research project. |                                                                                                                      |       |
| 1.1  | title             | A title of the associated project.                                                                                                                                            | NFDI4Energy                                                                                                          | Gold  | 
| 1.2  | homepage          | A URL of the project.                                                                                                                                                         | https://nfdi4energy.uol.de/                                                                                          | Gold  | 
| 1.3  | documentation     | A URL of the project documentation.                                                                                                                                           | https://nfdi4energy.uol.de/sites/about_us/                                                                           | Gold  | 
| 1.4  | sourceCode        | A URL of the source code of the project.                                                                                                                                      | https://github.com/NFDI4Energy                                                                                       | Gold  | 
| 1.5  | publisher         | The publishing agency of the data. This can be the OEP.                                                                                                                       | Open Energy Platform (OEP)                                                                                           | Gold  | 
| 1.6  | publisherLogo     | A URL to the logo of the publishing agency of data.                                                                                                                           | https://github.com/OpenEnergyPlatform/organisation/blob/production/logo/OpenEnergyFamily_Logo_OpenEnergyPlatform.svg | Gold  | 
| 1.7  | contact           | A reference to the creator or maintainer of the data set. It can be an email address or a GitHub handle.                                                                      | info@nfdi4energy.org                                                                                                 | Gold  | 
| 1.8  | fundingAgency     | A name of the entity providing the funding. This can be a government agency or a company.                                                                                     | Deutsche Forschungsgemeinschaft (DFG)                                                                                | Gold  | 
| 1.9  | fundingAgencyLogo | A URL to the logo or image of the funding agency.                                                                                                                             | https://upload.wikimedia.org/wikipedia/commons/8/86/DFG-logo-blau.svg                                                | Gold  | 
| 1.10 | grantNo           | An identifying grant number. In case of a publicly funded project, this number is assigned by the funding agency.                                                             | 501865131                                                                                                            | Gold  | 

### Resource - Spatial Keys
| #     | Key             | Description                                                                                                                   | Example                                 | Badge    |
|-------|-----------------|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------|----------|
| 1     | **spatial**     | An object that describes the spatial context of the data.                                                                     |                                         |          |
| 1.1   | **location**    | An object that describes a covered area or region.                                                                            |                                         |          |
| 1.1.1 | address         | An address of the location of the data. May be specified with street name, house number, zip code, and city name.             | Rudower Chaussee 12, 12489 Berlin       | Silver   |
| 1.1.2 | @id             | A path or URI to a specific location. It can use Wikidata or OpenStreetMap.                                                   | https://www.wikidata.org/wiki/Q77077223 | Platinum |
| 1.1.3 | longitude       | The latitude (lat) information of the location.                                                                               | 52.432822                               | Gold     |
| 1.1.4 | longitude       | The longitude (lon) information of the location.                                                                              | 13.5351004                              | Gold     |
| 1.2   | **extent**      | An object that describes a covered area or region.                                                                            |                                         |          |
| 1.2.1 | name            | The name of the region.                                                                                                       | Berlin                                  | Silver   |
| 1.2.2 | @id             | A URI reference for the region.                                                                                               | https://www.wikidata.org/wiki/Q64       | Platinum |
| 1.2.3 | resolutionValue | The value of the resolution.                                                                                                  | 100                                     | Silver   |
| 1.2.4 | resolutionUnit  | The unit of the resolution.                                                                                                   | m                                       | Silver   |
| 1.2.5 | boundingBox     | The covered area specified by the coordinates of a bounding box. The format is [minLon, minLat, maxLon, maxLat] or [W,S,E,N]. | [13.08825, 52.33859, 13.76104, 52.6754] | Gold     |
| 1.2.6 | crs             | The Coordinate Reference System, specified as an EPSG code.                                                                   | EPSG:4326                               | Gold     |

### Resource - Temporal Keys
| #     | Key             | Description                                                                                                                                                                   | Example                   | Badge  |
|-------|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------|--------|
| 1     | **temporal**    | An object with the time period covered in the data. Temporal information should contain either a "referenceDate" or the keys that describe a time series, in rare cases both. |                           |        |
| 1.1   | referenceDate   | A base year, month or day. The time for which the data is should be accurate. Date Format is ISO 8601.                                                                        | 2020-01-01                | Silver |
| 1.2   | **timeseries**  | An array that describes the timeseries.                                                                                                                                       |                           |        |
| 1.2.1 | start           | The start time of a time series.                                                                                                                                              | 2020-01-01T00:00:00+00:00 | Silver |
| 1.2.2 | end             | The temporal end point of a time series.                                                                                                                                      | 2020-01-01T23:59:30+00:00 | Silver |
| 1.2.3 | resolution      | The time span between individual information points in a time series.                                                                                                         | 30 s                      | Silver |
| 1.2.4 | alignment       | An indicator of whether timestamps in a time series are to the left, right or in the centre.                                                                                  | left                      | Silver |
| 1.2.5 | aggregationType | An indicator of whether the values are a sum, an average or a current value.                                                                                                  | current                   | Silver |

### Resource - Sources Keys
| #     | Key                | Description                                                                                                                                                                   | Example                                                                                                                                                                                           | Badge  |
|-------|--------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| 1     | **sources**        | An array of objects with the used and underlying sources of the data and metadata.                                                                                            |                                                                                                                                                                                                   |        |
| 1.1   | title              | A human readable title of the source, a document title or organisation name.                                                                                                  | IPCC Sixth Assessment Report (AR6) - Climate Change 2023 - Synthesis Report                                                                                                                       | Bronze |
| 1.2   | authors            | An array of the full names of the authors of the source material.                                                                                                             | Hoesung Lee,José Romero, The Core Writing Team                                                                                                                                                    | Bronze |
| 1.3   | description        | A free text description of the source.                                                                                                                                        | A Report of the Intergovernmental Panel on Climate Change                                                                                                                                         | Bronze |
| 1.4   | publicationYear    | Indicates the year when the work was published.                                                                                                                               | 2023                                                                                                                                                                                              | Bronze |
| 1.5   | path               | A URL to the original source.                                                                                                                                                 | https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf                                                                                                                   | Bronze |
| 1.6   | **licenses**       | An array of objects of licenses under which the described source is provided. See https://openenergyplatform.github.io/academy/courses/08_licensing/ for further information. |                                                                                                                                                                                                   |        |
| 1.6.1 | name               | The [SPDX](https://spdx.org/licenses/) identifier.                                                                                                                            | ODbL-1.0                                                                                                                                                                                          | Bronze |
| 1.6.2 | title              | The official (human-readable) title of the license.                                                                                                                           | Open Data Commons Open Database License 1.0                                                                                                                                                       | Bronze |
| 1.6.3 | path               | A link or path to the license text.                                                                                                                                           | https://opendatacommons.org/licenses/odbl/1-0/index.html                                                                                                                                          | Bronze |
| 1.6.4 | instruction        | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.                                                                | You are free to share and change, but you must attribute, and share derivations under the same license. See https://tldrlegal.com/license/odc-open-database-license-odbl for further information. | Bronze |
| 1.6.5 | attribution        | A copyright owner of the **source**. Must be provided if attribution licenses are used.                                                                                       | © Intergovernmental Panel on Climate Change 2023                                                                                                                                                  | Bronze |
| 1.6.6 | copyrightStatement | A link or path that proves that the source or data has the appropriate license. This can be a page number or website imprint.                                                 | https://www.ipcc.ch/copyright/                                                                                                                                                                    | Bronze |

### Resource - Licenses Keys
| #   | Key                | Description                                                                                                         | Example                                                                                                                                                                                           | Badge  |
|-----|--------------------|---------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------|
| 1   | **licenses**       | An array of objects of licenses under which the described data is provided.                                         |                                                                                                                                                                                                   |        |
| 1.1 | name               | The [SPDX](https://spdx.org/licenses/) identifier.                                                                  | ODbL-1.0                                                                                                                                                                                          | Bronze |
| 1.2 | title              | The official (human-readable) title of the license.                                                                 | Open Data Commons Open Database License 1.0                                                                                                                                                       | Bronze |
| 1.3 | path               | A link or path to the license text.                                                                                 | https://opendatacommons.org/licenses/odbl/1-0/index.html                                                                                                                                          | Bronze |
| 1.4 | instruction        | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.      | You are free to share and change, but you must attribute, and share derivations under the same license. See https://tldrlegal.com/license/odc-open-database-license-odbl for further information. | Bronze |
| 1.5 | attribution        | A copyright owner of the **data**. Must be provided if attribution licenses are used.                               | © Reiner Lemoine Institut                                                                                                                                                                         | Bronze |
| 1.6 | copyrightStatement | A link or path that proves that the data has the appropriate license. This can be a page number or website imprint. | https://www.ipcc.ch/copyright/                                                                                                                                                                    | Bronze |

### Resource - Provenance Keys
| #   | Key              | Description                                                                                                                                                                                                                                 | Example                  | Badge  |
|-----|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------|--------|
| 1   | **contributors** | An array of objects of the people or organizations who contributed to the data or metadata.                                                                                                                                                 |                          |        |
| 1.1 | title            | A full name of the contributor.                                                                                                                                                                                                             | Ludwig Hülk              | Bronze |
| 1.2 | path             | A qualified link or path pointing to a relevant location online for the contributor. This can be the GitHub page or ORCID.                                                                                                                  | https://github.com/Ludee | Bronze |
| 1.3 | organization     | A string describing the organization this contributor is affiliated to. This can be relevant for the copyright.                                                                                                                             | Reiner Lemoine Institut  | Bronze |
| 1.4 | roles            | An array describing the roles of the contributor. A role is recommended to follow an established vocabulary, such as DataCite Metadata Schema’s contributorRole or CreDIT. Useful roles to indicate are: creator, contact, and dataCurator. | creator, dataCurator     | Bronze |
| 1.5 | date             | The date of the final contribution. Date Format is ISO 8601.                                                                                                                                                                                | 2024-10-21               | Bronze |
| 1.6 | object           | The target of the contribution. This can be the data, the metadata or both (data and metadata).                                                                                                                                             | data and metadata        | Bronze |
| 1.7 | comment          | A free-text commentary on what has been done.                                                                                                                                                                                               | Add general context.     | Bronze |

### Resource - Type Keys
| # | Key      | Description                                                                                                                                   | Example    | Badge |
|---|----------|-----------------------------------------------------------------------------------------------------------------------------------------------|------------|-------|
| 1 | type     | The 'table' type indicates that the resource is tabular as per 'Frictionless Tabular Data' definition.                                        | table      | Gold  |
| 2 | format   | A file extension format. Possible options are 'csv', 'xlsx', 'json', 'PostgreSQL', 'SQLite' and other standard file extensions.               | PostgreSQL | Gold  |
| 3 | encoding | Specifies the character encoding of the resource's data file. The default is 'UTF-8'. The values should be one of the 'Preferred MIME Names'. | UTF-8      | Gold  |

#### Resource - Fields Keys
| #       | Key                | Description                                                                                                                                                                          | Example                                                  | Badge    |
|---------|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|----------|
| 1       | **schema**         | An object that describes the structure of a table. It contains all fields (columns of the table), the primary key and optional foreign keys.                                         |                                                          |          |
| 1.1     | **fields**         | An array of objects that describes a field (column) and its detailed information.                                                                                                    |                                                          |          |
| 1.1.1   | name               | The name of the field. The name may only consist of lowercase alphanumeric characters or underscores. It must not begin with a number or an underscore.                              | year                                                     | Iron     |
| 1.1.2   | description        | A text describing the field.                                                                                                                                                         | Reference year for which the data were collected.        | Silver   |
| 1.1.3   | type               | The data type of the field. In case of a geom column in a database, also indicate the shape and CRS.                                                                                 | geometry(Point, 4326)                                    | Iron     |
| 1.1.4   | nullable           | A boolean key to specify that a column can be nullable. True is the default value.                                                                                                   | True                                                     | Iron     |
| 1.1.5   | unit               | The unit of a field. If it does not apply, use 'null'. If the unit is given in a separate field, reference this field (e.g. 'unit').  Use a space between numbers and units (100 m). | MW                                                       | Silver   |
| 1.1.6   | **isAbout**        | An array of objects that describes the field in ontology terms.                                                                                                                      | 
| 1.1.6.1 | name               | The class label of the ontology term.                                                                                                                                                | wind energy converting unit                              | Platinum |
| 1.1.6.2 | path               | The path of the ontology term (IRI).                                                                                                                                                 | https://openenergyplatform.org/ontology/oeo/OEO_00000044 | Platinum |
| 1.1.7   | **valueReference** | An array of objects for an extended description of the values in the column in ontology terms.                                                                                       |                                                          |          |
| 1.1.7.1 | value              | The name of the value in the column.                                                                                                                                                 | onshore                                                  | Platinum |
| 1.1.7.2 | name               | The class label of the ontology term in the column.                                                                                                                                  | onshore wind farm                                        | Platinum |
| 1.1.7.3 | path               | The path of the ontology term (IRI) in the column.                                                                                                                                   | https://openenergyplatform.org/ontology/oeo/OEO_00000311 | Platinum |

#### Resource - Properties Keys
| #       | Key              | Description                                                                                                                                                                | Example                                          | Badge |
|---------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|-------|
| 1.2     | primaryKey       | An array of fields that uniquely identifies each row in the table. The default value is the “id” column.                                                                   | id                                               | Iron  |
| 1.3     | **foreignKeys**  | An array of objects with foreign keys that describe a field that relates to a field in another table.                                                                      |                                                  |       |
| 1.3.1   | fields           | An array of fields in the table that is constrained by the foreign key.                                                                                                    | id, version                                      | Iron  |
| 1.3.2   | **reference**    | The reference to the foreign table.                                                                                                                                        |                                                  |       |
| 1.3.2.1 | resource         | The referenced foreign table.                                                                                                                                              | model_draft.oep_oemetadata_table_example_version | Iron  |
| 1.3.2.2 | fields           | The foreign resource column.                                                                                                                                               | id, version                                      | Iron  |
| 1.4     | **dialect**      | The Dialect defines a simple format for describing the various dialects of CSV files in a language-independent manner. In a database, the values in the fields are 'null'. |                                                  |       |
| 1.4.1   | delimiter        | The delimiter specifies the character sequence which should separate fields (columns). Common characters are ',' (comma), ';' (semicolon), '.' (point) and '\t' (tab).     | ,                                                | Iron  |
| 1.4.2   | decimalSeparator | The symbol used to separate the integer part from the fractional part of a number written in decimal form. Depending on language and region this symbol can be '.' or ','. | .                                                | Iron  |

### Resource - Review Keys
| #   | Key        | Description                                                                                                                                                                                                  | Example                 |
|-----|------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------|
| 1.  | **review** | The metadata on the OEP can go through an open peer review process. See the Academy course [Open Peer Review](https://openenergyplatform.github.io/academy/courses/09_peer_review/) for further information. |                         |
| 1.1 | path       | A link or path to the documented open peer review.                                                                                                                                                           | https://www.example.com |
| 1.2 | badge      | A badge of either Iron, Bronze, Silver, Gold or Platinum is used to label the quality of the metadata.                                                                                                       | Platinum                |

### MetaMetadata Keys
| #     | Key                 | Description                                                                          | Example                                            |
|-------|---------------------|--------------------------------------------------------------------------------------|----------------------------------------------------|
| 1     | **metaMetadata**    | An object that describes the metadata themselves, their format, version and license. |                                                    |
| 1.1   | metadataVersion     | Type and version number of the metadata.                                             | OEMetadata-2.0                                     |
| 1.2   | **metadataLicense** | The license of the provided metadata.                                                |                                                    |
| 1.2.1 | name                | The [SPDX](https://spdx.org/licenses/) identifier.                                   | CC0-1.0                                            |
| 1.2.2 | title               | The official (human-readable) title of the license.                                  | Creative Commons Zero v1.0 Universal               |
| 1.2.3 | path                | A link or path to the license text.                                                  | https://creativecommons.org/publicdomain/zero/1.0/ |
