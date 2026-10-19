---
title: TRM and abapGit
description: Understand the complementary roles of abapGit source synchronization and TRM release packaging, dependency resolution, CTS delivery, and uninstall.
---

# TRM and abapGit

TRM and abapGit solve different parts of the ABAP software lifecycle and can be used together. **abapGit is a Git client for ABAP development**, while **TRM is a package manager for versioned delivery across SAP systems**.

## At a glance

| Need | abapGit | TRM |
| --- | --- | --- |
| Work with ABAP source in Git | Primary purpose | Can include repository metadata and serialized source in an artifact |
| Review source history and branches | Yes, through Git | Not its purpose |
| Produce a versioned delivery artifact | Repository archives/source are available | Produces a `.trm` artifact containing manifest and CTS transports |
| Resolve compatible package dependencies | APACK manifests can declare metadata; resolution depends on surrounding tooling | Resolves versioned TRM dependencies and checks SAP prerequisites |
| Reproduce exact dependency versions | Git commits identify source | TRM lockfiles record package versions and integrity values |
| Deliver the same built transports | No; objects are deserialized on the target | Yes; the artifact carries the transports produced for the release |
| Move customizing and translations | Not the core workflow | Supported through dedicated CTS transports |
| Remove a delivered release | Repository objects can be removed through source synchronization | Creates deletion transports and can propagate removal through the landscape |

The table describes documented workflows as of 19 October 2026. Corrections are welcome through the documentation repository.

## A combined workflow

```text
Git repository and abapGit
          │
          │ develop, review, merge
          ▼
ABAP development system
          │
          │ trm publish
          ▼
Versioned .trm artifact ──► registry
                               │
                               │ trm install / update
                               ▼
                    target SAP system and landscape
```

Use abapGit where its fast Git-based development loop is valuable. Once a version is ready for controlled delivery, use TRM to publish a release with its transports, manifest, prerequisites, and dependency contract.

## Why release artifacts matter

An abapGit pull reconstructs objects from serialized source in the receiving system. That is useful during development, but the result is built and activated in the state of that target system.

TRM publishes the transports created for the release and installs those transports on the target. This lets a team promote the release artifact it tested instead of reconstructing a new one at every destination.

## Continue reading

- [What is an ABAP package manager?](what-is-an-abap-package-manager.md)
- [TRM artifact format](../commons/artifact.md)
- [How TRM uses transports](../commons/transports.md)
- [Publish a package](../commons/publish.md)

References: [abapGit documentation](https://docs.abapgit.org/), [APACK specification](https://github.com/abapGit/abapGit-Docs/blob/main/docs/user-guide/reference/apack.md).

*Author: TRM maintainers. Technical review: Regesta Group engineering. Last reviewed: 19 October 2026.*
