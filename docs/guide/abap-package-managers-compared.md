---
title: Compare ABAP package and delivery tools
description: A sourced comparison of TRM, abapGit, apm, APACK, raw CTS transports, and SAINT or SPAM for ABAP software delivery.
---

# Compare ABAP package and delivery tools

ABAP teams can choose among source-control clients, manifest conventions, package managers, transport files, and SAP add-on tooling. They overlap, but they are not interchangeable.

This comparison focuses on the lifecycle of independently versioned ABAP software. It is based on public documentation available on 19 October 2026. A blank or limited capability is not a quality judgment: each tool has a different purpose.

## Capability matrix

| Capability | TRM | abapGit | apm | APACK | Raw CTS transports | SAINT/SPAM |
| --- | --- | --- | --- | --- | --- | --- |
| Git-based ABAP source workflow | Integrates with source metadata | Yes | Built on the abapGit ecosystem | Manifest convention used with abapGit | No | No |
| Named, semantic package releases | Yes | Tags/releases can identify source | Yes | Declares package coordinates and versions | Manual convention | SAP add-on/support-package levels |
| Installable release artifact | `.trm` artifact | Serialized repository/archive | abapGit-based package delivery | Not by itself | Transport files | SAR/PAT delivery |
| Version-range dependency resolution | Yes | Not by itself | Consult current apm documentation | Describes dependencies; resolver is separate | No | Prerequisite add-ons/support packages |
| Lockfile with integrity values | Yes | Git commit pins source | Consult current apm documentation | No | No | Delivery tooling controls archives |
| Public/private registry protocol | Yes | Git hosting rather than a package registry | Public package catalog | No registry by itself | No | SAP delivery channels |
| CTS-based install/update | Yes | No | No | No | Yes, manually | Uses SAP add-on mechanisms |
| Customizing and translation transports | Yes | Limited to serialized object support | Based on abapGit support | Not by itself | Yes | Yes |
| Transport-based uninstall | Yes | No dedicated deletion-transport lifecycle | Consult current apm documentation | No | Must be engineered manually | Only add-ons explicitly prepared as deletable |
| CLI and CI/CD workflow | Yes | abapGit offers APIs/background modes; integrations vary | Yes | Not by itself | External tooling required | Primarily SAP administration tooling |

## How to choose

- Choose **abapGit** for an ABAP development workflow centered on Git repositories, branches, source review, and synchronization.
- Choose **TRM** when the unit you distribute must be a versioned artifact with dependencies, registry delivery, repeatable installation, and uninstall across CTS landscapes.
- Evaluate **apm** when an abapGit-based package-manager workflow matches the target environment; verify the current feature set against the project's documentation.
- Use **APACK** when projects need a standard way to declare coordinates and dependencies in an abapGit-compatible repository; APACK is a manifest specification rather than a complete distribution lifecycle by itself.
- Use **raw CTS transports** for landscape-controlled change movement when package identity, resolution, registry discovery, and lifecycle automation are handled elsewhere.
- Use **SAINT/SPAM and AAK** for SAP-style add-on and support-package delivery when their governance, assembly, and registration model fits the product.

## Method and sources

Capabilities are marked only when a public source documents them. Product behavior can change, so verify before making an architecture decision:

- [TRM documentation](https://docs.trmregistry.com/)
- [abapGit documentation](https://docs.abapgit.org/)
- [apm project](https://www.abappm.com/)
- [SAP Community introduction to APACK](https://community.sap.com/t5/technology-blog-posts-by-sap/introducing-apack-a-package-and-dependency-manager-for-abap/ba-p/13422397)
- [SAP Add-On Installation Tool](https://help.sap.com/docs/SAP_ADD-ON_INSTALLATION_TOOL_AND_SUPPORT_PACKAGE_MANAGER/)

Open a documentation issue or pull request with a source if any cell needs correction.

*Last reviewed: 19 October 2026.*
