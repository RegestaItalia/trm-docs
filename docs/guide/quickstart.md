---
title: TRM ABAP package manager quick start
description: Install the TRM CLI, connect an SAP system, find a package, install it, verify it, update it, and understand how uninstall works.
---

# TRM ABAP package manager quick start

This guide takes you from the TRM command line to an installed ABAP package. Allow extra time for the one-off SAP-side server setup.

## 1. Prepare the SAP system

Install and configure `trm-server` in the SAP system that will publish or receive packages. Follow the [system setup guide](../server/setup.md), including the ICF service and authentication steps.

## 2. Install the TRM CLI

Install a current Node.js LTS release, then run:

```bash
npm install --global trm-client
trm --help
```

The second command should print the available TRM commands.

## 3. Add the SAP connection

Create a named system alias and provide the target system details when prompted:

```bash
trm alias create <NAME>
```

For the supported authentication and SAP Logon options, use the complete [client setup guide](../client/setup.md). SAP BTP destinations are covered separately in [Connect through SAP BTP](../client/btp_destination.md).

## 4. Find and install a package

Browse public packages at [trmregistry.com](https://trmregistry.com/search), then install the chosen package:

```bash
trm install <package-name>
```

TRM downloads the selected release, checks its requirements, resolves compatible dependencies, and imports its transports. Read [Install and update](../commons/install.md) before using the command in a governed landscape.

## 5. Verify the result

List installed TRM packages:

```bash
trm list
```

The installed name and version should appear. For a repeatable installation in another environment, commit the generated [lockfile](../commons/lockfile.md) and use the clean-install workflow documented there.

## 6. Update or uninstall

Use the install workflow to select a newer compatible release. When a package must be removed, TRM can create and import a deletion transport:

```bash
trm uninstall <package-name>
```

Uninstall can delete repository objects and data. Review the full [uninstall guide](../commons/uninstall.md), its prompts, backups, rollback behavior, and landscape transport before running it.

## Next steps

- [Publish your first package](../commons/publish.md)
- [Declare dependencies](../commons/dependencies.md)
- [Automate delivery with GitHub Actions](../commons/github_actions.md)
- [Understand the `.trm` artifact](../commons/artifact.md)

*Author: TRM maintainers. Technical review: Regesta Group engineering. Last reviewed: 19 October 2026.*
