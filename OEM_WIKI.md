#Metadata

## DCAT-AP

1. [EC JoinUp](https://joinup.ec.europa.eu/collection/semantic-interoperability-community-semic/dcat-ap)
1. [Vokabulare und Dokumente für DCAT-AP.de](https://www.dcat-ap.de/def/)
1. [Deutscher IT-Planungsrats](https://www.it-planungsrat.de/SharedDocs/Sitzungen/DE/2018/Sitzung_26.html?pos=9)
1. [DCAT-AP Validator](http://dcat-ap.semic.eu/dcat-ap_validator.html)
1. [DCAT-AP.de Spezifikation](https://www.dcat-ap.de/def/dcatde/1.0.1/spec/specification.pdf)
1. [DCAT-AP.de Konventionenhandbuch](https://www.dcat-ap.de/def/dcatde/1_0/implRules.pdf)
1. [GeoDCAT-AP](https://joinup.ec.europa.eu/solution/dcat-application-profile-data-portals-europe/releases)
1. [w3 - Best Practices for Sharing Public Sector Information](https://www.w3.org/2013/share-psi/bp/)

## Used Ontologies

1. xmlns:dcterms="http://purl.org/dc/terms/" 
1. xmlns:dcat="http://www.w3.org/ns/dcat#" 
1. xmlns:locn="http://www.w3.org/ns/locn#"


## OEP-Metadata-Set v1.4 - discussion

Presentation of the [current metadata version (v1.4)](https://github.com/OpenEnergyPlatform/examples/blob/5358a6b1abbd3e11d388cda84bbf86e2144136ef/metadata/oep_metadata_example_v1.4.sql) by RLI and discussion per element.  
Preliminary decisions per element in the current version are marked with (OK; Revise key; Specify best-practice).

|Attribute name |Attribute DCAT-AP name |Source| Status |Comment |
|---|---|---|---|---|
| **name** |  |  | ? | Name des Datapackages, siehe title | 
| **title** | dct:title | IR S.16 1.1.6.2 | OK | Der Titel einer Datenstruktur oder einer Distribution wird in dct:title hinterlegt. Der Titel sollte dabei a) keine Metadaten, insbesondere keinen Zeit- und Ortsbezug enthalten (diese sollten in den dafür vorgesehenen Metadatenfeldern gemacht werden), b)  menschenlesbar sein. |
| **id** | dct:identifier | IR S18 1.1.8  | OK  | Use persistent URL (URI), ensure that the metadata exists even when the data is deleted. see [A2](https://www.go-fair.org/fair-principles/a2-metadata-accessible-even-data-no-longer-available/). In der Regel soll in dct:identifier der „Original-“URI der Datenstruktur hinterlegt werden| 
| **description** | dct:description | Sp S.20 Nr. 24  | OK |  Diese Eigenschaft enthält eine Beschreibung des Kataloges als Freitext. Diese Eigenschaft kann für parallel existierende Sprachversionen der Katalogbeschreibung wiederholt werden (xml:lang="de").  | 
| **language** | dct:language | Sp S.20 Nr. 29 | OK | Diese Eigenschaft bezieht sich auf die Sprache, welche in der textuellen Beschreibung der Metadaten der dem Katalog zugehörigen Datenstrukturen Verwendung findet (z.B. Titel, Beschreibungen usw.). Diese Eigenschaft kann wiederholt werden, falls die Metadaten in verschiedenen Sprachen zur Verfügung stehen. Standard: [IETF (BCP47)](https://tools.ietf.org/html/bcp47) | 
| **keywords** | dcat:keyword | Sp S.22 Nr. 43 | OK | Diese Eigenschaft enthält ein Schlagwort oder Schlüsselbegriff zur Beschreibung der Datenstruktur. Diese Eigenschaft kann für parallel existierende Sprachversionen von Schlagworten wiederholt werden. Comment: tags or key-value pairs; Insert upper limit against abuse. | 
| **publication_date** |  |  |  | new | 
| **project** |  |  |  | new | 
| homepage |  |  |  | new | 
| documentation |  |  |  | new | 
| source_code |  |  |  | new | 
| contact |  |  |  | new | 
| **spatial** | dct:spatial | Sp S.25 Nr. 66 | OK | Dieses Eigenschaft bezieht sich auf eine geographische Region, welche durch die Datenstruktur abgedeckt wird.  | 
| location | dct:location | IR S6 | OK | kann sowohl geometrische Ortsbezüge, als auch geografische Ortsbezüge per URI und strukturierte Adressanschriften aufnehmen. | 
| extent | locn:geometry / locn:geographicName | IR S6 | OK | Meist wird der Ortsbezug in Form einer Geometrie (z.B. einer Bounding Box) vorliegen. | 
| resolution | rdfs:comment | Geo S.24 | https://github.com/OpenEnergyPlatform/organisation/issues/11 |  | 
| **temporal** | dct:temporal |  | https://github.com/OpenEnergyPlatform/organisation/issues/13 |  | 
| reference_date |  |  |  | Standard: ISO 8601 prüfen ob UTC Offset inkludieren | 
| ts_start | dct:PeriodOfTime & schema:startDate | DCAT1.1 S.16 | OK | Ein Zeitintervall, welches durch Start- und Endzeitpunkt bezeichnet bzw. definiert ist. Comment: Check ISO 8601 | 
| ts_end | dct:PeriodOfTime  & schema:endDate | DCAT1.1 S.16 | OK | Comment: Check ISO 8601 | 
| ts_resolution |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/13 | Separate the number and unit with a space | 
| **sources** | dct:source  | DCAT-ap_1.1 p.13 | https://github.com/OpenEnergyPlatform/organisation/issues/14 |  | 
| title| dct:title | DCAT-ap_1.1 p.14 |  | This property contains a name given to the Catalogue Record. This property can be repeated for parallel language versions of the name. | 
| description | dct:description | DCAT-ap_1.1 p.14 |  | This property contains a free-text account of the Dataset. This property can be repeated for parallel language versions of the description. | 
| url | dcat:landingPage | DCAT-ap_1.1 p.13 | https://github.com/OpenEnergyPlatform/organisation/issues/14 | This property refers to a web page that provides access to the Dataset, its Distributions and/or additional information. It is intended to point to a landing page at the original data provider, not to a page on a site of a third party, such as an aggregator. | 
| license | dct:accessRights & dct:RightsStatement | DCAT-ap_1.1 p.13 | https://github.com/OpenEnergyPlatform/organisation/issues/14 | Comment: complete name and license id in brackets. Standard: [SPDX License List](https://spdx.org/licenses/) ... This property refers to information that indicates whether the Dataset is open data, has access restrictions or is not public. A controlled vocabulary with three members (:public, restricted, :non-public) will be created and maintained by the Publications Office of the EU.| 
| copyright | dct:accessRights & dct:RightsStatement | DCAT-ap_1.1 p.13 | https://github.com/OpenEnergyPlatform/organisation/issues/14 | This property refers to information that indicates whether the Dataset is open data, has access restrictions or is not public. A controlled vocabulary with three members (:public, :restricted, :non-public) will be created and maintained by the Publications Office of the EU. | 
| **licenses** | dct:license & dct:LicenseDocument | DCAT-ap_1.1 p.14 | https://github.com/OpenEnergyPlatform/organisation/issues/17 | Comment: complete name and license id in brackets. Standard: [SPDX License List](https://spdx.org/licenses/) | 
| id | dct:license |  | https://github.com/OpenEnergyPlatform/organisation/issues/17 | Standard: SPDX and [DCAT](https://www.dcat-ap.de/def/licenses/20180514.html#1.0/) | 
| _title_ |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/17 | if no ID | 
| _url_ | dct:LicenseDocument | DCAT-ap_1.1 p.14 |  | if no ID | 
| instruction | dcatde:licenseAttributionByText | IR S.23 | Optional? https://github.com/OpenEnergyPlatform/organisation/issues/17 | Standard: [tldrlegal](https://tldrlegal.com) | 
| copyright | dcatde:originator (foaf:Agent) | IR S.27 | https://github.com/OpenEnergyPlatform/organisation/issues/15 |  | 
| **contributors** | dct:contributor | IR S.27 | https://github.com/OpenEnergyPlatform/organisation/issues/18 | Diese Eigenschaft verweist auf Stellen oder Personen, die die Daten bearbeitet haben (z.B. durch Formatierung derselben). | 
| title | dct:contributor (foaf:Agent) & (foaf:Person) | IR S.27 |  | Comment: GitHub username possible Kommentar: Stellen oder Personen, die die Daten bearbeitet haben.| 
| email | dcat:contactPoint (vCard:Kind) | IR S.26 | https://github.com/OpenEnergyPlatform/organisation/issues/18 | Comment: optional | 
| date |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/18 | Standard: ISO 8601 | 
| comment |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/18 | https://github.com/OpenEnergyPlatform/organisation/issues/16 | 
| **resources** |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/19 | https://github.com/GovDataOfficial | 
| name |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/19 |  | 
| path |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/19 |  | 
| profile |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/19 |  | 
| format |  |  | https://github.com/OpenEnergyPlatform/organisation/issues/19 |  | 
| encoding |  |  |  |  | 
| fields |  |  |  |  | 
| _name_ |  |  |  |  | 
| _description_ |  |  |  |  | 
| _type_ | dcat:mediaType | DCAT-ap_1.1 p.14 |  |  | 
| _unit_ |  |  |  |  | 

  * **_comment:**: OK / Comment: Comments start with an underscore
    * **_metadata_version**: OK
    * **_metadata_license**: OK
    * **_metadata_license_url**: OK

## Decisions

* We use RDF-Turtle
* 

# Metadata Description

This pages describes the OEP Metadata version 1.4.0 You can have a look at an empty [template](https://github.com/OpenEnergyPlatform/metadata/blob/master/metadata/v140/template.json) and a filled out [example](https://github.com/OpenEnergyPlatform/metadata/blob/master/metadata/v140/example.json) of a metadata string.


# Table with all Metadata keys and a short description

|#|Key |Description |Example |
|---|---|---|---|
| 1 | name | File name or database table name | oep_metadata_table_example_v14 |
| 2 | title | Human readable title | Metadata Example Table |
| 3 | id | Uniform Resource Identifier (URI) that unambiguously identifies the resource. This can be a URL on the data set. It can also be a Digital Object Identifier (DOI). | https://example.com |
| 4 | description | A description of the package. It should be usable as summary information for the entire package that is described by the metadata. | Example table used to illustrate the metadata structure and meaning |
| 5 | language | Language used within the described data structures (e.g. titles, descriptions). The language key can be repeated if more languages are used. Standard: IETF (BCP47) | [en-GB, de-DE, fr-FR] |
| 6 | keywords | An Array of string keywords to assist users searching for the package in catalogs. | [example, template, test] |
| 7 | publicationDate | Date of publishing. Date Format is ISO 8601 (YYYY-MM-DD) | 2019-02-06 |
| 8 | context | Object. Contains name-value-pairs that describe the general setting, evironment or project leading to the creation or maintenance of this dataset. ||
| 8.1 | homepage | URL of Project | https://openenergy-platform.org/ | 
| 8.2 | documentation | URL of the projects source code | https://github.com/OpenEnergyPlatform/examples/wiki/Metadata-Description | 
| 8.3 | sourceCode | URL of Project | https://github.com/OpenEnergyPlatform | 
| 8.4 | contact | Reference to the creator or maintainer of the data set | contact@example.com | 
| 8.5 | grantNo | In a publicly funded Project: the identifying grant number | 01AB2345 | 
| 8.6 | fundingAgency | In a funded Project: The name of the funding agency | Bundesministerium für Wirtschaft und Energie | 
| 8.7 | fundingAgencyLogo | In a publicly funded Project: A link to the Logo of the funding agency | https://www.innovation-beratung-foerderung.de/INNO/Redaktion/DE/Bilder/Titelbilder/titel_foerderlogo_bmwi.jpg?__blob=poster&v=2 | 
| 8.8 | publisherLogo | Link to the logo of the publishing institution | https://reiner-lemoine-institut.de//wp-content/uploads/2015/09/rlilogo.png | 
| 9 | spatial | Object. Contains name-value-pairs describing the spatial context of the contained data. | |
| 9.1 | location | In the case of data where the location can be described as a point. May come as coordinates, URI or addresses with street, house number and zip code | 52.433509, 13.535855 |
| 9.2 | extent | Covered area. May be the name of a region, or the geometry of a bounding box. | Europe |
| 9.3 | resolution | Pixel size in case of a regular raster image. Reference to administrative level or other spatial division that is present as the smallest spatially distinguished unit size. | 30 m |
| 10 | temporal | Object. Time period covered in the data. Temporal information should either contain a "referenceDate" or the keys describing a time series; in rare cases both. Use `null` for the ones that don't apply. |  |
| 10.1 | referenceDate | Base year, month or day. Point in time for which the data is meant to be accurate. A census will generally have a reference year. A satellite image will have a reference date. Date Format is ISO 8601. |  2016-01-01 |
| 10.2 | timeseries | Object ||
| 10.2.1 | start | The beginning point in time of a time series. |  2019-02-06T10:12:04+00:00 |
| 10.2.2 | end | The end point in time of a time series. | 2019-02-07T10:12:04+00:00 |
| 10.2.3 | resolution | The time span between individual points of information in a time series. | 30 s |
| 10.2.4 | alignment | Indicator whether stamps in a time series are left, right or middle. `null` if there is no time series. | left |
| 10.2.5 | aggregationType | Indicates whether the values are a sum, average or current. | sum |
| 11 | sources | List of Objects. Each object has all name-value-pairs ||
| 11.1 | title | Human readable title of the source, e.g. document title or organisation name | IPCC Fifth Assessment Report |
| 11.2 | description | Free text description of the data set. | Scientific climate change report by the UN |
| 11.3 | path | URL to original source | https://www.ipcc.ch/site/assets/uploads/2018/02/ipcc_wg3_ar5_full.pdf |
| 11.4 | licenses | List of Objects. Each object has all name-value-pairs. The license(s) under which the source is provided. | |
| 11.4.1 | name | [SPDX](https://spdx.org/licenses/) identifier | ODbL-1.0 |
| 11.4.2 | title | Official (human readable) title | Open Data Commons Open Database License 1.0 |
| 11.4.3 | path | A link to the license | https://opendatacommons.org/licenses/odbl/1-0/index.html |
| 11.4.4 | instruction | short description of rights and restrictions |  You are free to share and change, but you must attribute, and share derivations under the same license. |
| 11.4.5 | attribution | copyrightholder of the source | © Intergovernmental Panel on Climate Change 2014 |
| 12 | licenses | The license(s) under which the described package is provided. List of Objects. Each object has all name-value-pairs  |  |
| 12.1 | name | SPDX identifier | ODbL-1.0 |
| 12.2 | title | Official (human readable) title | Open Data Commons Open Database License 1.0 |
| 12.3 | path | A url-or-path string, that is a fully qualified HTTP address, or a relative POSIX path (see the url-or-path definition in Data Resource for details). | https://opendatacommons.org/licenses/odbl/1-0/index.html |
| 12.4 | instruction | short description of rights and restrictions |  You are free to share and change, but you must attribute, and share derivations under the same license. |
| 12.5 | attribution | copyrightholder of the produced data set | © Reiner Lemoine Institut |
| 13 | contributors | The people or organizations who contributed to this Data Package. This has to be a list. Each object refers to one contributor. Every contributor must have a title and property. A path, email, role and organization properties are optional extras. |  |
| 13.1 | title | Name/title of the contributor (name for a person, name or title for an organization) | Jon Doe |
| 13.2 | email | E-mail address of the contributor | contact@example.com |
| 13.3 | date | Date of the contribution. If the contribution took more than a day, use the date of the final contribiution. Date Format is ISO 8601. | 2016-06-16 |
| 13.4 | object | Target of contribution. Which part of the package was supplied/changed | Metadata |
| 13.5 | comment | Free text comment on what's been done | Fixed a typo in the title |
| 14 | resources | The Data Resource format describes a data resource as an individual file or table. |  |
| 14.1 | profile | A string identifying the profile of this descriptor as per the profiles specification. This information is retained in order to comply with the "Tabular Data Package" standard. If at all in doubt the value should read "tabular-data-resource". | tabular-data-resource |
| 14.2 | name | A resource MUST contain a name unique to amongst all resources in this data package. To comply with the data package standard it must consist of only lowercase alphanumeric character plus ".", "-" and "_". It may not start with a number. In a database this will be the name of the table within its containing schema. It would be usual for the name to correspond to the file name (minus the file-extension) of the data file the resource describes.  | sandbox.example_table |
| 14.3 | path | A url-or-path string, that should be a permanent http(s) address or other path directly linking to the resource. | https://openenergy-platform.org/dataedit/view/openstreetmap/osm_deu_roads |
| 14.4 | format | 'csv', 'xls', 'json' etc. would be expected to be the standard file extension for this type of resource. When you upload your data to the OEDB, in the shown metadata string, the format will be changed accordingly to 'PostgreSQL', since the data there are stored in a data base. | csv |
14.5 | encoding | Specifies the character encoding of the resource's data file. The values should be one of the "Preferred MIME Names" for a character encoding registered with IANA. If no value for this key is specified then the default is UTF-8. | UTF-8 |
| 14.6 | schema | Object containing fields and primary key. Describes the structure of the present data. |  |
| 14.6.1 | fields | List of objects. Every object describes a column and provides name, description, type and unit. ||
| 14.6.1.1 | name | Name string unique within its scope. | year |
| 14.6.1.2 | description | Free-text describing the field. | Reference year for which the data were collected. |
| 14.6.1.3 | type | Data type of the field. In case of a geom-column in a database, also indicate the shape and  CRS. | geometry(Point, 4326) |
| 14.6.1.4 | unit | Unit, preferably SI-Unit, that values in this field are mapped to. If 'unit' doesn't apply to a field, use 'none' | MW |
| 14.6.2 | primaryKey | A primary key is a field or set of fields that uniquely identifies each row in the table. It's recorded as a list of strings, since it is possible to define the primary key as made up of several columns. | id |
| 14.6.3 | foreignKeys | A foreign key is a field that refers to a column in another table. | |
| 14.6.3.1 | fields | The column in the table that is constrainted by the foreign key. | version |
| 14.6.3.2 | reference | The reference to the foreign table. | |
| 14.6.3.2.1 | resource | The foreign resource (table) | schema.table |
| 14.6.3.2.2 | fields | The foreign resource column | version |
| 14.7 | dialect | Object. A CSV Dialect defines a simple format to describe the various dialects of CSV files in a language agnostic manner. In case of a database, the values in the containing fields are "none". ||
| 14.7.1 | delimiter | Specifies the character sequence which should separate fields (aka columns). Common characters are "," (comma), "." (point) and "\t" (tab). | , |
| 14.7.2 | decimalSeparator | Symbol used to separate the integer part from the fractional part of a number written in decimal form. Depending on language and region this symbol can be "." or ",". | . |
| 15. | review | Data uploaded through the OEP needs to go through review. The review will cover the areas described here: https://github.com/OpenEnergyPlatform/data-preprocessing/wiki and carried out by a team of the platform. The review itself is documented at the specified path and a badge is rewarded with regards to completeness. |  |
| 15.1 | path | A URL or path string, that should be a permanent http(s) address directly linking to the documented review. | https://www.example.com |
| 15.2 | badge | A badge of either Bronze, Silver, Gold or Platin is used to label the given metadata based on its quality. | Platin |
| 16 | metaMetadata | Object. Description about the metadata themselves, their format, version and license. These fields should already be provided when you’re filling out your metadata. ||
| 16.1 | metadataVersion | Type and version number of the metadata | OEP-1.4 |
| 16.2 | metadataLicense | Object describing the license of the provided metadata ||
| 16.2.1 | name | SPDX identifier | CC0-1.0 |
| 16.2.2 | title | Official (human readable) license title | Creative Commons Zero v1.0 Universal |
| 16.2.3 | path | Url or path string, that is a fully qualified HTTP address | https://creativecommons.org/publicdomain/zero/1.0/ |
| 17 | _comment| Array of objects. The “_comment”-section is used as a self-description of the final metadata-file. It is text, intended for humans and can include a link to the metadata documentation(s), required value formats and similar remarks. The comment section has no fix structure or mandatory values, but a useful self-description, similar to the one depicted here, is encouraged. ||
| 17.1 | metadata | Reference to the metadata documentation in use. | "Metadata documentation and explanation (https://github.com/OpenEnergyPlatform/organisation/wiki/metadata)" |
| 17.2 | dates | Comment on data/time format | Dates and time must follow the ISO8601 including time zone (YYYY-MM-DD or YYYY-MM-DDThh:mm:ss±hh) |
| 17.3 | units | Comment on units | If you must use units in cells (which is discouraged), leave a space between numbers and units (100 m) |
| 17.4 | languages | Comment on language format | Languages must follow the IETF (BCP47) format (en-GB, en-US, de-DE) |
| 17.5 | licenses | Reference to license format | License name must follow the SPDX License List (https://spdx.org/licenses/) |
| 17.6 | review | Reference to review documentation | Following the OEP Data Review (https://github.com/OpenEnergyPlatform/data-preprocessing/wiki) |
| 17.7 | ... | Feel free to add more descriptive comments. Like "none" | If a field is not applicable just enter "none" |