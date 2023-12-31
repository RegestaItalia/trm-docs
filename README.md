# TRM - Transport Request Manager

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-1.3.0-4baaaa.svg)](code_of_conduct.md)

[![trm-client version](https://img.shields.io/npm/v/trm-client?label=trm-client)](https://www.npmjs.com/package/trm-client)
[![trm-server version](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/version?package=trm-server&label=trm-server)](https://trmregistry/#/package/trm-server)
[![trm-core version](https://img.shields.io/npm/v/trm-core?label=trm-core)](https://www.npmjs.com/package/trm-core)
[![trm-registry-types version](https://img.shields.io/npm/v/trm-registry-types?label=trm-registry-types)](https://www.npmjs.com/package/trm-registry-types)

[![trm roadmap stage](https://img.shields.io/badge/trm%20roadmap%20stage-alpha-blue)](/commons/roadmap.md)
[![trm-registry roadmap stage](https://img.shields.io/badge/public%20registry%20roadmap%20stage-alpha-blue)](/registry/public/roadmap.md)

> Current TRM stage: Stage 1 - Alpha. Learn more about the [TRM Roadmap](/commons/roadmap.md).

> Current registry stage: Stage 1 - Alpha. Learn more about the [TRM Registry Roadmap](/registry/public/roadmap.md).

TRM (Transport Request Manager) is a software designed to **make transports** between SAP ECC/S4 systems **easy**.

<p align="center">
  <img src="./_media/banner_small.jpg" height="250" />
</p>

In order to start using TRM, all three of these components must be setup:
- [Client](client/README.md)
- [Server](server/README.md)
- [Registry](registry/README.md)

This document will guide you through the installation and configuration of each of the necessary components.

To understand the role of the component, press on its name in the side bar and navigate through its documentation.

If you just wish to run your first demos and see TRM in action, navigate to the "**Getting Started**" section and follow each step of the guide.


The registry documentation is only needed if you decide to create your own private registry, otherwise **TRM Client is already configured to work** with the [Public Registry](https://trmregistry.com).

If you wish to integrate your applications with the [Public Registry](https://trmregistry.com), you may visit its [API Documentation](/registry/public/api.md).