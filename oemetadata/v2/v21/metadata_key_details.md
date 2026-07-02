<!--
SPDX-FileCopyrightText: 2026 Ludwig Hülk <Ludee> © Reiner Lemoine Institut
SPDX-FileCopyrightText: 2026 Jonas Huber <jh-RLI> © Reiner Lemoine Institut

SPDX-License-Identifier: MIT
-->

# OEMetadata - Key Description Details

This pages describes the key of **OEMetadata version 2.1 .** <br>
You can have a look at an empty [template](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/oemetadata/latest/template.json) and a filled out [example](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/oemetadata/latest/example.json) of the metadata string.<br>
The [`schema.json`](https://github.com/OpenEnergyPlatform/oemetadata/blob/production/oemetadata/latest/schema.json) contains the complete metadata schema.

## Introduction

### JSON Format

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

### Cardinality
The cardinality defines the number of times an element can occur.

* [1]  Mandatory
* [0..1] Optional
* [*] Multiple optional
* [1..*] Mandatory and multiple optional

### Badges
Badges indicate the priority of metadata keys.<br>
They are implemented as part of the [Open Peer Review Process](https://openenergyplatform.github.io/academy/courses/09_peer_review/).

### Additional information:<br>
If a field is not applicable use: `null`.<br>
If a value is not yet available, use: `ToDo`.


## Metadata Keys - Dataset

### Dataset - @context
|                    |                                                                                                                           |
|--------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Key**            | @context                                                                                                                  |
| **Description**    | Explanation of metadata keys in ontology terms.                                                                           |
| **Example**        | [context.json](https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/oemetadata/latest/context.json) |
| **Ontology Class** |                                                                                                                           |
| **Badge**          | Platinum                                                                                                                  |
| **Card.**          | [0..1]                                                                                                                    |

### Dataset - @id
|                    |                                                                                                                                                                                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Key**            | @id                                                                                                                                                                            |
| **Description**    | A unique identifier (UUID/DOI) for the dataset. This is the Databus Artifact.                                                                                                  |
| **Example**        | [databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/](https://databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/) |
| **Ontology Class** | [dct:identifier](http://purl.org/dc/terms/identifier)                                                                                                                          |
| **Badge**          | Platinum                                                                                                                                                                       |
| **Card.**          | [0..1]                                                                                                                                                                         |

### Dataset - name
|                    |                                                            |
|--------------------|------------------------------------------------------------|
| **Key**            | name                                                       |
| **Description**    | A filename or database conform dataset name.               |
| **Example**        | oep_oemetadata                                             |
| **Ontology Class** | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| **Badge**          | Iron                                                       |
| **Card.**          | [1]                                                        |

### Dataset - title
|                    |                                             |
|--------------------|---------------------------------------------|
| **Key**            | title                                       |
| **Description**    | A human readable dataset name.              |
| **Example**        | OEP OEMetadata                              |
| **Ontology Class** | [dct:title](http://purl.org/dc/terms/title) |
| **Badge**          | Bronze                                      |
| **Card.**          | [0..1]                                      |

### Dataset - description
|                    |                                                         |
|--------------------|---------------------------------------------------------|
| **Key**            | description                                             |
| **Description**    | A free text description of the dataset.                 |
| **Example**        | A collection of tables for the OEMetadata examples.     |
| **Ontology Class** | [dct:description](http://purl.org/dc/terms/description) |
| **Badge**          | Bronze                                                  |
| **Card.**          | [0..1]                                                  |

### Dataset - languages
|                |                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | languages                                                                                                                                                                         |
| Description    | An array of languages used within the described data structures (e.g. titles, descriptions). The language key can be repeated if more languages are used. Standard: IETF (BCP47). |
| Example        | en-GB, de-DE                                                                                                                                                                      |
| Ontology Class | [dct:language](http://purl.org/dc/terms/language)                                                                                                                                 |
| Badge          | Gold                                                                                                                                                                              |
| Card.          | [*]                                                                                                                                                                               |

### Dataset - version
|                |                                                          |
|----------------|----------------------------------------------------------|
| Key            | version                                                  |
| Description    | A version string identifying the version of the package. |
| Example        | 0.1.0                                                    |
| Ontology Class | [dcat:version](https://www.w3.org/ns/dcat#version)       |
| Badge          | Silver                                                   |
| Card.          | [0..1]                                                   |

### Dataset - image
|                |                                                                                  |
|----------------|----------------------------------------------------------------------------------|
| Key            | image                                                                            |
| Description    | An image to use for this data package.                                           |
| Example        | https://openenergyplatform.org/static/img/about/OpenEnergyFamily_GroupPhoto2.png |
| Ontology Class | [schema.org:image](https://schema.org/image)                                     |
| Badge          | Gold                                                                             |
| Card.          | [0..1]                                                                           |

### Dataset - subject
|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| Key            | subject                                                                             |
| Description    | An array of objects that references the subjects of the resource in ontology terms. |
| Example        |                                                                                     |
| Ontology Class |                                                                                     |
| Badge          |                                                                                     |
| Card.          | [*]                                                                                 |

### Dataset - subject (name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | A class label of the ontology term.                        |
| Example        | energy                                                     |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Platinum                                                   |
| Card.          | [0..1]                                                     |

### Dataset - subject (@id)
|                |                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Key            | @id                                                                                                          |
| Description    | A unique identifier (URI/IRI) of the ontology class.                                                         |
| Example        | [openenergyplatform.org/ontology/oeo/OEO_00000150](https://openenergyplatform.org/ontology/oeo/OEO_00000150) |
| Ontology Class | [dct:subject](http://purl.org/dc/terms/subject)                                                              |
| Badge          | Platinum                                                                                                     |
| Card.          | [0..1]                                                                                                       |

### Dataset - keywords
|                |                                                                                  |
|----------------|----------------------------------------------------------------------------------|
| Key            | keywords                                                                         |
| Description    | An array of freely selectable keywords that help with searching and structuring. |
| Example        | example, ODbL-1.0, NFDI4Energy                                                   |
| Ontology Class | [dcat:keyword](http://www.w3.org/ns/dcat#keyword)                                |
| Badge          | Silver                                                                           |
| Card.          | [*]                                                                              |

## Dataset - context

### Dataset - context
|                |                                                                                                                                                                             |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | context                                                                                                                                                                     |
| Description    | An object that describes the general setting, environment, or project leading to the creation or maintenance of this dataset. In science, this can be the research project. |
| Example        |                                                                                                                                                                             |
| Ontology Class |                                                                                                                                                                             |
| Badge          |                                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                                      |

### Dataset - context (title)
|                |                                             |
|----------------|---------------------------------------------|
| Key            | title                                       |
| Description    | A title of the associated project.          |
| Example        | NFDI4Energy                                 |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title) |
| Badge          | Gold                                        |
| Card.          | [0..1]                                      |

### Dataset - context (homepage)
|                |                                                     |
|----------------|-----------------------------------------------------|
| Key            | homepage                                            |
| Description    | A URL of the project.                               |
| Example        | [nfdi4energy.uol.de](https://nfdi4energy.uol.de/)   |
| Ontology Class | [foaf:homepage](http://xmlns.com/foaf/0.1/homepage) |
| Badge          | Gold                                                |
| Card.          | [0..1]                                              |

### Dataset - context (documentation)
|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| Key            | documentation                                                                   |
| Description    | A URL of the project documentation.                                             |
| Example        | [nfdi4energy.uol.de/sites/about_us](https://nfdi4energy.uol.de/sites/about_us/) |
| Ontology Class | [ncit:Project Description](http://purl.obolibrary.org/obo/NCIT_C165054)         |
| Badge          | Gold                                                                            |
| Card.          | [0..1]                                                                          |

### Dataset - context (sourceCode)
|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| Key            | sourceCode                                                                   |
| Description    | A URL of the source code of the project.                                     |
| Example        | [github.com/NFDI4Energy](https://github.com/NFDI4Energy)                     |
| Ontology Class | [oeo:code source](https://openenergyplatform.org/ontology/oeo/OEO_00000091/) |
| Badge          | Gold                                                                         |
| Card.          | [0..1]                                                                       |

### Dataset - context (publisher)
|                |                                                         |
|----------------|---------------------------------------------------------|
| Key            | publisher                                               |
| Description    | The publishing agency of the data. This can be the OEP. |
| Example        | Open Energy Platform (OEP)                              |
| Ontology Class | [dct:publisher](http://purl.org/dc/terms/publisher)     |
| Badge          | Gold                                                    |
| Card.          | [0..1]                                                  |

### Dataset - context (publisherLogo)
|                |                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | publisherLogo                                                                                                                                                        |
| Description    | A URL to the logo of the publishing agency of data.                                                                                                                  |
| Example        | [OpenEnergyFamily_Logo_OpenEnergyPlatform.svg](https://github.com/OpenEnergyPlatform/organisation/blob/production/logo/OpenEnergyFamily_Logo_OpenEnergyPlatform.svg) |
| Ontology Class | [foaf:logo](http://xmlns.com/foaf/0.1/logo)                                                                                                                          |
| Badge          | Gold                                                                                                                                                                 |
| Card.          | [0..1]                                                                                                                                                               |

### Dataset - context (contact)
|                |                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------|
| Key            | contact                                                                                                  |
| Description    | A reference to the creator or maintainer of the data set. It can be an email address or a GitHub handle. |
| Example        | info@nfdi4energy.org                                                                                     |
| Ontology Class | [oeo:contact person](https://openenergyplatform.org/ontology/oeo/OEO_00000107/)                          |
| Badge          | Gold                                                                                                     |
| Card.          | [0..1]                                                                                                   |

### Dataset - context (fundingAgency)
|                |                                                                                           |
|----------------|-------------------------------------------------------------------------------------------|
| Key            | fundingAgency                                                                             |
| Description    | A name of the entity providing the funding. This can be a government agency or a company. |
| Example        | Deutsche Forschungsgemeinschaft (DFG)                                                     |
| Ontology Class | [sc:FundingAgency](http://schema.org/fundingAgency)                                       |
| Badge          | Gold                                                                                      |
| Card.          | [0..1]                                                                                    |

### Dataset - context (fundingAgencyLogo)
|                |                                                                                            |
|----------------|--------------------------------------------------------------------------------------------|
| Key            | fundingAgencyLogo                                                                          |
| Description    | A URL to the logo or image of the funding agency.                                          |
| Example        | [DFG-logo-blau.svg](https://upload.wikimedia.org/wikipedia/commons/8/86/DFG-logo-blau.svg) |
| Ontology Class | [foaf:logo](http://xmlns.com/foaf/0.1/logo)                                                |
| Badge          | Gold                                                                                       |
| Card.          | [0..1]                                                                                     |

### Dataset - context (grantNo)
|                |                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------|
| Key            | grantNo                                                                                                           |
| Description    | An identifying grant number. In case of a publicly funded project, this number is assigned by the funding agency. |
| Example        | 501865131                                                                                                         |
| Ontology Class | [sc:Grant](http://schema.org/)                                                                                    |
| Badge          | Gold                                                                                                              |
| Card.          | [0..1]                                                                                                            |

## Dataset - Provenance Keys

### Dataset - Provenance Keys
|                |                                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | contributors                                                                                                                                                    |
| Description    | An array of objects of the people or organizations who contributed to the data or metadata. Should have "Date of data creation" and "Date of metadata creation" |
| Example        |                                                                                                                                                                 |
| Ontology Class | [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)                                                                                                                   |
| Badge          |                                                                                                                                                                 |
| Card.          | [*]                                                                                                                                                             |

### Dataset - Provenance Keys (title)
|                |                                             |
|----------------|---------------------------------------------|
| Key            | title                                       |
| Description    | A full name of the contributor.             |
| Example        | Ludwig Hülk                                 |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title) |
| Badge          | Bronze                                      |
| Card.          | [0..1]                                      |

### Dataset - Provenance Keys (path)
|                |                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                                       |
| Description    | A qualified link or path pointing to a relevant location online for the contributor. This can be the GitHub page or ORCID. |
| Example        | https://github.com/Ludee                                                                                                   |
| Ontology Class | [sc:url](https://schema.org/url)                                                                                           |
| Badge          | Bronze                                                                                                                     |
| Card.          | [0..1]                                                                                                                     |

### Dataset - Provenance Keys (organization)
|                |                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| Key            | organization                                                                                                    |
| Description    | A string describing the organization this contributor is affiliated to. This can be relevant for the copyright. |
| Example        | Reiner Lemoine Institut                                                                                         |
| Ontology Class | [oeo:organisation](https://openenergyplatform.org/ontology/oeo/OEO_00030022/)                                   |
| Badge          | Bronze                                                                                                          |
| Card.          | [0..1]                                                                                                          |

### Dataset - Provenance Keys (roles)
|                |                                                                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | roles                                                                                                                                                                                                                                                                              |
| Description    | An array describing the roles of the contributor. A role is recommended to follow the established vocabulary: [DataCite Metadata Schema’s contributorRole](https://support.datacite.org/docs/datacite-metadata-schema-v44-recommended-and-optional-properties#7a-contributortype). |
| Example        | DataCollector, DataCurator                                                                                                                                                                                                                                                         |
| Ontology Class | [oeo:role](https://openenergyplatform.org/ontology/oeo/BFO_0000023/)                                                                                                                                                                                                               |
| Badge          | Bronze                                                                                                                                                                                                                                                                             |
| Card.          | [*]                                                                                                                                                                                                                                                                                |

### Dataset - Provenance Keys (date)
|                |                                                        |
|----------------|--------------------------------------------------------|
| Key            | date                                                   |
| Description    | The date of the contribution. Date Format is ISO 8601. |
| Example        | 2024-10-21                                             |
| Ontology Class | [dct:issued](http://purl.org/dc/terms/issued)          |
| Badge          | Bronze                                                 |
| Card.          | [0..1]                                                 |

### Dataset - Provenance Keys (object)
|                |                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------|
| Key            | object                                                                                          |
| Description    | The target of the contribution. This can be the data, the metadata or both (data and metadata). |
| Example        | data and metadata                                                                               |
| Ontology Class | [dct:type](http://purl.org/dc/terms/type)                                                       |
| Badge          | Bronze                                                                                          |
| Card.          | [0..1]                                                                                          |

### Dataset - Provenance Keys (comment)
|                |                                                               |
|----------------|---------------------------------------------------------------|
| Key            | comment                                                       |
| Description    | A free-text commentary on what has been done.                 |
| Example        | Add general context.                                          |
| Ontology Class | [rdfs:comment](https://www.w3.org/2000/01/rdf-schema#comment) |
| Badge          | Bronze                                                        |
| Card.          | [0..1]                                                        |

## Dataset - Dataset Licenses

### Dataset - datasetLicenses
|                |                                                                                |
|----------------|--------------------------------------------------------------------------------|
| Key            | datasetLicenses                                                                |
| Description    | An array of objects of licenses under which the described dataset is provided. |
| Example        |                                                                                |
| Ontology Class | [dct:license](http://purl.org/dc/terms/license)                                |
| Badge          |                                                                                |
| Card.          | [*]                                                                            |

### Resources - datasetLicenses (name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | The [SPDX](https://spdx.org/licenses/) identifier.         |
| Example        | ODbL-1.0                                                   |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Bronze                                                     |
| Card.          | [0..1]                                                     |

### Dataset - datasetLicenses (title)
|                |                                                     |
|----------------|-----------------------------------------------------|
| Key            | title                                               |
| Description    | The official (human-readable) title of the license. |
| Example        | Open Data Commons Open Database License 1.0         |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title)         |
| Badge          | Bronze                                              |
| Card.          | [0..1]                                              |

### Dataset - datasetLicenses (path)
|                |                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                         |
| Description    | A link or path to the license text.                                                                          |
| Example        | [opendatacommons.org/licenses/odbl/1-0/index.html](https://opendatacommons.org/licenses/odbl/1-0/index.html) |
| Ontology Class | [dcat:accessURL](https://www.w3.org/ns/dcat#accessURL)                                                       |
| Badge          | Bronze                                                                                                       |
| Card.          | [0..1]                                                                                                       |

### Dataset - datasetLicenses (instruction)
|                |                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | instruction                                                                                                                                                                                                        |
| Description    | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.                                                                                                     |
| Example        | You are free to share and change, but you must attribute, and share derivations under the same license. See [tldrlegal.com](https://tldrlegal.com/license/odc-open-database-license-odbl) for further information. |
| Ontology Class | [dc:rights](http://purl.org/dc/elements/1.1/rights)                                                                                                                                                                |
| Badge          | Bronze                                                                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                                                                             |

### Dataset - datasetLicenses (attribution)
|                |                                                                                          |
|----------------|------------------------------------------------------------------------------------------|
| Key            | attribution                                                                              |
| Description    | A copyright owner of the **dataset**. Must be provided if attribution licenses are used. |
| Example        | © Reiner Lemoine Institut                                                                |
| Ontology Class | [spdx:attributionText](http://spdx.org/rdf/terms#attributionText)                        |
| Badge          | Bronze                                                                                   |
| Card.          | [0..1]                                                                                   |

### Dataset - datasetLicenses (copyrightStatement)
|                |                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------|
| Key            | copyrightStatement                                                                                                     |
| Description    | A link or path that proves that the dataset has the appropriate license. This can be a page number or website imprint. |
| Example        | [www.ipcc.ch/copyright/](https://www.ipcc.ch/copyright/)                                                               |
| Ontology Class | [dct:rights](http://purl.org/dc/terms/rights)                                                                          |
| Badge          | Bronze                                                                                                                 |
| Card.          | [0..1]                                                                                                                 |

### Dataset - Review Keys
|                |                                                                                                                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **review**                                                                                                                                                                                                   |
| Description    | The metadata on the OEP can go through an open peer review process. See the Academy course [Open Peer Review](https://openenergyplatform.github.io/academy/courses/09_peer_review/) for further information. |
| Example        |                                                                                                                                                                                                              |
| Ontology Class |                                                                                                                                                                                                              |
| Badge          | [0..1]                                                                                                                                                                                                       |

### Dataset - Review Keys - path
|                |                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| Key            | **path**                                                                                                             |
| Description    | A link or path to the documented open peer review (under development).                                               |
| Example        | [open_peer_review/9](https://openenergyplatform.org/dataedit/view/model_draft/oep_table_example/open_peer_review/9/) |
| Ontology Class | [sc:url](https://schema.org/url)                                                                                     |
| Badge          | [0..1]                                                                                                               |

### Dataset - Review Keys - badge
|                |                                                                                                        |
|----------------|--------------------------------------------------------------------------------------------------------|
| Key            | **badge**                                                                                              |
| Description    | A badge of either Iron, Bronze, Silver, Gold or Platinum is used to label the quality of the metadata. |
| Example        | Platinum                                                                                               |
| Ontology Class | [oeo:quality control flag](https://openenergyplatform.org/ontology/oeo/OEO_00140098/)                  |
| Badge          | [0..1]                                                                                                 |


## Resources

### Dataset - resources
|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| **Key**            | resources                                                                                |
| **Description**    | An array of objects of the resources. The dataset can contain several (database) tables. |
| **Example**        |                                                                                          |
| **Ontology Class** | [dcat:Dataset](https://www.w3.org/ns/dcat#dataset)                                       |
| **Badge**          |                                                                                          |
| **Card.**          | [*]                                                                                      |

### Resources - General - @id
|                |                                                                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | @id                                                                                                                                                                                     |
| Description    | A Uniform Resources Identifier (URI) that links the resource via the OpenEnergyDatabus (DBpedia Databus).                                                                               |
| Example        | [wri_global_power_plant_database](https://databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/2022-11-07/wri_global_power_plant_database_variant=data.csv) |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)                                                                                                                                   |
| Badge          | Platinum                                                                                                                                                                                |
| Card.          | [0..1]                                                                                                                                                                                  |

### Resources - General - path
|                |                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                                       |
| Description    | A unique identifier (URI/UUID/DOI) for the table or file.                                                                  |
| Example        | [model_draft/oemetadata_table_template](http://openenergyplatform.org/dataedit/view/model_draft/oemetadata_table_template) |
| Ontology Class | [dcat:accessURL](https://www.w3.org/ns/dcat#accessURL)                                                                     |
| Badge          | Bronze                                                                                                                     |
| Card.          | [0..1]                                                                                                                     |

### Resources - General - name
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | A filename or database conform table name.                 |
| Example        | oemetadata_table_template                                  |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Iron                                                       |
| Card.          | [1]                                                        |

### Resources - General - title
|                |                                             |
|----------------|---------------------------------------------|
| Key            | title                                       |
| Description    | A human readable resource or table name.    |
| Example        | OEMetadata Table                            |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title) |
| Badge          | Silver                                      |
| Card.          | [0..1]                                      |

### Resource - General - topics
|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| Key            | topics                                                                            |
| Description    | An array of predefined topics that correspond to the database schemas of the OEP. |
| Example        | model_draft                                                                       |
| Ontology Class | [foaf:topic](http://xmlns.com/foaf/spec/#term_topic)                              |
| Badge          | Bronze                                                                            |
| Card.          | [*]                                                                               |

### Resources - General - description
|                |                                                                                                                         |
|----------------|-------------------------------------------------------------------------------------------------------------------------|
| Key            | description                                                                                                             |
| Description    | A description of the table. It should be usable as summary information for the table that is described by the metadata. |
| Example        | Example table used to illustrate the OEMetadata structure and features.                                                 |
| Ontology Class | [dct:description](http://purl.org/dc/terms/description)                                                                 |
| Badge          | Silver                                                                                                                  |
| Card.          | [0..1]                                                                                                                  |

### Resources - General - publicationDate
|                |                                                                                          |
|----------------|------------------------------------------------------------------------------------------|
| Key            | publicationDate                                                                          |
| Description    | A date of publication of the data or metadata. The date format is ISO 8601 (YYYY-MM-DD). |
| Example        | 2024-10-15                                                                               |
| Ontology Class | [dct:issued](http://purl.org/dc/terms/issued)                                            |
| Badge          | Bronze                                                                                   |
| Card.          | [0..1]                                                                                   |

### Resources - General - subject
|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| Key            | subject                                                                             |
| Description    | An array of objects that references the subjects of the resource in ontology terms. |
| Example        |                                                                                     |
| Ontology Class |                                                                                     |
| Badge          |                                                                                     |
| Card.          | [*]                                                                                 |

### Resources - General - subject (name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | A class label of the ontology term.                        |
| Example        | energy                                                     |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Platinum                                                   |
| Card.          | [0..1]                                                     |

### Resources - General - subject (@id)
|                |                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Key            | @id                                                                                                          |
| Description    | A unique identifier (URI/IRI) of the ontology class.                                                         |
| Example        | [openenergyplatform.org/ontology/oeo/OEO_00000150](https://openenergyplatform.org/ontology/oeo/OEO_00000150) |
| Ontology Class | [dct:subject](http://purl.org/dc/terms/subject)                                                              |
| Badge          | Platinum                                                                                                     |
| Card.          | [0..1]                                                                                                       |

### Resources - General - keywords
|                |                                                                                  |
|----------------|----------------------------------------------------------------------------------|
| Key            | keywords                                                                         |
| Description    | An array of freely selectable keywords that help with searching and structuring. |
| Example        | example, ODbL-1.0, NFDI4Energy                                                   |
| Ontology Class | [dcat:keyword](http://www.w3.org/ns/dcat#keyword)                                |
| Badge          | Silver                                                                           |
| Card.          | [*]                                                                              |

### Resources - General - embargoPeriod
|                |                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------|
| Key            | embargoPeriod                                                                                      |
| Description    | An object that describes the embargo period during which public access to the data is not allowed. |
| Example        |                                                                                                    |
| Ontology Class |                                                                                                    |
| Badge          |                                                                                                    |
| Card.          | [0..1]                                                                                             |

### Resources - General - embargoPeriod (start)
|                |                                                                               |
|----------------|-------------------------------------------------------------------------------|
| Key            | start                                                                         |
| Description    | The start date of the embargo period. The date of the data (metadata) upload. |
| Example        | 2024-10-11                                                                    |
| Ontology Class | [dbo:startDateTime](https://dbpedia.org/ontology/startDateTime)               |
| Badge          | Bronze                                                                        |
| Card.          | [0..1]                                                                        |

### Resources - General - embargoPeriod (end)
|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| Key            | end                                                                          |
| Description    | The end date of the embargo period. This is the envisioned publication date. |
| Example        | 2025-01-01                                                                   |
| Ontology Class | [dbo:endDateTime](https://dbpedia.org/ontology/endDateTime)                  |
| Badge          | Bronze                                                                       |
| Card.          | [0..1]                                                                       |

### Resources - General - embargoPeriod (isActive)
|                |                                                                                                                                  |
|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| Key            | isActive                                                                                                                         |
| Description    | A boolean key that indicates if the embargo period is currently active. Must be changed to False on the embargo period end date. |
| Example        | True                                                                                                                             |
| Ontology Class | [adms:status](http://www.w3.org/ns/adms#status)                                                                                  |
| Badge          | Bronze                                                                                                                           |
| Card.          | [0..1]                                                                                                                           |

### Resources - Spatial
|                |                                                           |
|----------------|-----------------------------------------------------------|
| Key            | spatial                                                   |
| Description    | An object that describes the spatial context of the data. |
| Example        |                                                           |
| Ontology Class |                                                           |
| Badge          |                                                           |
| Card.          | [0..1]                                                    |

### Resources - Spatial - location
|                |                                                   |
|----------------|---------------------------------------------------|
| Key            | location                                          |
| Description    | An object that describes a specific location.     |
| Example        |                                                   |
| Ontology Class | [dct:location](http://purl.org/dc/terms/Location) |
| Badge          |                                                   |
| Card.          | [0..1]                                            |

### Resources - Spatial - location (address)
|                |                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------|
| Key            | address                                                                                                           |
| Description    | An address of the location of the data. May be specified with street name, house number, zip code, and city name. |
| Example        | Rudower Chaussee 12, 12489 Berlin                                                                                 |
| Ontology Class | [schema:address](https://schema.org/address)                                                                      |
| Badge          | Silver                                                                                                            |
| Card.          | [0..1]                                                                                                            |

### Resources - Spatial - location (@id)
|                |                                                                             |
|----------------|-----------------------------------------------------------------------------|
| Key            | @id                                                                         |
| Description    | A path or URI to a specific location. It can use Wikidata or OpenStreetMap. |
| Example        | [www.wikidata.org/wiki/Q77077223](https://www.wikidata.org/wiki/Q77077223)  |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)                       |
| Badge          | Platinum                                                                    |
| Card.          | [0..1]                                                                      |

### Resources - Spatial - location (latitude)
|                |                                                 |
|----------------|-------------------------------------------------|
| Key            | latitude                                        |
| Description    | The latitude (lat) information of the location. |
| Example        | 52.432822                                       |
| Ontology Class | [schema:latitude](https://schema.org/latitude)  |
| Badge          | Gold                                            |
| Card.          | [0..1]                                          |

### Resources - Spatial - location (longitude)
|                |                                                  |
|----------------|--------------------------------------------------|
| Key            | longitude                                        |
| Description    | The longitude (lon) information of the location. |
| Example        | 13.5351004                                       |
| Ontology Class | [schema:longitude](https://schema.org/longitude) |
| Badge          | Gold                                             |
| Card.          | [0..1]                                           |

### Resources - Spatial - extent
|                |                                                                  |
|----------------|------------------------------------------------------------------|
| Key            | extent                                                           |
| Description    | An object that describes a covered area or region.               |
| Example        |                                                                  |
| Ontology Class | [oeo:spatial region](http://purl.obolibrary.org/obo/BFO_0000006) |
| Badge          |                                                                  |
| Card.          | [0..1]                                                           |

### Resources - Spatial - extent (name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | The name of the region.                                    |
| Example        | Berlin                                                     |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Silver                                                     |
| Card.          | [0..1]                                                     |

### Resources - Spatial - extent (@id)
|                |                                                                |
|----------------|----------------------------------------------------------------|
| Key            | @id                                                            |
| Description    | A URI reference for the region.                                |
| Example        | [www.wikidata.org/wiki/Q64](https://www.wikidata.org/wiki/Q64) |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)          |
| Badge          | Platinum                                                       |
| Card.          | [0..1]                                                         |

### Resources - Spatial - extent (resolutionValue)
|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| Key            | resolutionValue                                                                       |
| Description    | The value of the spatial resolution.                                                  |
| Example        | 100                                                                                   |
| Ontology Class | [dcat:spatialResolutionInMeters](http://www.w3.org/ns/dcat#spatialResolutionInMeters) |
| Badge          | Silver                                                                                |
| Card.          | [0..1]                                                                                |

### Resources - Spatial - extent (resolutionUnit)
|                |                                                                     |
|----------------|---------------------------------------------------------------------|
| Key            | resolutionUnit                                                      |
| Description    | The unit of the spatial resolution.                                 |
| Example        | m                                                                   |
| Ontology Class | [oeo:unit](http://openenergyplatform.org/ontology/oeo/OEO_00010489) |
| Badge          | Silver                                                              |
| Card.          | [0..1]                                                              |

### Resources - Spatial - extent (boundingBox)
|                |                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|
| Key            | boundingBox                                                                                                                   |
| Description    | The covered area specified by the coordinates of a bounding box. The format is [minLon, minLat, maxLon, maxLat] or [W,S,E,N]. |
| Example        | [13.08825, 52.33859, 13.76104, 52.6754]                                                                                       |
| Ontology Class | [dcat:bbox](http://www.w3.org/ns/dcat#bbox)                                                                                   |
| Badge          | Gold                                                                                                                          |
| Card.          | [*]                                                                                                                           |

### Resources - Spatial - extent (crs)
|                |                                                                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | crs                                                                                                                                      |
| Description    | The Coordinate Reference System, specified as an EPSG code.                                                                              |
| Example        | EPSG:4326                                                                                                                                |
| Ontology Class | [cco:Geospatial Coordinate Reference System](http://www.ontologyrepository.com/CommonCoreOntologies/GeospatialCoordinateReferenceSystem) |
| Badge          | Gold                                                                                                                                     |
| Card.          | [0..1]                                                                                                                                   |

### Resources - Temporal
|                |                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | temporal                                                                                                                                                    |
| Description    | An object with the time period covered in the data. Temporal information should contain a "referenceDate" or the keys that describe a time series, or both. |
| Example        |                                                                                                                                                             |
| Ontology Class | [schema:temporalCoverage](https://schema.org/temporalCoverage)                                                                                              |
| Badge          |                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                      |

### Resources - Temporal - referenceDate
|                |                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------|
| Key            | referenceDate                                                                                       |
| Description    | A base year, month or day. The time for which the data should be accurate. Date Format is ISO 8601. |
| Example        | 2020-01-01                                                                                          |
| Ontology Class | [dct:date](http://purl.org/dc/terms/date)                                                           |
| Badge          | Silver                                                                                              |
| Card.          | [0..1]                                                                                              |

### Resources - Temporal - timeseries
|                |                                                           |
|----------------|-----------------------------------------------------------|
| Key            | timeseries                                                |
| Description    | An array that describes the timeseries.                   |
| Example        |                                                           |
| Ontology Class | [dct:PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime) |
| Badge          |                                                           |
| Card.          | [*]                                                       |

### Resources - Temporal - timeseries (start)
|                |                                                                 |
|----------------|-----------------------------------------------------------------|
| Key            | start                                                           |
| Description    | The start time of a time series.                                |
| Example        | 2020-01-01T00:00:00+00:00                                       |
| Ontology Class | [dbo:startDateTime](https://dbpedia.org/ontology/startDateTime) |
| Badge          | Silver                                                          |
| Card.          | [0..1]                                                          |

### Resources - Temporal - timeseries (end)
|                |                                                             |
|----------------|-------------------------------------------------------------|
| Key            | end                                                         |
| Description    | The temporal end point of a time series.                    |
| Example        | 2020-01-01T23:59:30+00:00                                   |
| Ontology Class | [dbo:endDateTime](https://dbpedia.org/ontology/endDateTime) |
| Badge          | Silver                                                      |
| Card.          | [0..1]                                                      |

### Resources - Temporal - timeseries (resolutionValue)
|                |                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------|
| Key            | resolutionValue                                                                                    |
| Description    | The time span between individual information points in a time series. The value of the resolution. |
| Example        | 30 s                                                                                               |
| Ontology Class | [dcat:spatialResolutionInMeters](http://www.w3.org/ns/dcat#spatialResolutionInMeters)              |
| Badge          | Silver                                                                                             |
| Card.          | [0..1]                                                                                             |

### Resources - Temporal - timeseries (resolutionUnit)
|                |                                                                     |
|----------------|---------------------------------------------------------------------|
| Key            | resolutionUnit                                                      |
| Description    | The unit of the temporal resolution.                                |
| Example        | 30 s                                                                |
| Ontology Class | [oeo:unit](http://openenergyplatform.org/ontology/oeo/OEO_00010489) |
| Badge          | Silver                                                              |
| Card.          | [0..1]                                                              |

### Resources - Temporal - timeseries (alignment)
|                |                                                                                              |
|----------------|----------------------------------------------------------------------------------------------|
| Key            | alignment                                                                                    |
| Description    | An indicator of whether timestamps in a time series are to the left, right or in the centre. |
| Example        | left                                                                                         |
| Ontology Class | [oeo:time stamp alignment](http://openenergyplatform.org/ontology/oeo/OEO_00140044)          |
| Badge          | Silver                                                                                       |
| Card.          | [0..1]                                                                                       |

### Resources - Temporal - timeseries (aggregationType)
|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| Key            | aggregationType                                                                   |
| Description    | An indicator of whether the values are a sum, an average or a current value.      |
| Example        | current                                                                           |
| Ontology Class | [oeo:aggregation type](https://openenergyplatform.org/ontology/oeo/OEO_00140068/) |
| Badge          | Silver                                                                            |
| Card.          | [0..1]                                                                            |

## Resources - Sources

### Resources - sources
|                |                                                                                    |
|----------------|------------------------------------------------------------------------------------|
| Key            | sources                                                                            |
| Description    | An array of objects with the used and underlying sources of the data and metadata. |
| Example        |                                                                                    |
| Ontology Class | [dct:source](http://purl.org/dc/terms/source)                                      |
| Badge          |                                                                                    |
| Card.          | [*]                                                                                |

### Resources - sources - title
|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| Key            | title                                                                        |
| Description    | A human readable title of the source, a document title or organisation name. |
| Example        | IPCC Sixth Assessment Report (AR6) - Climate Change 2023 - Synthesis Report  |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title)                                  |
| Badge          | Bronze                                                                       |
| Card.          | [0..1]                                                                       |

### Resources - sources - authors
|                |                                                                         |
|----------------|-------------------------------------------------------------------------|
| Key            | authors                                                                 |
| Description    | An array of the full names of the authors of the source material.       |
| Example        | Hoesung Lee, José Romero, The Core Writing Team                         |
| Ontology Class | [oeo:author](https://openenergyplatform.org/ontology/oeo/OEO_00000064/) |
| Badge          | Bronze                                                                  |
| Card.          | [*]                                                                     |

### Resources - sources - description
|                |                                                           |
|----------------|-----------------------------------------------------------|
| Key            | description                                               |
| Description    | A free text description of the source.                    |
| Example        | A Report of the Intergovernmental Panel on Climate Change |
| Ontology Class | [dct:description](http://purl.org/dc/terms/description)   |
| Badge          | Bronze                                                    |
| Card.          | [0..1]                                                    |

### Resources - sources - publicationYear
|                |                                                 |
|----------------|-------------------------------------------------|
| Key            | publicationYear                                 |
| Description    | Indicates the year when the work was published. |
| Example        | 2023                                            |
| Ontology Class | [dct:issued](http://purl.org/dc/terms/issued)   |
| Badge          | Bronze                                          |
| Card.          | [0..1]                                          |

### Resources - sources - path
|                |                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                           |
| Description    | A DOI or link to the original source.                                                                          |
| Example        | [IPCC_AR6_SYR_FullVolume.pdf](https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf) |
| Ontology Class | [sc:url](https://schema.org/url)                                                                               |
| Badge          | Bronze                                                                                                         |
| Card.          | [0..1]                                                                                                         |

### Resources - sourceLicenses
|                |                                                                                                                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | sourceLicenses                                                                                                                                                                                                |
| Description    | An array of objects of licenses under which the described source is provided. See [academy/courses/08_licensing](https://openenergyplatform.github.io/academy/courses/08_licensing/) for further information. |
| Example        |                                                                                                                                                                                                               |
| Ontology Class | [dct:license](http://purl.org/dc/terms/license)                                                                                                                                                               |
| Badge          |                                                                                                                                                                                                               |
| Card.          | [*]                                                                                                                                                                                                           |

### Resources - sourceLicenses (name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | The [SPDX](https://spdx.org/licenses/) identifier.         |
| Example        | ODbL-1.0                                                   |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Bronze                                                     |
| Card.          | [0..1]                                                     |

### Resources - sourceLicenses (title)
|                |                                                     |
|----------------|-----------------------------------------------------|
| Key            | title                                               |
| Description    | The official (human-readable) title of the license. |
| Example        | Open Data Commons Open Database License 1.0         |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title)         |
| Badge          | Bronze                                              |
| Card.          | [0..1]                                              |

### Resources - sourceLicenses (path)
|                |                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                         |
| Description    | A link or path to the license text.                                                                          |
| Example        | [opendatacommons.org/licenses/odbl/1-0/index.html](https://opendatacommons.org/licenses/odbl/1-0/index.html) |
| Ontology Class | [sc:url](https://schema.org/url)                                                                             |
| Badge          | Bronze                                                                                                       |
| Card.          | [0..1]                                                                                                       |

### Resources - sourceLicenses (instruction)
|                |                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | instruction                                                                                                                                                                                                        |
| Description    | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.                                                                                                     |
| Example        | You are free to share and change, but you must attribute, and share derivations under the same license. See [tldrlegal.com](https://tldrlegal.com/license/odc-open-database-license-odbl) for further information. |
| Ontology Class | [rdfs:comment](https://www.w3.org/2000/01/rdf-schema#comment)                                                                                                                                                      |
| Badge          | Bronze                                                                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                                                                             |

### Resources - sourceLicenses (attribution)
|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| Key            | attribution                                                                             |
| Description    | A copyright owner of the **source**. Must be provided if attribution licenses are used. |
| Example        | © Intergovernmental Panel on Climate Change 2023                                        |
| Ontology Class | [ms:copyright notice](http://purl.obolibrary.org/obo/MS_1003198)                        |
| Badge          | Bronze                                                                                  |
| Card.          | [0..1]                                                                                  |

### Resources - sourceLicenses (copyrightStatement)
|                |                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|
| Key            | copyrightStatement                                                                                                            |
| Description    | A link or path that proves that the source or data has the appropriate license. This can be a page number or website imprint. |
| Example        | [www.ipcc.ch/copyright](https://www.ipcc.ch/copyright/)                                                                       |
| Ontology Class | [dct:rights](http://purl.org/dc/terms/rights)                                                                                 |
| Badge          | Bronze                                                                                                                        |
| Card.          | [0..1]                                                                                                                        |

### Resources - resourceLicenses
|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| Key            | resourceLicenses                                                                        |
| Description    | An array of objects of licenses under which the described resource (table) is provided. |
| Example        |                                                                                         |
| Ontology Class | [dct:license](http://purl.org/dc/terms/license)                                         |
| Badge          |                                                                                         |
| Card.          | [*]                                                                                     |

### Resources - resourceLicenses - name
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | The [SPDX](https://spdx.org/licenses/) identifier.         |
| Example        | ODbL-1.0                                                   |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Bronze                                                     |
| Card.          | [0..1]                                                     |

### Resources - resourceLicenses - title
|                |                                                     |
|----------------|-----------------------------------------------------|
| Key            | title                                               |
| Description    | The official (human-readable) title of the license. |
| Example        | Open Data Commons Open Database License 1.0         |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title)         |
| Badge          | Bronze                                              |
| Card.          | [0..1]                                              |

### Resources - resourceLicenses - path
|                |                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                         |
| Description    | A link or path to the license text.                                                                          |
| Example        | [opendatacommons.org/licenses/odbl/1-0/index.html](https://opendatacommons.org/licenses/odbl/1-0/index.html) |
| Ontology Class | [dcat:accessURL](https://www.w3.org/ns/dcat#accessURL)                                                       |
| Badge          | Bronze                                                                                                       |
| Card.          | [0..1]                                                                                                       |

### Resources - resourceLicenses - instruction
|                |                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | instruction                                                                                                                                                                                                        |
| Description    | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.                                                                                                     |
| Example        | You are free to share and change, but you must attribute, and share derivations under the same license. See [tldrlegal.com](https://tldrlegal.com/license/odc-open-database-license-odbl) for further information. |
| Ontology Class | [dc:rights](http://purl.org/dc/elements/1.1/rights)                                                                                                                                                                |
| Badge          | Bronze                                                                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                                                                             |

### Resources - resourceLicenses - attribution
|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| Key            | attribution                                                                           |
| Description    | A copyright owner of the **data**. Must be provided if attribution licenses are used. |
| Example        | © Reiner Lemoine Institut                                                             |
| Ontology Class | [spdx:attributionText](http://spdx.org/rdf/terms#attributionText)                     |
| Badge          | Bronze                                                                                |
| Card.          | [0..1]                                                                                |

### Resources - resourceLicenses - copyrightStatement
|                |                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------|
| Key            | copyrightStatement                                                                                                  |
| Description    | A link or path that proves that the data has the appropriate license. This can be a page number or website imprint. |
| Example        | [www.ipcc.ch/copyright/](https://www.ipcc.ch/copyright/)                                                            |
| Ontology Class | [dct:rights](http://purl.org/dc/terms/rights)                                                                       |
| Badge          | Bronze                                                                                                              |
| Card.          | [0..1]                                                                                                              |

## Resources - Type

### Resources - Type
| Key            | type                                                                                                   |
|----------------|--------------------------------------------------------------------------------------------------------|
| Description    | The 'table' type indicates that the resource is tabular as per 'Frictionless Tabular Data' definition. |
| Example        | table                                                                                                  |
| Ontology Class | [csvw:datatype](https://www.w3.org/ns/csvw#datatype)                                                   |
| Badge          | Gold                                                                                                   |
| Card.          | [0..1]                                                                                                 |

### Resources - Format
| Key            | format                                                                                                                          |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Description    | A file extension format. Possible options are 'csv', 'xlsx', 'json', 'PostgreSQL', 'SQLite' and other standard file extensions. |
| Example        | PostgreSQL                                                                                                                      |
| Ontology Class | [dct:format](http://purl.org/dc/terms/format)                                                                                   |
| Badge          | Gold                                                                                                                            |
| Card.          | [0..1]                                                                                                                          |

### Resources - Encoding
| Key            | encoding                                                                                                                                      |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Specifies the character encoding of the resource's data file. The default is 'UTF-8'. The values should be one of the 'Preferred MIME Names'. |
| Example        | UTF-8                                                                                                                                         |
| Ontology Class | [csvw:encoding](http://www.w3.org/ns/csvw#encoding)                                                                                           |
| Badge          | Gold                                                                                                                                          |
| Card.          | [0..1]                                                                                                                                        |

### Resources - Fields Keys
|                |                                                                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **schema**                                                                                                                                   |
| Description    | An object that describes the structure of a table. It contains all fields (columns of the table), the primary key and optional foreign keys. |
| Example        |                                                                                                                                              |
| Ontology Class | [schema:table](https://schema.org/Table)                                                                                                     |
| Badge          |                                                                                                                                              |
| Card.          | [1]                                                                                                                                          |

### Resources - Fields Keys - fields
|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| Key            | **fields**                                                                        |
| Description    | An array of objects that describes a field (column) and its detailed information. |
| Example        |                                                                                   |
| Ontology Class | [csvw:column](http://www.w3.org/ns/csvw#column)                                   |
| Badge          |                                                                                   |
| Card.          | [1]                                                                               |

### Resources - Fields Keys - name
|                |                                                                                                                                                         |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **name**                                                                                                                                                |
| Description    | The name of the field. The name may only consist of lowercase alphanumeric characters or underscores. It must not begin with a number or an underscore. |
| Example        | year                                                                                                                                                    |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)                                                                                              |
| Badge          | Iron                                                                                                                                                    |
| Card.          | [1]                                                                                                                                                     |

### Resources - Fields Keys - description
|                |                                                         |
|----------------|---------------------------------------------------------|
| Key            | **description**                                         |
| Description    | A text describing the field.                            |
| Example        | Reference year for which the data were collected.       |
| Ontology Class | [dct:description](http://purl.org/dc/terms/description) |
| Badge          | Silver                                                  |
| Card.          | [0..1]                                                  |

### Resources - Fields Keys - type
|                |                                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------|
| Key            | **type**                                                                                             |
| Description    | The data type of the field. In case of a geom column in a database, also indicate the shape and CRS. |
| Example        | geometry(Point, 4326)                                                                                |
| Ontology Class | [csvw:datatype](https://www.w3.org/ns/csvw#datatype)                                                 |
| Badge          | Iron                                                                                                 |
| Card.          | [1]                                                                                                  |

### Resources - Fields Keys - nullable
|                |                                                                                    |
|----------------|------------------------------------------------------------------------------------|
| Key            | **nullable**                                                                       |
| Description    | A boolean key to specify that a column can be nullable. True is the default value. |
| Example        | True                                                                               |
| Ontology Class | [ncit:null](http://purl.obolibrary.org/obo/NCIT_C47840)                            |
| Badge          | Iron                                                                               |
| Card.          | [1]                                                                                |

### Resources - Fields Keys - unit
|                |                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **unit**                                                                                                                                                                            |
| Description    | The unit of a field. If it does not apply, use 'null'. If the unit is given in a separate field, reference this field (e.g. 'unit'). Use a space between numbers and units (100 m). |
| Example        | MW                                                                                                                                                                                  |
| Ontology Class | [oeo:has unit](https://openenergyplatform.org/ontology/oeo/OEO_00040010/)                                                                                                           |
| Badge          | Silver                                                                                                                                                                              |
| Card.          | [0..1]                                                                                                                                                                              |

### Resources - Fields Keys - isAbout
|                |                                                                 |
|----------------|-----------------------------------------------------------------|
| Key            | **isAbout**                                                     |
| Description    | An array of objects that describes the field in ontology terms. |
| Example        |                                                                 |
| Ontology Class | [sc:about](https://schema.org/about)                            |
| Badge          |                                                                 |
| Card.          | [*]                                                             |

### Resources - Fields Keys - name (isAbout)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | **name**                                                   |
| Description    | The class label of the ontology term.                      |
| Example        | wind energy converting unit                                |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Platinum                                                   |
| Card.          | [0..1]                                                     |

### Resources - Fields Keys - @id (isAbout)
|                |                                                                          |
|----------------|--------------------------------------------------------------------------|
| Key            | **@id**                                                                  |
| Description    | The path of the ontology term (IRI).                                     |
| Example        | [OEO_00000044](https://openenergyplatform.org/ontology/oeo/OEO_00000044) |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)                    |
| Badge          | Platinum                                                                 |
| Card.          | [0..1]                                                                   |

### Resources - Fields Keys - valueReference
|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| Key            | **valueReference**                                                                             |
| Description    | An array of objects for an extended description of the values in the column in ontology terms. |
| Example        |                                                                                                |
| Ontology Class | [prov:value](https://www.w3.org/ns/prov#value)                                                 |
| Badge          |                                                                                                |
| Card.          | [*]                                                                                            |

### Resources - Fields Keys - value
|                |                                                                |
|----------------|----------------------------------------------------------------|
| Key            | **value**                                                      |
| Description    | The name of the value in the column.                           |
| Example        | onshore                                                        |
| Ontology Class | [rdf:value](https://www.w3.org/1999/02/22-rdf-syntax-ns#value) |
| Badge          | Platinum                                                       |
| Card.          | [0..1]                                                         |

### Resources - Fields Keys - name (valueReference)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | **name**                                                   |
| Description    | The class label of the ontology term in the column.        |
| Example        | onshore wind farm                                          |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Platinum                                                   |
| Card.          | [0..1]                                                     |

### Resources - Fields Keys - @id (valueReference)
|                |                                                                          |
|----------------|--------------------------------------------------------------------------|
| Key            | **@id**                                                                  |
| Description    | The path of the ontology term (IRI) in the column.                       |
| Example        | [OEO_00000311](https://openenergyplatform.org/ontology/oeo/OEO_00000311) |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)                    |
| Badge          | Platinum                                                                 |
| Card.          | [0..1]                                                                   |

### Resources - Properties Keys
|                |                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------|
| Key            | **primaryKey**                                                                                           |
| Description    | An array of fields that uniquely identifies each row in the table. The default value is the “id” column. |
| Example        | id                                                                                                       |
| Ontology Class | [csvw:primaryKey](https://www.w3.org/ns/csvw#primaryKey)                                                 |
| Badge          | Iron                                                                                                     |
| Card.          | [1..*]                                                                                                   |

### Resources - Properties Keys - foreignKeys
|                |                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------|
| Key            | **foreignKeys**                                                                                       |
| Description    | An array of objects with foreign keys that describe a field that relates to a field in another table. |
| Example        |                                                                                                       |
| Ontology Class | [csvw:foreignKey](https://www.w3.org/ns/csvw#foreignKey)                                              |
| Badge          |                                                                                                       |
| Card.          | [*]                                                                                                   |

### Resources - Properties Keys - fields (foreignKeys)
|                |                                                                         |
|----------------|-------------------------------------------------------------------------|
| Key            | **fields**                                                              |
| Description    | An array of fields in the table that is constrained by the foreign key. |
| Example        | id, version                                                             |
| Ontology Class | [ex:nestedFields](http://example.org/nestedFields)                      |
| Badge          | Iron                                                                    |
| Card.          | [*]                                                                     |

### Resources - Properties Keys - reference
|                |                                     |
|----------------|-------------------------------------|
| Key            | **reference**                       |
| Description    | The reference to the foreign table. |
| Example        |                                     |
| Ontology Class |                                     |
| Badge          |                                     |
| Card.          | [0..1]                              |

### Resources - Properties Keys - resource (reference)
|                |                                                    |
|----------------|----------------------------------------------------|
| Key            | **resource**                                       |
| Description    | The referenced foreign table.                      |
| Example        | model_draft.oep_oemetadata_table_example_version   |
| Ontology Class | [dcat:Dataset](https://www.w3.org/ns/dcat#dataset) |
| Badge          | Iron                                               |
| Card.          | [0..1]                                             |

### Resources - Properties Keys - fields (reference)
|                |                                                 |
|----------------|-------------------------------------------------|
| Key            | **fields**                                      |
| Description    | The foreign resource column.                    |
| Example        | id, version                                     |
| Ontology Class | [csvw:column](http://www.w3.org/ns/csvw#column) |
| Badge          | Iron                                            |
| Card.          | [*]                                             |

### Resources - Properties Keys - dialect
|                |                                                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **dialect**                                                                                                                                                                |
| Description    | The Dialect defines a simple format for describing the various dialects of CSV files in a language-independent manner. In a database, the values in the fields are 'null'. |
| Example        |                                                                                                                                                                            |
| Ontology Class |                                                                                                                                                                            |
| Badge          |                                                                                                                                                                            |
| Card.          | [1]                                                                                                                                                                        |

### Resources - Properties Keys - delimiter
|                |                                                                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **delimiter**                                                                                                                                                          |
| Description    | The delimiter specifies the character sequence which should separate fields (columns). Common characters are ',' (comma), ';' (semicolon), '.' (point) and '\t' (tab). |
| Example        | ,                                                                                                                                                                      |
| Ontology Class | [csvw:delimiter](http://www.w3.org/ns/csvw#delimiter)                                                                                                                  |
| Badge          | Iron                                                                                                                                                                   |
| Card.          | [1]                                                                                                                                                                    |

### Resources - Properties Keys - decimalSeparator
|                |                                                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **decimalSeparator**                                                                                                                                                       |
| Description    | The symbol used to separate the integer part from the fractional part of a number written in decimal form. Depending on language and region this symbol can be '.' or ','. |
| Example        | .                                                                                                                                                                          |
| Ontology Class | [csvw:decimalChar](http://www.w3.org/ns/csvw#decimalChar)                                                                                                                  |
| Badge          | Iron                                                                                                                                                                       |
| Card.          | [1]                                                                                                                                                                        |

### Resources - Review Keys
|                |                                                                                                                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **review**                                                                                                                                                                                                   |
| Description    | The metadata on the OEP can go through an open peer review process. See the Academy course [Open Peer Review](https://openenergyplatform.github.io/academy/courses/09_peer_review/) for further information. |
| Example        |                                                                                                                                                                                                              |
| Ontology Class |                                                                                                                                                                                                              |
| Card.          | [0..1]                                                                                                                                                                                                       |

### Resources - Review Keys - path
|                |                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| Key            | **path**                                                                                                             |
| Description    | A link or path to the documented open peer review.                                                                   |
| Example        | [open_peer_review/9](https://openenergyplatform.org/dataedit/view/model_draft/oep_table_example/open_peer_review/9/) |
| Ontology Class | [sc:url](https://schema.org/url)                                                                                     |
| Card.          | [0..1]                                                                                                               |

### Resources - Review Keys - badge
|                |                                                                                                        |
|----------------|--------------------------------------------------------------------------------------------------------|
| Key            | **badge**                                                                                              |
| Description    | A badge of either Iron, Bronze, Silver, Gold or Platinum is used to label the quality of the metadata. |
| Example        | Platinum                                                                                               |
| Ontology Class | [oeo:quality control flag](https://openenergyplatform.org/ontology/oeo/OEO_00140098/)                  |
| Card.          | [0..1]                                                                                                 |


## Dataset - Modules

### Dataset - Module - Energy Systems
|                |                                                                  |
|----------------|------------------------------------------------------------------|
| Key            | **moduleEnergySystems**                                          |
| Description    | An Object that describes the main concepts of an energy system.  |
| Example        |                                                                  |
| Ontology Class |                                                                  |
| Card.          | [0..1]                                                           |

### Dataset - Module - Energy Systems - supplyTechnologies
|                |                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Key            | **supplyTechnologies**                                                                                                     |
| Description    | A supply technology describes how specific technical components and processes are combined to generate or provide energy.  |
| Example        |                                                                                                                            |
| Ontology Class |                                                                                                                            |
| Card.          | [0..1]                                                                                                                     |

### Dataset - Module - Energy Systems - storageTechnologies
|                |                                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **storageTechnologies**                                                                                                                                         |
| Description    | An energy storage technology describes how energy storage components and energy carriers are combined to charge, store, and discharge energy for temporary use. |
| Example        |                                                                                                                                                                 |
| Ontology Class |                                                                                                                                                                 |
| Card.          | [0..1]                                                                                                                                                          |

### Dataset - Module - Energy Systems - supplyGrid
|                |                                                                                                                                 |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Key            | **supplyGrid**                                                                                                                  |
| Description    | A supply grid is a system of interconnected technical components that together enable the distribution and delivery of energy.  |
| Example        |                                                                                                                                 |
| Ontology Class |                                                                                                                                 |
| Card.          | [0..1]                                                                                                                          |

### Dataset - Module - Energy Systems - finalEnergyCarrier
|                |                                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **finalEnergyCarrier**                                                                                                                                         |
| Description    | An energy storage technology describes how energy storage components and energy carriers are combined to charge, store, and discharge energy for temporary use. |
| Example        |                                                                                                                                                                 |
| Ontology Class |                                                                                                                                                                 |
| Card.          | [0..1]                                                                                                                                                          |

### Dataset - Module - Energy Systems - demandSectors
|                |                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **demandSectors**                                                                                                                   |
| Description    | An energy demand sector is a sector of the energy system that groups together energy consumers with similar usage characteristics.  |
| Example        |                                                                                                                                     |
| Ontology Class |                                                                                                                                     |
| Card.          | [0..1]                                                                                                                              |

### Dataset - Module - Energy Systems - moduleDescription
|                |                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Key            | **moduleDescription**                                                                                                      |
| Description    | A description of the module. It should be usable as summary information for the module that is described by the metadata.  |
| Example        |                                                                                                                            |
| Ontology Class |                                                                                                                            |
| Card.          | [0..1]                                                                                                                     |


### Dataset - Module - Measurement Data
|                |                                                                   |
|----------------|-------------------------------------------------------------------|
| Key            | **moduleMeasurementData**                                         |
| Description    | An Object that describes the instruments used in the measurement. |
| Example        |                                                                   |
| Ontology Class |                                                                   |
| Card.          | [0..1]                                                            |

### Dataset - Module - Measurement Data - instrumentIdentifier
|                |                                                                     |
|----------------|---------------------------------------------------------------------|
| Key            | **instrumentIdentifier**                                            |
| Description    | Unique string that identifies the instrument instance.              |
| Example        | http://hdl.handle.net/21.11157/a9250866-bbec-4542-86b3-a5f78c0c6922 |
| Ontology Class |                                                                     |
| Card.          | [0..1]                                                              |

### Dataset - Module - Measurement Data - instrumentPath
|                |                                                 |
|----------------|-------------------------------------------------|
| Key            | **instrumentPath**                              |
| Description    | A landing page that the identifier resolves to. |
| Example        | https://sms.atmohub.kit.edu/devices/961         |
| Ontology Class |                                                 |
| Card.          | [0..1]                                          |

### Dataset - Module - Measurement Data - instrumentName
|                |                                                    |
|----------------|----------------------------------------------------|
| Key            | **instrumentName**                                 |
| Description    | Name by which the instrument instance is known.    |
| Example        | MFC_001000_02 - Merck KGaA - FC-2926V - DH9806004  |
| Ontology Class |                                                    |
| Card.          | [0..1]                                             |

### Dataset - Module - Measurement Data - instrumentOwner
|                |                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **instrumentOwner**                                                                                                                                                  |
| Description    | Institution(s) responsible for the management of the instrument. This may include the legal owner, the operator, or an institute providing access to the instrument. |
| Example        | Karlsruhe Institute of Technology (KIT)                                                                                                                              |
| Ontology Class |                                                                                                                                                                      |
| Card.          | [0..1]                                                                                                                                                               |

### Dataset - Module - Measurement Data - manufacturerName
|                |                                |
|----------------|--------------------------------|
| Key            | **manufacturerName**           |
| Description    | Full name of the manufacturer. |
| Example        | Merck KGaA                     |
| Ontology Class |                                |
| Card.          | [0..1]                         |

### Dataset - Module - Measurement Data - moduleDescription
|                |                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Key            | **moduleDescription**                                                                                                      |
| Description    | A description of the module. It should be usable as summary information for the module that is described by the metadata.  |
| Example        |                                                                                                                            |
| Ontology Class |                                                                                                                            |
| Card.          | [0..1]                                                                                                                     |


### MetaMetadata Keys
|                |                                                                                      |
|----------------|--------------------------------------------------------------------------------------|
| Key            | **metaMetadata**                                                                     |
| Description    | An object that describes the metadata themselves, their format, version and license. |
| Example        |                                                                                      |
| Ontology Class |                                                                                      |
| Card.          | [1]                                                                                  |

### MetaMetadata Keys - metadataVersion
|                |                                                              |
|----------------|--------------------------------------------------------------|
| Key            | **metadataVersion**                                          |
| Description    | Type and version number of the metadata.                     |
| Example        | OEMetadata-2.0                                               |
| Ontology Class | [owl:versionInfo](http://www.w3.org/2002/07/owl#versionInfo) |
| Card.          | [1]                                                          |

### MetaMetadata Keys - metadataLicense
|                |                                                 |
|----------------|-------------------------------------------------|
| Key            | **metadataLicense**                             |
| Description    | The license of the provided metadata.           |
| Example        |                                                 |
| Ontology Class | [dct:license](http://purl.org/dc/terms/license) |
| Card.          | [1]                                             |

### MetaMetadata Keys - metadataLicense - name
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | **name**                                                   |
| Description    | The [SPDX](https://spdx.org/licenses/) identifier.         |
| Example        | CC0-1.0                                                    |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Card.          | [1]                                                        |

### MetaMetadata Keys - metadataLicense - title
|                |                                                     |
|----------------|-----------------------------------------------------|
| Key            | **title**                                           |
| Description    | The official (human-readable) title of the license. |
| Example        | Creative Commons Zero v1.0 Universal                |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title)         |
| Card.          | [1]                                                 |

### MetaMetadata Keys - metadataLicense - path
|                |                                                                                                  |
|----------------|--------------------------------------------------------------------------------------------------|
| Key            | **path**                                                                                         |
| Description    | A link or path to the license text.                                                              |
| Example        | [creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/) |
| Ontology Class | [sc:url](https://schema.org/url)                                                                 |
| Card.          | [1]                                                                                              |
