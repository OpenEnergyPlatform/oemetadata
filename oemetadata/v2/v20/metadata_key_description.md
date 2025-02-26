<!--
SPDX-FileCopyrightText: 2024 Ludwig Hülk <Ludee> © Reiner Lemoine Institut
SPDX-FileCopyrightText: 2024 Jonas Huber <jh-RLI> © Reiner Lemoine Institut

SPDX-License-Identifier: MIT
-->

# OEMetadata - Key Description

This pages describes the key of **OEMetadata version 2.0 .** <br>
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

## Overview

### Collection Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                | <div style="width:20em">Example</div>                                                                                                                                          | <div style="width:20em">Ontology Class</div>               | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | @context                         | Explanation of metadata keys in ontology terms.                                          | [context.json](https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/oemetadata/latest/context.json)                                                      |                                                            | Platinum                           | [0..1]                             |
| 2                              | name                             | A filename or database conform dataset name.                                             | oep_oemetadata                                                                                                                                                                 | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) | Iron                               | [1]                                |
| 3                              | title                            | A human readable dataset name.                                                           | OEP OEMetadata                                                                                                                                                                 | [dct:title](http://purl.org/dc/terms/title)                | Bronze                             | [0..1]                             |
| 4                              | description                      | A free text description of the dataset.                                                  | A collection of tables for the OEMetadata examples.                                                                                                                            | [dct:description](http://purl.org/dc/terms/description)    | Bronze                             | [0..1]                             |
| 5                              | @id                              | A unique identifier (UUID/DOI) for the dataset. This is the Databus Artifact.            | [databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/](https://databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/) | [dct:identifier](http://purl.org/dc/terms/identifier)      | Platinum                           | [0..1]                             |
| 6                              | **resources**                    | An array of objects of the resources. The dataset can contain several (database) tables. |                                                                                                                                                                                | [dcat:Dataset](https://www.w3.org/ns/dcat#dataset)         |                                    | [*]                                |

### Resource - General Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                                                        | <div style="width:20em">Example</ div>                                                                                                 | <div style="width:20em">Ontology Class</div>                    | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | @id                              | A Uniform Resource Identifier (URI) that links the resource via the OpenEnergyDatabus (DBpedia Databus).                                                                         | [wri_global_power_plant_database](https://databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/2022-11-07) | [dct:identifier](http://purl.org/dc/terms/identifier)           | Platinum                           | [0..1]                             |
| 2                              | name                             | A filename or database conform table name.                                                                                                                                       | oemetadata_table_template                                                                                                              | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)      | Iron                               | [1]                                |
| 3                              | topics                           | An array of predefined topics that correspond to the database schemas of the OEP.                                                                                                | model_draft                                                                                                                            | [foaf:topic](http://xmlns.com/foaf/spec/#term_topic)            | Bronze                             | [*]                                |
| 4                              | title                            | A human readable resource or table name.                                                                                                                                         | OEMetadata Table                                                                                                                       | [dct:title](http://purl.org/dc/terms/title)                     | Silver                             | [0..1]                             |
| 5                              | path                             | A unique identifier (URI/UUID/DOI) for the table or file.                                                                                                                        | [model_draft/oemetadata_table_template](http://openenergyplatform.org/dataedit/view/model_draft/oemetadata_table_template)             | [dcat:accessURL](https://www.w3.org/ns/dcat#accessURL)          | Bronze                             | [0..1]                             |
| 6                              | description                      | A description of the table. It should be usable as summary information for the table that is described by the metadata.                                                          | Example table used to illustrate the OEMetadata structure and features.                                                                | [dct:description](http://purl.org/dc/terms/description)         | Silver                             | [0..1]                             |
| 7                              | languages                        | An array of languages used within the described data structures (e.g. titles, descriptions). The language key can be repeated if more languages are used. Standard: IETF (BCP47) | en-GB, de-DE                                                                                                                           | [dct:language](http://purl.org/dc/terms/language)               | Gold                               | [*]                                |
| 8                              | **subject**                      | An array of objects that references to the subjects of the resource in ontology terms.                                                                                           |                                                                                                                                        |                                                                 |                                    | [*]                                |
| 8.1                            | name                             | A class label of the ontology term.                                                                                                                                              | energy                                                                                                                                 | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)      | Platinum                           | [0..1]                             |
| 8.2                            | @id                              | A unique identifier (URI/IRI) of the ontology class.                                                                                                                             | [openenergyplatform.org/ontology/oeo/OEO_00000150](https://openenergyplatform.org/ontology/oeo/OEO_00000150)                           | [dct:subject](http://purl.org/dc/terms/subject)                 | Platinum                           | [0..1]                             |
| 9                              | keywords                         | An array of freely selectable keywords that help with searching and structuring. The keyword are used and managed in the OEP as table tags.                                      | example, ODbL-1.0, NFDI4Energy                                                                                                         | [dcat:keyword](http://www.w3.org/ns/dcat#keyword)               | Silver                             | [*]                                |
| 10                             | publicationDate                  | A date of publication of the data or metadata. The date format is ISO 8601 (YYYY-MM-DD).                                                                                         | 2024-10-15                                                                                                                             | [dct:issued](http://purl.org/dc/terms/issued)                   | Bronze                             | [0..1]                             |
| 11                             | **embargoPeriod**                | An object that describes the embargo period during which public access to the data is not allowed.                                                                               |                                                                                                                                        |                                                                 |                                    | [0..1]                             |
| 11.1                           | start                            | The start date of the embargo period. The date of the data (metadata) upload.                                                                                                    | 2024-10-11                                                                                                                             | [dbo:startDateTime](https://dbpedia.org/ontology/startDateTime) | Bronze                             | [0..1]                             |
| 11.2                           | end                              | The end date of the embargo period. This is the envisioned publication date.                                                                                                     | 2025-01-01                                                                                                                             | [dbo:endDateTime](https://dbpedia.org/ontology/endDateTime)     | Bronze                             | [0..1]                             |
| 11.3                           | isActive                         | A boolean key that indicates if the embargo period is currently active. Must be changed to False on the embargo period end date.                                                 | True                                                                                                                                   | [adms:status](http://www.w3.org/ns/adms#status)                 | Bronze                             | [0..1]                             |

### Resource - Context Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                                                     | <div style="width:20em">Example</div>                                                                                                                                | <div style="width:20em">Ontology Class</div>                                    | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | **context**                      | An object that describes the general setting, environment, or project leading to the creation or maintenance of this dataset. In science this is can be the research project. |                                                                                                                                                                      |                                                                                 |                                    | [0..1]                             |
| 1.1                            | title                            | A title of the associated project.                                                                                                                                            | NFDI4Energy                                                                                                                                                          | [dct:title](http://purl.org/dc/terms/title)                                     | Gold                               | [0..1]                             |
| 1.2                            | homepage                         | A URL of the project.                                                                                                                                                         | [nfdi4energy.uol.de](https://nfdi4energy.uol.de/)                                                                                                                    | [foaf:homepage](http://xmlns.com/foaf/0.1/homepage)                             | Gold                               | [0..1]                             |
| 1.3                            | documentation                    | A URL of the project documentation.                                                                                                                                           | [nfdi4energy.uol.de/sites/about_us](https://nfdi4energy.uol.de/sites/about_us/)                                                                                      | [ncit:Project Description](http://purl.obolibrary.org/obo/NCIT_C165054)         | Gold                               | [0..1]                             |
| 1.4                            | sourceCode                       | A URL of the source code of the project.                                                                                                                                      | [github.com/NFDI4Energy](https://github.com/NFDI4Energy)                                                                                                             | [oeo:code source](https://openenergyplatform.org/ontology/oeo/OEO_00000091/)    | Gold                               | [0..1]                             |
| 1.5                            | publisher                        | The publishing agency of the data. This can be the OEP.                                                                                                                       | Open Energy Platform (OEP)                                                                                                                                           | [dct:publisher](http://purl.org/dc/terms/publisher)                             | Gold                               | [0..1]                             |
| 1.6                            | publisherLogo                    | A URL to the logo of the publishing agency of data.                                                                                                                           | [OpenEnergyFamily_Logo_OpenEnergyPlatform.svg](https://github.com/OpenEnergyPlatform/organisation/blob/production/logo/OpenEnergyFamily_Logo_OpenEnergyPlatform.svg) | [foaf:logo](http://xmlns.com/foaf/0.1/logo)                                     | Gold                               | [0..1]                             |
| 1.7                            | contact                          | A reference to the creator or maintainer of the data set. It can be an email address or a GitHub handle.                                                                      | info@nfdi4energy.org                                                                                                                                                 | [oeo:contact person](https://openenergyplatform.org/ontology/oeo/OEO_00000107/) | Gold                               | [0..1]                             |
| 1.8                            | fundingAgency                    | A name of the entity providing the funding. This can be a government agency or a company.                                                                                     | Deutsche Forschungsgemeinschaft (DFG)                                                                                                                                | [sc:FundingAgency](http://schema.org/fundingAgency)                             | Gold                               | [0..1]                             |
| 1.9                            | fundingAgencyLogo                | A URL to the logo or image of the funding agency.                                                                                                                             | [DFG-logo-blau.svg](https://upload.wikimedia.org/wikipedia/commons/8/86/DFG-logo-blau.svg)                                                                           | [foaf:logo](http://xmlns.com/foaf/0.1/logo)                                     | Gold                               | [0..1]                             |
| 1.10                           | grantNo                          | An identifying grant number. In case of a publicly funded project, this number is assigned by the funding agency.                                                             | 501865131                                                                                                                                                            | [sc:Grant](http://schema.org/)                                                  | Gold                               | [0..1]                             |

### Resource - Spatial Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                     | <div style="width:20em">Example</div>                                      | <div style="width:20em">Ontology Class</div>                                                                                             | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | **spatial**                      | An object that describes the spatial context of the data.                                                                     |                                                                            |                                                                                                                                          |                                    | [0..1]                             |
| 1.1                            | **location**                     | An object that describes a specific location.                                                                                 |                                                                            | [dct:location](http://purl.org/dc/terms/Location)                                                                                        |                                    | [0..1]                             |
| 1.1.1                          | address                          | An address of the location of the data. May be specified with street name, house number, zip code, and city name.             | Rudower Chaussee 12, 12489 Berlin                                          | [schema:address](https://schema.org/address)                                                                                             | Silver                             | [0..1]                             |
| 1.1.2                          | @id                              | A path or URI to a specific location. It can use Wikidata or OpenStreetMap.                                                   | [www.wikidata.org/wiki/Q77077223](https://www.wikidata.org/wiki/Q77077223) | [dct:identifier](http://purl.org/dc/terms/identifier)                                                                                    | Platinum                           | [0..1]                             |
| 1.1.3                          | latitude                         | The latitude (lat) information of the location.                                                                               | 52.432822                                                                  | [schema:latitude](https://schema.org/latitude)                                                                                           | Gold                               | [0..1]                             |
| 1.1.4                          | longitude                        | The longitude (lon) information of the location.                                                                              | 13.5351004                                                                 | [schema:longitude](https://schema.org/longitude)                                                                                         | Gold                               | [0..1]                             |
| 1.2                            | **extent**                       | An object that describes a covered area or region.                                                                            |                                                                            | [oeo:spatial region](http://purl.obolibrary.org/obo/BFO_0000006)                                                                         |                                    | [0..1]                             |
| 1.2.1                          | name                             | The name of the region.                                                                                                       | Berlin                                                                     | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)                                                                               | Silver                             | [0..1]                             |
| 1.2.2                          | @id                              | A URI reference for the region.                                                                                               | [www.wikidata.org/wiki/Q64](https://www.wikidata.org/wiki/Q64)             | [dct:identifier](http://purl.org/dc/terms/identifier)                                                                                    | Platinum                           | [0..1]                             |
| 1.2.3                          | resolutionValue                  | The value of the spatial resolution.                                                                                          | 100                                                                        | [dcat:spatialResolutionInMeters](http://www.w3.org/ns/dcat#spatialResolutionInMeters)                                                    | Silver                             | [0..1]                             |
| 1.2.4                          | resolutionUnit                   | The unit of the spatial resolution.                                                                                           | m                                                                          | [oeo:unit](http://openenergyplatform.org/ontology/oeo/OEO_00010489)                                                                      | Silver                             | [0..1]                             |
| 1.2.5                          | boundingBox                      | The covered area specified by the coordinates of a bounding box. The format is [minLon, minLat, maxLon, maxLat] or [W,S,E,N]. | [13.08825, 52.33859, 13.76104, 52.6754]                                    | [dcat:bbox](http://www.w3.org/ns/dcat#bbox)                                                                                              | Gold                               | [*]                                |
| 1.2.6                          | crs                              | The Coordinate Reference System, specified as an EPSG code.                                                                   | EPSG:4326                                                                  | [cco:Geospatial Coordinate Reference System](http://www.ontologyrepository.com/CommonCoreOntologies/GeospatialCoordinateReferenceSystem) | Gold                               | [0..1]                             |

### Resource - Temporal Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                                   | <div style="width:20em">Example</div> | <div style="width:20em">Ontology Class</div>                                          | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|---------------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | **temporal**                     | An object with the time period covered in the data. Temporal information should contain a "referenceDate" or the keys that describe a time series, or both. |                                       | [schema:temporalCoverage](https://schema.org/temporalCoverage)                        |                                    | [0..1]                             |
| 1.1                            | referenceDate                    | A base year, month or day. The time for which the data should be accurate. Date Format is ISO 8601.                                                         | 2020-01-01                            | [dct:date](http://purl.org/dc/terms/date)                                             | Silver                             | [0..1]                             |
| 1.2                            | **timeseries**                   | An array that describes the timeseries.                                                                                                                     |                                       | [dct:PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime)                             |                                    | [*]                                |
| 1.2.1                          | start                            | The start time of a time series.                                                                                                                            | 2020-01-01T00:00:00+00:00             | [dbo:startDateTime](https://dbpedia.org/ontology/startDateTime)                       | Silver                             | [0..1]                             |
| 1.2.2                          | end                              | The temporal end point of a time series.                                                                                                                    | 2020-01-01T23:59:30+00:00             | [dbo:endDateTime](https://dbpedia.org/ontology/endDateTime)                           | Silver                             | [0..1]                             |
| 1.2.3                          | resolutionValue                  | The time span between individual information points in a time series. The value of the resolution.                                                          | 30 s                                  | [dcat:spatialResolutionInMeters](http://www.w3.org/ns/dcat#spatialResolutionInMeters) | Silver                             | [0..1]                             |
| 1.2.4                          | resolutionUnit                   | The unit of the temporal resolution.                                                                                                                        | 30 s                                  | [oeo:unit](http://openenergyplatform.org/ontology/oeo/OEO_00010489)                   | Silver                             | [0..1]                             |
| 1.2.5                          | alignment                        | An indicator of whether timestamps in a time series are to the left, right or in the centre.                                                                | left                                  | [oeo:time stamp alignment](http://openenergyplatform.org/ontology/oeo/OEO_00140044)   | Silver                             | [0..1]                             |
| 1.2.6                          | aggregationType                  | An indicator of whether the values are a sum, an average or a current value.                                                                                | current                               | [oeo:aggregation type](https://openenergyplatform.org/ontology/oeo/OEO_00140068/)     | Silver                             | [0..1]                             |

### Resource - Sources Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                                                                                     | <div style="width:20em">Example</div>                                                                                                                                                                              | <div style="width:20em">Ontology Class</div>                            | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | **sources**                      | An array of objects with the used and underlying sources of the data and metadata.                                                                                                                            |                                                                                                                                                                                                                    | [dct:source](http://purl.org/dc/terms/source)                           |                                    | [*]                                |
| 1.1                            | title                            | A human readable title of the source, a document title or organisation name.                                                                                                                                  | IPCC Sixth Assessment Report (AR6) - Climate Change 2023 - Synthesis Report                                                                                                                                        | [dct:title](http://purl.org/dc/terms/title)                             | Bronze                             | [0..1]                             |
| 1.2                            | authors                          | An array of the full names of the authors of the source material.                                                                                                                                             | Hoesung Lee,José Romero, The Core Writing Team                                                                                                                                                                     | [oeo:author](https://openenergyplatform.org/ontology/oeo/OEO_00000064/) | Bronze                             | [*]                                |
| 1.3                            | description                      | A free text description of the source.                                                                                                                                                                        | A Report of the Intergovernmental Panel on Climate Change                                                                                                                                                          | [dct:description](http://purl.org/dc/terms/description)                 | Bronze                             | [0..1]                             |
| 1.4                            | publicationYear                  | Indicates the year when the work was published.                                                                                                                                                               | 2023                                                                                                                                                                                                               | [dct:issued](http://purl.org/dc/terms/issued)                           | Bronze                             | [0..1]                             |
| 1.5                            | path                             | A DOI or link to the original source.                                                                                                                                                                         | [IPCC_AR6_SYR_FullVolume.pdf](https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf)                                                                                                     | [sc:url](https://schema.org/url)                                        | Bronze                             | [0..1]                             |
| 1.6                            | **sourceLicenses**               | An array of objects of licenses under which the described source is provided. See [academy/courses/08_licensing](https://openenergyplatform.github.io/academy/courses/08_licensing/) for further information. |                                                                                                                                                                                                                    | [dct:license](http://purl.org/dc/terms/license)                         |                                    | [*]                                |
| 1.6.1                          | name                             | The [SPDX](https://spdx.org/licenses/) identifier.                                                                                                                                                            | ODbL-1.0                                                                                                                                                                                                           | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)              | Bronze                             | [0..1]                             |
| 1.6.2                          | title                            | The official (human-readable) title of the license.                                                                                                                                                           | Open Data Commons Open Database License 1.0                                                                                                                                                                        | [dct:title](http://purl.org/dc/terms/title)                             | Bronze                             | [0..1]                             |
| 1.6.3                          | path                             | A link or path to the license text.                                                                                                                                                                           | [opendatacommons.org/licenses/odbl/1-0/index.html](https://opendatacommons.org/licenses/odbl/1-0/index.html)                                                                                                       | [sc:url](https://schema.org/url)                                        | Bronze                             | [0..1]                             |
| 1.6.4                          | instruction                      | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.                                                                                                | You are free to share and change, but you must attribute, and share derivations under the same license. See [tldrlegal.com](https://tldrlegal.com/license/odc-open-database-license-odbl) for further information. | [rdfs:comment](https://www.w3.org/2000/01/rdf-schema#comment)           | Bronze                             | [0..1]                             |
| 1.6.5                          | attribution                      | A copyright owner of the **source**. Must be provided if attribution licenses are used.                                                                                                                       | © Intergovernmental Panel on Climate Change 2023                                                                                                                                                                   | [ms:copyright notice](http://purl.obolibrary.org/obo/MS_1003198)        | Bronze                             | [0..1]                             |
| 1.6.6                          | copyrightStatement               | A link or path that proves that the source or data has the appropriate license. This can be a page number or website imprint.                                                                                 | [www.ipcc.ch/copyright](https://www.ipcc.ch/copyright/)                                                                                                                                                            | [dct:rights](http://purl.org/dc/terms/rights)                           | Bronze                             | [0..1]                             |

### Resource - Licenses Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                           | <div style="width:20em">Example</div>                                                                                                                                                                              | <div style="width:20em">Ontology Class</div>                        | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | **licenses**                     | An array of objects of licenses under which the described data is provided.                                         |                                                                                                                                                                                                                    | [dct:license](http://purl.org/dc/terms/license)                     |                                    | [*]                                |
| 1.1                            | name                             | The [SPDX](https://spdx.org/licenses/) identifier.                                                                  | ODbL-1.0                                                                                                                                                                                                           | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)          | Bronze                             | [0..1]                             |
| 1.2                            | title                            | The official (human-readable) title of the license.                                                                 | Open Data Commons Open Database License 1.0                                                                                                                                                                        | [dct:title](http://purl.org/dc/terms/title)                         | Bronze                             | [0..1]                             |
| 1.3                            | path                             | A link or path to the license text.                                                                                 | [opendatacommons.org/licenses/odbl/1-0/index.html](https://opendatacommons.org/licenses/odbl/1-0/index.html)                                                                                                       | [dcat:accessURL](https://www.w3.org/ns/dcat#accessURL)              | Bronze                             | [0..1]                             |
| 1.4                            | instruction                      | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.      | You are free to share and change, but you must attribute, and share derivations under the same license. See [tldrlegal.com](https://tldrlegal.com/license/odc-open-database-license-odbl) for further information. | [dc:rights](http://purl.org/dc/elements/1.1/rights)                 | Bronze                             | [0..1]                             |
| 1.5                            | attribution                      | A copyright owner of the **data**. Must be provided if attribution licenses are used.                               | © Reiner Lemoine Institut                                                                                                                                                                                          | [spdx:attributionText](http://spdx.org/rdf/terms#attributionText)   | Bronze                             | [0..1]                             |
| 1.6                            | copyrightStatement               | A link or path that proves that the data has the appropriate license. This can be a page number or website imprint. | [www.ipcc.ch/copyright/](https://www.ipcc.ch/copyright/)                                                                                                                                                           | [dct:rights](http://purl.org/dc/terms/rights)                       | Bronze                             | [0..1]                             |

### Resource - Provenance Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                                                                                                                                                                                                                                       | <div style="width:20em">Example</div> | <div style="width:20em">Ontology Class</div>                                  | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|-------------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | **contributors**                 | An array of objects of the people or organizations who contributed to the data or metadata. Should have "Date of data creation" and "Date of metadata creation"                                                                                                                                                                                                 |                                       | [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)                                 |                                    | [*]                                |
| 1.1                            | title                            | A full name of the contributor.                                                                                                                                                                                                                                                                                                                                 | Ludwig Hülk                           | [dct:title](http://purl.org/dc/terms/title)                                   | Bronze                             | [0..1]                             |
| 1.2                            | path                             | A qualified link or path pointing to a relevant location online for the contributor. This can be the GitHub page or ORCID.                                                                                                                                                                                                                                      | https://github.com/Ludee              | [sc:url](https://schema.org/url)                                              | Bronze                             | [0..1]                             |
| 1.3                            | organization                     | A string describing the organization this contributor is affiliated to. This can be relevant for the copyright.                                                                                                                                                                                                                                                 | Reiner Lemoine Institut               | [oeo:organisation](https://openenergyplatform.org/ontology/oeo/OEO_00030022/) | Bronze                             | [0..1]                             |
| 1.4                            | roles                            | An array describing the roles of the contributor. A role is recommended to follow the established vocabulary: [DataCite Metadata Schema’s contributorRole](https://support.datacite.org/docs/datacite-metadata-schema-v44-recommended-and-optional-properties#7a-contributortype). Useful roles to indicate are: DataCollector, ContactPerson, and DataCurator. | DataCollector, DataCurator            | [oeo:role](https://openenergyplatform.org/ontology/oeo/BFO_0000023/)          | Bronze                             | [*]                                |
| 1.5                            | date                             | The date of the contribution. Date Format is ISO 8601.                                                                                                                                                                                                                                                                                                          | 2024-10-21                            | [dct:issued](http://purl.org/dc/terms/issued)                                 | Bronze                             | [0..1]                             |
| 1.6                            | object                           | The target of the contribution. This can be the data, the metadata or both (data and metadata).                                                                                                                                                                                                                                                                 | data and metadata                     | [dct:type](http://purl.org/dc/terms/type)                                     | Bronze                             | [0..1]                             |
| 1.7                            | comment                          | A free-text commentary on what has been done.                                                                                                                                                                                                                                                                                                                   | Add general context.                  | [rdfs:comment](https://www.w3.org/2000/01/rdf-schema#comment)                 | Bronze                             | [0..1]                             |

### Resource - Type Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                     | <div style="width:20em">Example</div> | <div style="width:20em">Ontology Class</div>         | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------|------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | type                             | The 'table' type indicates that the resource is tabular as per 'Frictionless Tabular Data' definition.                                        | table                                 | [csvw:datatype](https://www.w3.org/ns/csvw#datatype) | Gold                               | [0..1]                             |
| 2                              | format                           | A file extension format. Possible options are 'csv', 'xlsx', 'json', 'PostgreSQL', 'SQLite' and other standard file extensions.               | PostgreSQL                            | [dct:format](http://purl.org/dc/terms/format)        | Gold                               | [0..1]                             |
| 3                              | encoding                         | Specifies the character encoding of the resource's data file. The default is 'UTF-8'. The values should be one of the 'Preferred MIME Names'. | UTF-8                                 | [csvw:encoding](http://www.w3.org/ns/csvw#encoding)  | Gold                               | [0..1]                             |

#### Resource - Fields Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                                                            | <div style="width:20em">Example</div>                                    | <div style="width:20em">Ontology Class</div>                              | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------|---------------------------------------------------------------------------|------------------------------------|------------------------------------|
| 1                              | **schema**                       | An object that describes the structure of a table. It contains all fields (columns of the table), the primary key and optional foreign keys.                                         |                                                                          | [schema:table](https://schema.org/Table)                                  |                                    | [1]                                |
| 1.1                            | **fields**                       | An array of objects that describes a field (column) and its detailed information.                                                                                                    |                                                                          | [csvw:column](http://www.w3.org/ns/csvw#column)                           |                                    | [1]                                |
| 1.1.1                          | name                             | The name of the field. The name may only consist of lowercase alphanumeric characters or underscores. It must not begin with a number or an underscore.                              | year                                                                     | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)                | Iron                               | [1]                                |
| 1.1.2                          | description                      | A text describing the field.                                                                                                                                                         | Reference year for which the data were collected.                        | [dct:description](http://purl.org/dc/terms/description)                   | Silver                             | [0..1]                             |
| 1.1.3                          | type                             | The data type of the field. In case of a geom column in a database, also indicate the shape and CRS.                                                                                 | geometry(Point, 4326)                                                    | [csvw:datatype](https://www.w3.org/ns/csvw#datatype)                      | Iron                               | [1]                                |
| 1.1.4                          | nullable                         | A boolean key to specify that a column can be nullable. True is the default value.                                                                                                   | True                                                                     | [ncit:null](http://purl.obolibrary.org/obo/NCIT_C47840)                   | Iron                               | [1]                                |
| 1.1.5                          | unit                             | The unit of a field. If it does not apply, use 'null'. If the unit is given in a separate field, reference this field (e.g. 'unit').  Use a space between numbers and units (100 m). | MW                                                                       | [oeo:has unit](https://openenergyplatform.org/ontology/oeo/OEO_00040010/) | Silver                             | [0..1]                             |
| 1.1.6                          | **isAbout**                      | An array of objects that describes the field in ontology terms.                                                                                                                      |                                                                          | [sc:about](https://schema.org/about)                                      |                                    | [*]                                |
| 1.1.6.1                        | name                             | The class label of the ontology term.                                                                                                                                                | wind energy converting unit                                              | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)                | Platinum                           | [0..1]                             |
| 1.1.6.2                        | @id                              | The path of the ontology term (IRI).                                                                                                                                                 | [OEO_00000044](https://openenergyplatform.org/ontology/oeo/OEO_00000044) | [dct:identifier](http://purl.org/dc/terms/identifier)                     | Platinum                           | [0..1]                             |
| 1.1.7                          | **valueReference**               | An array of objects for an extended description of the values in the column in ontology terms.                                                                                       |                                                                          | [prov:value](https://www.w3.org/ns/prov#value)                            |                                    | [*]                                |
| 1.1.7.1                        | value                            | The name of the value in the column.                                                                                                                                                 | onshore                                                                  | [rdf:value](https://www.w3.org/1999/02/22-rdf-syntax-ns#value)            | Platinum                           | [0..1]                             |
| 1.1.7.2                        | name                             | The class label of the ontology term in the column.                                                                                                                                  | onshore wind farm                                                        | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)                | Platinum                           | [0..1]                             |
| 1.1.7.3                        | @id                              | The path of the ontology term (IRI) in the column.                                                                                                                                   | [OEO_00000311](https://openenergyplatform.org/ontology/oeo/OEO_00000311) | [dct:identifier](http://purl.org/dc/terms/identifier)                     | Platinum                           | [0..1]                             |

#### Resource - Properties Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                                                  | <div style="width:20em">Example</div>            | <div style="width:20em">Ontology Class</div>              | <div style="width:4em">Badge</div> | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------------------|------------------------------------|------------------------------------|
| 1.2                            | primaryKey                       | An array of fields that uniquely identifies each row in the table. The default value is the “id” column.                                                                   | id                                               | [csvw:primaryKey](https://www.w3.org/ns/csvw#primaryKey)  | Iron                               | [1..*]                             |
| 1.3                            | **foreignKeys**                  | An array of objects with foreign keys that describe a field that relates to a field in another table.                                                                      |                                                  | [csvw:foreignKey](https://www.w3.org/ns/csvw#foreignKey)  |                                    | [*]                                |
| 1.3.1                          | fields                           | An array of fields in the table that is constrained by the foreign key.                                                                                                    | id, version                                      | [ex:nestedFields](http://example.org/nestedFields)        | Iron                               | [*]                                |
| 1.3.2                          | **reference**                    | The reference to the foreign table.                                                                                                                                        |                                                  |                                                           |                                    | [0..1]                             |
| 1.3.2.1                        | resource                         | The referenced foreign table.                                                                                                                                              | model_draft.oep_oemetadata_table_example_version | [dcat:Dataset](https://www.w3.org/ns/dcat#dataset)        | Iron                               | [0..1]                             |
| 1.3.2.2                        | fields                           | The foreign resource column.                                                                                                                                               | id, version                                      | [csvw:column](http://www.w3.org/ns/csvw#column)           | Iron                               | [*]                                |
| 1.4                            | **dialect**                      | The Dialect defines a simple format for describing the various dialects of CSV files in a language-independent manner. In a database, the values in the fields are 'null'. |                                                  |                                                           |                                    | [1]                                |
| 1.4.1                          | delimiter                        | The delimiter specifies the character sequence which should separate fields (columns). Common characters are ',' (comma), ';' (semicolon), '.' (point) and '\t' (tab).     | ,                                                | [csvw:delimiter](http://www.w3.org/ns/csvw#delimiter)     | Iron                               | [1]                                |
| 1.4.2                          | decimalSeparator                 | The symbol used to separate the integer part from the fractional part of a number written in decimal form. Depending on language and region this symbol can be '.' or ','. | .                                                | [csvw:decimalChar](http://www.w3.org/ns/csvw#decimalChar) | Iron                               | [1]                                |

### Resource - Review Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                                                                                                                                                    | <div style="width:20em">Example</div>                                                                                | <div style="width:20em">Ontology Class</div>                                          | <div style="width:4em">Badge</div> |
|--------------------------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------|------------------------------------|
| 1.                             | **review**                       | The metadata on the OEP can go through an open peer review process. See the Academy course [Open Peer Review](https://openenergyplatform.github.io/academy/courses/09_peer_review/) for further information. |                                                                                                                      |                                                                                       | [0..1]                             |
| 1.1                            | path                             | A link or path to the documented open peer review.                                                                                                                                                           | [open_peer_review/9](https://openenergyplatform.org/dataedit/view/model_draft/oep_table_example/open_peer_review/9/) | [sc:url](https://schema.org/url)                                                      | [0..1]                             |
| 1.2                            | badge                            | A badge of either Iron, Bronze, Silver, Gold or Platinum is used to label the quality of the metadata.                                                                                                       | Platinum                                                                                                             | [oeo:quality control flag](https://openenergyplatform.org/ontology/oeo/OEO_00140098/) | [0..1]                             |

### MetaMetadata Keys
| <div style="width:1em">#</div> | <div style="width:6em">Key</div> | <div style="width:20em">Description</div>                                            | <div style="width:20em">Example</div>                                                            | <div style="width:20em">Ontology Class</div>                 | <div style="width:3em">Card.</div> |
|--------------------------------|----------------------------------|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|--------------------------------------------------------------|------------------------------------|
| 1                              | **metaMetadata**                 | An object that describes the metadata themselves, their format, version and license. |                                                                                                  |                                                              | [1]                                |
| 1.1                            | metadataVersion                  | Type and version number of the metadata.                                             | OEMetadata-2.0                                                                                   | [owl:versionInfo](http://www.w3.org/2002/07/owl#versionInfo) | [1]                                |
| 1.2                            | **metadataLicense**              | The license of the provided metadata.                                                |                                                                                                  | [dct:license](http://purl.org/dc/terms/license)              | [1]                                |
| 1.2.1                          | name                             | The [SPDX](https://spdx.org/licenses/) identifier.                                   | CC0-1.0                                                                                          | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)   | [1]                                |
| 1.2.2                          | title                            | The official (human-readable) title of the license.                                  | Creative Commons Zero v1.0 Universal                                                             | [dct:title](http://purl.org/dc/terms/title)                  | [1]                                |
| 1.2.3                          | path                             | A link or path to the license text.                                                  | [creativecommons.org/publicdomain/zero/1.0/](https://creativecommons.org/publicdomain/zero/1.0/) | [sc:url](https://schema.org/url)                             | [1]                                |


## Metadata Keys

### Dataset - @context
|                    |                                                                                                                           |
|--------------------|---------------------------------------------------------------------------------------------------------------------------|
| **Key**            | @context                                                                                                                  |
| **Description**    | Explanation of metadata keys in ontology terms.                                                                           |
| **Example**        | [context.json](https://raw.githubusercontent.com/OpenEnergyPlatform/oemetadata/production/oemetadata/latest/context.json) |
| **Ontology Class** |                                                                                                                           |
| **Badge**          | Platinum                                                                                                                  |
| **Card.**          | [0..1]                                                                                                                    |


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


### Dataset - @id
|                    |                                                                                                                                                                                |
|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Key**            | @id                                                                                                                                                                            |
| **Description**    | A unique identifier (UUID/DOI) for the dataset. This is the Databus Artifact.                                                                                                  |
| **Example**        | [databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/](https://databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/) |
| **Ontology Class** | [dct:identifier](http://purl.org/dc/terms/identifier)                                                                                                                          |
| **Badge**          | Platinum                                                                                                                                                                       |
| **Card.**          | [0..1]                                                                                                                                                                         |


### Dataset - resources
|                    |                                                                                          |
|--------------------|------------------------------------------------------------------------------------------|
| **Key**            | resources                                                                                |
| **Description**    | An array of objects of the resources. The dataset can contain several (database) tables. |
| **Example**        |                                                                                          |
| **Ontology Class** | [dcat:Dataset](https://www.w3.org/ns/dcat#dataset)                                       |
| **Badge**          |                                                                                          |
| **Card.**          | [*]                                                                                      |

### Resource - @id
|                |                                                                                                                                                                                         |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | @id                                                                                                                                                                                     |
| Description    | A Uniform Resource Identifier (URI) that links the resource via the OpenEnergyDatabus (DBpedia Databus).                                                                                |
| Example        | [wri_global_power_plant_database](https://databus.openenergyplatform.org/oeplatform/supply/wri_global_power_plant_database/2022-11-07/wri_global_power_plant_database_variant=data.csv) |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)                                                                                                                                   |
| Badge          | Platinum                                                                                                                                                                                |
| Card.          | [0..1]                                                                                                                                                                                  |


### Resource - name
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | A filename or database conform table name.                 |
| Example        | oemetadata_table_template                                  |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Iron                                                       |
| Card.          | [1]                                                        |


### Resource - topics
|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| Key            | topics                                                                            |
| Description    | An array of predefined topics that correspond to the database schemas of the OEP. |
| Example        | model_draft                                                                       |
| Ontology Class | [foaf:topic](http://xmlns.com/foaf/spec/#term_topic)                              |
| Badge          | Bronze                                                                            |
| Card.          | [*]                                                                               |


### Resource - title
|                |                                             |
|----------------|---------------------------------------------|
| Key            | title                                       |
| Description    | A human readable resource or table name.    |
| Example        | OEMetadata Table                            |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title) |
| Badge          | Silver                                      |
| Card.          | [0..1]                                      |


### Resource - path
|                |                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                                       |
| Description    | A unique identifier (URI/UUID/DOI) for the table or file.                                                                  |
| Example        | [model_draft/oemetadata_table_template](http://openenergyplatform.org/dataedit/view/model_draft/oemetadata_table_template) |
| Ontology Class | [dcat:accessURL](https://www.w3.org/ns/dcat#accessURL)                                                                     |
| Badge          | Bronze                                                                                                                     |
| Card.          | [0..1]                                                                                                                     |


### Resource - description
|                |                                                                                                                         |
|----------------|-------------------------------------------------------------------------------------------------------------------------|
| Key            | description                                                                                                             |
| Description    | A description of the table. It should be usable as summary information for the table that is described by the metadata. |
| Example        | Example table used to illustrate the OEMetadata structure and features.                                                 |
| Ontology Class | [dct:description](http://purl.org/dc/terms/description)                                                                 |
| Badge          | Silver                                                                                                                  |
| Card.          | [0..1]                                                                                                                  |


### Resource - languages
|                |                                                                                                                                                                                   |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | languages                                                                                                                                                                         |
| Description    | An array of languages used within the described data structures (e.g. titles, descriptions). The language key can be repeated if more languages are used. Standard: IETF (BCP47). |
| Example        | en-GB, de-DE                                                                                                                                                                      |
| Ontology Class | [dct:language](http://purl.org/dc/terms/language)                                                                                                                                 |
| Badge          | Gold                                                                                                                                                                              |
| Card.          | [*]                                                                                                                                                                               |


### Resource - subject
|                |                                                                                     |
|----------------|-------------------------------------------------------------------------------------|
| Key            | subject                                                                             |
| Description    | An array of objects that references the subjects of the resource in ontology terms. |
| Example        |                                                                                     |
| Ontology Class |                                                                                     |
| Badge          |                                                                                     |
| Card.          | [*]                                                                                 |


### Resource - subject (name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | A class label of the ontology term.                        |
| Example        | energy                                                     |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Platinum                                                   |
| Card.          | [0..1]                                                     |


### Resource - subject (@id)
|                |                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Key            | @id                                                                                                          |
| Description    | A unique identifier (URI/IRI) of the ontology class.                                                         |
| Example        | [openenergyplatform.org/ontology/oeo/OEO_00000150](https://openenergyplatform.org/ontology/oeo/OEO_00000150) |
| Ontology Class | [dct:subject](http://purl.org/dc/terms/subject)                                                              |
| Badge          | Platinum                                                                                                     |
| Card.          | [0..1]                                                                                                       |


### Resource - keywords
|                |                                                                                  |
|----------------|----------------------------------------------------------------------------------|
| Key            | keywords                                                                         |
| Description    | An array of freely selectable keywords that help with searching and structuring. |
| Example        | example, ODbL-1.0, NFDI4Energy                                                   |
| Ontology Class | [dcat:keyword](http://www.w3.org/ns/dcat#keyword)                                |
| Badge          | Silver                                                                           |
| Card.          | [*]                                                                              |


### Resource - publicationDate
|                |                                                                                          |
|----------------|------------------------------------------------------------------------------------------|
| Key            | publicationDate                                                                          |
| Description    | A date of publication of the data or metadata. The date format is ISO 8601 (YYYY-MM-DD). |
| Example        | 2024-10-15                                                                               |
| Ontology Class | [dct:issued](http://purl.org/dc/terms/issued)                                            |
| Badge          | Bronze                                                                                   |
| Card.          | [0..1]                                                                                   |


### Resource - embargoPeriod
|                |                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------|
| Key            | embargoPeriod                                                                                      |
| Description    | An object that describes the embargo period during which public access to the data is not allowed. |
| Example        |                                                                                                    |
| Ontology Class |                                                                                                    |
| Badge          |                                                                                                    |
| Card.          | [0..1]                                                                                             |


### Resource - embargoPeriod (start)
|                |                                                                               |
|----------------|-------------------------------------------------------------------------------|
| Key            | start                                                                         |
| Description    | The start date of the embargo period. The date of the data (metadata) upload. |
| Example        | 2024-10-11                                                                    |
| Ontology Class | [dbo:startDateTime](https://dbpedia.org/ontology/startDateTime)               |
| Badge          | Bronze                                                                        |
| Card.          | [0..1]                                                                        |


### Resource - embargoPeriod (end)
|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| Key            | end                                                                          |
| Description    | The end date of the embargo period. This is the envisioned publication date. |
| Example        | 2025-01-01                                                                   |
| Ontology Class | [dbo:endDateTime](https://dbpedia.org/ontology/endDateTime)                  |
| Badge          | Bronze                                                                       |
| Card.          | [0..1]                                                                       |


### Resource - embargoPeriod (isActive)
|                |                                                                                                                                  |
|----------------|----------------------------------------------------------------------------------------------------------------------------------|
| Key            | isActive                                                                                                                         |
| Description    | A boolean key that indicates if the embargo period is currently active. Must be changed to False on the embargo period end date. |
| Example        | True                                                                                                                             |
| Ontology Class | [adms:status](http://www.w3.org/ns/adms#status)                                                                                  |
| Badge          | Bronze                                                                                                                           |
| Card.          | [0..1]                                                                                                                           |

### Resource - context
|                |                                                                                                                                                                             |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | context                                                                                                                                                                     |
| Description    | An object that describes the general setting, environment, or project leading to the creation or maintenance of this dataset. In science, this can be the research project. |
| Example        |                                                                                                                                                                             |
| Ontology Class |                                                                                                                                                                             |
| Badge          |                                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                                      |


### Resource - context (title)
|                |                                             |
|----------------|---------------------------------------------|
| Key            | title                                       |
| Description    | A title of the associated project.          |
| Example        | NFDI4Energy                                 |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title) |
| Badge          | Gold                                        |
| Card.          | [0..1]                                      |

### Resource - context (homepage)
|                |                                                     |
|----------------|-----------------------------------------------------|
| Key            | homepage                                            |
| Description    | A URL of the project.                               |
| Example        | [nfdi4energy.uol.de](https://nfdi4energy.uol.de/)   |
| Ontology Class | [foaf:homepage](http://xmlns.com/foaf/0.1/homepage) |
| Badge          | Gold                                                |
| Card.          | [0..1]                                              |


### Resource - context (documentation)
|                |                                                                                 |
|----------------|---------------------------------------------------------------------------------|
| Key            | documentation                                                                   |
| Description    | A URL of the project documentation.                                             |
| Example        | [nfdi4energy.uol.de/sites/about_us](https://nfdi4energy.uol.de/sites/about_us/) |
| Ontology Class | [ncit:Project Description](http://purl.obolibrary.org/obo/NCIT_C165054)         |
| Badge          | Gold                                                                            |
| Card.          | [0..1]                                                                          |


### Resource - context (sourceCode)
|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| Key            | sourceCode                                                                   |
| Description    | A URL of the source code of the project.                                     |
| Example        | [github.com/NFDI4Energy](https://github.com/NFDI4Energy)                     |
| Ontology Class | [oeo:code source](https://openenergyplatform.org/ontology/oeo/OEO_00000091/) |
| Badge          | Gold                                                                         |
| Card.          | [0..1]                                                                       |


### Resource - context (publisher)
|                |                                                         |
|----------------|---------------------------------------------------------|
| Key            | publisher                                               |
| Description    | The publishing agency of the data. This can be the OEP. |
| Example        | Open Energy Platform (OEP)                              |
| Ontology Class | [dct:publisher](http://purl.org/dc/terms/publisher)     |
| Badge          | Gold                                                    |
| Card.          | [0..1]                                                  |


### Resource - context (publisherLogo)
|                |                                                                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | publisherLogo                                                                                                                                                        |
| Description    | A URL to the logo of the publishing agency of data.                                                                                                                  |
| Example        | [OpenEnergyFamily_Logo_OpenEnergyPlatform.svg](https://github.com/OpenEnergyPlatform/organisation/blob/production/logo/OpenEnergyFamily_Logo_OpenEnergyPlatform.svg) |
| Ontology Class | [foaf:logo](http://xmlns.com/foaf/0.1/logo)                                                                                                                          |
| Badge          | Gold                                                                                                                                                                 |
| Card.          | [0..1]                                                                                                                                                               |


### Resource - context (contact)
|                |                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------|
| Key            | contact                                                                                                  |
| Description    | A reference to the creator or maintainer of the data set. It can be an email address or a GitHub handle. |
| Example        | info@nfdi4energy.org                                                                                     |
| Ontology Class | [oeo:contact person](https://openenergyplatform.org/ontology/oeo/OEO_00000107/)                          |
| Badge          | Gold                                                                                                     |
| Card.          | [0..1]                                                                                                   |


### Resource - context (fundingAgency)
|                |                                                                                           |
|----------------|-------------------------------------------------------------------------------------------|
| Key            | fundingAgency                                                                             |
| Description    | A name of the entity providing the funding. This can be a government agency or a company. |
| Example        | Deutsche Forschungsgemeinschaft (DFG)                                                     |
| Ontology Class | [sc:FundingAgency](http://schema.org/fundingAgency)                                       |
| Badge          | Gold                                                                                      |
| Card.          | [0..1]                                                                                    |


### Resource - context (fundingAgencyLogo)
|                |                                                                                            |
|----------------|--------------------------------------------------------------------------------------------|
| Key            | fundingAgencyLogo                                                                          |
| Description    | A URL to the logo or image of the funding agency.                                          |
| Example        | [DFG-logo-blau.svg](https://upload.wikimedia.org/wikipedia/commons/8/86/DFG-logo-blau.svg) |
| Ontology Class | [foaf:logo](http://xmlns.com/foaf/0.1/logo)                                                |
| Badge          | Gold                                                                                       |
| Card.          | [0..1]                                                                                     |


### Resource - context (grantNo)
|                |                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------|
| Key            | grantNo                                                                                                           |
| Description    | An identifying grant number. In case of a publicly funded project, this number is assigned by the funding agency. |
| Example        | 501865131                                                                                                         |
| Ontology Class | [sc:Grant](http://schema.org/)                                                                                    |
| Badge          | Gold                                                                                                              |
| Card.          | [0..1]                                                                                                            |

### Resource - spatial
|                |                                                           |
|----------------|-----------------------------------------------------------|
| Key            | spatial                                                   |
| Description    | An object that describes the spatial context of the data. |
| Example        |                                                           |
| Ontology Class |                                                           |
| Badge          |                                                           |
| Card.          | [0..1]                                                    |


### Resource - spatial (location)
|                |                                                   |
|----------------|---------------------------------------------------|
| Key            | location                                          |
| Description    | An object that describes a specific location.     |
| Example        |                                                   |
| Ontology Class | [dct:location](http://purl.org/dc/terms/Location) |
| Badge          |                                                   |
| Card.          | [0..1]                                            |


### Resource - spatial (location - address)
|                |                                                                                                                   |
|----------------|-------------------------------------------------------------------------------------------------------------------|
| Key            | address                                                                                                           |
| Description    | An address of the location of the data. May be specified with street name, house number, zip code, and city name. |
| Example        | Rudower Chaussee 12, 12489 Berlin                                                                                 |
| Ontology Class | [schema:address](https://schema.org/address)                                                                      |
| Badge          | Silver                                                                                                            |
| Card.          | [0..1]                                                                                                            |


### Resource - spatial (location - @id)
|                |                                                                             |
|----------------|-----------------------------------------------------------------------------|
| Key            | @id                                                                         |
| Description    | A path or URI to a specific location. It can use Wikidata or OpenStreetMap. |
| Example        | [www.wikidata.org/wiki/Q77077223](https://www.wikidata.org/wiki/Q77077223)  |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)                       |
| Badge          | Platinum                                                                    |
| Card.          | [0..1]                                                                      |


### Resource - spatial (location - latitude)
|                |                                                 |
|----------------|-------------------------------------------------|
| Key            | latitude                                        |
| Description    | The latitude (lat) information of the location. |
| Example        | 52.432822                                       |
| Ontology Class | [schema:latitude](https://schema.org/latitude)  |
| Badge          | Gold                                            |
| Card.          | [0..1]                                          |


### Resource - spatial (location - longitude)
|                |                                                  |
|----------------|--------------------------------------------------|
| Key            | longitude                                        |
| Description    | The longitude (lon) information of the location. |
| Example        | 13.5351004                                       |
| Ontology Class | [schema:longitude](https://schema.org/longitude) |
| Badge          | Gold                                             |
| Card.          | [0..1]                                           |


### Resource - spatial (extent)
|                |                                                                  |
|----------------|------------------------------------------------------------------|
| Key            | extent                                                           |
| Description    | An object that describes a covered area or region.               |
| Example        |                                                                  |
| Ontology Class | [oeo:spatial region](http://purl.obolibrary.org/obo/BFO_0000006) |
| Badge          |                                                                  |
| Card.          | [0..1]                                                           |


### Resource - spatial (extent - name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | The name of the region.                                    |
| Example        | Berlin                                                     |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Silver                                                     |
| Card.          | [0..1]                                                     |


### Resource - spatial (extent - @id)
|                |                                                                |
|----------------|----------------------------------------------------------------|
| Key            | @id                                                            |
| Description    | A URI reference for the region.                                |
| Example        | [www.wikidata.org/wiki/Q64](https://www.wikidata.org/wiki/Q64) |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)          |
| Badge          | Platinum                                                       |
| Card.          | [0..1]                                                         |


### Resource - spatial (extent - resolutionValue)
|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| Key            | resolutionValue                                                                       |
| Description    | The value of the spatial resolution.                                                  |
| Example        | 100                                                                                   |
| Ontology Class | [dcat:spatialResolutionInMeters](http://www.w3.org/ns/dcat#spatialResolutionInMeters) |
| Badge          | Silver                                                                                |
| Card.          | [0..1]                                                                                |


### Resource - spatial (extent - resolutionUnit)
|                |                                                                     |
|----------------|---------------------------------------------------------------------|
| Key            | resolutionUnit                                                      |
| Description    | The unit of the spatial resolution.                                 |
| Example        | m                                                                   |
| Ontology Class | [oeo:unit](http://openenergyplatform.org/ontology/oeo/OEO_00010489) |
| Badge          | Silver                                                              |
| Card.          | [0..1]                                                              |


### Resource - spatial (extent - boundingBox)
|                |                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|
| Key            | boundingBox                                                                                                                   |
| Description    | The covered area specified by the coordinates of a bounding box. The format is [minLon, minLat, maxLon, maxLat] or [W,S,E,N]. |
| Example        | [13.08825, 52.33859, 13.76104, 52.6754]                                                                                       |
| Ontology Class | [dcat:bbox](http://www.w3.org/ns/dcat#bbox)                                                                                   |
| Badge          | Gold                                                                                                                          |
| Card.          | [*]                                                                                                                           |


### Resource - spatial (extent - crs)
|                |                                                                                                                                          |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | crs                                                                                                                                      |
| Description    | The Coordinate Reference System, specified as an EPSG code.                                                                              |
| Example        | EPSG:4326                                                                                                                                |
| Ontology Class | [cco:Geospatial Coordinate Reference System](http://www.ontologyrepository.com/CommonCoreOntologies/GeospatialCoordinateReferenceSystem) |
| Badge          | Gold                                                                                                                                     |
| Card.          | [0..1]                                                                                                                                   |

### Resource - temporal
|                |                                                                                                                                                             |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | temporal                                                                                                                                                    |
| Description    | An object with the time period covered in the data. Temporal information should contain a "referenceDate" or the keys that describe a time series, or both. |
| Example        |                                                                                                                                                             |
| Ontology Class | [schema:temporalCoverage](https://schema.org/temporalCoverage)                                                                                              |
| Badge          |                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                      |


### Resource - temporal (referenceDate)
|                |                                                                                                     |
|----------------|-----------------------------------------------------------------------------------------------------|
| Key            | referenceDate                                                                                       |
| Description    | A base year, month or day. The time for which the data should be accurate. Date Format is ISO 8601. |
| Example        | 2020-01-01                                                                                          |
| Ontology Class | [dct:date](http://purl.org/dc/terms/date)                                                           |
| Badge          | Silver                                                                                              |
| Card.          | [0..1]                                                                                              |


### Resource - temporal (timeseries)
|                |                                                           |
|----------------|-----------------------------------------------------------|
| Key            | timeseries                                                |
| Description    | An array that describes the timeseries.                   |
| Example        |                                                           |
| Ontology Class | [dct:PeriodOfTime](http://purl.org/dc/terms/PeriodOfTime) |
| Badge          |                                                           |
| Card.          | [*]                                                       |


### Resource - temporal (timeseries - start)
|                |                                                                 |
|----------------|-----------------------------------------------------------------|
| Key            | start                                                           |
| Description    | The start time of a time series.                                |
| Example        | 2020-01-01T00:00:00+00:00                                       |
| Ontology Class | [dbo:startDateTime](https://dbpedia.org/ontology/startDateTime) |
| Badge          | Silver                                                          |
| Card.          | [0..1]                                                          |


### Resource - temporal (timeseries - end)
|                |                                                             |
|----------------|-------------------------------------------------------------|
| Key            | end                                                         |
| Description    | The temporal end point of a time series.                    |
| Example        | 2020-01-01T23:59:30+00:00                                   |
| Ontology Class | [dbo:endDateTime](https://dbpedia.org/ontology/endDateTime) |
| Badge          | Silver                                                      |
| Card.          | [0..1]                                                      |


### Resource - temporal (timeseries - resolutionValue)
|                |                                                                                                    |
|----------------|----------------------------------------------------------------------------------------------------|
| Key            | resolutionValue                                                                                    |
| Description    | The time span between individual information points in a time series. The value of the resolution. |
| Example        | 30 s                                                                                               |
| Ontology Class | [dcat:spatialResolutionInMeters](http://www.w3.org/ns/dcat#spatialResolutionInMeters)              |
| Badge          | Silver                                                                                             |
| Card.          | [0..1]                                                                                             |


### Resource - temporal (timeseries - resolutionUnit)
|                |                                                                     |
|----------------|---------------------------------------------------------------------|
| Key            | resolutionUnit                                                      |
| Description    | The unit of the temporal resolution.                                |
| Example        | 30 s                                                                |
| Ontology Class | [oeo:unit](http://openenergyplatform.org/ontology/oeo/OEO_00010489) |
| Badge          | Silver                                                              |
| Card.          | [0..1]                                                              |


### Resource - temporal (timeseries - alignment)
|                |                                                                                              |
|----------------|----------------------------------------------------------------------------------------------|
| Key            | alignment                                                                                    |
| Description    | An indicator of whether timestamps in a time series are to the left, right or in the centre. |
| Example        | left                                                                                         |
| Ontology Class | [oeo:time stamp alignment](http://openenergyplatform.org/ontology/oeo/OEO_00140044)          |
| Badge          | Silver                                                                                       |
| Card.          | [0..1]                                                                                       |


### Resource - temporal (timeseries - aggregationType)
|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| Key            | aggregationType                                                                   |
| Description    | An indicator of whether the values are a sum, an average or a current value.      |
| Example        | current                                                                           |
| Ontology Class | [oeo:aggregation type](https://openenergyplatform.org/ontology/oeo/OEO_00140068/) |
| Badge          | Silver                                                                            |
| Card.          | [0..1]                                                                            |

### Resource - sources
|                |                                                                                    |
|----------------|------------------------------------------------------------------------------------|
| Key            | sources                                                                            |
| Description    | An array of objects with the used and underlying sources of the data and metadata. |
| Example        |                                                                                    |
| Ontology Class | [dct:source](http://purl.org/dc/terms/source)                                      |
| Badge          |                                                                                    |
| Card.          | [*]                                                                                |


### Resource - sources (title)
|                |                                                                              |
|----------------|------------------------------------------------------------------------------|
| Key            | title                                                                        |
| Description    | A human readable title of the source, a document title or organisation name. |
| Example        | IPCC Sixth Assessment Report (AR6) - Climate Change 2023 - Synthesis Report  |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title)                                  |
| Badge          | Bronze                                                                       |
| Card.          | [0..1]                                                                       |


### Resource - sources (authors)
|                |                                                                         |
|----------------|-------------------------------------------------------------------------|
| Key            | authors                                                                 |
| Description    | An array of the full names of the authors of the source material.       |
| Example        | Hoesung Lee, José Romero, The Core Writing Team                         |
| Ontology Class | [oeo:author](https://openenergyplatform.org/ontology/oeo/OEO_00000064/) |
| Badge          | Bronze                                                                  |
| Card.          | [*]                                                                     |


### Resource - sources (description)
|                |                                                           |
|----------------|-----------------------------------------------------------|
| Key            | description                                               |
| Description    | A free text description of the source.                    |
| Example        | A Report of the Intergovernmental Panel on Climate Change |
| Ontology Class | [dct:description](http://purl.org/dc/terms/description)   |
| Badge          | Bronze                                                    |
| Card.          | [0..1]                                                    |


### Resource - sources (publicationYear)
|                |                                                 |
|----------------|-------------------------------------------------|
| Key            | publicationYear                                 |
| Description    | Indicates the year when the work was published. |
| Example        | 2023                                            |
| Ontology Class | [dct:issued](http://purl.org/dc/terms/issued)   |
| Badge          | Bronze                                          |
| Card.          | [0..1]                                          |


### Resource - sources (path)
|                |                                                                                                                |
|----------------|----------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                           |
| Description    | A DOI or link to the original source.                                                                          |
| Example        | [IPCC_AR6_SYR_FullVolume.pdf](https://www.ipcc.ch/report/ar6/syr/downloads/report/IPCC_AR6_SYR_FullVolume.pdf) |
| Ontology Class | [sc:url](https://schema.org/url)                                                                               |
| Badge          | Bronze                                                                                                         |
| Card.          | [0..1]                                                                                                         |


### Resource - sourceLicenses
|                |                                                                                                                                                                                                               |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | sourceLicenses                                                                                                                                                                                                |
| Description    | An array of objects of licenses under which the described source is provided. See [academy/courses/08_licensing](https://openenergyplatform.github.io/academy/courses/08_licensing/) for further information. |
| Example        |                                                                                                                                                                                                               |
| Ontology Class | [dct:license](http://purl.org/dc/terms/license)                                                                                                                                                               |
| Badge          |                                                                                                                                                                                                               |
| Card.          | [*]                                                                                                                                                                                                           |


### Resource - sourceLicenses (name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | The [SPDX](https://spdx.org/licenses/) identifier.         |
| Example        | ODbL-1.0                                                   |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Bronze                                                     |
| Card.          | [0..1]                                                     |


### Resource - sourceLicenses (title)
|                |                                                     |
|----------------|-----------------------------------------------------|
| Key            | title                                               |
| Description    | The official (human-readable) title of the license. |
| Example        | Open Data Commons Open Database License 1.0         |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title)         |
| Badge          | Bronze                                              |
| Card.          | [0..1]                                              |


### Resource - sourceLicenses (path)
|                |                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                         |
| Description    | A link or path to the license text.                                                                          |
| Example        | [opendatacommons.org/licenses/odbl/1-0/index.html](https://opendatacommons.org/licenses/odbl/1-0/index.html) |
| Ontology Class | [sc:url](https://schema.org/url)                                                                             |
| Badge          | Bronze                                                                                                       |
| Card.          | [0..1]                                                                                                       |


### Resource - sourceLicenses (instruction)
|                |                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | instruction                                                                                                                                                                                                        |
| Description    | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.                                                                                                     |
| Example        | You are free to share and change, but you must attribute, and share derivations under the same license. See [tldrlegal.com](https://tldrlegal.com/license/odc-open-database-license-odbl) for further information. |
| Ontology Class | [rdfs:comment](https://www.w3.org/2000/01/rdf-schema#comment)                                                                                                                                                      |
| Badge          | Bronze                                                                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                                                                             |


### Resource - sourceLicenses (attribution)
|                |                                                                                         |
|----------------|-----------------------------------------------------------------------------------------|
| Key            | attribution                                                                             |
| Description    | A copyright owner of the **source**. Must be provided if attribution licenses are used. |
| Example        | © Intergovernmental Panel on Climate Change 2023                                        |
| Ontology Class | [ms:copyright notice](http://purl.obolibrary.org/obo/MS_1003198)                        |
| Badge          | Bronze                                                                                  |
| Card.          | [0..1]                                                                                  |


### Resource - sourceLicenses (copyrightStatement)
|                |                                                                                                                               |
|----------------|-------------------------------------------------------------------------------------------------------------------------------|
| Key            | copyrightStatement                                                                                                            |
| Description    | A link or path that proves that the source or data has the appropriate license. This can be a page number or website imprint. |
| Example        | [www.ipcc.ch/copyright](https://www.ipcc.ch/copyright/)                                                                       |
| Ontology Class | [dct:rights](http://purl.org/dc/terms/rights)                                                                                 |
| Badge          | Bronze                                                                                                                        |
| Card.          | [0..1]                                                                                                                        |

### Resource - licenses
|                |                                                                             |
|----------------|-----------------------------------------------------------------------------|
| Key            | licenses                                                                    |
| Description    | An array of objects of licenses under which the described data is provided. |
| Example        |                                                                             |
| Ontology Class | [dct:license](http://purl.org/dc/terms/license)                             |
| Badge          |                                                                             |
| Card.          | [*]                                                                         |


### Resource - licenses (name)
|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | name                                                       |
| Description    | The [SPDX](https://spdx.org/licenses/) identifier.         |
| Example        | ODbL-1.0                                                   |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Bronze                                                     |
| Card.          | [0..1]                                                     |


### Resource - licenses (title)
|                |                                                     |
|----------------|-----------------------------------------------------|
| Key            | title                                               |
| Description    | The official (human-readable) title of the license. |
| Example        | Open Data Commons Open Database License 1.0         |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title)         |
| Badge          | Bronze                                              |
| Card.          | [0..1]                                              |


### Resource - licenses (path)
|                |                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                         |
| Description    | A link or path to the license text.                                                                          |
| Example        | [opendatacommons.org/licenses/odbl/1-0/index.html](https://opendatacommons.org/licenses/odbl/1-0/index.html) |
| Ontology Class | [dcat:accessURL](https://www.w3.org/ns/dcat#accessURL)                                                       |
| Badge          | Bronze                                                                                                       |
| Card.          | [0..1]                                                                                                       |


### Resource - licenses (instruction)
|                |                                                                                                                                                                                                                    |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | instruction                                                                                                                                                                                                        |
| Description    | A short description of rights and obligations. The use of [tl;drLegal](https://tldrlegal.com/) is recommended.                                                                                                     |
| Example        | You are free to share and change, but you must attribute, and share derivations under the same license. See [tldrlegal.com](https://tldrlegal.com/license/odc-open-database-license-odbl) for further information. |
| Ontology Class | [dc:rights](http://purl.org/dc/elements/1.1/rights)                                                                                                                                                                |
| Badge          | Bronze                                                                                                                                                                                                             |
| Card.          | [0..1]                                                                                                                                                                                                             |


### Resource - licenses (attribution)
|                |                                                                                       |
|----------------|---------------------------------------------------------------------------------------|
| Key            | attribution                                                                           |
| Description    | A copyright owner of the **data**. Must be provided if attribution licenses are used. |
| Example        | © Reiner Lemoine Institut                                                             |
| Ontology Class | [spdx:attributionText](http://spdx.org/rdf/terms#attributionText)                     |
| Badge          | Bronze                                                                                |
| Card.          | [0..1]                                                                                |


### Resource - licenses (copyrightStatement)
|                |                                                                                                                     |
|----------------|---------------------------------------------------------------------------------------------------------------------|
| Key            | copyrightStatement                                                                                                  |
| Description    | A link or path that proves that the data has the appropriate license. This can be a page number or website imprint. |
| Example        | [www.ipcc.ch/copyright/](https://www.ipcc.ch/copyright/)                                                            |
| Ontology Class | [dct:rights](http://purl.org/dc/terms/rights)                                                                       |
| Badge          | Bronze                                                                                                              |
| Card.          | [0..1]                                                                                                              |

### Resource - Provenance Keys
|                |                                                                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | contributors                                                                                                                                                    |
| Description    | An array of objects of the people or organizations who contributed to the data or metadata. Should have "Date of data creation" and "Date of metadata creation" |
| Example        |                                                                                                                                                                 |
| Ontology Class | [foaf:Agent](http://xmlns.com/foaf/0.1/Agent)                                                                                                                   |
| Badge          |                                                                                                                                                                 |
| Card.          | [*]                                                                                                                                                             |


### Resource - Provenance Keys (title)
|                |                                             |
|----------------|---------------------------------------------|
| Key            | title                                       |
| Description    | A full name of the contributor.             |
| Example        | Ludwig Hülk                                 |
| Ontology Class | [dct:title](http://purl.org/dc/terms/title) |
| Badge          | Bronze                                      |
| Card.          | [0..1]                                      |


### Resource - Provenance Keys (path)
|                |                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------|
| Key            | path                                                                                                                       |
| Description    | A qualified link or path pointing to a relevant location online for the contributor. This can be the GitHub page or ORCID. |
| Example        | https://github.com/Ludee                                                                                                   |
| Ontology Class | [sc:url](https://schema.org/url)                                                                                           |
| Badge          | Bronze                                                                                                                     |
| Card.          | [0..1]                                                                                                                     |


### Resource - Provenance Keys (organization)
|                |                                                                                                                 |
|----------------|-----------------------------------------------------------------------------------------------------------------|
| Key            | organization                                                                                                    |
| Description    | A string describing the organization this contributor is affiliated to. This can be relevant for the copyright. |
| Example        | Reiner Lemoine Institut                                                                                         |
| Ontology Class | [oeo:organisation](https://openenergyplatform.org/ontology/oeo/OEO_00030022/)                                   |
| Badge          | Bronze                                                                                                          |
| Card.          | [0..1]                                                                                                          |


### Resource - Provenance Keys (roles)
|                |                                                                                                                                                                                                                                                                                    |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | roles                                                                                                                                                                                                                                                                              |
| Description    | An array describing the roles of the contributor. A role is recommended to follow the established vocabulary: [DataCite Metadata Schema’s contributorRole](https://support.datacite.org/docs/datacite-metadata-schema-v44-recommended-and-optional-properties#7a-contributortype). |
| Example        | DataCollector, DataCurator                                                                                                                                                                                                                                                         |
| Ontology Class | [oeo:role](https://openenergyplatform.org/ontology/oeo/BFO_0000023/)                                                                                                                                                                                                               |
| Badge          | Bronze                                                                                                                                                                                                                                                                             |
| Card.          | [*]                                                                                                                                                                                                                                                                                |


### Resource - Provenance Keys (date)
|                |                                                        |
|----------------|--------------------------------------------------------|
| Key            | date                                                   |
| Description    | The date of the contribution. Date Format is ISO 8601. |
| Example        | 2024-10-21                                             |
| Ontology Class | [dct:issued](http://purl.org/dc/terms/issued)          |
| Badge          | Bronze                                                 |
| Card.          | [0..1]                                                 |


### Resource - Provenance Keys (object)
|                |                                                                                                 |
|----------------|-------------------------------------------------------------------------------------------------|
| Key            | object                                                                                          |
| Description    | The target of the contribution. This can be the data, the metadata or both (data and metadata). |
| Example        | data and metadata                                                                               |
| Ontology Class | [dct:type](http://purl.org/dc/terms/type)                                                       |
| Badge          | Bronze                                                                                          |
| Card.          | [0..1]                                                                                          |


### Resource - Provenance Keys (comment)
|                |                                                               |
|----------------|---------------------------------------------------------------|
| Key            | comment                                                       |
| Description    | A free-text commentary on what has been done.                 |
| Example        | Add general context.                                          |
| Ontology Class | [rdfs:comment](https://www.w3.org/2000/01/rdf-schema#comment) |
| Badge          | Bronze                                                        |
| Card.          | [0..1]                                                        |

### Resource - Type Keys

| Key            | type                                                                                                   |
|----------------|--------------------------------------------------------------------------------------------------------|
| Description    | The 'table' type indicates that the resource is tabular as per 'Frictionless Tabular Data' definition. |
| Example        | table                                                                                                  |
| Ontology Class | [csvw:datatype](https://www.w3.org/ns/csvw#datatype)                                                   |
| Badge          | Gold                                                                                                   |
| Card.          | [0..1]                                                                                                 |


| Key            | format                                                                                                                          |
|----------------|---------------------------------------------------------------------------------------------------------------------------------|
| Description    | A file extension format. Possible options are 'csv', 'xlsx', 'json', 'PostgreSQL', 'SQLite' and other standard file extensions. |
| Example        | PostgreSQL                                                                                                                      |
| Ontology Class | [dct:format](http://purl.org/dc/terms/format)                                                                                   |
| Badge          | Gold                                                                                                                            |
| Card.          | [0..1]                                                                                                                          |


| Key            | encoding                                                                                                                                      |
|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------|
| Description    | Specifies the character encoding of the resource's data file. The default is 'UTF-8'. The values should be one of the 'Preferred MIME Names'. |
| Example        | UTF-8                                                                                                                                         |
| Ontology Class | [csvw:encoding](http://www.w3.org/ns/csvw#encoding)                                                                                           |
| Badge          | Gold                                                                                                                                          |
| Card.          | [0..1]                                                                                                                                        |

### Resource - Fields Keys

|                |                                                                                                                                              |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **schema**                                                                                                                                   |
| Description    | An object that describes the structure of a table. It contains all fields (columns of the table), the primary key and optional foreign keys. |
| Example        |                                                                                                                                              |
| Ontology Class | [schema:table](https://schema.org/Table)                                                                                                     |
| Badge          |                                                                                                                                              |
| Card.          | [1]                                                                                                                                          |


### Resource - Fields Keys - fields

|                |                                                                                   |
|----------------|-----------------------------------------------------------------------------------|
| Key            | **fields**                                                                        |
| Description    | An array of objects that describes a field (column) and its detailed information. |
| Example        |                                                                                   |
| Ontology Class | [csvw:column](http://www.w3.org/ns/csvw#column)                                   |
| Badge          |                                                                                   |
| Card.          | [1]                                                                               |


### Resource - Fields Keys - name

|                |                                                                                                                                                         |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **name**                                                                                                                                                |
| Description    | The name of the field. The name may only consist of lowercase alphanumeric characters or underscores. It must not begin with a number or an underscore. |
| Example        | year                                                                                                                                                    |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label)                                                                                              |
| Badge          | Iron                                                                                                                                                    |
| Card.          | [1]                                                                                                                                                     |


### Resource - Fields Keys - description

|                |                                                         |
|----------------|---------------------------------------------------------|
| Key            | **description**                                         |
| Description    | A text describing the field.                            |
| Example        | Reference year for which the data were collected.       |
| Ontology Class | [dct:description](http://purl.org/dc/terms/description) |
| Badge          | Silver                                                  |
| Card.          | [0..1]                                                  |


### Resource - Fields Keys - type

|                |                                                                                                      |
|----------------|------------------------------------------------------------------------------------------------------|
| Key            | **type**                                                                                             |
| Description    | The data type of the field. In case of a geom column in a database, also indicate the shape and CRS. |
| Example        | geometry(Point, 4326)                                                                                |
| Ontology Class | [csvw:datatype](https://www.w3.org/ns/csvw#datatype)                                                 |
| Badge          | Iron                                                                                                 |
| Card.          | [1]                                                                                                  |


### Resource - Fields Keys - nullable

|                |                                                                                    |
|----------------|------------------------------------------------------------------------------------|
| Key            | **nullable**                                                                       |
| Description    | A boolean key to specify that a column can be nullable. True is the default value. |
| Example        | True                                                                               |
| Ontology Class | [ncit:null](http://purl.obolibrary.org/obo/NCIT_C47840)                            |
| Badge          | Iron                                                                               |
| Card.          | [1]                                                                                |


### Resource - Fields Keys - unit

|                |                                                                                                                                                                                     |
|----------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **unit**                                                                                                                                                                            |
| Description    | The unit of a field. If it does not apply, use 'null'. If the unit is given in a separate field, reference this field (e.g. 'unit'). Use a space between numbers and units (100 m). |
| Example        | MW                                                                                                                                                                                  |
| Ontology Class | [oeo:has unit](https://openenergyplatform.org/ontology/oeo/OEO_00040010/)                                                                                                           |
| Badge          | Silver                                                                                                                                                                              |
| Card.          | [0..1]                                                                                                                                                                              |


### Resource - Fields Keys - isAbout

|                |                                                                 |
|----------------|-----------------------------------------------------------------|
| Key            | **isAbout**                                                     |
| Description    | An array of objects that describes the field in ontology terms. |
| Example        |                                                                 |
| Ontology Class | [sc:about](https://schema.org/about)                            |
| Badge          |                                                                 |
| Card.          | [*]                                                             |


### Resource - Fields Keys - name (isAbout)

|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | **name**                                                   |
| Description    | The class label of the ontology term.                      |
| Example        | wind energy converting unit                                |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Platinum                                                   |
| Card.          | [0..1]                                                     |


### Resource - Fields Keys - @id (isAbout)

|                |                                                                          |
|----------------|--------------------------------------------------------------------------|
| Key            | **@id**                                                                  |
| Description    | The path of the ontology term (IRI).                                     |
| Example        | [OEO_00000044](https://openenergyplatform.org/ontology/oeo/OEO_00000044) |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)                    |
| Badge          | Platinum                                                                 |
| Card.          | [0..1]                                                                   |


### Resource - Fields Keys - valueReference

|                |                                                                                                |
|----------------|------------------------------------------------------------------------------------------------|
| Key            | **valueReference**                                                                             |
| Description    | An array of objects for an extended description of the values in the column in ontology terms. |
| Example        |                                                                                                |
| Ontology Class | [prov:value](https://www.w3.org/ns/prov#value)                                                 |
| Badge          |                                                                                                |
| Card.          | [*]                                                                                            |


### Resource - Fields Keys - value

|                |                                                                |
|----------------|----------------------------------------------------------------|
| Key            | **value**                                                      |
| Description    | The name of the value in the column.                           |
| Example        | onshore                                                        |
| Ontology Class | [rdf:value](https://www.w3.org/1999/02/22-rdf-syntax-ns#value) |
| Badge          | Platinum                                                       |
| Card.          | [0..1]                                                         |


### Resource - Fields Keys - name (valueReference)

|                |                                                            |
|----------------|------------------------------------------------------------|
| Key            | **name**                                                   |
| Description    | The class label of the ontology term in the column.        |
| Example        | onshore wind farm                                          |
| Ontology Class | [rdfs:label](https://www.w3.org/2000/01/rdf-schema#/label) |
| Badge          | Platinum                                                   |
| Card.          | [0..1]                                                     |


### Resource - Fields Keys - @id (valueReference)

|                |                                                                          |
|----------------|--------------------------------------------------------------------------|
| Key            | **@id**                                                                  |
| Description    | The path of the ontology term (IRI) in the column.                       |
| Example        | [OEO_00000311](https://openenergyplatform.org/ontology/oeo/OEO_00000311) |
| Ontology Class | [dct:identifier](http://purl.org/dc/terms/identifier)                    |
| Badge          | Platinum                                                                 |
| Card.          | [0..1]                                                                   |

### Resource - Properties Keys

|                |                                                                                                          |
|----------------|----------------------------------------------------------------------------------------------------------|
| Key            | **primaryKey**                                                                                           |
| Description    | An array of fields that uniquely identifies each row in the table. The default value is the “id” column. |
| Example        | id                                                                                                       |
| Ontology Class | [csvw:primaryKey](https://www.w3.org/ns/csvw#primaryKey)                                                 |
| Badge          | Iron                                                                                                     |
| Card.          | [1..*]                                                                                                   |


### Resource - Properties Keys - foreignKeys

|                |                                                                                                       |
|----------------|-------------------------------------------------------------------------------------------------------|
| Key            | **foreignKeys**                                                                                       |
| Description    | An array of objects with foreign keys that describe a field that relates to a field in another table. |
| Example        |                                                                                                       |
| Ontology Class | [csvw:foreignKey](https://www.w3.org/ns/csvw#foreignKey)                                              |
| Badge          |                                                                                                       |
| Card.          | [*]                                                                                                   |


### Resource - Properties Keys - fields (foreignKeys)

|                |                                                                         |
|----------------|-------------------------------------------------------------------------|
| Key            | **fields**                                                              |
| Description    | An array of fields in the table that is constrained by the foreign key. |
| Example        | id, version                                                             |
| Ontology Class | [ex:nestedFields](http://example.org/nestedFields)                      |
| Badge          | Iron                                                                    |
| Card.          | [*]                                                                     |


### Resource - Properties Keys - reference

|                |                                     |
|----------------|-------------------------------------|
| Key            | **reference**                       |
| Description    | The reference to the foreign table. |
| Example        |                                     |
| Ontology Class |                                     |
| Badge          |                                     |
| Card.          | [0..1]                              |


### Resource - Properties Keys - resource (reference)

|                |                                                    |
|----------------|----------------------------------------------------|
| Key            | **resource**                                       |
| Description    | The referenced foreign table.                      |
| Example        | model_draft.oep_oemetadata_table_example_version   |
| Ontology Class | [dcat:Dataset](https://www.w3.org/ns/dcat#dataset) |
| Badge          | Iron                                               |
| Card.          | [0..1]                                             |


### Resource - Properties Keys - fields (reference)

|                |                                                 |
|----------------|-------------------------------------------------|
| Key            | **fields**                                      |
| Description    | The foreign resource column.                    |
| Example        | id, version                                     |
| Ontology Class | [csvw:column](http://www.w3.org/ns/csvw#column) |
| Badge          | Iron                                            |
| Card.          | [*]                                             |


### Resource - Properties Keys - dialect

|                |                                                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **dialect**                                                                                                                                                                |
| Description    | The Dialect defines a simple format for describing the various dialects of CSV files in a language-independent manner. In a database, the values in the fields are 'null'. |
| Example        |                                                                                                                                                                            |
| Ontology Class |                                                                                                                                                                            |
| Badge          |                                                                                                                                                                            |
| Card.          | [1]                                                                                                                                                                        |


### Resource - Properties Keys - delimiter

|                |                                                                                                                                                                        |
|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **delimiter**                                                                                                                                                          |
| Description    | The delimiter specifies the character sequence which should separate fields (columns). Common characters are ',' (comma), ';' (semicolon), '.' (point) and '\t' (tab). |
| Example        | ,                                                                                                                                                                      |
| Ontology Class | [csvw:delimiter](http://www.w3.org/ns/csvw#delimiter)                                                                                                                  |
| Badge          | Iron                                                                                                                                                                   |
| Card.          | [1]                                                                                                                                                                    |


### Resource - Properties Keys - decimalSeparator

|                |                                                                                                                                                                            |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **decimalSeparator**                                                                                                                                                       |
| Description    | The symbol used to separate the integer part from the fractional part of a number written in decimal form. Depending on language and region this symbol can be '.' or ','. |
| Example        | .                                                                                                                                                                          |
| Ontology Class | [csvw:decimalChar](http://www.w3.org/ns/csvw#decimalChar)                                                                                                                  |
| Badge          | Iron                                                                                                                                                                       |
| Card.          | [1]                                                                                                                                                                        |

### Resource - Review Keys

|                |                                                                                                                                                                                                              |
|----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Key            | **review**                                                                                                                                                                                                   |
| Description    | The metadata on the OEP can go through an open peer review process. See the Academy course [Open Peer Review](https://openenergyplatform.github.io/academy/courses/09_peer_review/) for further information. |
| Example        |                                                                                                                                                                                                              |
| Ontology Class |                                                                                                                                                                                                              |
| Badge          | [0..1]                                                                                                                                                                                                       |


### Resource - Review Keys - path

|                |                                                                                                                      |
|----------------|----------------------------------------------------------------------------------------------------------------------|
| Key            | **path**                                                                                                             |
| Description    | A link or path to the documented open peer review.                                                                   |
| Example        | [open_peer_review/9](https://openenergyplatform.org/dataedit/view/model_draft/oep_table_example/open_peer_review/9/) |
| Ontology Class | [sc:url](https://schema.org/url)                                                                                     |
| Badge          | [0..1]                                                                                                               |


### Resource - Review Keys - badge

|                |                                                                                                        |
|----------------|--------------------------------------------------------------------------------------------------------|
| Key            | **badge**                                                                                              |
| Description    | A badge of either Iron, Bronze, Silver, Gold or Platinum is used to label the quality of the metadata. |
| Example        | Platinum                                                                                               |
| Ontology Class | [oeo:quality control flag](https://openenergyplatform.org/ontology/oeo/OEO_00140098/)                  |
| Badge          | [0..1]                                                                                                 |

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
