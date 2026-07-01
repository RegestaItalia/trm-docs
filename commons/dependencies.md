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
| DOCV | Documentation (independent) | Type `DT`: Whenever called by function module `POPUP_DISPLAY_TEXT` |

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

| Object Type | Description | Supported | Issue |
| ----------- | ----------- | --------- | ---- |
| ACID | Checkpoint Group | No | [#64](https://github.com/RegestaItalia/trm-server/issues/64) |
| ADVC | App Variant (LRep cross-client content) | No | [#88](https://github.com/RegestaItalia/trm-server/issues/88) |
| AMSD | Logical Database Schema | No | [#89](https://github.com/RegestaItalia/trm-server/issues/89) |
| AOBJ | Archiving Object | No | [#90](https://github.com/RegestaItalia/trm-server/issues/90) |
| APIC | API Catalog | No | [#91](https://github.com/RegestaItalia/trm-server/issues/91) |
| APIS | API Release State of Objects | No | [#92](https://github.com/RegestaItalia/trm-server/issues/92) |
| APLO | Application Log Object | No | [#93](https://github.com/RegestaItalia/trm-server/issues/93) |
| AVAR | Activation Variants for Assertions and Breakpoints | No | [#94](https://github.com/RegestaItalia/trm-server/issues/94) |
| AVAS | Classification | No | [#95](https://github.com/RegestaItalia/trm-server/issues/95) |
| BCCH | Business Configuration Check | No | [#96](https://github.com/RegestaItalia/trm-server/issues/96) |
| BCCU | Business Configuration Check Units | No | [#97](https://github.com/RegestaItalia/trm-server/issues/97) |
| BGQC | Background Processing Context | No | [#98](https://github.com/RegestaItalia/trm-server/issues/98) |
| BOBF | BOPF: Business Object Model | No | [#99](https://github.com/RegestaItalia/trm-server/issues/99) |
| BOBX | BOPF: Business Object Model Extension | No | [#103](https://github.com/RegestaItalia/trm-server/issues/103) |
| CASP | SCC: Check Aspect | No | [#100](https://github.com/RegestaItalia/trm-server/issues/100) |
| CASV | SCC: Check Aspect Value | No | [#101](https://github.com/RegestaItalia/trm-server/issues/101) |
| CCAC | CDM Catalog (LREP cross-client content) | No | [#102](https://github.com/RegestaItalia/trm-server/issues/102) |
| CCFG | SCC: Check Configuration | No | [#104](https://github.com/RegestaItalia/trm-server/issues/104) |
| CCPR | Client Copy Profile | No | [#105](https://github.com/RegestaItalia/trm-server/issues/105) |
| CFD1 | Custom fields: IDoc Type Registry | No | [#106](https://github.com/RegestaItalia/trm-server/issues/106) |
| CFDA | Custom Logic Registration | No | [#107](https://github.com/RegestaItalia/trm-server/issues/107) |
| CFDB | Custom Fields: Business Context Registry | No | [#108](https://github.com/RegestaItalia/trm-server/issues/108) |
| CFDC | Custom Fields: CDS View Registry | No | [#109](https://github.com/RegestaItalia/trm-server/issues/109) |
| CFDF | Custom Field | No | [#110](https://github.com/RegestaItalia/trm-server/issues/110) |
| CFDG | Custom Fields: SAP GUI Registry | No | [#111](https://github.com/RegestaItalia/trm-server/issues/111) |
| CFDM | Custom fields: Function Module Registry | No | [#112](https://github.com/RegestaItalia/trm-server/issues/112) |
| CFDO | Custom Fields: OData Model Registry | No | [#113](https://github.com/RegestaItalia/trm-server/issues/113) |
| CFDP | Custom fields: SOAP Service Interface Registry | No | [#114](https://github.com/RegestaItalia/trm-server/issues/114) |
| CFDR | Custom Fields: Association Target | No | [#115](https://github.com/RegestaItalia/trm-server/issues/115) |
| CFDS | Custom Fields: Business Scenario Registry | No | [#116](https://github.com/RegestaItalia/trm-server/issues/116) |
| CFDT | Custom Fields: Data Transfer Registry | No | [#117](https://github.com/RegestaItalia/trm-server/issues/117) |
| CFDY | Custom Fields: Abstract Entity Registry | No | [#118](https://github.com/RegestaItalia/trm-server/issues/118) |
| CGRC | CDM Group (LREP cross-client content) | No | [#119](https://github.com/RegestaItalia/trm-server/issues/119) |
| CHAR | Object characteristic | No | [#120](https://github.com/RegestaItalia/trm-server/issues/120) |
| CHDO | Change Document Object | No | [#121](https://github.com/RegestaItalia/trm-server/issues/121) |
| CHKE | Check Exemptions | No | [#122](https://github.com/RegestaItalia/trm-server/issues/122) |
| CMHC | Cloud Management Health Check | No | [#65](https://github.com/RegestaItalia/trm-server/issues/65) |
| CMOD | Customer enhancement projects | No | [#123](https://github.com/RegestaItalia/trm-server/issues/123) |
| CMPT | Code Composer Template | No | [#66](https://github.com/RegestaItalia/trm-server/issues/66) |
| CUS0 | Customizing IMG Activity | No | [#124](https://github.com/RegestaItalia/trm-server/issues/124) |
| DDLA | CDS Annotation Definition | No | [#125](https://github.com/RegestaItalia/trm-server/issues/125) |
| DDLV | CDS Variant | No | [#126](https://github.com/RegestaItalia/trm-server/issues/126) |
| DEVC | Package | No | [#127](https://github.com/RegestaItalia/trm-server/issues/127) |
| DOBJ | Data Destruction Object | No | [#128](https://github.com/RegestaItalia/trm-server/issues/128) |
| DRTY | CDS Type Definitions | No | [#129](https://github.com/RegestaItalia/trm-server/issues/129) |
| DRUL | Dependency Rule | No | [#130](https://github.com/RegestaItalia/trm-server/issues/130) |
| DSEL | Selection View | No | [#131](https://github.com/RegestaItalia/trm-server/issues/131) |
| DSFD | CDS Scalar Function Definition | No | [#132](https://github.com/RegestaItalia/trm-server/issues/132) |
| DSFI | CDS Scalar Function Implementation Reference | No | [#133](https://github.com/RegestaItalia/trm-server/issues/133) |
| DTDC | Dictionary Tuning: Dynamic Cache | No | [#134](https://github.com/RegestaItalia/trm-server/issues/134) |
| DTEB | Entity Buffer | No | [#135](https://github.com/RegestaItalia/trm-server/issues/135) |
| ECAT | eCATT Test Script | No | [#136](https://github.com/RegestaItalia/trm-server/issues/136) |
| ECSD | eCATT System Data Container | No | [#137](https://github.com/RegestaItalia/trm-server/issues/137) |
| ECSP | eCATT Start Profile | No | [#138](https://github.com/RegestaItalia/trm-server/issues/138) |
| ECTC | eCATT Test Configuration | No | [#139](https://github.com/RegestaItalia/trm-server/issues/139) |
| ECTD | eCATT Test Data Container | No | [#140](https://github.com/RegestaItalia/trm-server/issues/140) |
| ECVO | eCATT Validation Object | No | [#141](https://github.com/RegestaItalia/trm-server/issues/141) |
| EDCC | EDCC | No | [#67](https://github.com/RegestaItalia/trm-server/issues/67) |
| EDOI | EDOI | No | [#68](https://github.com/RegestaItalia/trm-server/issues/68) |
| EDOM | EDOM | No | [#69](https://github.com/RegestaItalia/trm-server/issues/69) |
| EDOP | EDOP | No | [#70](https://github.com/RegestaItalia/trm-server/issues/70) |
| EDOT | EDOT | No | [#71](https://github.com/RegestaItalia/trm-server/issues/71) |
| EEEC | Enterprise Event Enablement - Event Consumer | No | [#142](https://github.com/RegestaItalia/trm-server/issues/142) |
| ENSC | Composite Enhancement Spot | No | [#143](https://github.com/RegestaItalia/trm-server/issues/143) |
| FDT0 | FDT/BRFplus: System Application | No | [#144](https://github.com/RegestaItalia/trm-server/issues/144) |
| FUGS | Function Group with Customer Include: SAP Part | No | [#145](https://github.com/RegestaItalia/trm-server/issues/145) |
| G4BA | SAP Gateway OData V4 Backend Service Group & Assignments | No | [#146](https://github.com/RegestaItalia/trm-server/issues/146) |
| G4BS | SAP Gateway OData V4 Backend Service | No | [#147](https://github.com/RegestaItalia/trm-server/issues/147) |
| GCCV | Cross-Client Validation Check | No | [#148](https://github.com/RegestaItalia/trm-server/issues/148) |
| GCPM | SAP Gateway OData Client Proxy - Proxy Model | No | [#149](https://github.com/RegestaItalia/trm-server/issues/149) |
| GSMP | Generic Simple Metric Provider | No | [#72](https://github.com/RegestaItalia/trm-server/issues/72) |
| HOTA | Full Package (SAP HANA Transport for ABAP) | No | [#150](https://github.com/RegestaItalia/trm-server/issues/150) |
| HTTP | HTTP Service | No | [#151](https://github.com/RegestaItalia/trm-server/issues/151) |
| IAML | Language-Dependent IAC Binary Data | No | [#152](https://github.com/RegestaItalia/trm-server/issues/152) |
| IAMU | Language-Independent IAC Binary Data | No | [#153](https://github.com/RegestaItalia/trm-server/issues/153) |
| IARP | Parameters of IAC Language Resource | No | [#154](https://github.com/RegestaItalia/trm-server/issues/154) |
| IATL | Language-Dependent IAC Templates | No | [#155](https://github.com/RegestaItalia/trm-server/issues/155) |
| IAXU | ITS: XML Templates for HTML Templates | No | [#156](https://github.com/RegestaItalia/trm-server/issues/156) |
| ILMB | ILM Object | No | [#157](https://github.com/RegestaItalia/trm-server/issues/157) |
| INA1 | InA Service | No | [#158](https://github.com/RegestaItalia/trm-server/issues/158) |
| INTM | Intelligent Scenario Model | No | [#159](https://github.com/RegestaItalia/trm-server/issues/159) |
| INTS | Intelligent Scenario | No | [#160](https://github.com/RegestaItalia/trm-server/issues/160) |
| IWMO | SAP Gateway Business Suite Enablement - Model | No | [#161](https://github.com/RegestaItalia/trm-server/issues/161) |
| IWOM | SAP Gateway: Model Metadata | No | [#162](https://github.com/RegestaItalia/trm-server/issues/162) |
| IWPR | SAP Gateway BSE - Service Builder Project | No | [#163](https://github.com/RegestaItalia/trm-server/issues/163) |
| IWSG | SAP Gateway: Service Groups Metadata | No | [#164](https://github.com/RegestaItalia/trm-server/issues/164) |
| IWSV | SAP Gateway Business Suite Enablement - Service | No | [#165](https://github.com/RegestaItalia/trm-server/issues/165) |
| IWVB | SAP Gateway Business Suite Enablement -Vocabulary Annotation | No | [#166](https://github.com/RegestaItalia/trm-server/issues/166) |
| JOBD | Technical Job Definition | No | [#167](https://github.com/RegestaItalia/trm-server/issues/167) |
| LRCC | LRepository cross-client content | No | [#168](https://github.com/RegestaItalia/trm-server/issues/168) |
| NHDU | HANA Transport Container | No | [#169](https://github.com/RegestaItalia/trm-server/issues/169) |
| NROB | Number Range Object | No | [#170](https://github.com/RegestaItalia/trm-server/issues/170) |
| OA2P | OAuth 2.0 Client Profile | No | [#171](https://github.com/RegestaItalia/trm-server/issues/171) |
| OCAO | OCAO | No | [#73](https://github.com/RegestaItalia/trm-server/issues/73) |
| OMLM | Output Management: T100 Longtext Link Mapping | No | [#172](https://github.com/RegestaItalia/trm-server/issues/172) |
| OTGR | Object type group | No | [#173](https://github.com/RegestaItalia/trm-server/issues/173) |
| PDAC | Standard rule | No | [#174](https://github.com/RegestaItalia/trm-server/issues/174) |
| PDTS | Standard Task | No | [#175](https://github.com/RegestaItalia/trm-server/issues/175) |
| PDWS | Workflow template | No | [#176](https://github.com/RegestaItalia/trm-server/issues/176) |
| PT01 | Migration Project Template - Direct Transfer | No | [#177](https://github.com/RegestaItalia/trm-server/issues/177) |
| PT02 | Migration Object Template - Direct Transfer | No | [#178](https://github.com/RegestaItalia/trm-server/issues/178) |
| RMTC | RMTC | No | [#74](https://github.com/RegestaItalia/trm-server/issues/74) |
| RONT | RESTful ABAP Programming Model: Object (Node) Type | No | [#179](https://github.com/RegestaItalia/trm-server/issues/179) |
| RPDF | Report definition for the classification tool-set | No | [#75](https://github.com/RegestaItalia/trm-server/issues/75) |
| SAJC | Application Job Catalog Entry | No | [#180](https://github.com/RegestaItalia/trm-server/issues/180) |
| SAJT | Application Job Template | No | [#181](https://github.com/RegestaItalia/trm-server/issues/181) |
| SAMC | ABAP Messaging Channel Application | No | [#182](https://github.com/RegestaItalia/trm-server/issues/182) |
| SAPC | ABAP Push Channel Application | No | [#183](https://github.com/RegestaItalia/trm-server/issues/183) |
| SBCL | Semantic Business Configuration Lock Definition | No | [#184](https://github.com/RegestaItalia/trm-server/issues/184) |
| SBLE | Customer Extension of Business Logic with restricted ABAP | No | [#185](https://github.com/RegestaItalia/trm-server/issues/185) |
| SCAT | Test case | No | [#186](https://github.com/RegestaItalia/trm-server/issues/186) |
| SCBO | Custom Business Object | No | [#187](https://github.com/RegestaItalia/trm-server/issues/187) |
| SCCL | Custom Code List | No | [#188](https://github.com/RegestaItalia/trm-server/issues/188) |
| SCCV | Custom CDS Views | No | [#189](https://github.com/RegestaItalia/trm-server/issues/189) |
| SCGR | Service Consumer Group | No | [#190](https://github.com/RegestaItalia/trm-server/issues/190) |
| SCP1 | BC Set or Customizing Profile | No | [#191](https://github.com/RegestaItalia/trm-server/issues/191) |
| SCP2 | Switch BC Sets | No | [#192](https://github.com/RegestaItalia/trm-server/issues/192) |
| SCRL | Custom Reuse Library | No | [#193](https://github.com/RegestaItalia/trm-server/issues/193) |
| SDAT | SAP Delivered Table Authorization Group Assignments | No | [#194](https://github.com/RegestaItalia/trm-server/issues/194) |
| SFKX | Foreign Key Check Exception | No | [#195](https://github.com/RegestaItalia/trm-server/issues/195) |
| SFPF | Form Object: Form | No | [#196](https://github.com/RegestaItalia/trm-server/issues/196) |
| SFPI | Form Object: Interface | No | [#197](https://github.com/RegestaItalia/trm-server/issues/197) |
| SHMA | Shared Objects: Defined Area Attributes | No | [#198](https://github.com/RegestaItalia/trm-server/issues/198) |
| SICF | ICF Service | No | [#199](https://github.com/RegestaItalia/trm-server/issues/199) |
| SITB | SITB | No | [#76](https://github.com/RegestaItalia/trm-server/issues/76) |
| SITO | SITO | No | [#77](https://github.com/RegestaItalia/trm-server/issues/77) |
| SMBC | Business Configuration Object | No | [#200](https://github.com/RegestaItalia/trm-server/issues/200) |
| SMD1 | Definition of an R-LOIO class | No | [#201](https://github.com/RegestaItalia/trm-server/issues/201) |
| SMD2 | Definition of a V-LOIO class | No | [#202](https://github.com/RegestaItalia/trm-server/issues/202) |
| SMD3 | Definition of an R-PHIO class | No | [#203](https://github.com/RegestaItalia/trm-server/issues/203) |
| SMD4 | Definition of a V-PHIO class | No | [#204](https://github.com/RegestaItalia/trm-server/issues/204) |
| SMD5 | Definition of an R-RELA class | No | [#205](https://github.com/RegestaItalia/trm-server/issues/205) |
| SMD6 | Definition of a V-RELA class | No | [#206](https://github.com/RegestaItalia/trm-server/issues/206) |
| SMDA | Definition of an IO attribute | No | [#207](https://github.com/RegestaItalia/trm-server/issues/207) |
| SMDC | IO class link area | No | [#209](https://github.com/RegestaItalia/trm-server/issues/209) |
| SMDK | Definition of a context class | No | [#208](https://github.com/RegestaItalia/trm-server/issues/208) |
| SMDM | Document model area | No | [#210](https://github.com/RegestaItalia/trm-server/issues/210) |
| SMIM | Info Object from the MIME Repository | No | [#211](https://github.com/RegestaItalia/trm-server/issues/211) |
| SMOD | SAP enhancements | No | [#212](https://github.com/RegestaItalia/trm-server/issues/212) |
| SMTG | OM: Email Template | No | [#213](https://github.com/RegestaItalia/trm-server/issues/213) |
| SOD1 | Api Package | No | [#214](https://github.com/RegestaItalia/trm-server/issues/214) |
| SOD2 | API Package Assignment | No | [#215](https://github.com/RegestaItalia/trm-server/issues/215) |
| SPRX | Proxy Object | No | [#216](https://github.com/RegestaItalia/trm-server/issues/216) |
| SPSE | Security: PSE Definition | No | [#217](https://github.com/RegestaItalia/trm-server/issues/217) |
| SQAQ | Question | No | [#78](https://github.com/RegestaItalia/trm-server/issues/78) |
| SQL1 | SQL Service Binding (SQL1) | No | [#218](https://github.com/RegestaItalia/trm-server/issues/218) |
| SQSC | Database Procedure Proxy | No | [#219](https://github.com/RegestaItalia/trm-server/issues/219) |
| SRFA | SRFA | No | [#79](https://github.com/RegestaItalia/trm-server/issues/79) |
| SRFC | RFC Service | No | [#220](https://github.com/RegestaItalia/trm-server/issues/220) |
| SRFP | SRFP | No | [#80](https://github.com/RegestaItalia/trm-server/issues/80) |
| SRFQ | SRFQ | No | [#81](https://github.com/RegestaItalia/trm-server/issues/81) |
| SRFR | SRFR | No | [#82](https://github.com/RegestaItalia/trm-server/issues/82) |
| SRFS | SRFS | No | [#83](https://github.com/RegestaItalia/trm-server/issues/83) |
| SRVB | Service Binding | No | [#221](https://github.com/RegestaItalia/trm-server/issues/221) |
| SRVC | Service Consumption Model | No | [#222](https://github.com/RegestaItalia/trm-server/issues/222) |
| SRVD | Service Definition | No | [#223](https://github.com/RegestaItalia/trm-server/issues/223) |
| STC1 | Configuration Entity | No | [#224](https://github.com/RegestaItalia/trm-server/issues/224) |
| STCS | TC Task List | No | [#225](https://github.com/RegestaItalia/trm-server/issues/225) |
| STYC | Embedded Analytics Story | No | [#226](https://github.com/RegestaItalia/trm-server/issues/226) |
| SUCD | Scenario for Switchable Authorization Check (Definition) | No | [#227](https://github.com/RegestaItalia/trm-server/issues/227) |
| SUCK | Header Data for General Authorization Groups | No | [#228](https://github.com/RegestaItalia/trm-server/issues/228) |
| SUSC | Authorization object class | No | [#229](https://github.com/RegestaItalia/trm-server/issues/229) |
| SUSH | Assignment: Service --> Authorization Objects | No | [#230](https://github.com/RegestaItalia/trm-server/issues/230) |
| SXCI | Business Add-Ins - Implementations | No | [#231](https://github.com/RegestaItalia/trm-server/issues/231) |
| SXSD | Business Add-Ins - Definitions | No | [#232](https://github.com/RegestaItalia/trm-server/issues/232) |
| TOBJ | Definition of a Maintenance and Transport Object | No | [#233](https://github.com/RegestaItalia/trm-server/issues/233) |
| TRUL | Transformation Rule | No | [#234](https://github.com/RegestaItalia/trm-server/issues/234) |
| UCSA | Unified Connectivity Service Assembly | No | [#235](https://github.com/RegestaItalia/trm-server/issues/235) |
| UIAC | Fiori Launchpad Technical Catalog | No | [#236](https://github.com/RegestaItalia/trm-server/issues/236) |
| UIAD | Fiori Launchpad App Descriptor Item | No | [#237](https://github.com/RegestaItalia/trm-server/issues/237) |
| VCMD | VCMD | No | [#84](https://github.com/RegestaItalia/trm-server/issues/84) |
| VKOI | VKOI | No | [#85](https://github.com/RegestaItalia/trm-server/issues/85) |
| VKOS | VKOS | No | [#86](https://github.com/RegestaItalia/trm-server/issues/86) |
| VTRM | Verticalization Terminology | No | [#238](https://github.com/RegestaItalia/trm-server/issues/238) |
| VTRR | Verticalization: Text repository Registration | No | [#239](https://github.com/RegestaItalia/trm-server/issues/239) |
| WDCA | Web Dynpro Application Configuration | No | [#240](https://github.com/RegestaItalia/trm-server/issues/240) |
| WDCC | Web Dynpro Component Configuration | No | [#241](https://github.com/RegestaItalia/trm-server/issues/241) |
| WDCP | Web Dynpro CHIP | No | [#242](https://github.com/RegestaItalia/trm-server/issues/242) |
| WEBI | Virtual End Point | No | [#243](https://github.com/RegestaItalia/trm-server/issues/243) |
| WEBS | Web Services | No | [#244](https://github.com/RegestaItalia/trm-server/issues/244) |
| WGRP | Object Type Group (ABAP Workbench / R3TR) | No | [#245](https://github.com/RegestaItalia/trm-server/issues/245) |
| WTAG | BSP Extension | No | [#246](https://github.com/RegestaItalia/trm-server/issues/246) |
| WTHM | O2: Topics for BSP Application | No | [#247](https://github.com/RegestaItalia/trm-server/issues/247) |
| XINX | Ext. Index | No | [#248](https://github.com/RegestaItalia/trm-server/issues/248) |
| XSLT | Transformation | No | [#249](https://github.com/RegestaItalia/trm-server/issues/249) |

## SAP Objects

If a dependency is identified and the referenced object belongs to a **standard SAP package**, TRM includes the requirement as part of the **TADIR SAP entries**. This ensures that references to standard objects are properly managed without bundling SAP-owned code.