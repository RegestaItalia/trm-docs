# TRM Artifact

A **TRM artifact** is a file with the `.trm` extension. It is an archive that packages **transports** along with a **manifest** file describing the TRM package.

## Structure

A typical TRM artifact has the following directory layout:

```
├── src
│   ├── .abapgit.xml
├── dist
│   ├── TRMK100001
│   │   ├── K100001.TRM
│   │   ├── R100001.TRM
│   ├── TRMK100002
│   │   ├── K100002.TRM
│   │   ├── R100002.TRM
├── manifest.json
├── sap_entries.json
```

# Transport Types

Each transport in a TRM artifact is categorized by type, guiding its publish and install behavior. TRM-relevant transports also include two ZTRM comment objects that specify the package name and version from the manifest.

## DEVC

- **Description**: Contains R3TR objects of type `DEVC` (ABAP package definitions).
- **Usage**: Typically *not* imported by TRM, as ABAP packages are usually generated dynamically. However, users may choose to install original DEVC objects from a TRM package if needed.

## TADIR

- **Description**: Contains all objects from the package and its subpackages, *excluding* DEVC objects.
- **Role**: It includes the package manifest.
- **Purpose**: Workbench objects.

## LANG

- **Description**: Includes translation objects.
- **Purpose**: Ensures multilingual support by providing translated content.

## CUST

- **Description**: Contains customizing data.
- **Purpose**: Used to transport table data.

If you want to publish a TRM package with customizing transports, make sure to read the [customizing guidelines](customizing_guidelines.md) first.

# Source code

When available in the publisher system, ABAPGit is used to serialize the package source code and it's bundled inside the artifact.

# Manifest and SAP Entries

Read more about [manifest](manifest.md) and [SAP Entries](sap_entries.md).