---
title: What is an ABAP package manager?
description: Learn what an SAP ABAP package manager does and how manifests, semantic versions, dependencies, registries, lockfiles, CTS delivery, and uninstall fit together.
---

# What is an ABAP package manager?

An **ABAP package manager** is software that turns ABAP developments into named, versioned releases and manages their complete lifecycle: publishing, discovery, dependency resolution, installation, update, and removal. TRM provides that lifecycle while using SAP Change and Transport System (CTS) transports for delivery.

This is different from an ABAP development package. A development package groups repository objects inside an SAP system. A package-manager package is a distributable software release with an identity, version, requirements, and installable artifact.

## Package-manager capabilities

| Capability | Why it matters | How TRM provides it |
| --- | --- | --- |
| Package identity | A release needs a stable name | A TRM manifest names the package and its publisher |
| Semantic versions | Consumers need to distinguish compatible and breaking releases | Releases and dependency ranges use SemVer |
| Artifact creation | The exact release must be distributable | Publishing produces a portable `.trm` artifact containing its manifest and transports |
| Registry | People and tools need to discover and retrieve releases | Public and private registries expose package metadata and artifacts |
| Dependency resolution | Required components must be present in compatible versions | TRM discovers and resolves TRM dependencies and checks SAP prerequisites |
| Reproducibility | Repeated installations should select the same inputs | A lockfile records exact releases and integrity values |
| Install and update | A target system must receive the release predictably | TRM validates the target and imports the release through CTS |
| Uninstall | A package lifecycle must include removal | TRM creates and imports deletion transports, with rollback if the operation fails |
| Automation | Delivery should work in pipelines as well as interactively | The TRM CLI supports non-interactive workflows and GitHub Actions |

## Repository, transport, artifact, and package

These terms describe different layers:

- A **Git repository** stores source history and supports collaborative development.
- An **ABAP development package** organizes repository objects inside one SAP system.
- A **transport request** moves recorded changes between SAP systems.
- A **`.trm` artifact** is an immutable, versioned delivery assembled from one or more transports plus a manifest.
- A **TRM package** is the named product whose releases, dependencies, and lifecycle the package manager controls.

TRM can be used with Git and abapGit. Source control manages how software is developed; TRM manages how a tested release is packaged and delivered.

## Why CTS is part of the design

SAP landscapes already use CTS to move repository and customizing changes in a controlled order. TRM adds the product layer that a raw transport does not provide: identity, semantic version, prerequisites, dependencies, integrity, registry distribution, and lifecycle commands.

The result is a package-manager workflow without replacing the transport mechanism used by the target landscape.

## See it in practice

1. Follow the [five-minute quick start](quickstart.md).
2. Read how [publishing creates an artifact](../commons/publish.md).
3. See how [dependency management](../commons/dependencies.md) works.
4. Learn how a [lockfile makes installation repeatable](../commons/lockfile.md).
5. Review [transport-based uninstall](../commons/uninstall.md).

*Last reviewed: 19 October 2026.*
