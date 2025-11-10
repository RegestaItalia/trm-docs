# TRM - Transport Request Manager

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-1.3.0-4baaaa.svg)](code_of_conduct.md)

[![trm-client version](https://img.shields.io/npm/v/trm-client?label=trm-client)](https://www.npmjs.com/package/trm-client)
[![trm-server version](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/version?package=trm-server&label=trm-server)](https://trmregistry/#/package/trm-server)
[![trm-core version](https://img.shields.io/npm/v/trm-core?label=trm-core)](https://www.npmjs.com/package/trm-core)
[![trm-registry-types version](https://img.shields.io/npm/v/trm-registry-types?label=trm-registry-types)](https://www.npmjs.com/package/trm-registry-types)

[![trm-registry roadmap stage](https://img.shields.io/badge/public%20registry%20roadmap%20stage-production-green)](/registry/public/roadmap.md)

| 🚀 This project is funded and maintained by 🏦 | 🔗                                                             |
|-------------------------------------------------|----------------------------------------------------------------|
| Regesta S.p.A.                                  | [https://www.regestaitalia.eu/](https://www.regestaitalia.eu/) |
| Clarex S.r.l.                                   | [https://www.clarex.it/](https://www.clarex.it/)               |

**TRM (Transport Request Manager)** is a package manager inspired solution built leveraging CTS that simplifies SAP ABAP transports.

<p align="center">
  <img src="./_media/logo.png" style="max-width:40%; height:auto;" alt="Logo" />
</p>

TRM introduces **package-based software delivery** to the SAP ecosystem, bringing with it semantic versioning, dependency management, and automated deployment activities.

---

## What is TRM?

TRM (Transport Request Manager) is a software that transforms how custom ABAP developments are published, installed, and maintained across SAP landscapes.
Inspired by modern package managers, TRM introduces a declarative, version-controlled, and automated way to manage your SAP transports.

With TRM, you can:

- **Define a manifest** for each ABAP package (similar to `package.json` with Node.js or `pom.xml` with Maven)
- **Version your products** ([SemVer](https://semver.org/) compliance)
- **Declare dependencies** (to other TRM packages, SAP standard objects, or customizing data)
- **Automate post-install activities**, such as client dependant customizing, cache invalidation etc.
- **Validate system requirements** prior to installation
- **Compare versions** of the same product across multiple SAP systems (in or outside the same landscape)
- **Distribute** your product release to the public or to a restricted number of users:
  - Registry (e.g., [trmregistry.com](https://trmregistry.com) or private registry)
  - Local `.trm` files for offline installations

## Modern approach for ABAP

- Publish ABAP packages from a **central development system**
- Deliver packages to target systems (outside of the original landscape e.g. customers development system) using a single CLI command (or in a pipeline)
- Full support for **workbench objects**, **customizing**, and **translations**

## Structured Manifest

Each package includes a `manifest.json` that declares:

- Version and metadata
- System requirements
- Dependencies
- Post-install scripts

# Architecture Overview

- [**Server**](server/README.md): SAP temporary package installed on source and destination systems
- [**Client**](client/README.md): Command-line interface that talks with SAP instances
- [**Registry**](https://trmregistry.com/): Cloud registry where package releases are safely stored for end users to install

---

# Contributors

<!-- {docsify-add CONTRIBUTORS} -->

[<img src="https://trmregistry.com/public/contributors?image=true">](https://docs.trmregistry.com/#/?id=contributors) <!-- {docsify-remove} -->
