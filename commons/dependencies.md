# Dependency Recognition

TRM can automatically detect the dependencies required by a TRM package to prevent syntax and runtime errors.

This detection is based on the types of objects used within the package. As support for additional object types may be needed over time, you can request support by opening an [incident](/incidents.md)

## Objects with ABAP source code

Some objects (such as classes, function modules, programs, and includes) fall into the category of ABAP objects, meaning they contain ABAP source code.

In ABAP, certain dependencies can be subtle: the system may not raise a syntax error even if a referenced object is missing or inactive. Instead, these issues only surface at runtime, for example when using dynamic calls or string-based object references.

The following is a list of objects and scenarios where such dependencies can still be detected:

| Object Type | Description | Usage |
| ----------- | ----------- | ----- |
| NROB | Number Range Object | Whenever called by function module `NUMBER_GET_NEXT` |

## Object types that can be detected

Assuming the analyzed object type is supported, the following is a list of possible object types that may be encountered.

If an object type is supported but one of its dependencies cannot be found, please open an [incident](/incidents.md).

| Object Type | Description | Supported |
| ----------- | ----------- | --------- |
| ACID | Checkpoint Group | Yes |
| AUTH | Authorization Check Fields | Yes |
| AVAS | Classification | Yes |
| BDEF | Behavior Definition | Yes |
| BMFR | Application Component | Yes |
| CFDM | Custom fields: Function Module Registry | Yes |
| CHAR | Object characteristic | Yes |
| CLAS | Class (ABAP Objects) | Yes |
| CMHC | Cloud Management Health Check | Yes |
| CUS0 | Customizing IMG Activity | Yes |
| DCLS | ABAP Data Control Language Sources | Yes |
| DDLS | Data Definition Language Source | Yes |
| DEVC | Package | Yes |
| DIAL | Dialog Module | Yes |
| DOMA | Domain | Yes |
| DRTY | CDS Type Definitions | Yes |
| DSFD | CDS Scalar Function Definition | Yes |
| DTEL | Data Element | Yes |
| ENHC | Composite Enhancement Implementation | Yes |
| ENHO | Enhancement Implementation | Yes |
| ENHS | Enhancement Spot | Yes |
| ENQU | Lock Object | Yes |
| ENSC | Composite Enhancement Spot | Yes |
| FUGR | Function Group | Yes |
| IASP | Parameters of an IAC service | Yes |
| IATU | Language-Independent IAC Templates | Yes |
| INTF | Interface (ABAP Objects) | Yes |
| IWPR | SAP Gateway BSE - Service Builder Project | Yes |
| JOBD | Technical Job Definition | Yes |
| LDBA | Logical Database | Yes |
| MSAG | Message Class | Yes |
| NROB | Number Range Object | Yes |
| OA2P | OAuth 2.0 Client Profile | Yes |
| PARA | SPA/GPA Parameters | Yes |
| PDTS | Standard Task | Yes |
| PDWS | Workflow template | Yes |
| PINF | Package interface | Yes |
| PROG | Program | Yes |
| SAMC | ABAP Messaging Channel Application | Yes |
| SCGR | Service Consumer Group | Yes |
| SFBF | Business Function + Assignment | Yes |
| SFBS | Business Function Set + Assignment | Yes |
| SFPF | Form Object: Form | Yes |
| SFPI | Form Object: Interface | Yes |
| SFSW | Switch + Assignment of Objects to the Switch | Yes |
| SHI3 | General structure storage: Definition of a structure | Yes |
| SHLP | Search Help | Yes |
| SMIM | Info Object from the MIME Repository | Yes |
| SOBJ | Business object types | Yes |
| SOD1 | Api Package | Yes |
| SOD2 | API Package Assignment | Yes |
| SOTR | All Concepts (OTR) of a Package - Short Texts | Yes |
| SPRX | Proxy Object | Yes |
| SRVB | Service Binding | Yes |
| STOB | Structured Object | Yes |
| SUSO | Authorization object | Yes |
| SXCI | Business Add-Ins - Implementations | Yes |
| TABL | Table | Yes |
| TOBJ | Definition of a Maintenance and Transport Object | Yes |
| TRAN | Transaction | Yes |
| TTYP | Table Type | Yes |
| TYPE | Type Group | Yes |
| UDMO | Data model | Yes |
| UENO | Entity type | Yes |
| VIEW | View | Yes |
| WAPA | BSP (Business Server Pages) Application | Yes |
| WDYA | Web Dynpro Application | Yes |
| WDYN | Web Dynpro Component | Yes |
| WEBI | Virtual End Point | Yes |
| WGRP | Object Type Group (ABAP Workbench / R3TR) | Yes |
| WTAG | BSP Extension | Yes |
| XSLT | Transformation | Yes |

## Objects where dependencies aren't analyzed

This is a list of objects that are currently not supported. If automatic dependency detection is required, a custom implementation will be necessary (request it by [incident](/incidents.md)).

Some objects in this list **may be irrelevant** (for example, if no dependencies are possible).
This list was auto-generated: feel free to update it and remove any that do not apply.

