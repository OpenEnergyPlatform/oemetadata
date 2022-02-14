# OEMetadata - Key Description

This pages describes the key of **OEMetadata version 1.5.1.** <br>
You can have a look at an empty [template](https://github.com/OpenEnergyPlatform/metadata/blob/master/metadata/v151/template.json) and a filled out [example](https://github.com/OpenEnergyPlatform/metadata/blob/master/metadata/v151/example.json) of the metadata string.


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
    {"key":
        {"key":"value"},
        {"key":"value"}}
    ```
* array of objects {nested array}:
    ```JSON
    {"key": [
        {"key":"value"},
        {"key":"value"}]}
    ```


## Metadata keys with a description and example


### General Keys
|#|Key |Description |Example |
|---|---|---|---|
| 1 | name | A file name or database table name. | oep_metadata_table_example_v15 |
| 2 | title | A human readable full title including author. | RLI - OEMetadata - Metadata example table |
| 3 | id | An Uniform Resource Identifier (URI) that unambiguously identifies the resource. This can be a URL on the data set. It can also be a Digital Object Identifier (DOI). | https://example.com |
| 4 | description | A description or abstract of the package. It should be usable as summary information for the entire package that is described by the metadata. | Example table used to illustrate the metadata structure and meaning. |
| 5 | language | An array of languages used within the described data structures (e.g. titles, descriptions). The language key can be repeated if more languages are used. Standard: IETF (BCP47) | en-GB, de-DE, fr-FR |
| 6 | subject | An array of topics of the data in OEO terms. |
| 6.1 | name | An class label of the OEO terms. | energy |
| 6.2 | path | A URI of the class. | https://openenergy-platform.org/ontology/oeo/OEO_00000150 |
| 7 | keywords | An array of keywords to assist users searching for the package in catalogs. | example, template, test |
| 8 | publicationDate | A date of publishing of the data or metadata. Date format is ISO 8601 (YYYY-MM-DD). | 2019-02-06 |

### Context Keys
|#|Key |Description |Example |
|---|---|---|---|
| 9 | context | An object that describes the general setting, environment, or project leading to the creation or maintenance of this dataset. In science this is can be the research project. | |
| 9.1 | homepage | A URL of the project | https://openenergy-platform.org/ | 
| 9.2 | documentation | A URL of the project documentation. | https://openenergy-platform.org/about/ | 
| 9.3 | sourceCode | A URL of the projects source code. | https://github.com/OpenEnergyPlatform | 
| 9.4 | contact | A reference to the creator or maintainer of the data set. Can be an email address or a GitHub handle. | contact@example.com | 
| 9.5 | grantNo | An identifying grant number. In the case of a publicly funded project, this number is assigned by the funding agency. | 01AB2345 | 
| 9.6 | fundingAgency | A name of the entity providing the funding. This can be a government agency or a company. | Bundesministerium für Wirtschaft und Klimaschutz | 
| 9.7 | fundingAgencyLogo | A URL to the logo or image of the funding agency. | https://commons.wikimedia.org/wiki/File:BMWi_Logo_2021.svg#/media/File:BMWi_Logo_2021.svg | 
| 9.8 | publisherLogo | A URL to the logo of the publishing agency of data. | https://reiner-lemoine-institut.de//wp-content/uploads/2015/09/rlilogo.png | 

### Spatial and Temporal Keys
|#|Key |Description |Example |
|---|---|---|---|
| 10 | spatial | An object that describing the spatial context of the contained data. | |
| 10.1 | location | A location of the data. In the case of data where the location can be described as a point. May come as coordinates, URI or addresses with street, house number and zip code | 52.433509, 13.535855 |
| 10.2 | extent | A covered area. May be the name of a region, or the geometry of a bounding box. | Europe |
| 10.3 | resolution | Pixel size in case of a regular raster image. Reference to administrative level or other spatial division that is present as the smallest spatially distinguished unit size. | 1 ha |
| 11 | temporal | An object with the time period covered in the data. Temporal information should either contain a "referenceDate" or the keys describing a time series; in rare cases both. | |
| 11.1 | referenceDate | The base year, month or day. Point in time for which the data is meant to be accurate. The census data or a satellite image will have a reference date. Date Format is ISO 8601. | 2016-01-01 |
| 11.2 | timeseries | An array that describes the timeseries. ||
| 11.2.1 | start | The beginning point in time of a time series. |  2019-02-06T10:12:04+00:00 |
| 11.2.2 | end | The end point in time of a time series. | 2019-02-07T10:12:04+00:00 |
| 11.2.3 | resolution | The time span between individual points of information in a time series. | 30 s |
| 11.2.4 | alignment | An indicator whether stamps in a time series are left, right or middle.  | left |
| 11.2.5 | aggregationType | Indicates whether the values are a sum, average or current. | sum |

### Source Keys
|#|Key |Description |Example |
|---|---|---|---|
| 12 | sources | An array of objects with the used and underlying sources of the data and metadata. | |
| 12.1 | title | A human readable title of the source, a document title or organisation name. | IPCC Fifth Assessment Report |
| 12.2 | description | A free text description of the data set. | Scientific climate change report by the UN |
| 12.3 | path | A URL to the original source | https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_full.pdf |
| 12.4 | licenses | An array of objects under which the source is provided. | |
| 12.4.1 | name | The [SPDX](https://spdx.org/licenses/) identifier. | ODbL-1.0 |
| 12.4.2 | title | An official (human readable) title of the license. | Open Data Commons Open Database License 1.0 |
| 12.4.3 | path | A link to the license text. | https://opendatacommons.org/licenses/odbl/1-0/index.html |
| 12.4.4 | instruction | A short description of rights and restrictions. The use of [tl;drLegal](https://tldrlegal.com/) is recommended. | You are free to share and change, but you must attribute, and share derivations under the same license. See https://tldrlegal.com/license/odc-open-database-license-(odbl) for further information. |
| 12.4.5 | attribution | The copyright owner of the **source**. If attribution licenses are used, that name must be acknowledged. | © Intergovernmental Panel on Climate Change 2014 |

### License Keys
| 13 | licenses | An array of objects of the license(s) under which the described package is provided. It can depend on the licenses of the sources (copyleft or share-alike) or can be granted by the creator of the data. |  |
| 13.1 | name | The [SPDX](https://spdx.org/licenses/) identifier. | ODbL-1.0 |
| 13.2 | title | An official (human readable) title of the license. | Open Data Commons Open Database License 1.0 |
| 13.3 | path | A link to the license text. | https://opendatacommons.org/licenses/odbl/1-0/index.html |
| 13.4 | instruction | A short description of rights and restrictions. The use of [tl;drLegal](https://tldrlegal.com/) is recommended. | You are free to share and change, but you must attribute, and share derivations under the same license. See https://tldrlegal.com/license/odc-open-database-license-(odbl) for further information. |
| 13.5 | attribution | The copyright owner of the **data**. If attribution licenses are used, that name must be acknowledged. | © Reiner Lemoine Institut |

### Provenience Keys
|#|Key |Description |Example |
|---|---|---|---|
| 14 | contributors | The people or organizations who contributed to this Data Package. This has to be a list. Each object refers to one contributor. Every contributor must have a title and property. A path, email, role and organization properties are optional extras. |  |
| 14.1 | title | Name/title of the contributor (name for a person, name or title for an organization) | Jon Doe |
| 14.2 | email | E-mail address of the contributor | contact@example.com |
| 14.3 | date | Date of the contribution. If the contribution took more than a day, use the date of the final contribiution. Date Format is ISO 8601. | 2016-06-16 |
| 14.4 | object | Target of contribution. Which part of the package was supplied/changed | Metadata |
| 14.5 | comment | Free text comment on what's been done | Fixed a typo in the title |

### Resource Keys
|#|Key |Description |Example |
|---|---|---|---|
| 15 | resources | The Data Resource format describes a data resource as an individual file or table. |  |
| 15.1 | profile | A string identifying the profile of this descriptor as per the profiles specification. This information is retained in order to comply with the "Tabular Data Package" standard. If at all in doubt the value should read "tabular-data-resource". | tabular-data-resource |
| 15.2 | name | A resource MUST contain a name unique to amongst all resources in this data package. To comply with the data package standard it must consist of only lowercase alphanumeric character plus ".", "-" and "_". It may not start with a number. In a database this will be the name of the table within its containing schema. It would be usual for the name to correspond to the file name (minus the file-extension) of the data file the resource describes.  | sandbox.example_table |
| 15.3 | path | A url-or-path string, that should be a permanent http(s) address or other path directly linking to the resource. | https://openenergy-platform.org/dataedit/view/openstreetmap/osm_deu_roads |
| 15.4 | format | 'csv', 'xls', 'json' etc. would be expected to be the standard file extension for this type of resource. When you upload your data to the OEDB, in the shown metadata string, the format will be changed accordingly to 'PostgreSQL', since the data there are stored in a data base. | csv |
| 15.5 | encoding | Specifies the character encoding of the resource's data file. The values should be one of the "Preferred MIME Names" for a character encoding registered with IANA. If no value for this key is specified then the default is UTF-8. | UTF-8 |
| 15.6 | schema | Object containing fields and primary key. Describes the structure of the present data. |  |
| 15.6.1 | fields | List of objects. Every object describes a column and provides name, description, type and unit. ||
| 15.6.1.1 | name | Name string unique within its scope. | year |
| 15.6.1.2 | description | Free-text describing the field. | Reference year for which the data were collected. |
| 15.6.1.3 | type | Data type of the field. In case of a geom-column in a database, also indicate the shape and  CRS. | geometry(Point, 4326) |
| 15.6.1.4 | isAbout | An array of Ontology URI that describe the column header | {"wind energy converting unit" : "https://openenergy-platform.org/ontology/oeo/OEO_00000044"}, {"declared net capacity" : "https://openenergy-platform.org/ontology/oeo/OEO_00230002"} |
| 15.6.1.5 | valueReference | An array of Ontology URI for an extended description of the values in the column |"valueReference": [{"offshore ":{"name": "onshore wind farm" ,"path" : "https://openenergy-platform.org/ontology/oeo/OEO_00000311"}}, {"onshore ":{"name": "offshore wind farm" ,"path" : "https://openenergy-platform.org/ontology/oeo/OEO_00000308"}}]|
| 15.6.1.6 | unit | Unit, preferably SI-Unit, that values in this field are mapped to. If 'unit' doesn't apply to a field, use 'null' | MW |
| 15.6.2 | primaryKey | A primary key is a field or set of fields that uniquely identifies each row in the table. It's recorded as a list of strings, since it is possible to define the primary key as made up of several columns. | id |
| 15.6.3 | foreignKeys | A foreign key is a field that refers to a column in another table. | |
| 15.6.3.1 | fields | The column in the table that is constrainted by the foreign key. | version |
| 15.6.3.2 | reference | The reference to the foreign table. | |
| 15.6.3.2.1 | resource | The foreign resource (table) | schema.table |
| 15.6.3.2.2 | fields | The foreign resource column | version |
| 15.7 | dialect | Object. A CSV Dialect defines a simple format to describe the various dialects of CSV files in a language agnostic manner. In case of a database, the values in the containing fields are 'null'. ||
| 15.7.1 | delimiter | Specifies the character sequence which should separate fields (aka columns). Common characters are "," (comma), "." (point) and "\t" (tab). | , |
| 15.7.2 | decimalSeparator | Symbol used to separate the integer part from the fractional part of a number written in decimal form. Depending on language and region this symbol can be "." or ",". | . |

### Review Keys
| 16 | @id | Uniform Resource Identifier (URI) that links the resource via the dpedia databus | https://databus.dbpedia.org/kurzum/mastr/bnetza-mastr/01.04.00 |
| 17 | @context | Explanation of metadata keys in ontology terms | https://raw.githubusercontent.com/LOD-GEOSS/databus-snippets/master/oep_metadata/context.jsonld |
| 18. | review | Data uploaded through the OEP needs to go through review. The review will cover the areas described here: https://github.com/OpenEnergyPlatform/data-preprocessing/wiki and carried out by a team of the platform. The review itself is documented at the specified path and a badge is rewarded with regards to completeness. |  |
| 18.1 | path | A URL or path string, that should be a permanent http(s) address directly linking to the documented review. | https://www.example.com |
| 18.2 | badge | A badge of either Bronze, Silver, Gold or Platin is used to label the given metadata based on its quality. | Platin |

### MetaMetadata Keys
| 19 | metaMetadata | Object. Description about the metadata themselves, their format, version and license. These fields should already be provided when you’re filling out your metadata. ||
| 19.1 | metadataVersion | Type and version number of the metadata | OEP-1.5 |
| 19.2 | metadataLicense | Object describing the license of the provided metadata ||
| 19.2.1 | name | SPDX identifier | CC0-1.0 |
| 19.2.2 | title | Official (human readable) license title | Creative Commons Zero v1.0 Universal |
| 19.2.3 | path | Url or path string, that is a fully qualified HTTP address | https://creativecommons.org/publicdomain/zero/1.0/ |
| 20 | _comment| Array of objects. The “_comment”-section is used as a self-description of the final metadata-file. It is text, intended for humans and can include a link to the metadata documentation(s), required value formats and similar remarks. The comment section has no fix structure or mandatory values, but a useful self-description, similar to the one depicted here, is encouraged. ||
| 20.1 | metadata | Reference to the metadata documentation in use. | "Metadata documentation and explanation (https://github.com/OpenEnergyPlatform/organisation/wiki/metadata)" |
| 20.2 | dates | Comment on data/time format | Dates and time must follow the ISO8601 including time zone (YYYY-MM-DD or YYYY-MM-DDThh:mm:ss±hh) |
| 20.3 | units | Comment on units | If you must use units in cells (which is discouraged), leave a space between numbers and units (100 m) |
| 20.4 | languages | Comment on language format | Languages must follow the IETF (BCP47) format (en-GB, en-US, de-DE) |
| 20.5 | licenses | Reference to license format | License name must follow the SPDX License List (https://spdx.org/licenses/) |
| 20.6 | review | Reference to review documentation | Following the OEP Data Review (https://github.com/OpenEnergyPlatform/data-preprocessing/wiki) |
| 20.7 | null | If a field is not applicable just enter: null | null |
| 20.8 | todo | If an applicable value is not yet available and will be inserted later on, use: "todo" | "todo" |
| 20.9 | ... | Feel free to add more descriptive comments. | |
