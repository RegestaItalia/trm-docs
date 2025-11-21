# Dependency Recognition

TRM can automatically detect the dependencies required by a TRM package to prevent syntax and runtime errors.

This detection is based on the types of objects used within the package. As support for additional object types may be needed over time, you can request support by opening an [incident](/incidents.md)

## Supported Object Types

This is a list of **ALL** workbench objects: mind that this list needs revision and some of the objects in this list **might be irrelevant**.
This table answers the question: does TRM automatically find objects used by object of type X?

| Object Type | Description | Supported | Notes |
|---|---|---|---|
| CLAS | Class (ABAP Objects) | ✅ | Read [ABAP Objects note](#abap-objects-note) |
| DDLS | Data Definition Language Source | ✅ |  |
| DDLX | CDS metadata extension | ✅ |  |
| DTEL | Data Element | ✅ |  |
| FUGR | Function Group | ✅ | Read [ABAP Objects note](#abap-objects-note) |
| INTF | Interface (ABAP Objects) | ✅ | |
| PROG | Program | ✅ | Read [ABAP Objects note](#abap-objects-note) |
| TABL | Table | ✅ |  |
| VIEW | View | ✅ |  |
| 1APP | BPC: APPLICATION | ❓ | Not tested yet |
| AABC | BPC APA Global Bands & KPI Category Setting | ❓ | Not tested yet |
| AADT | BPC APA Application Global Setting | ❓ | Not tested yet |
| AAOE | Analysis Office Excel Workbook | ❓ | Not tested yet |
| AAOP | Analysis Office Powerpoint | ❓ | Not tested yet |
| AAPP | BPC Model | ❓ | Not tested yet |
| AAPS | BPC Environment Info | ❓ | Not tested yet |
| ABLC | Settings for ABAP Language Version for Software Component | ❓ | Not tested yet |
| ABPC | BPC Objects | ❓ | Not tested yet |
| ABPF | BPC BPF | ❓ | Not tested yet |
| ABRU | BPC Business Rule | ❓ | Not tested yet |
| ACGA | BPC Environment Configuration | ❓ | Not tested yet |
| ACGP | BPC Model Configuration | ❓ | Not tested yet |
| ACGR | Role | ❓ | Not tested yet |
| ACGS | BPC System Configuration | ❓ | Not tested yet |
| ACGT | Role - User assignment | ❓ | Not tested yet |
| ACID | Checkpoint Group | ❓ | Not tested yet |
| ACLA | Archiving Class | ❓ | Not tested yet |
| ACLB | BPC Library | ❓ | Not tested yet |
| ACTR | BPC Control | ❓ | Not tested yet |
| ADAF | BPC Data Access Profile | ❓ | Not tested yet |
| ADEE | BPC Deletion Entity | ❓ | Not tested yet |
| ADEI | BPC deletion item | ❓ | Not tested yet |
| ADEL | BPC Deletion | ❓ | Not tested yet |
| ADIM | BPC Dimension | ❓ | Not tested yet |
| ADMC | BPC DM Data File | ❓ | Not tested yet |
| ADMD | BPC DM File Folder | ❓ | Not tested yet |
| ADMF | BPC DM File | ❓ | Not tested yet |
| ADMG | BPC Data Mananger Package Group | ❓ | Not tested yet |
| ADML | BPC DM Package Link | ❓ | Not tested yet |
| ADMP | BPC DM Package | ❓ | Not tested yet |
| ADSO | Datastore Object | ❓ | Not tested yet |
| ADTC | ADT Compatibility Graph | ❓ | Not tested yet |
| ADTG | BPC Drill Through | ❓ | Not tested yet |
| ADTS | ADT scopes for HTTP resource authorization via OAUTH2 | ❓ | Not tested yet |
| ADVC | App Variant (LRep cross-client content) | ❓ | Not tested yet |
| ADVD | App Variant (LRep client-dependent content) | ❓ | Not tested yet |
| ADVT | App Variant (LRep client-dependent content customizing req.) | ❓ | Not tested yet |
| AFCS | ABAP Fiori Code snippet | ❓ | Not tested yet |
| AFLC | BPC File Category | ❓ | Not tested yet |
| AFLD | BPC File Folder | ❓ | Not tested yet |
| AFLE | BPC Files | ❓ | Not tested yet |
| AFLG | BPC File Group | ❓ | Not tested yet |
| AFOT | ABAP Fiori Object Type | ❓ | Not tested yet |
| AGGR | Aggregate | ❓ | Not tested yet |
| AIFC | Objects from AIF content | ❓ | Not tested yet |
| AIFE | Object for extension content | ❓ | Not tested yet |
| AJUT | BPC Jounal Template | ❓ | Not tested yet |
| AKPI | BPC AVA KPI | ❓ | Not tested yet |
| ALID | Transport Object for Alternative ID Types | ❓ | Not tested yet |
| ALPT | BPC Web documents - LiveReport | ❓ | Not tested yet |
| ALVC | ALV Templates (for example, Crystal Layouts) from Customer | ❓ | Not tested yet |
| ALVL | Aggregation Level | ❓ | Not tested yet |
| ALVT | ALV Templates (for example, Crystal Layouts) from SAP | ❓ | Not tested yet |
| ALVW | ALV (WebDynroABAP) - BLOBs for Views delivered by SAP | ❓ | Not tested yet |
| AMBR | BPC Dimension member | ❓ | Not tested yet |
| AMHC | ABAP-Managed (Logical) HDI Containers | ❓ | Not tested yet |
| AMPF | BPC Member Access Profile | ❓ | Not tested yet |
| AMSD | Logical Database Schema | ❓ | Not tested yet |
| AMSM | Mapping of Logical Schema to Physical Schema | ❓ | Not tested yet |
| ANMO | Analytical Model | ❓ | Not tested yet |
| ANPR | Analysis Process | ❓ | Not tested yet |
| ANSE | Analytical Service | ❓ | Not tested yet |
| ANSO | Source for analytical model | ❓ | Not tested yet |
| ANST | Analytical service types | ❓ | Not tested yet |
| AOBJ | Archiving Object | ❓ | Not tested yet |
| APCO | Application components | ❓ | Not tested yet |
| APIA | API Release: API Catalog Assignment | ❓ | Not tested yet |
| APIC | API Catalog | ❓ | Not tested yet |
| APIS | API Release State of Objects | ❓ | Not tested yet |
| APIV | API Version | ❓ | Not tested yet |
| APIX | API Snapshot | ❓ | Not tested yet |
| APLO | Application Log Object | ❓ | Not tested yet |
| APOB | Application Object | ❓ | Not tested yet |
| APPL | Application Class | ❓ | Not tested yet |
| APPS | BPC Appset | ❓ | Not tested yet |
| AQBG | ABAP Query: User group | ❓ | Not tested yet |
| AQHT | SAP Query: HTML Templates | ❓ | Not tested yet |
| AQQU | ABAP Query: Query | ❓ | Not tested yet |
| AQQV | ABAP Query: Query variant | ❓ | Not tested yet |
| AQSG | ABAP Query: Functional area | ❓ | Not tested yet |
| AQTR | SAP Query: HTML Templates (raw) | ❓ | Not tested yet |
| AQXI | ABAP Query: Additional functions | ❓ | Not tested yet |
| AREA | InfoArea | ❓ | Not tested yet |
| ARLE | Meta Data for Derivation Cluster | ❓ | Not tested yet |
| ARTP | BPC Report template | ❓ | Not tested yet |
| ASFC | SAP AS: Field Catalog | ❓ | Not tested yet |
| ASIS | SAP AS: Archiving Information Structure | ❓ | Not tested yet |
| ASOB | Analytics Security Object (BI Analysis Authorizations) | ❓ | Not tested yet |
| ASPD | BPC Script Folder | ❓ | Not tested yet |
| ASPF | BPC Script File | ❓ | Not tested yet |
| ASPR | BPC Script File Resource | ❓ | Not tested yet |
| ATCS | ABAP Test Cockpit: Step | ❓ | Not tested yet |
| ATEM | BPC Team | ❓ | Not tested yet |
| ATOC | System Data for Cross Release Customizing Transports | ❓ | Not tested yet |
| ATOD | System Data for Cross Release Transports | ❓ | Not tested yet |
| ATOM | ATO Manifest | ❓ | Not tested yet |
| ATOT | ATO System Transfer | ❓ | Not tested yet |
| ATPF | BPC Task Profile | ❓ | Not tested yet |
| ATPL | Transport of Profile Generator templates | ❓ | Not tested yet |
| ATRT | Data Types for Attributes | ❓ | Not tested yet |
| ATTR | Logical Transport Object for Set Type Attributes | ❓ | Not tested yet |
| AUTH | Authorization Check Fields | ❓ | Not tested yet |
| AVAR | Activation Variants for Assertions and Breakpoints | ❓ | Not tested yet |
| AVAS | Classification | ❓ | Not tested yet |
| AVRS | ABAP Version | ❓ | Not tested yet |
| AWDC | BPC Web document category | ❓ | Not tested yet |
| AWFD | BPC Web document folder | ❓ | Not tested yet |
| AWKP | BPC Web document - workspace | ❓ | Not tested yet |
| AWSS | BPC Workstatus | ❓ | Not tested yet |
| AXDB | BPC Web documents - XcelsiusDashBoard | ❓ | Not tested yet |
| AXEC | Rapid Application Embedded Views (Customer maintained) | ❓ | Not tested yet |
| AXEM | Embeddable view | ❓ | Not tested yet |
| AXES | Rapid Application Embedded Views (SAP delivered) | ❓ | Not tested yet |
| AXTA | Application Group | ❓ | Not tested yet |
| AXTB | Extensible business objects | ❓ | Not tested yet |
| AXTC | Generation Catalogue | ❓ | Not tested yet |
| AXTE | Extension | ❓ | Not tested yet |
| AXTL | Logical Table object | ❓ | Not tested yet |
| AXTN | Extensibility number range definition | ❓ | Not tested yet |
| AXTO | Extension object type | ❓ | Not tested yet |
| AXTP | Extensible place | ❓ | Not tested yet |
| AXTS | Extensible search | ❓ | Not tested yet |
| AXTT | Extensible table place | ❓ | Not tested yet |
| AXTV | Navigational object | ❓ | Not tested yet |
| AZAP | Analysis Application | ❓ | Not tested yet |
| AZEX | Design Studio Extension | ❓ | Not tested yet |
| BAOE | BPC: Workbook | ❓ | Not tested yet |
| BBPF | BPC: BPF | ❓ | Not tested yet |
| BCCH | Business Configuration Check | ❓ | Not tested yet |
| BCCU | Business Configuration Check Units | ❓ | Not tested yet |
| BCDE | BC-Sets for Delta Activation | ❓ | Not tested yet |
| BCTC | Business Configuration - Table Field Classification | ❓ | Not tested yet |
| BDAP | BPC: Data access profile | ❓ | Not tested yet |
| BDEF | Behavior Definition | ❓ | Not tested yet |
| BFTR | Business Feature | ❓ | Not tested yet |
| BGQC | Background Processing Context | ❓ | Not tested yet |
| BIBD | BI Content Bundle | ❓ | Not tested yet |
| BIDC | Logical Transport object for BP ID Categories | ❓ | Not tested yet |
| BIMO | BI Meta (Transport) Object Type | ❓ | Not tested yet |
| BITM | BI Web Items (NW7.0+) | ❓ | Not tested yet |
| BIXP | Object for Controlling Data Conversions in BI | ❓ | Not tested yet |
| BLFO | BW: LOIO Class Folder | ❓ | Not tested yet |
| BLMA | BW: LOIO Class Master Data | ❓ | Not tested yet |
| BLRC | Customizing for RFC Blacklist Entries | ❓ | Not tested yet |
| BLRF | Blacklist Entries RFC | ❓ | Not tested yet |
| BLSC | Build Script | ❓ | Not tested yet |
| BLTM | BW: LOIO Class Web Templates | ❓ | Not tested yet |
| BMAO | Any object | ❓ | Not tested yet |
| BMBS | Collaborative Business Scenario | ❓ | Not tested yet |
| BMEF | Function in process model | ❓ | Not tested yet |
| BMEO | Enterprise OrgUnit type (3.0 only) | ❓ | Not tested yet |
| BMEP | Diagram in process model | ❓ | Not tested yet |
| BMET | Process hierarchy level below OrgUnit (3.0 only) | ❓ | Not tested yet |
| BMEV | Event in process model | ❓ | Not tested yet |
| BMFR | Application Component | ❓ | Not tested yet |
| BMFU | Function | ❓ | Not tested yet |
| BMFV | Global function variant | ❓ | Not tested yet |
| BMFZ | Function relationship diagram | ❓ | Not tested yet |
| BMGR | Group | ❓ | Not tested yet |
| BMGT | Process list for application components 3.1 | ❓ | Not tested yet |
| BMHF | Process list for application components, 3.0 | ❓ | Not tested yet |
| BMHT | Application component hierarchy level | ❓ | Not tested yet |
| BMPC | Software Module | ❓ | Not tested yet |
| BMPM | Process selection matrix for components (3.0 only) | ❓ | Not tested yet |
| BMPV | Software Variant | ❓ | Not tested yet |
| BMSL | Diagram variants in process model | ❓ | Not tested yet |
| BMSM | Process selection matrix for OrgUnits (3.0 only) | ❓ | Not tested yet |
| BMSP | Scenario process (3.0 only) | ❓ | Not tested yet |
| BMSZ | Scenario (3.0 only) | ❓ | Not tested yet |
| BMTH | Structure Repository for Processes: Node Definition | ❓ | Not tested yet |
| BMVA | Component selection for IMG | ❓ | Not tested yet |
| BMVG | Display group process model | ❓ | Not tested yet |
| BOBC | BOPF Contract Compliance Check Configuration | ❓ | Not tested yet |
| BOBF | BOPF: Business Object Model | ❓ | Not tested yet |
| BOBL | BOPF: Business Object Library | ❓ | Not tested yet |
| BOBX | BOPF: Business Object Model Extension | ❓ | Not tested yet |
| BOCT | Linked Analytics Story | ❓ | Not tested yet |
| BOTY | Object Type for General Object Number | ❓ | Not tested yet |
| BPMA | BW: PHIO Class Master Data | ❓ | Not tested yet |
| BPTM | BW: PHIO Class Web Templates | ❓ | Not tested yet |
| BR01 | SAP Object Type | ❓ | Not tested yet |
| BR02 | SAP Object Node Type | ❓ | Not tested yet |
| BRCL | Attributes - Producer/Distributor Classes in Broadcasting BW | ❓ | Not tested yet |
| BRF0 | BRF: Application Class | ❓ | Not tested yet |
| BRR1 | Business Rule | ❓ | Not tested yet |
| BRR2 | Business Rule (Client-Specific) | ❓ | Not tested yet |
| BRSE | Broadcasting Settings (BW) | ❓ | Not tested yet |
| BSAL | Business Suite Side Panel: Logical information object | ❓ | Not tested yet |
| BSAP | Business Suite Side Panel: Physical information object | ❓ | Not tested yet |
| BSNL | Business Suite Side Panel: Logical information object | ❓ | Not tested yet |
| BSNP | Business Suite Side Panel: Physical information object | ❓ | Not tested yet |
| BSVI | Status management: System status | ❓ | Not tested yet |
| BSVO | Status management: Object type | ❓ | Not tested yet |
| BSVS | Status management: status profile | ❓ | Not tested yet |
| BSVV | Status management: Process | ❓ | Not tested yet |
| BTMP | BI Web Templates (NW7.0+) | ❓ | Not tested yet |
| BWBK | BPC: Workbook | ❓ | Not tested yet |
| BWLA | BW: Processor for Language Export in BW | ❓ | Not tested yet |
| CACC | CDM App Config (LREP cross-client content) | ❓ | Not tested yet |
| CACD | CDM App Config (LREP client-dependent content) | ❓ | Not tested yet |
| CACT | CDM App Config (LREP client-dependent cont. - custom. req.) | ❓ | Not tested yet |
| CALE | Public Holidays | ❓ | Not tested yet |
| CASP | SCC: Check Aspect | ❓ | Not tested yet |
| CASV | SCC: Check Aspect Value | ❓ | Not tested yet |
| CBAL | Floorplan Manager - Context Based Adaptations - Links/Rules | ❓ | Not tested yet |
| CBAS | Floorplan Manager - Context Based Adaptations - Sets | ❓ | Not tested yet |
| CCAC | CDM Catalog (LREP cross-client content) | ❓ | Not tested yet |
| CCAD | CDM Catalog (LREP client-dependent content) | ❓ | Not tested yet |
| CCAT | CDM Catalog (LREP client-dependent content - custom. req.) | ❓ | Not tested yet |
| CCEI | Client Export-/Import Helper Object - Never Change Manually | ❓ | Not tested yet |
| CCFG | SCC: Check Configuration | ❓ | Not tested yet |
| CCPR | Client Copy Profile | ❓ | Not tested yet |
| CCRU | SCC: Check Configuration Rule | ❓ | Not tested yet |
| CDAT | View Cluster Maintenance: Data | ❓ | Not tested yet |
| CDBO | Customer Data Browser | ❓ | Not tested yet |
| CDDH | Packages for Table Entries: Granularity | ❓ | Not tested yet |
| CDDL | Default Original Language in Customizing | ❓ | Not tested yet |
| CDDO | Default Originality Attributes in Customizing | ❓ | Not tested yet |
| CDLH | Original Language for Table Entries: Granularity | ❓ | Not tested yet |
| CDOH | Originality for Table Entries: Granularity | ❓ | Not tested yet |
| CEBR | BPC: Consolidation business rule for environment | ❓ | Not tested yet |
| CELM | Elements of the Query Builder (SAP Delivery) | ❓ | Not tested yet |
| CFD1 | Custom fields: IDoc Type Registry | ❓ | Not tested yet |
| CFDA | Custom Logic Registration | ❓ | Not tested yet |
| CFDB | Custom Fields: Business Context Registry | ❓ | Not tested yet |
| CFDC | Custom Fields: CDS View Registry | ❓ | Not tested yet |
| CFDE | Data Source Extension | ❓ | Not tested yet |
| CFDF | Custom Field | ❓ | Not tested yet |
| CFDG | Custom Fields: SAP GUI Registry | ❓ | Not tested yet |
| CFDH | Custom Behavior Extension Registration | ❓ | Not tested yet |
| CFDM | Custom fields: Function Module Registry | ❓ | Not tested yet |
| CFDO | Custom Fields: OData Model Registry | ❓ | Not tested yet |
| CFDP | Custom fields: SOAP Service Interface Registry | ❓ | Not tested yet |
| CFDR | Custom Fields: Association Target | ❓ | Not tested yet |
| CFDS | Custom Fields: Business Scenario Registry | ❓ | Not tested yet |
| CFDT | Custom Fields: Data Transfer Registry | ❓ | Not tested yet |
| CFDX | Custom Fields: Suffix Registry | ❓ | Not tested yet |
| CFDY | Custom Fields: Abstract Entity Registry | ❓ | Not tested yet |
| CGRC | CDM Group (LREP cross-client content) | ❓ | Not tested yet |
| CGRD | CDM Group (LREP client-dependent content) | ❓ | Not tested yet |
| CGRT | CDM Group (LREP client-dependent content - customizing req.) | ❓ | Not tested yet |
| CHAR | Object characteristic | ❓ | Not tested yet |
| CHDO | Change Document Object | ❓ | Not tested yet |
| CHKC | Check category | ❓ | Not tested yet |
| CHKE | Check Exemptions | ❓ | Not tested yet |
| CHKO | Check | ❓ | Not tested yet |
| CHKV | Check Variant | ❓ | Not tested yet |
| CINS | Correction Instruction | ❓ | Not tested yet |
| CMBR | BPC: Consolidation business rule for model | ❓ | Not tested yet |
| CMBT | BPC: Consolidation task sequence for model | ❓ | Not tested yet |
| CMHC | Cloud Management Health Check | ❓ | Not tested yet |
| CMOD | Customer enhancement projects | ❓ | Not tested yet |
| CMPA | Client Multiplexer Scenario Task List Parameters | ❓ | Not tested yet |
| CMPT | Code Composer Template | ❓ | Not tested yet |
| CMSQ | Client Multiplexer Scenario Sequence | ❓ | Not tested yet |
| CMTM | Cloud Management Tenant Multiplexer Trigger | ❓ | Not tested yet |
| CNPA | DMC: Definition of a control parameter | ❓ | Not tested yet |
| CNPC | DMC: Migration Settings of a Control Parameter | ❓ | Not tested yet |
| CNTN | DMC: Definition of a Container (Sender/Recipient) | ❓ | Not tested yet |
| CNTX | Context | ❓ | Not tested yet |
| CNVN | Conversion Tools: Notification Events | ❓ | Not tested yet |
| COAC | ESF: Action | ❓ | Not tested yet |
| COAS | ESF: Aspect | ❓ | Not tested yet |
| COBJ | DMC: Definition of a Conversion Object | ❓ | Not tested yet |
| COBO | ESF: Business Object | ❓ | Not tested yet |
| COCF | ESF: Configuration | ❓ | Not tested yet |
| COCO | Control Composite | ❓ | Not tested yet |
| COPR | CompositeProvider | ❓ | Not tested yet |
| CORL | ESF: Relation | ❓ | Not tested yet |
| COSM | ESF: Service Modules | ❓ | Not tested yet |
| CPKM | Meta data of a transport-based correction instruction | ❓ | Not tested yet |
| CRME | CRM Enterpise Search | ❓ | Not tested yet |
| CRWB | Crystal Reports Template | ❓ | Not tested yet |
| CTAF | Condition Technique - Application Field | ❓ | Not tested yet |
| CTAP | Condition Technique - Application | ❓ | Not tested yet |
| CTCR | BPC: Control for BPC embeded model | ❓ | Not tested yet |
| CTCS | BPC: Control set for BPC embeded model | ❓ | Not tested yet |
| CTCT | Condition Technique - Condition Table | ❓ | Not tested yet |
| CTDD | Condition Technique - Procedure Type for Info. Determination | ❓ | Not tested yet |
| CTEM | Customizing templates | ❓ | Not tested yet |
| CTFD | Condition Technique - Data Element in Global Field Catalog | ❓ | Not tested yet |
| CTFF | Condition Technique - Field Name in Global Field Catalog | ❓ | Not tested yet |
| CTFP | Condition Technique - Dependencies in Global Field Catalog | ❓ | Not tested yet |
| CTFR | Condition Technique - Relationships in Global Field Catalog | ❓ | Not tested yet |
| CTMC | Condition Technique - Maintenance Context for Cond. Maint. | ❓ | Not tested yet |
| CTRF | Condition Technique: Reference Type for Condition Maint. | ❓ | Not tested yet |
| CTRT | Currency Translation Type | ❓ | Not tested yet |
| CTSB | Condition Technque - Scale Base Type of Scale | ❓ | Not tested yet |
| CTTK | Condition Technique - Task (Signature Part) | ❓ | Not tested yet |
| CTTS | Condition Technique - Task (Definition Part) | ❓ | Not tested yet |
| CTUF | Condition Technique - Field of a Usage | ❓ | Not tested yet |
| CTUS | Condition Technique - Usage | ❓ | Not tested yet |
| CUAT | Customer enhancements: Menu enhancement texts | ❓ | Not tested yet |
| CUBE | InfoCube | ❓ | Not tested yet |
| CUCF | Configuration of a customer initiated Add-On Uninstallation | ❓ | Not tested yet |
| CUS0 | Customizing IMG Activity | ❓ | Not tested yet |
| CUS1 | Customizing Transactions | ❓ | Not tested yet |
| CUS2 | Customizing Attributes | ❓ | Not tested yet |
| CUS3 | Variants of IMG Attributes | ❓ | Not tested yet |
| CWBN | Note Assistant Modification Data | ❓ | Not tested yet |
| DAAG | Data Aging Object | ❓ | Not tested yet |
| DAGP | Partitioning Object | ❓ | Not tested yet |
| DAGR | Aggregate (SAP Delivery) | ❓ | Not tested yet |
| DAGW | Data Aging Object Relevant in Cloud and On-Premise | ❓ | Not tested yet |
| DALV | Aggregation Level (SAP Delivery) | ❓ | Not tested yet |
| DANM | Analytical Model (shipped version) | ❓ | Not tested yet |
| DANP | Analysis Process (SAP Delivery) | ❓ | Not tested yet |
| DANS | Source for analytical model (shipment version) | ❓ | Not tested yet |
| DAOE | Analysis Office Excel Workbook (SAP Delivery Version) | ❓ | Not tested yet |
| DAOP | Analysis Office Powerpoint (SAP Delivery Version) | ❓ | Not tested yet |
| DAPA | BW Data Archiving Process (Active Version) | ❓ | Not tested yet |
| DAPC | Application Components (SAP Delivery) | ❓ | Not tested yet |
| DAPD | BW Data Archiving Process (Delivered Version) | ❓ | Not tested yet |
| DAQC | Data Analyzer Query(Cross-client content) | ❓ | Not tested yet |
| DAQR | Embedded Data Analyzer Query | ❓ | Not tested yet |
| DARE | InfoArea (SAP Delivery) | ❓ | Not tested yet |
| DASO | D Version for Analytics Security Object (BI Analysis Auth.) | ❓ | Not tested yet |
| DBBP | BPC: BPF (Delivery Version) | ❓ | Not tested yet |
| DBDA | BPC: Data access profile (Delivery Version) | ❓ | Not tested yet |
| DBIT | BI Web Item (NW7.0+) D-Version | ❓ | Not tested yet |
| DBIX | Delivery Version Control for Data Conversions in BI | ❓ | Not tested yet |
| DBRS | D-Version: Broadcast Settings (BW) | ❓ | Not tested yet |
| DBTM | BI Web Templates (NW7.0+) D-Version | ❓ | Not tested yet |
| DCAT | Data Category | ❓ | Not tested yet |
| DCLS | ABAP Data Control Language Sources | ❓ | Not tested yet |
| DCOP | Composite Provider (SAP Delivery) | ❓ | Not tested yet |
| DCRW | Crystal Reports Template (SAP Delivery) | ❓ | Not tested yet |
| DCTR | Currency Translation Type (SAP Delivery) | ❓ | Not tested yet |
| DCUB | InfoCube  (SAP Delivery) | ❓ | Not tested yet |
| DDAS | Modeled Data Access Service | ❓ | Not tested yet |
| DDBF | Actions for Database Functions | ❓ | Not tested yet |
| DDCC | DD: Cache Configuration | ❓ | Not tested yet |
| DDDA | Modeled Data Access Service (SAP Delivery) | ❓ | Not tested yet |
| DDDD | Changes to Nametab Structure | ❓ | Not tested yet |
| DDES | Open Hub Destination (SAP Delivery) | ❓ | Not tested yet |
| DDIL | ABAP Dictionary: Trigger CBDA Persistence Update (Ini. Load) | ❓ | Not tested yet |
| DDLA | CDS Annotation Definition | ❓ | Not tested yet |
| DDLV | CDS Variant | ❓ | Not tested yet |
| DDMM | DataMining Model (Shipped Version) | ❓ | Not tested yet |
| DDMO | Data Flow (SAP Shipment) | ❓ | Not tested yet |
| DDOC | Documents Application (SAP Delivery) | ❓ | Not tested yet |
| DDSO | Datastore Object (SAP Delivery) | ❓ | Not tested yet |
| DEBR | BPC: Consolidation business rule for environment(D Version) | ❓ | Not tested yet |
| DELM | Elements of the Query Builder (SAP Delivery) | ❓ | Not tested yet |
| DENV | BPC: Environment (Delivery Version) | ❓ | Not tested yet |
| DEST | Open Hub Destination | ❓ | Not tested yet |
| DEVC | Package | ❓ | Not tested yet |
| DEVE | Event Chain Processing (SAP Delivery) | ❓ | Not tested yet |
| DFTH | Structure Buffer for Scenarios: Definition of Nodes | ❓ | Not tested yet |
| DHAA | HANA Analysis Process (SAP Delivery) | ❓ | Not tested yet |
| DHCP | Hana Composite Provider (SAP Delivery) | ❓ | Not tested yet |
| DHIE | BW Hierarchy (SAP Delivery) | ❓ | Not tested yet |
| DHYB | HybridProvider  (SAP Delivery) | ❓ | Not tested yet |
| DIAL | Dialog Module | ❓ | Not tested yet |
| DICA | InfoCatalog (SAP Delivery) | ❓ | Not tested yet |
| DINS | IQM Inspection Plan (BI) (D Version) | ❓ | Not tested yet |
| DIOB | InfoObject (SAP Delivery) | ❓ | Not tested yet |
| DIOC | InfoObjectCatalog (SAP Delivery) | ❓ | Not tested yet |
| DISC | Call Package (SAP Delivery) | ❓ | Not tested yet |
| DISE | InfoSet in BW (SAP Delivery) | ❓ | Not tested yet |
| DISG | InfoPackage Groups (SAP Delivery) | ❓ | Not tested yet |
| DITM | Transport Object for BW Web Items (D Version) | ❓ | Not tested yet |
| DKEY | Logical Transport Object for Differentiation Key Types | ❓ | Not tested yet |
| DKPC | BI: KPI Catalog Folder (Delivery) | ❓ | Not tested yet |
| DKPD | BI: KPI Definition (Delivery) | ❓ | Not tested yet |
| DLCC | CRM UIF, Dynamic Layout Configuration / Customer Layer | ❓ | Not tested yet |
| DLCS | CRM UIF, Dynamic Layout Configuration / SAP layer | ❓ | Not tested yet |
| DLXX | Extension Index for Table Entities | ❓ | Not tested yet |
| DMBR | BPC: Consolidation business rule for model(Delivery Version) | ❓ | Not tested yet |
| DMBT | BPC: Consolidation task sequence for model (D version) | ❓ | Not tested yet |
| DMDL | BPC: Model (Delivery Version) | ❓ | Not tested yet |
| DME1 | DMEE Format Tree for Outgoing/Incoming Files | ❓ | Not tested yet |
| DMMO | DataMining Model | ❓ | Not tested yet |
| DMOD | Data Flow | ❓ | Not tested yet |
| DMON | ABAP Daemon Application | ❓ | Not tested yet |
| DMPR | Multi Provider (SAP Delivery) | ❓ | Not tested yet |
| DMSK | Data Masking: Logical transport object | ❓ | Not tested yet |
| DOBJ | Data Destruction Object | ❓ | Not tested yet |
| DOCA | Document Store | ❓ | Not tested yet |
| DOCT | General Text | ❓ | Not tested yet |
| DOCV | Documentation (Independent) | ❓ | Not tested yet |
| DODS | DataStore Object (SAP Delivery) | ❓ | Not tested yet |
| DOKU | Nodes for Documentation Structure | ❓ | Not tested yet |
| DOMA | Domain | ❓ | Not tested yet |
| DPLC | Planning: Characteristic Relationship Object (SAP Delivery) | ❓ | Not tested yet |
| DPLD | Planning: Data Slices (SAP Delivery) | ❓ | Not tested yet |
| DPLQ | Planning Sequence (SAP Delivery) | ❓ | Not tested yet |
| DPLS | Planning Service (SAP Delivery) | ❓ | Not tested yet |
| DPLT | Planning Service Type (SAP Delivery) | ❓ | Not tested yet |
| DQVI | Transport Object for BW Query Views (D Version) | ❓ | Not tested yet |
| DRAS | CDS Aspects | ❓ | Not tested yet |
| DREL | Report Designer: Reusable Elements, D Version | ❓ | Not tested yet |
| DRNL | BPC: Journal (Delivery version) | ❓ | Not tested yet |
| DROU | Routine (SAP Delivery) | ❓ | Not tested yet |
| DRPM | Dictionary Replication Metadata | ❓ | Not tested yet |
| DRPT | BW Enterprise Report Delivery Version | ❓ | Not tested yet |
| DRTY | CDS Type Definitions | ❓ | Not tested yet |
| DRUL | Dependency Rule | ❓ | Not tested yet |
| DSAA | DataSource Application Component Hierarchy (Active Version) | ❓ | Not tested yet |
| DSAD | DataSource Application Component (Delivered Version) | ❓ | Not tested yet |
| DSCS | Communication Structure (SAP Delivery) | ❓ | Not tested yet |
| DSEL | Selection View | ❓ | Not tested yet |
| DSFD | CDS Scalar Function Definition | ❓ | Not tested yet |
| DSFI | CDS Scalar Function Implementation Reference | ❓ | Not tested yet |
| DSFO | BW Formula (Version for Delivery) | ❓ | Not tested yet |
| DSPC | Process Chain (SAP Delivery) | ❓ | Not tested yet |
| DSPI | Interrupting Process (SAP Delivery) | ❓ | Not tested yet |
| DSPT | Process Chain Starter (SAP Delivery) | ❓ | Not tested yet |
| DSPV | Process Variant (SAP Delivery) | ❓ | Not tested yet |
| DSTD | InfoSource Transaction Data (SAP Delivery) | ❓ | Not tested yet |
| DSYS | Chapter of a Book Structure | ❓ | Not tested yet |
| DTCR | BPC: Control for BPC embeded model (D version) | ❓ | Not tested yet |
| DTCS | BPC: Control set for BPC embeded model (D version) | ❓ | Not tested yet |
| DTDC | Dictionary Tuning: Dynamic Cache | ❓ | Not tested yet |
| DTEA | BPC: Team (Delivery Version) | ❓ | Not tested yet |
| DTEB | Entity Buffer | ❓ | Not tested yet |
| DTF1 | Date Functions | ❓ | Not tested yet |
| DTHJ | Key Date Derivation Type (SAP Delivery) | ❓ | Not tested yet |
| DTMP | Transport Object for BW Web Templates (D Version) | ❓ | Not tested yet |
| DTPA | Data Transfer Process: Active Version | ❓ | Not tested yet |
| DTPD | Data Transfer Process (SAP Delivery) | ❓ | Not tested yet |
| DTPT | Dictionary Tuning: Partitioning | ❓ | Not tested yet |
| DTRC | Communication Structure for Transfomration (SAP Delivery) | ❓ | Not tested yet |
| DTRF | Transformation (SAP Delivery) | ❓ | Not tested yet |
| DTSC | Dictionary Tuning: Static Cache | ❓ | Not tested yet |
| DTTG | Dictionary Tuning: Table Grouping | ❓ | Not tested yet |
| DUOM | Quantity Conversion Type (SAP Delivery) | ❓ | Not tested yet |
| DUPD | Update Rules (SAP Delivery) | ❓ | Not tested yet |
| DVSL | KW: Logical info object (DVS) | ❓ | Not tested yet |
| DVSP | KW: Physical info object (DVS) | ❓ | Not tested yet |
| DVSS | KW: Structure storage for DVS | ❓ | Not tested yet |
| DWIB | BW Web Item (BI-Runtime) | ❓ | Not tested yet |
| DWKS | BPC: workspace (Delivery Version) | ❓ | Not tested yet |
| DWPA | BW Web Runtime:  Parameter (for Web Item or Command) | ❓ | Not tested yet |
| DXCL | Xcelcius Dashboard Delivery version | ❓ | Not tested yet |
| DXLW | Excel Workbook (SAP Delivery) | ❓ | Not tested yet |
| DZAP | Analysis Application (SAP Delivery Version) | ❓ | Not tested yet |
| DZEX | Design Studio Extension (SAP Delivery Version) | ❓ | Not tested yet |
| ECAT | eCATT Test Script | ❓ | Not tested yet |
| ECSD | eCATT System Data Container | ❓ | Not tested yet |
| ECSP | eCATT Start Profile | ❓ | Not tested yet |
| ECTC | eCATT Test Configuration | ❓ | Not tested yet |
| ECTD | eCATT Test Data Container | ❓ | Not tested yet |
| ECVO | eCATT Validation Object | ❓ | Not tested yet |
| EEEC | Enterprise Event Enablement - Event Consumer | ❓ | Not tested yet |
| EEEP | Enterprise Event Enablement - Event Producer | ❓ | Not tested yet |
| EFCL | Form Class | ❓ | Not tested yet |
| EFOM | Print Workbench Application Form | ❓ | Not tested yet |
| ELEM | Elements of the Query Builder | ❓ | Not tested yet |
| ELEV | Query Designer: Text Verticalization | ❓ | Not tested yet |
| ENBC | Switch On/Off BAdI Implementation per IMG | ❓ | Not tested yet |
| ENHC | Composite Enhancement Implementation | ❓ | Not tested yet |
| ENHO | Enhancement Implementation | ❓ | Not tested yet |
| ENHS | Enhancement Spot | ❓ | Not tested yet |
| ENQU | Lock Object | ❓ | Not tested yet |
| ENSC | Composite Enhancement Spot | ❓ | Not tested yet |
| ENVM | BPC: Environment | ❓ | Not tested yet |
| EREL | Report Designer: Reusable Element | ❓ | Not tested yet |
| ERPT | BW Enterprise Report | ❓ | Not tested yet |
| ESH1 | ESH: CDS Search Model | ❓ | Not tested yet |
| ETDC | ETD Configuration | ❓ | Not tested yet |
| EVEN | Event- Administration Chains | ❓ | Not tested yet |
| EVTB | RAP Event Binding | ❓ | Not tested yet |
| EXCC | External operating system command defined by customer | ❓ | Not tested yet |
| EXCS | External operating system command delivered by SAP | ❓ | Not tested yet |
| FBPA | BW: Open ODS View | ❓ | Not tested yet |
| FBPD | BW: Open ODS View (SAP Delivery) | ❓ | Not tested yet |
| FDT0 | FDT/BRFplus: System Application | ❓ | Not tested yet |
| FDT1 | FDT/BRFplus: Customizing Application | ❓ | Not tested yet |
| FDT3 | BRFplus ATO Transport (Application) | ❓ | Not tested yet |
| FDT4 | BRFplus CTS Transport (System) | ❓ | Not tested yet |
| FDT5 | BRFplus CTS Transport (Customizing) | ❓ | Not tested yet |
| FILE | File Container | ❓ | Not tested yet |
| FORM | SAPscript Form | ❓ | Not tested yet |
| FSIP | Implementation Project (Service Implementation Workbench) | ❓ | Not tested yet |
| FTCT | Feature Toggle: activation for business configuration | ❓ | Not tested yet |
| FTG2 | Feature Toggle | ❓ | Not tested yet |
| FTGL | Feature toggle | ❓ | Not tested yet |
| FTIN | Feature Toggle - PFDB Innovation Data | ❓ | Not tested yet |
| FUGS | Function Group with Customer Include: SAP Part | ❓ | Not tested yet |
| FUGX | Function Group with Customer Include: Customer Part | ❓ | Not tested yet |
| FVAC | DMC: Migration Settings of a Fixed Value | ❓ | Not tested yet |
| FVAL | DMC: Definition and Standard Variant of a Fixed Value | ❓ | Not tested yet |
| G4BA | SAP Gateway OData V4 Backend Service Group & Assignments | ❓ | Not tested yet |
| G4BG | OBSOLETE - replaced by G4BA | ❓ | Not tested yet |
| G4BS | SAP Gateway OData V4 Backend Service | ❓ | Not tested yet |
| GADO | Generic Audit Filter - Registered Data Objects | ❓ | Not tested yet |
| GAFI | Generic Audit Filter - Audit Filter Set | ❓ | Not tested yet |
| GALF | Generic Audit Filter - Logical Field | ❓ | Not tested yet |
| GAPR | Generic Audit Filter - Mapp Report SelScreen to Data Object | ❓ | Not tested yet |
| GCCV | Cross-Client Validation Check | ❓ | Not tested yet |
| GCLP | Registry Entry of a Code in Generic Codelist Provider | ❓ | Not tested yet |
| GCPM | SAP Gateway OData Client Proxy - Proxy Model | ❓ | Not tested yet |
| GFSQ | Generic Fast Search Query | ❓ | Not tested yet |
| GFSV | Generic Fast Search View | ❓ | Not tested yet |
| GILE | GenIL Component Enhancement | ❓ | Not tested yet |
| GLOS | Transport of Glossary Tables | ❓ | Not tested yet |
| GPVD | Variants for locally gen.proga. with client-spec.meta object | ❓ | Not tested yet |
| GPVI | Variants for locally gen.prog.with client-indep.meta object | ❓ | Not tested yet |
| GSMP | Generic Simple Metric Provider | ❓ | Not tested yet |
| GURL | Predefined URL | ❓ | Not tested yet |
| HAAP | HANA Analysis Process | ❓ | Not tested yet |
| HCFQ | Help Center: FAQs | ❓ | Not tested yet |
| HCLN | Help Center: Documents | ❓ | Not tested yet |
| HCNS | Help Center: Namespace | ❓ | Not tested yet |
| HCPR | SAP HANA Composite Provider | ❓ | Not tested yet |
| HDSA | Derivation Tree (HDS) / Application Data | ❓ | Not tested yet |
| HDSI | Derivation Tree (HDS) / System Customizing | ❓ | Not tested yet |
| HDST | Derivation Tree (HDS) | ❓ | Not tested yet |
| HIER | BW Hierarchies | ❓ | Not tested yet |
| HLPF | Link DS/screen field | ❓ | Not tested yet |
| HOTA | Full Package (SAP HANA Transport for ABAP) | ❓ | Not tested yet |
| HRNR | Organizational Management and Workflow: Prefix Numbers | ❓ | Not tested yet |
| HTST | HTTP State | ❓ | Not tested yet |
| HTTP | HTTP Service | ❓ | Not tested yet |
| HYBR | HybridProvider | ❓ | Not tested yet |
| IAJU | IAC - JavaScript Objects (Non-Language-Specific) | ❓ | Not tested yet |
| IAKC | Table for Converting IAC Object Names | ❓ | Not tested yet |
| IAMA | MiniApps | ❓ | Not tested yet |
| IAML | Language-Dependent IAC Binary Data | ❓ | Not tested yet |
| IAMU | Language-Independent IAC Binary Data | ❓ | Not tested yet |
| IAMX | MiniApp | ❓ | Not tested yet |
| IAPD | Project Data for Implementation Assistant Nodes | ❓ | Not tested yet |
| IARP | Parameters of IAC Language Resource | ❓ | Not tested yet |
| IASP | Parameters of an IAC service | ❓ | Not tested yet |
| IATH | Implementation Assistant: Nodes | ❓ | Not tested yet |
| IATL | Language-Dependent IAC Templates | ❓ | Not tested yet |
| IATU | Language-Independent IAC Templates | ❓ | Not tested yet |
| IAXU | ITS: XML Templates for HTML Templates | ❓ | Not tested yet |
| ICFA | Administrative ICF services | ❓ | Not tested yet |
| IDCV | View of logical message for IDoc type | ❓ | Not tested yet |
| IDOC | IDoc Type | ❓ | Not tested yet |
| IEXT | Enhancement | ❓ | Not tested yet |
| IFFI | Interface Definition | ❓ | Not tested yet |
| IFFM | Interface Mapping | ❓ | Not tested yet |
| ILM1 | OBSOLETE, NOT TO BE USED | ❓ | Not tested yet |
| ILM2 | OBSOLETE, NOT TO BE USED | ❓ | Not tested yet |
| ILMB | ILM Object | ❓ | Not tested yet |
| ILMP | ILM Object (Paper Documents) | ❓ | Not tested yet |
| ILOT | Logic. Transport Object for Object Types for Object Relships | ❓ | Not tested yet |
| ILTP | Logical Transport Object for Relationship Types | ❓ | Not tested yet |
| INA1 | InA Service | ❓ | Not tested yet |
| INSP | IQM Inspection Plan (BI) | ❓ | Not tested yet |
| INTM | Intelligent Scenario Model | ❓ | Not tested yet |
| INTS | Intelligent Scenario | ❓ | Not tested yet |
| IOBC | InfoObject catalog | ❓ | Not tested yet |
| IOBJ | InfoObject | ❓ | Not tested yet |
| IOBV | BI InfoObject Texts for Text Verticalization | ❓ | Not tested yet |
| ISCP | Call Package | ❓ | Not tested yet |
| ISCS | Communication structure | ❓ | Not tested yet |
| ISET | InfoSet in BW | ❓ | Not tested yet |
| ISFS | DataSource Replica | ❓ | Not tested yet |
| ISIG | InfoPackage group | ❓ | Not tested yet |
| ISIP | InfoPackage | ❓ | Not tested yet |
| ISMD | InfoSource master data | ❓ | Not tested yet |
| ISMP | Transfer Rules | ❓ | Not tested yet |
| ISMT | Transfer InfoSource master data | ❓ | Not tested yet |
| ISRV | Intelligent Services | ❓ | Not tested yet |
| ISTD | InfoSource transaction data | ❓ | Not tested yet |
| ISTS | Transfer structure | ❓ | Not tested yet |
| ISTT | Transfer InfoSource transaction data | ❓ | Not tested yet |
| ISVC | Services: Assignment to Classes | ❓ | Not tested yet |
| ITEM | Transport Object for BW Web Items | ❓ | Not tested yet |
| IWCL | Logical information object | ❓ | Not tested yet |
| IWCP | Physical Information Object | ❓ | Not tested yet |
| IWCS | Structure storage system | ❓ | Not tested yet |
| IWMO | SAP Gateway Business Suite Enablement - Model | ❓ | Not tested yet |
| IWNG | Notification Gateway - Notification Provider Registration | ❓ | Not tested yet |
| IWOM | SAP Gateway: Model Metadata | ❓ | Not tested yet |
| IWPR | SAP Gateway BSE - Service Builder Project | ❓ | Not tested yet |
| IWSC | SAP Gateway:Screen scraping | ❓ | Not tested yet |
| IWSG | SAP Gateway: Service Groups Metadata | ❓ | Not tested yet |
| IWSV | SAP Gateway Business Suite Enablement - Service | ❓ | Not tested yet |
| IWVB | SAP Gateway Business Suite Enablement -Vocabulary Annotation | ❓ | Not tested yet |
| IWVO | SAP Gateway Business Suite Enablement - Vocabulary | ❓ | Not tested yet |
| JOBD | Technical Job Definition | ❓ | Not tested yet |
| JRNL | BPC: Journal | ❓ | Not tested yet |
| KPCE | BI: KPI Catalog Folder | ❓ | Not tested yet |
| KPDF | BI: KPI Definition | ❓ | Not tested yet |
| KWPL | KWPW: Logical Information Object | ❓ | Not tested yet |
| KWPP | KWPW: Physical Information Object (Help) | ❓ | Not tested yet |
| KWPW | KWPW: Structure Storage | ❓ | Not tested yet |
| LDBA | Logical Database | ❓ | Not tested yet |
| LOBJ | Object relevant for translation | ❓ | Not tested yet |
| LOIO | Solution Manager Document: Logical Info Object | ❓ | Not tested yet |
| LPDC | Launchpad short texts | ❓ | Not tested yet |
| LPDS | Launchpad Short Texts | ❓ | Not tested yet |
| LPDT | Launchpad Short Texts | ❓ | Not tested yet |
| LPOA | Semantically partitioned object: Active version | ❓ | Not tested yet |
| LPOD | Semantically partitioned object: Content version | ❓ | Not tested yet |
| LRCC | LRepository cross-client content | ❓ | Not tested yet |
| LRCD | LRepository client-dependent content | ❓ | Not tested yet |
| LRST | LRepository client-dependent content - customizing requests | ❓ | Not tested yet |
| LTHR | ALV: HTML Templates (Raw Version) | ❓ | Not tested yet |
| LTHT | ALV: HTML Templates (Translated Templates) | ❓ | Not tested yet |
| LTRC | Landscape Transformation Repository: Object Version | ❓ | Not tested yet |
| LTRD | Landscape Transformation Repository: Object Header | ❓ | Not tested yet |
| LTXP | Language Transport: Exit Handling | ❓ | Not tested yet |
| MAPN | Solution Map: Node definition | ❓ | Not tested yet |
| MCID | Matchcode ID | ❓ | Not tested yet |
| MCOB | Matchcode Object | ❓ | Not tested yet |
| MDGT | Transport Tool: Client Copy - Piece List | ❓ | Not tested yet |
| MESD | Mobile Solution Descriptor | ❓ | Not tested yet |
| MGCF | Device Configuration - Configuration Template | ❓ | Not tested yet |
| MODL | BPC: Model | ❓ | Not tested yet |
| MPRO | MultiProvider | ❓ | Not tested yet |
| MSAG | Message Class | ❓ | Not tested yet |
| MTXT | Manual Activities in the Correction Instructions | ❓ | Not tested yet |
| MWBU | MWB: Data for Integrated Upgrade | ❓ | Not tested yet |
| NHDU | HANA Transport Container | ❓ | Not tested yet |
| NHLC | HANA Language Container | ❓ | Not tested yet |
| NONT | RESTful ABAP Programming Model: Object Node Type | ❓ | Not tested yet |
| NOTE | SAP Note | ❓ | Not tested yet |
| NROB | Number Range Object | ❓ | Not tested yet |
| NSPC | Namespace in R/3 Repository | ❓ | Not tested yet |
| NTTA | Note Type Assignments for RAP | ❓ | Not tested yet |
| NTTY | Note Types for RAP | ❓ | Not tested yet |
| OA2G | OAuth 2.0 Scopeset | ❓ | Not tested yet |
| OA2P | OAuth 2.0 Client Profile | ❓ | Not tested yet |
| OA2S | OAuth2 Scope | ❓ | Not tested yet |
| OBJA | SOBJ: API called by an after import method | ❓ | Not tested yet |
| OBJM | SOBJ: Meta data of an AIM of a transport object | ❓ | Not tested yet |
| ODPE | Operational Data Provider (ESH-Based) | ❓ | Not tested yet |
| ODPN | ODP | ❓ | Not tested yet |
| ODSO | DataStore Object | ❓ | Not tested yet |
| OFAM | Logical Transport Object for Object Families | ❓ | Not tested yet |
| OMLM | Output Management: T100 Longtext Link Mapping | ❓ | Not tested yet |
| OSOA | DataSource (Active Version) | ❓ | Not tested yet |
| OSOD | DataSource (Delivered Version) | ❓ | Not tested yet |
| OTGR | Object type group | ❓ | Not tested yet |
| PAI1 | Predictive Analytics Integrator : Predictive Scenario | ❓ | Not tested yet |
| PAIM | Predictive Analytics Integrator : Predictive Model | ❓ | Not tested yet |
| PARA | SPA/GPA Parameters | ❓ | Not tested yet |
| PCEX | Exceptions for Package Check | ❓ | Not tested yet |
| PCFF | Predefined Custom Field | ❓ | Not tested yet |
| PCFN | Predefined Field: Extensible Node | ❓ | Not tested yet |
| PCHK | Setting Parameters for Package Check | ❓ | Not tested yet |
| PCLA | Program Class for BW Generation Tools | ❓ | Not tested yet |
| PDAC | Standard rule | ❓ | Not tested yet |
| PDTG | Task Group | ❓ | Not tested yet |
| PDTS | Standard Task | ❓ | Not tested yet |
| PDWA | Workflow Pattern with All Versions | ❓ | Not tested yet |
| PDWS | Workflow template | ❓ | Not tested yet |
| PE00 | Posting Engine Used TRules | ❓ | Not tested yet |
| PE01 | Migration Project - Direct Transfer | ❓ | Not tested yet |
| PE02 | Migration Object - Direct Transfer | ❓ | Not tested yet |
| PE12 | Migration Interface - Direct Transfer | ❓ | Not tested yet |
| PE14 | Migration Interface Mapping - Direct Transfer | ❓ | Not tested yet |
| PERS | Personalization object | ❓ | Not tested yet |
| PHIO | Solution Manager Document: Physical Info Object | ❓ | Not tested yet |
| PINF | Package interface | ❓ | Not tested yet |
| PLCR | Characteristic Relationship Object for Planning | ❓ | Not tested yet |
| PLDS | Planning Data Slices | ❓ | Not tested yet |
| PLGN | Plugin | ❓ | Not tested yet |
| PLGX | cCTS Service Plug-Ins | ❓ | Not tested yet |
| PLSE | Planning Service | ❓ | Not tested yet |
| PLSQ | Planning Sequence | ❓ | Not tested yet |
| PLST | Planning Service Type | ❓ | Not tested yet |
| PORG | Organizational Dependency Types (Product Master) | ❓ | Not tested yet |
| PRAG | Pragma in ABAP Source Code | ❓ | Not tested yet |
| PRAP | Logical Transport Object for Applications in Product Master | ❓ | Not tested yet |
| PRIN | Printer Description | ❓ | Not tested yet |
| PROJ | DMC: Definition of a Project | ❓ | Not tested yet |
| PROX | Proxy for Interface from IFR | ❓ | Not tested yet |
| PRWZ | Wizard Definition | ❓ | Not tested yet |
| PSRO | Project Status Report (Element and Sample) | ❓ | Not tested yet |
| PT01 | Migration Project Template - Direct Transfer | ❓ | Not tested yet |
| PT02 | Migration Object Template - Direct Transfer | ❓ | Not tested yet |
| PTYP | Logical Transport Object for Product Types | ❓ | Not tested yet |
| PURP | Purpose | ❓ | Not tested yet |
| QMML | KW: Logical Information Object (QM_MANUAL) | ❓ | Not tested yet |
| QMMP | Logical Transport Object | ❓ | Not tested yet |
| QMMS | KW: Structure repository for QMMANUAL | ❓ | Not tested yet |
| QVIW | Transport Object for BW Query View | ❓ | Not tested yet |
| RABR | Read Access Logging: Recording | ❓ | Not tested yet |
| RADB | Read Access Logging: Dynpro | ❓ | Not tested yet |
| RADY | Read Access Logging: Dynpro (old) | ❓ | Not tested yet |
| RAGB | Read Access Logging: Generic Channel | ❓ | Not tested yet |
| RAGC | Read Access Logging: Generic Channel (old) | ❓ | Not tested yet |
| RAPA | Planning package for the Report Agent | ❓ | Not tested yet |
| RARB | Read Access Logging: Remote Function Call | ❓ | Not tested yet |
| RARF | Read Access Logging: Remote Function Call (old) | ❓ | Not tested yet |
| RASB | Read Access Logging: Web-Service | ❓ | Not tested yet |
| RASE | Settings for the Report Agent (BW) | ❓ | Not tested yet |
| RAWB | Read Access Logging: Web Dynpro | ❓ | Not tested yet |
| RAWD | Read Access Logging: Web Dynpro (old) | ❓ | Not tested yet |
| RAWS | Read Access Logging: Web-Service (old) | ❓ | Not tested yet |
| RCAL | DMC: Rule Calls | ❓ | Not tested yet |
| RDOM | Read Access Logging: Log Domain | ❓ | Not tested yet |
| RECW | Recording Object for Web Dynpro Applications | ❓ | Not tested yet |
| REP0 | Reports | ❓ | Not tested yet |
| REP1 | Report Evaluations | ❓ | Not tested yet |
| REP2 | Reports | ❓ | Not tested yet |
| REP3 | Report Evaluations | ❓ | Not tested yet |
| REVN | Nodes for SAP Review Program | ❓ | Not tested yet |
| RFCT | Transport RFC Destination | ❓ | Not tested yet |
| RFST | RFC State | ❓ | Not tested yet |
| RGRP | Role Group | ❓ | Not tested yet |
| RLBL | Reuse Library: Libraries | ❓ | Not tested yet |
| RLBP | Reuse Library: Products | ❓ | Not tested yet |
| RLBT | Reuse Library: Transport Object for Structure Repository | ❓ | Not tested yet |
| RONT | RESTful ABAP Programming Model: Object (Node) Type | ❓ | Not tested yet |
| ROUT | Routine | ❓ | Not tested yet |
| RPDF | Report definition for the classification tool-set | ❓ | Not tested yet |
| RPUR | Read Access Logging: Purpose | ❓ | Not tested yet |
| RRCA | BW: RRI InfoCube Recipient | ❓ | Not tested yet |
| RRCD | BW: RRI InfoCube Recipient (SAP Outbound Delivery) | ❓ | Not tested yet |
| RRQA | BW: RRI Query Recipient | ❓ | Not tested yet |
| RRQD | BW: RRI Query Recipient (SAP Outbound Delivery) | ❓ | Not tested yet |
| RRUL | Remodeling Rule | ❓ | Not tested yet |
| RSDC | Display Component Tree | ❓ | Not tested yet |
| RSDS | DataSource in BW | ❓ | Not tested yet |
| RSFO | BW Formula | ❓ | Not tested yet |
| RSPC | Process chain | ❓ | Not tested yet |
| RSPE | BEx Personalization Application | ❓ | Not tested yet |
| RSPI | Interrupt Process | ❓ | Not tested yet |
| RSPT | Process Chain Starter | ❓ | Not tested yet |
| RSPV | Process variants | ❓ | Not tested yet |
| RSRV | Package for RSRV Tests | ❓ | Not tested yet |
| RULC | DMC: Migration Settings of a Rule | ❓ | Not tested yet |
| RULE | DMC: Definition and Implementation of a Rule | ❓ | Not tested yet |
| RVBA | Review Booklet Application | ❓ | Not tested yet |
| RVBC | Review Booklet Configuration | ❓ | Not tested yet |
| SAAC | Component Use in the System Administration Assistant | ❓ | Not tested yet |
| SAAT | Customizing Settings for System Administration Assistant | ❓ | Not tested yet |
| SACT | Standalone SAP Analytics Cloud Applications | ❓ | Not tested yet |
| SADT | ABAP Development Tools REST Service Group | ❓ | Not tested yet |
| SAID | Language-Independent Doc. for mySAP.com Application Server | ❓ | Not tested yet |
| SAIM | Audit Info System - Check Sets for Automatic Monitoring | ❓ | Not tested yet |
| SAIS | Data Object in Audit Info System | ❓ | Not tested yet |
| SAJC | Application Job Catalog Entry | ❓ | Not tested yet |
| SAJT | Application Job Template | ❓ | Not tested yet |
| SAJX | Application Job Template - App | ❓ | Not tested yet |
| SAJY | Application Job Catalog - App | ❓ | Not tested yet |
| SALC | Application Log Catalog Entry | ❓ | Not tested yet |
| SALO | Logical Info Object in SAP Solution Architect | ❓ | Not tested yet |
| SALV | ALV ATO Transport for Standard Layouts | ❓ | Not tested yet |
| SAMC | ABAP Messaging Channel Application | ❓ | Not tested yet |
| SAMD | S&AM Design Time Metadata | ❓ | Not tested yet |
| SAMS | SAM Metadata | ❓ | Not tested yet |
| SAMT | Message Types for ABAP Messaging Channels | ❓ | Not tested yet |
| SAPC | ABAP Push Channel Application | ❓ | Not tested yet |
| SAPH | Physical Info Object in SAP Solution Architect | ❓ | Not tested yet |
| SAPL | Storage Plan: SAP Records | ❓ | Not tested yet |
| SASD | Document for mySAP.com Application Server | ❓ | Not tested yet |
| SAUA | ABAP Unit Method Attributes | ❓ | Not tested yet |
| SBC1 | Techical Object Group | ❓ | Not tested yet |
| SBCL | Semantic Business Configuration Lock Definition | ❓ | Not tested yet |
| SBCT | Semantic Business Configuration Lock Token | ❓ | Not tested yet |
| SBDL | Logical information object for BDS | ❓ | Not tested yet |
| SBDP | Physical information object | ❓ | Not tested yet |
| SBDR | BDS: Relationship between information objects | ❓ | Not tested yet |
| SBEL | BW: LOIO Class Metadata | ❓ | Not tested yet |
| SBEP | BW: PHIO Class Metadata | ❓ | Not tested yet |
| SBGL | BW: LOIO Class Transaction Data | ❓ | Not tested yet |
| SBGP | BW: PHIO Class Transaction Data | ❓ | Not tested yet |
| SBHL | Logical Information Object for BDS | ❓ | Not tested yet |
| SBHP | Logical Information Object for BDS | ❓ | Not tested yet |
| SBHR | BDS: Relationship Between Information Objects | ❓ | Not tested yet |
| SBIL | Logical Information Object for BDS | ❓ | Not tested yet |
| SBIP | Physical Information Object | ❓ | Not tested yet |
| SBIR | Relationship between Information Objects | ❓ | Not tested yet |
| SBJL | Logical Information Object for BDS | ❓ | Not tested yet |
| SBJP | Logical Information Object for BDS | ❓ | Not tested yet |
| SBJR | BDS: Relationship Between Information Objects | ❓ | Not tested yet |
| SBLE | Customer Extension of Business Logic with restricted ABAP | ❓ | Not tested yet |
| SBNL | Logical Information Object for BDS | ❓ | Not tested yet |
| SBNP | Logical Information Object for BDS | ❓ | Not tested yet |
| SBNR | BDS: Relationship Between Information Objects | ❓ | Not tested yet |
| SBOL | Logical information object for BDS | ❓ | Not tested yet |
| SBOP | Physical information object | ❓ | Not tested yet |
| SBOR | BDS: Relationship between information objects | ❓ | Not tested yet |
| SBWL | Logical information object for BDS | ❓ | Not tested yet |
| SBWP | Logical information object for BDS | ❓ | Not tested yet |
| SBWR | BDS: Relationship between information objects | ❓ | Not tested yet |
| SBXL | Logical information object for BDS: AEW ABAP tools | ❓ | Not tested yet |
| SBXP | Physical information object | ❓ | Not tested yet |
| SBXR | BDS: Relationship between information objects | ❓ | Not tested yet |
| SBYL | Logical information object for BDS | ❓ | Not tested yet |
| SBYP | Logical information object for BDS | ❓ | Not tested yet |
| SBYR | BDS: Relationship between information objects | ❓ | Not tested yet |
| SCAT | Test case | ❓ | Not tested yet |
| SCAU | Customer authorization groups (SREPOATH) | ❓ | Not tested yet |
| SCBE | Custom Behaviour Extensions | ❓ | Not tested yet |
| SCBO | Custom Business Object | ❓ | Not tested yet |
| SCCL | Custom Code List | ❓ | Not tested yet |
| SCCV | Custom CDS Views | ❓ | Not tested yet |
| SCDT | Mapping Information for Scout and Customizing Synchronizer | ❓ | Not tested yet |
| SCGR | Service Consumer Group | ❓ | Not tested yet |
| SCHK | Check Results Management: Check ID | ❓ | Not tested yet |
| SCME | Custom Metadata Extension | ❓ | Not tested yet |
| SCNT | Workflow Container PPF (Definition + Data) | ❓ | Not tested yet |
| SCON | Parameter Condition | ❓ | Not tested yet |
| SCP1 | BC Set or Customizing Profile | ❓ | Not tested yet |
| SCP2 | Switch BC Sets | ❓ | Not tested yet |
| SCPD | SAP codepage definition | ❓ | Not tested yet |
| SCPR | Customizing Profile | ❓ | Not tested yet |
| SCPS | Code Page Segment | ❓ | Not tested yet |
| SCPX | BC Set: Exception Handling | ❓ | Not tested yet |
| SCRL | Custom Reuse Library | ❓ | Not tested yet |
| SCTA | Context Attributes (Central Context Management) | ❓ | Not tested yet |
| SCTM | Context Object Type (Central Context Management) | ❓ | Not tested yet |
| SCUH | Replacement information for hierarchies | ❓ | Not tested yet |
| SCUT | Customizing templates | ❓ | Not tested yet |
| SCVI | Screen variants | ❓ | Not tested yet |
| SDAT | SAP Delivered Table Authorization Group Assignments | ❓ | Not tested yet |
| SDBP | Microsoft SQL Server | ❓ | Not tested yet |
| SDEP | Object dependency | ❓ | Not tested yet |
| SDER | Spool: Device Description - Use SPDV Instead | ❓ | Not tested yet |
| SDEV | Output Devices (Use SPDV Instead) | ❓ | Not tested yet |
| SDM0 | DME: Metadata to describe a maintenance object | ❓ | Not tested yet |
| SDM1 | DME: Dialog pool | ❓ | Not tested yet |
| SDMI | TLogo for Silent Data Migration (Metadata for SUM uptime) | ❓ | Not tested yet |
| SECU | Security Audit Log Configuration | ❓ | Not tested yet |
| SEGR | Semantic Group | ❓ | Not tested yet |
| SESA | Enterprise Search: DDL Activation | ❓ | Not tested yet |
| SESR | Enterprise Search: Ranking Factor | ❓ | Not tested yet |
| SEST | Enterprise Search: Template | ❓ | Not tested yet |
| SETA | Entries in the Table COMC_SETTYP_ATTR | ❓ | Not tested yet |
| SETG | Object List for the Set Type Generation | ❓ | Not tested yet |
| SETO | Object Types in the Set Type Generation | ❓ | Not tested yet |
| SETT | Logical Transport Object for Set Types | ❓ | Not tested yet |
| SF01 | Status Tables Switch Framework Client-Specific | ❓ | Not tested yet |
| SF02 | Status Tables Switch Framework Cross-Client | ❓ | Not tested yet |
| SFB1 | Business Function Set | ❓ | Not tested yet |
| SFB2 | Business Function | ❓ | Not tested yet |
| SFBF | Business Function + Assignment | ❓ | Not tested yet |
| SFBS | Business Function Set + Assignment | ❓ | Not tested yet |
| SFCS | Conflict Switch Assignment - Dependent Switches | ❓ | Not tested yet |
| SFHI | Logical object - information object: System info - note | ❓ | Not tested yet |
| SFKX | Foreign Key Check Exception | ❓ | Not tested yet |
| SFLO | Form Template Logo | ❓ | Not tested yet |
| SFNH | Hierarchy Nodes in Complete List of Release Notes | ❓ | Not tested yet |
| SFPF | Form Object: Form | ❓ | Not tested yet |
| SFPI | Form Object: Interface | ❓ | Not tested yet |
| SFRH | SAPscript Form Tree: Transport Object for Node | ❓ | Not tested yet |
| SFRN | Logical object - information object: Release note | ❓ | Not tested yet |
| SFSS | Status of Switch | ❓ | Not tested yet |
| SFSW | Switch + Assignment of Objects to the Switch | ❓ | Not tested yet |
| SFSY | Logical object - hypertext: System profile parameter supplmt | ❓ | Not tested yet |
| SFTE | Form Template Text | ❓ | Not tested yet |
| SGFL | Global fields | ❓ | Not tested yet |
| SHAP | Shadow Tables for Application Components (Obsolete!) | ❓ | Not tested yet |
| SHAR | Nodes for archived structures read back | ❓ | Not tested yet |
| SHCS | OBSOLET shadow table communication structure | ❓ | Not tested yet |
| SHDI | Image data for transaction variants | ❓ | Not tested yet |
| SHDS | Shadow Table DataSource | ❓ | Not tested yet |
| SHFS | Can Maintain Data Source Manually - not R/3 (SAP Delivery) | ❓ | Not tested yet |
| SHI0 | Link type definition of general structure storage | ❓ | Not tested yet |
| SHI1 | Node type definition of general structure storage | ❓ | Not tested yet |
| SHI2 | Structure types of general structure storage | ❓ | Not tested yet |
| SHI3 | General structure storage: Definition of a structure | ❓ | Not tested yet |
| SHI5 | Gen. hierarchy storage extrension name | ❓ | Not tested yet |
| SHI6 | Gen. structure repos.: Extension ID / structure assignment | ❓ | Not tested yet |
| SHI7 | General hierarchy store node attribute | ❓ | Not tested yet |
| SHI8 | SFW Switch Assignment in Hierarchy Tool | ❓ | Not tested yet |
| SHI9 | General Structure Repository: Enhancement ID Order | ❓ | Not tested yet |
| SHIC | Hierarchy Tool: Comparison of Structures | ❓ | Not tested yet |
| SHIG | InfoPackage Group (SAP Delivery) Obsolete !!! | ❓ | Not tested yet |
| SHIM | OBSOLETE Shadow Tables InfoSource Master Data | ❓ | Not tested yet |
| SHIN | General structure storage: Definition of nodes | ❓ | Not tested yet |
| SHIP | InfoPackage (SAP Delivery) | ❓ | Not tested yet |
| SHIT | OBSOLETE Shadow Tables InfoSource Transaction Data | ❓ | Not tested yet |
| SHIV | Hierarchy Tool: Version of a Structure | ❓ | Not tested yet |
| SHK4 | SDOK: KPro Structure Repository (Definition of Nodes) | ❓ | Not tested yet |
| SHLP | Search Help | ❓ | Not tested yet |
| SHMA | Shared Objects: Defined Area Attributes | ❓ | Not tested yet |
| SHMP | Mapping DataS./Fields and InfoS/Objects (SAP Delivery) | ❓ | Not tested yet |
| SHPH | Project management: Node definitions | ❓ | Not tested yet |
| SHTR | Transfer Structure - 2.0  (SAP Delivery) | ❓ | Not tested yet |
| SHTS | Shadow Tables Transfer Structure | ❓ | Not tested yet |
| SHY6 | Hierarchy Storage - Structure Assignment to Enhancement ID | ❓ | Not tested yet |
| SI0L | KEN: Logical information object (general) | ❓ | Not tested yet |
| SI0P | KEN: Physical information object (general) | ❓ | Not tested yet |
| SI0R | KEN: Relationship between information objects (general) | ❓ | Not tested yet |
| SI0S | KEN: Structure repository for general objects | ❓ | Not tested yet |
| SI2L | KEN: Logical information object (training) | ❓ | Not tested yet |
| SI2P | KEN: Physical information object (training) | ❓ | Not tested yet |
| SI2R | KEN: Relationship between information objects (training) | ❓ | Not tested yet |
| SI2S | KW: Structure repository for training | ❓ | Not tested yet |
| SI3L | NR3: Logical Information Object (Help) | ❓ | Not tested yet |
| SI3P | NR3: Physical Information Object (Help) | ❓ | Not tested yet |
| SI3R | NR3: Relationship Between Information Objects (Help) | ❓ | Not tested yet |
| SICF | ICF Service | ❓ | Not tested yet |
| SIFL | Workflow Documents: Logical Information Object | ❓ | Not tested yet |
| SIFP | Workflow Documents: Physical Information Object | ❓ | Not tested yet |
| SIM1 | IMG attributes | ❓ | Not tested yet |
| SIMH | IMG Structure Repository: Nodes | ❓ | Not tested yet |
| SIRA | Definition of an IO attribute (runtime object) | ❓ | Not tested yet |
| SIRC | Definition of an IO class (runtime object) | ❓ | Not tested yet |
| SIRE | KPro: Content Repository for contents of information objects | ❓ | Not tested yet |
| SIRL | Logical information object | ❓ | Not tested yet |
| SIRM | Physical Information Object (Language Delivery-Compatible) | ❓ | Not tested yet |
| SIRP | Physical information object | ❓ | Not tested yet |
| SIRR | Relationship between information objects | ❓ | Not tested yet |
| SIRS | Customizing for Content Repositories | ❓ | Not tested yet |
| SISM | ISM Channel Group | ❓ | Not tested yet |
| SIWL | KEN: Logical information object (help) | ❓ | Not tested yet |
| SIWP | KEN: Physical information object (help) | ❓ | Not tested yet |
| SIWR | KEN: Relationship between information objects (help) | ❓ | Not tested yet |
| SIWS | KW: Structure repository for application help | ❓ | Not tested yet |
| SIXO | Index objects for logical databases | ❓ | Not tested yet |
| SIXT | Index types for logical databases | ❓ | Not tested yet |
| SKDL | KW: Logical Info Object (KW_DEMO) | ❓ | Not tested yet |
| SKDP | KW: Physical Info Object (KW_DEMO) | ❓ | Not tested yet |
| SKDS | Structure Storage for KW_DEMO | ❓ | Not tested yet |
| SKTD | Knowledge Transfer Document - Documentation Infrastructure | ❓ | Not tested yet |
| SKWL | KW: Logical Information Object (KWNet) | ❓ | Not tested yet |
| SKWN | KW: Structure Storage for HTML-Based Documents | ❓ | Not tested yet |
| SKWP | KW: Physical Information Object (KWNet) | ❓ | Not tested yet |
| SKWS | CM: Status Management | ❓ | Not tested yet |
| SLDC | Active Generic Application Access Rules | ❓ | Not tested yet |
| SLDD | Generic Application Access Rules (Definition) | ❓ | Not tested yet |
| SLDH | Generic Allowlist - Header Data | ❓ | Not tested yet |
| SLDO | SLAD: Object Set | ❓ | Not tested yet |
| SLDP | SLAD: Profile | ❓ | Not tested yet |
| SLEC | LEI Event Linkages (Customizing) | ❓ | Not tested yet |
| SLEI | LEI Event Linkages (Design) | ❓ | Not tested yet |
| SLOM | Logical output management systems | ❓ | Not tested yet |
| SMBC | Business Configuration Object | ❓ | Not tested yet |
| SMBL | XML Message Broker: Pipeline | ❓ | Not tested yet |
| SMD1 | Definition of an R-LOIO class | ❓ | Not tested yet |
| SMD2 | Definition of a V-LOIO class | ❓ | Not tested yet |
| SMD3 | Definition of an R-PHIO class | ❓ | Not tested yet |
| SMD4 | Definition of a V-PHIO class | ❓ | Not tested yet |
| SMD5 | Definition of an R-RELA class | ❓ | Not tested yet |
| SMD6 | Definition of a V-RELA class | ❓ | Not tested yet |
| SMDA | Definition of an IO attribute | ❓ | Not tested yet |
| SMDC | IO class link area | ❓ | Not tested yet |
| SMDD | DDIC Modification Logs | ❓ | Not tested yet |
| SMDK | Definition of a context class | ❓ | Not tested yet |
| SMDL | Internal Use | ❓ | Not tested yet |
| SMDM | Document model area | ❓ | Not tested yet |
| SMEH | Area Menu | ❓ | Not tested yet |
| SMIF | Matching Interface | ❓ | Not tested yet |
| SMIM | Info Object from the MIME Repository | ❓ | Not tested yet |
| SMOD | SAP enhancements | ❓ | Not tested yet |
| SMP0 | Solution Map: Process category | ❓ | Not tested yet |
| SMP1 | Solution Map: Main process | ❓ | Not tested yet |
| SMP2 | Solution Map: Process | ❓ | Not tested yet |
| SMPB | Solution Map: Best Practice | ❓ | Not tested yet |
| SMPC | Solution Map: Component | ❓ | Not tested yet |
| SMPD | Solution Map: Product information | ❓ | Not tested yet |
| SMPI | Solution Map: Key Performance Indicator | ❓ | Not tested yet |
| SMPP | Solution Map: Partner product | ❓ | Not tested yet |
| SMTC | Service Mapping Tool, Customer Mappings | ❓ | Not tested yet |
| SMTE | Service Mapping Tool: Extension | ❓ | Not tested yet |
| SMTG | OM: Email Template | ❓ | Not tested yet |
| SMTO | Service Mapping Tool | ❓ | Not tested yet |
| SMTV | Service Mapping Tool: Variant | ❓ | Not tested yet |
| SNAP | SNAPT texts (long texts for ABAP/4 short dump analysis) | ❓ | Not tested yet |
| SOAS | BTFR: Object Type-Specific Attributes Long Texts | ❓ | Not tested yet |
| SOAT | BTFR: Object Type-Specific Attributes Short Texts | ❓ | Not tested yet |
| SOBJ | Business object types | ❓ | Not tested yet |
| SOD1 | Api Package | ❓ | Not tested yet |
| SOD2 | API Package Assignment | ❓ | Not tested yet |
| SOMS | Output management systems | ❓ | Not tested yet |
| SONT | SAP Object Node Type | ❓ | Not tested yet |
| SOT1 | SAP Object Type | ❓ | Not tested yet |
| SOTR | All Concepts (OTR) of a Package - Short Texts | ❓ | Not tested yet |
| SOTS | All Concepts (OTR) of a Package - Long Texts | ❓ | Not tested yet |
| SPAR | Parameter Storage: Transport Object | ❓ | Not tested yet |
| SPCD | Command records to print | ❓ | Not tested yet |
| SPCO | Char. set manufacturers | ❓ | Not tested yet |
| SPCS | Character sets | ❓ | Not tested yet |
| SPDV | Spool: Output Devices | ❓ | Not tested yet |
| SPFL | Profile parameter | ❓ | Not tested yet |
| SPLO | Format Types | ❓ | Not tested yet |
| SPOK | BW InfoSpoke | ❓ | Not tested yet |
| SPPC | Normal Print Controls | ❓ | Not tested yet |
| SPPF | Page formats | ❓ | Not tested yet |
| SPRF | CheckMan: Logical Transport Object Check Profile | ❓ | Not tested yet |
| SPRJ | DMC: Definition of a Sub-Project | ❓ | Not tested yet |
| SPRL | SPRO: Transport object for logical information objects | ❓ | Not tested yet |
| SPRO | Projects | ❓ | Not tested yet |
| SPRP | SPRO: Physical transport object for project documents | ❓ | Not tested yet |
| SPRS | Printer Resources | ❓ | Not tested yet |
| SPRV | Service Provider for ADT | ❓ | Not tested yet |
| SPRX | Proxy Object | ❓ | Not tested yet |
| SPSE | Security: PSE Definition | ❓ | Not tested yet |
| SPSV | Spool: Formatting server | ❓ | Not tested yet |
| SPTP | Text pool for print formats | ❓ | Not tested yet |
| SQAB | Industry-specific question | ❓ | Not tested yet |
| SQAC | Question Category | ❓ | Not tested yet |
| SQAG | Industry-specific configuration group | ❓ | Not tested yet |
| SQAK | Configuration group | ❓ | Not tested yet |
| SQAQ | Question | ❓ | Not tested yet |
| SQAV | Question Context | ❓ | Not tested yet |
| SQBR | Industry | ❓ | Not tested yet |
| SQL1 | SQL Service Binding (SQL1) | ❓ | Not tested yet |
| SQLI | Links for Implementation Assistant | ❓ | Not tested yet |
| SQSC | Database Procedure Proxy | ❓ | Not tested yet |
| SRAE | Index Management Application Exit | ❓ | Not tested yet |
| SRAL | Read Access Logging: User Blacklist | ❓ | Not tested yet |
| SRC0 | Logical Information Object For SRM | ❓ | Not tested yet |
| SRC1 | Physical Information Object for SRM | ❓ | Not tested yet |
| SRC2 | Logical Information Object For SRM | ❓ | Not tested yet |
| SRC3 | Physical Information Object for SRM | ❓ | Not tested yet |
| SRC4 | Logical Information Object For SRM | ❓ | Not tested yet |
| SRC5 | Physical Information Object for SRM | ❓ | Not tested yet |
| SRC6 | Logical Information Object For SRM | ❓ | Not tested yet |
| SRC7 | Physical Information Object for SRM | ❓ | Not tested yet |
| SREL | DMC: Structure Relations | ❓ | Not tested yet |
| SRFC | RFC Service | ❓ | Not tested yet |
| SRHL | SRM: Hierarchical Lists | ❓ | Not tested yet |
| SRLD | Language-Dependent Client-Specific Retrieval Index Object | ❓ | Not tested yet |
| SRLI | Language-Dependent Cross-Client Retrieval Index Object | ❓ | Not tested yet |
| SRM1 | Element Type | ❓ | Not tested yet |
| SRM2 | Service Provider | ❓ | Not tested yet |
| SRM3 | Area - Definition | ❓ | Not tested yet |
| SRM4 | Area - Value for SPS Classification Parameter | ❓ | Not tested yet |
| SRM5 | Class Role | ❓ | Not tested yet |
| SRM6 | Service Provider Type | ❓ | Not tested yet |
| SRM7 | Records Management: Component Role | ❓ | Not tested yet |
| SRSR | Search Server Relation | ❓ | Not tested yet |
| SRTD | Transport Release/Configuration for SOAP Runtime | ❓ | Not tested yet |
| SRTI | Index Category | ❓ | Not tested yet |
| SRTL | Transport Object: SOAP Runtime Logical Port | ❓ | Not tested yet |
| SRTR | Report tree | ❓ | Not tested yet |
| SRVB | Service Binding | ❓ | Not tested yet |
| SRVC | Service Consumption Model | ❓ | Not tested yet |
| SRVD | Service Definition | ❓ | Not tested yet |
| SSB0 | Groups | ❓ | Not tested yet |
| SSB1 | KPIs | ❓ | Not tested yet |
| SSB2 | DO NOT USE -- Basic Data of Chips Representing KPI-Tiles | ❓ | Not tested yet |
| SSB3 | DO NOT USE -- Drill-Down-App Configurations in SSB | ❓ | Not tested yet |
| SSB4 | Associations between Groups | ❓ | Not tested yet |
| SSB5 | Groups | ❓ | Not tested yet |
| SSB6 | KPIs | ❓ | Not tested yet |
| SSB7 | Associations between Groups | ❓ | Not tested yet |
| SSB8 | Generic Drilldown Reports | ❓ | Not tested yet |
| SSB9 | Reports | ❓ | Not tested yet |
| SSFO | SAP Smart Form | ❓ | Not tested yet |
| SSST | SAP Smart Style | ❓ | Not tested yet |
| STC1 | Configuration Entity | ❓ | Not tested yet |
| STC2 | Technical Configuration Set | ❓ | Not tested yet |
| STC4 | Technical Configuration Layer | ❓ | Not tested yet |
| STC5 | Technical Configuration LM Scenario | ❓ | Not tested yet |
| STCB | TC Task List Group | ❓ | Not tested yet |
| STCS | TC Task List | ❓ | Not tested yet |
| STCV | TC Task List Variant | ❓ | Not tested yet |
| STOB | Structured Object | ❓ | Not tested yet |
| STOR | Storage Parameters | ❓ | Not tested yet |
| STVI | Transaction variants (cross-client) | ❓ | Not tested yet |
| STVR | Transaction variants | ❓ | Not tested yet |
| STYC | Embedded Analytics Story | ❓ | Not tested yet |
| STYL | SAPscript Style | ❓ | Not tested yet |
| SUCC | Scenario for Switchable Authorization Check (Runtime) | ❓ | Not tested yet |
| SUCD | Scenario for Switchable Authorization Check (Definition) | ❓ | Not tested yet |
| SUCK | Header Data for General Authorization Groups | ❓ | Not tested yet |
| SUCO | Assign Authorization Default Variant > Application | ❓ | Not tested yet |
| SUCU | Authorization Groups (TBRG_AUTH) | ❓ | Not tested yet |
| SUKR | Kernel Trace Revocation Object | ❓ | Not tested yet |
| SUSC | Authorization object class | ❓ | Not tested yet |
| SUSH | Assignment: Service --> Authorization Objects | ❓ | Not tested yet |
| SUSI | Assignment: Service --> Authorization Objects (with TADIR) | ❓ | Not tested yet |
| SUSK | Customer: Assignment of transaction -> authorization object | ❓ | Not tested yet |
| SUSO | Authorization object | ❓ | Not tested yet |
| SUSP | Templates for authorization profiles (Profile Generator) | ❓ | Not tested yet |
| SUST | Assignment transaction > auth. objects | ❓ | Not tested yet |
| SVAL | Version Management: Object Type Alias | ❓ | Not tested yet |
| SVCI | Selection Variants (Cross-Client) | ❓ | Not tested yet |
| SWFC | Workflow Correlation Definition | ❓ | Not tested yet |
| SWFL | WF: Logical Information Object | ❓ | Not tested yet |
| SWFP | WF: Physical Information Object | ❓ | Not tested yet |
| SWFS | Service-Definition for WebFlow | ❓ | Not tested yet |
| SWFT | Workflow: process type | ❓ | Not tested yet |
| SWFX | Workflow XML Proxy | ❓ | Not tested yet |
| SWHL | Logical Information Object for BDS: Excel Templates | ❓ | Not tested yet |
| SWHP | Logical Information Object for BDS: Excel Templates | ❓ | Not tested yet |
| SWHR | BDS: Relationship Between Information Objects:Excel Template | ❓ | Not tested yet |
| SWKL | Transport Object for SEM_STS | ❓ | Not tested yet |
| SWKP | Logical Information Object for BDS | ❓ | Not tested yet |
| SWKR | BDS: Relationship Between Information Objects | ❓ | Not tested yet |
| SXCC | Customizing Entries for Business Add-In Implementations | ❓ | Not tested yet |
| SXCI | Business Add-Ins - Implementations | ❓ | Not tested yet |
| SXFT | Customizing Entries for BAdI Definitions (Sorting) | ❓ | Not tested yet |
| SXMS | Interfaces for Archiving | ❓ | Not tested yet |
| SXSD | Business Add-Ins - Definitions | ❓ | Not tested yet |
| SYAG | System Log Messages | ❓ | Not tested yet |
| SYND | Syntax Documentation | ❓ | Not tested yet |
| TAAV | Table Analysis: Analysis Variant | ❓ | Not tested yet |
| TABU | Table Contents | ❓ | Not tested yet |
| TAPL | CTS: Template application type | ❓ | Not tested yet |
| TAVF | Table Analysis: Virtual Field | ❓ | Not tested yet |
| TBPS | Long texts for Tasked-Based Process Steps | ❓ | Not tested yet |
| TDAT | Customizing: Table Contents | ❓ | Not tested yet |
| TEAM | BPC: Team | ❓ | Not tested yet |
| TERM | Transport of Terminology Tables | ❓ | Not tested yet |
| TEXT | SAPscript Text | ❓ | Not tested yet |
| TFRT | Font | ❓ | Not tested yet |
| THED | Themes D version | ❓ | Not tested yet |
| THEM | Themes for BW Frontend (Analyzer, Reportdesigner) | ❓ | Not tested yet |
| THJT | Key Date of Type Derivation | ❓ | Not tested yet |
| TIMR | Date Rule | ❓ | Not tested yet |
| TMCO | TMC: Content Object | ❓ | Not tested yet |
| TMCW | Technical Monitoring Content | ❓ | Not tested yet |
| TMPL | BW Web Templates | ❓ | Not tested yet |
| TMWO | Tracking Multiplexer runs without Object List | ❓ | Not tested yet |
| TOBJ | Definition of a Maintenance and Transport Object | ❓ | Not tested yet |
| TRAN | Transaction | ❓ | Not tested yet |
| TRCS | Communication Structure for Transformation | ❓ | Not tested yet |
| TREP | Transformation Rule Repository | ❓ | Not tested yet |
| TRFN | Transformation | ❓ | Not tested yet |
| TRIF | Interface Definition | ❓ | Not tested yet |
| TRIM | Interface Mapping | ❓ | Not tested yet |
| TRMS | Transport of Syntax Check Messages | ❓ | Not tested yet |
| TROB | DMC: Definition of a Translation Object | ❓ | Not tested yet |
| TROC | DMC: Migration Settings of a Translation Object | ❓ | Not tested yet |
| TRPC | Translation Project - Customizing | ❓ | Not tested yet |
| TRPR | Translation Project | ❓ | Not tested yet |
| TRUC | Transformation Rule (Client Dependent) | ❓ | Not tested yet |
| TRUL | Transformation Rule | ❓ | Not tested yet |
| TTPL | Transaction Templates for Activity Groups | ❓ | Not tested yet |
| TTYP | Table Type | ❓ | Not tested yet |
| TUSE | TLOGO for Client Provisioning Include List | ❓ | Not tested yet |
| TVNS | Variant Group Definition | ❓ | Not tested yet |
| TVUS | Assignment User - Variant Group | ❓ | Not tested yet |
| TWBH | Test catalog | ❓ | Not tested yet |
| TYPE | Type Group | ❓ | Not tested yet |
| UAPO | Logical object ADW position | ❓ | Not tested yet |
| UCLO | Logical object area | ❓ | Not tested yet |
| UCOC | Transportobject UCON HTTP Customizing Object | ❓ | Not tested yet |
| UCOP | UCON: Transport object for Ucon Http Server Profile | ❓ | Not tested yet |
| UCSA | Unified Connectivity Service Assembly | ❓ | Not tested yet |
| UCSM | Transport object for SMTP hosts | ❓ | Not tested yet |
| UCVH | Transportobject for virtual hosts | ❓ | Not tested yet |
| UDMO | Data model | ❓ | Not tested yet |
| UDSC | Web Service User defined Search Configuration | ❓ | Not tested yet |
| UENO | Entity type | ❓ | Not tested yet |
| UFKT | Logical object - function | ❓ | Not tested yet |
| UHIE | Logical object - hierarchy | ❓ | Not tested yet |
| UI5F | UI5 File | ❓ | Not tested yet |
| UIAA | Fiori Launchpad App Descriptor Item Adaptation | ❓ | Not tested yet |
| UIAC | Fiori Launchpad Technical Catalog | ❓ | Not tested yet |
| UIAD | Fiori Launchpad App Descriptor Item | ❓ | Not tested yet |
| UIBA | UI2 Business Application | ❓ | Not tested yet |
| UIPC | Fiori Launchpad Page - Customizing | ❓ | Not tested yet |
| UIPG | Fiori Launchpad Page Template | ❓ | Not tested yet |
| UISC | Fiori Launchpad Space - Customizing | ❓ | Not tested yet |
| UIST | Fiori Launchpad Space Template | ❓ | Not tested yet |
| UOMT | Quantity Conversion Type | ❓ | Not tested yet |
| UPDR | Update rules | ❓ | Not tested yet |
| UWSF | Web Service Definition | ❓ | Not tested yet |
| UWSS | Web Survey Definition | ❓ | Not tested yet |
| UWST | Target Group Hierarchy | ❓ | Not tested yet |
| UXSD | Web Service Component | ❓ | Not tested yet |
| VBAP | Visual Business Application | ❓ | Not tested yet |
| VCLS | View cluster | ❓ | Not tested yet |
| VCN0 | VRS/CWB Testobject | ❓ | Not tested yet |
| VCN1 | VRS/CWB Testobject | ❓ | Not tested yet |
| VDAT | View Maintenance: Data | ❓ | Not tested yet |
| VERS | Version Number | ❓ | Not tested yet |
| VERT | Text Verticalization | ❓ | Not tested yet |
| VRBL | DMC: Definition of a Variable | ❓ | Not tested yet |
| VTRM | Verticalization Terminology | ❓ | Not tested yet |
| VTRR | Verticalization: Text repository Registration | ❓ | Not tested yet |
| VWDF | View Definition of Migration Object Modeler | ❓ | Not tested yet |
| W3HT | Web Reporting/Internet Transaction Server HTML Templates | ❓ | Not tested yet |
| W3MI | Web Reporting/Internet Transaction Server MIME Types(binary | ❓ | Not tested yet |
| WAPA | BSP (Business Server Pages) Application | ❓ | Not tested yet |
| WBTT | ABAP Workbench: Dummy object type for unit tests | ❓ | Not tested yet |
| WCPO | Workload Capture Profile | ❓ | Not tested yet |
| WDCA | Web Dynpro Application Configuration | ❓ | Not tested yet |
| WDCC | Web Dynpro Component Configuration | ❓ | Not tested yet |
| WDCL | Web Dynpro Customizing Data | ❓ | Not tested yet |
| WDCP | Web Dynpro CHIP | ❓ | Not tested yet |
| WDRC | Web Dynpro Condition for a Recording Plug-In | ❓ | Not tested yet |
| WDRP | Web Dynpro Recording Plug-In | ❓ | Not tested yet |
| WDYA | Web Dynpro Application | ❓ | Not tested yet |
| WDYL | Web Dynpro : UI Element Library | ❓ | Not tested yet |
| WDYN | Web Dynpro Component | ❓ | Not tested yet |
| WEBI | Virtual End Point | ❓ | Not tested yet |
| WEBS | Web Services | ❓ | Not tested yet |
| WGRP | Object Type Group (ABAP Workbench / R3TR) | ❓ | Not tested yet |
| WKSP | BPC: workspace | ❓ | Not tested yet |
| WMPC | Workload Management Process Classes | ❓ | Not tested yet |
| WSNO | Workspace Folder | ❓ | Not tested yet |
| WSPT | APC WebSocket protocol type | ❓ | Not tested yet |
| WSSC | Workflow Scenario | ❓ | Not tested yet |
| WTAG | BSP Extension | ❓ | Not tested yet |
| WTHM | O2: Topics for BSP Application | ❓ | Not tested yet |
| WWIB | BW Web Item (BI-Runtime) | ❓ | Not tested yet |
| WWIT | Item in Web framework | ❓ | Not tested yet |
| WWPA | BW Web Runtime:  Parameter (for Web Item or Command) | ❓ | Not tested yet |
| WXML | 02: XML Descriptions | ❓ | Not tested yet |
| X4WS | Workspace information for X4 Activation | ❓ | Not tested yet |
| XCLA | Logical Transport Object for Conversion Class (XCLA) | ❓ | Not tested yet |
| XCLS | Xcelcius Dashboard | ❓ | Not tested yet |
| XDPL | SAP KW: Logical IO for Area XML_DOKU | ❓ | Not tested yet |
| XDPP | KW: Physical IO for Area XML_DOKU | ❓ | Not tested yet |
| XDPS | KW: Structure Repository for Area XML_DOKU | ❓ | Not tested yet |
| XDYN | Screens with field exit | ❓ | Not tested yet |
| XINX | Ext. Index | ❓ | Not tested yet |
| XLWB | Excel workbook | ❓ | Not tested yet |
| XMLL | KW: Logical IO | ❓ | Not tested yet |
| XMLP | KW: Physical IO | ❓ | Not tested yet |
| XMLS | KW: Structure repository for objects | ❓ | Not tested yet |
| XPRA | Program Run after Transport | ❓ | Not tested yet |
| XPRL | TLogo for XPRA in uptime (Metadata for SUM uptime) | ❓ | Not tested yet |
| XSLT | Transformation | ❓ | Not tested yet |
| XTRA | Transformation/Mapping Between XML and ABAP | ❓ | Not tested yet |
| XWRD | Table of changed key words | ❓ | Not tested yet |

### ABAP Objects note

Some objects (such as classes, function modules, programs, and includes) fall into the category of ABAP objects, meaning they contain ABAP source code.

In ABAP, certain dependencies can be subtle: the system may not raise a syntax error even if a referenced object is missing or inactive. Instead, these issues only surface at runtime, for example when using dynamic calls or string-based object references.

The following is a list of objects and scenarios where such dependencies can still be detected:

| Object Type | Description | Usage |
|---|---|---|
| NROB | Number Range Object | Whenever called by function module `NUMBER_GET_NEXT` |

## SAP Objects

If a dependency is identified and the referenced object belongs to a **standard SAP package**, TRM includes the requirement as part of the **TADIR SAP entries**. This ensures that references to standard objects are properly managed without bundling SAP-owned code.