| Object Type | Description | Supported |
| ----------- | ----------- | --------- |
| ACID | Checkpoint Group | No |
| ADVC | App Variant (LRep cross-client content) | No |
| AMSD | Logical Database Schema | No |
| AOBJ | Archiving Object | No |
| APIC | API Catalog | No |
| APIS | API Release State of Objects | No |
| APLO | Application Log Object | No |
| AVAR | Activation Variants for Assertions and Breakpoints | No |
| AVAS | Classification | No |
| BCCH | Business Configuration Check | No |
| BCCU | Business Configuration Check Units | No |
| BGQC | Background Processing Context | No |
| BMFR | Application Component | No |
| BMPC | Software Module | No |
| BMPV | Software Variant | No |
| BOBF | BOPF: Business Object Model | No |
| BOBX | BOPF: Business Object Model Extension | No |
| CASP | SCC: Check Aspect | No |
| CASV | SCC: Check Aspect Value | No |
| CCAC | CDM Catalog (LREP cross-client content) | No |
| CCFG | SCC: Check Configuration | No |
| CCPR | Client Copy Profile | No |
| CFD1 | Custom fields: IDoc Type Registry | No |
| CFDA | Custom Logic Registration | No |
| CFDB | Custom Fields: Business Context Registry | No |
| CFDC | Custom Fields: CDS View Registry | No |
| CFDF | Custom Field | No |
| CFDG | Custom Fields: SAP GUI Registry | No |
| CFDM | Custom fields: Function Module Registry | No |
| CFDO | Custom Fields: OData Model Registry | No |
| CFDP | Custom fields: SOAP Service Interface Registry | No |
| CFDR | Custom Fields: Association Target | No |
| CFDS | Custom Fields: Business Scenario Registry | No |
| CFDT | Custom Fields: Data Transfer Registry | No |
| CFDY | Custom Fields: Abstract Entity Registry | No |
| CGRC | CDM Group (LREP cross-client content) | No |
| CHAR | Object characteristic | No |
| CHDO | Change Document Object | No |
| CHKE | Check Exemptions | No |
| CMHC | Cloud Management Health Check | No |
| CMOD | Customer enhancement projects | No |
| CMPT | Code Composer Template | No |
| CUS0 | Customizing IMG Activity | No |
| DDLA | CDS Annotation Definition | No |
| DDLV | CDS Variant | No |
| DEVC | Package | No |
| DOBJ | Data Destruction Object | No |
| DRTY | CDS Type Definitions | No |
| DRUL | Dependency Rule | No |
| DSEL | Selection View | No |
| DSFD | CDS Scalar Function Definition | No |
| DSFI | CDS Scalar Function Implementation Reference | No |
| DTDC | Dictionary Tuning: Dynamic Cache | No |
| DTEB | Entity Buffer | No |
| DTF1 | Date Functions | No |
| ECAT | eCATT Test Script | No |
| ECSD | eCATT System Data Container | No |
| ECSP | eCATT Start Profile | No |
| ECTC | eCATT Test Configuration | No |
| ECTD | eCATT Test Data Container | No |
| ECVO | eCATT Validation Object | No |
| EDCC | EDCC | No |
| EDOI | EDOI | No |
| EDOM | EDOM | No |
| EDOP | EDOP | No |
| EDOT | EDOT | No |
| EEEC | Enterprise Event Enablement - Event Consumer | No |
| ENSC | Composite Enhancement Spot | No |
| FDT0 | FDT/BRFplus: System Application | No |
| FTGL | Feature toggle | No |
| FUGS | Function Group with Customer Include: SAP Part | No |
| G4BA | SAP Gateway OData V4 Backend Service Group & Assignments | No |
| G4BS | SAP Gateway OData V4 Backend Service | No |
| GCCV | Cross-Client Validation Check | No |
| GCPM | SAP Gateway OData Client Proxy - Proxy Model | No |
| GSMP | Generic Simple Metric Provider | No |
| GURL | Predefined URL | No |
| HOTA | Full Package (SAP HANA Transport for ABAP) | No |
| HTTP | HTTP Service | No |
| IAML | Language-Dependent IAC Binary Data | No |
| IAMU | Language-Independent IAC Binary Data | No |
| IARP | Parameters of IAC Language Resource | No |
| IATL | Language-Dependent IAC Templates | No |
| IAXU | ITS: XML Templates for HTML Templates | No |
| ILMB | ILM Object | No |
| INA1 | InA Service | No |
| INTM | Intelligent Scenario Model | No |
| INTS | Intelligent Scenario | No |
| IWMO | SAP Gateway Business Suite Enablement - Model | No |
| IWOM | SAP Gateway: Model Metadata | No |
| IWPR | SAP Gateway BSE - Service Builder Project | No |
| IWSG | SAP Gateway: Service Groups Metadata | No |
| IWSV | SAP Gateway Business Suite Enablement - Service | No |
| IWVB | SAP Gateway Business Suite Enablement -Vocabulary Annotation | No |
| JOBD | Technical Job Definition | No |
| LRCC | LRepository cross-client content | No |
| MSAG | Message Class | No |
| NHDU | HANA Transport Container | No |
| NROB | Number Range Object | No |
| OA2P | OAuth 2.0 Client Profile | No |
| OA2S | OAuth2 Scope | No |
| OCAO | OCAO | No |
| OMLM | Output Management: T100 Longtext Link Mapping | No |
| OTGR | Object type group | No |
| PARA | SPA/GPA Parameters | No |
| PDAC | Standard rule | No |
| PDTS | Standard Task | No |
| PDWS | Workflow template | No |
| PRAG | Pragma in ABAP Source Code | No |
| PT01 | Migration Project Template - Direct Transfer | No |
| PT02 | Migration Object Template - Direct Transfer | No |
| RMTC | RMTC | No |
| RONT | RESTful ABAP Programming Model: Object (Node) Type | No |
| RPDF | Report definition for the classification tool-set | No |
| SAJC | Application Job Catalog Entry | No |
| SAJT | Application Job Template | No |
| SAMC | ABAP Messaging Channel Application | No |
| SAPC | ABAP Push Channel Application | No |
| SBCL | Semantic Business Configuration Lock Definition | No |
| SBLE | Customer Extension of Business Logic with restricted ABAP | No |
| SCAT | Test case | No |
| SCBO | Custom Business Object | No |
| SCCL | Custom Code List | No |
| SCCV | Custom CDS Views | No |
| SCGR | Service Consumer Group | No |
| SCP1 | BC Set or Customizing Profile | No |
| SCP2 | Switch BC Sets | No |
| SCRL | Custom Reuse Library | No |
| SDAT | SAP Delivered Table Authorization Group Assignments | No |
| SFKX | Foreign Key Check Exception | No |
| SFPF | Form Object: Form | No |
| SFPI | Form Object: Interface | No |
| SHMA | Shared Objects: Defined Area Attributes | No |
| SICF | ICF Service | No |
| SITB | SITB | No |
| SITO | SITO | No |
| SMBC | Business Configuration Object | No |
| SMD1 | Definition of an R-LOIO class | No |
| SMD2 | Definition of a V-LOIO class | No |
| SMD3 | Definition of an R-PHIO class | No |
| SMD4 | Definition of a V-PHIO class | No |
| SMD5 | Definition of an R-RELA class | No |
| SMD6 | Definition of a V-RELA class | No |
| SMDA | Definition of an IO attribute | No |
| SMDC | IO class link area | No |
| SMDK | Definition of a context class | No |
| SMDM | Document model area | No |
| SMIM | Info Object from the MIME Repository | No |
| SMOD | SAP enhancements | No |
| SMTG | OM: Email Template | No |
| SOD1 | Api Package | No |
| SOD2 | API Package Assignment | No |
| SOTR | All Concepts (OTR) of a Package - Short Texts | No |
| SOTS | All Concepts (OTR) of a Package - Long Texts | No |
| SPRX | Proxy Object | No |
| SPSE | Security: PSE Definition | No |
| SQAQ | Question | No |
| SQL1 | SQL Service Binding (SQL1) | No |
| SQSC | Database Procedure Proxy | No |
| SRFA | SRFA | No |
| SRFC | RFC Service | No |
| SRFP | SRFP | No |
| SRFQ | SRFQ | No |
| SRFR | SRFR | No |
| SRFS | SRFS | No |
| SRVB | Service Binding | No |
| SRVC | Service Consumption Model | No |
| SRVD | Service Definition | No |
| STC1 | Configuration Entity | No |
| STCS | TC Task List | No |
| STYC | Embedded Analytics Story | No |
| SUCD | Scenario for Switchable Authorization Check (Definition) | No |
| SUCK | Header Data for General Authorization Groups | No |
| SUSC | Authorization object class | No |
| SUSH | Assignment: Service --> Authorization Objects | No |
| SXCI | Business Add-Ins - Implementations | No |
| SXSD | Business Add-Ins - Definitions | No |
| SYAG | System Log Messages | No |
| TOBJ | Definition of a Maintenance and Transport Object | No |
| TRUL | Transformation Rule | No |
| UCSA | Unified Connectivity Service Assembly | No |
| UIAC | Fiori Launchpad Technical Catalog | No |
| UIAD | Fiori Launchpad App Descriptor Item | No |
| VCMD | VCMD | No |
| VKOI | VKOI | No |
| VKOS | VKOS | No |
| VTRM | Verticalization Terminology | No |
| VTRR | Verticalization: Text repository Registration | No |
| WDCA | Web Dynpro Application Configuration | No |
| WDCC | Web Dynpro Component Configuration | No |
| WDCP | Web Dynpro CHIP | No |
| WEBI | Virtual End Point | No |
| WEBS | Web Services | No |
| WGRP | Object Type Group (ABAP Workbench / R3TR) | No |
| WTAG | BSP Extension | No |
| WTHM | O2: Topics for BSP Application | No |
| XINX | Ext. Index | No |
| XSLT | Transformation | No |

## SAP Objects

If a dependency is identified and the referenced object belongs to a **standard SAP package**, TRM includes the requirement as part of the **TADIR SAP entries**. This ensures that references to standard objects are properly managed without bundling SAP-owned code.