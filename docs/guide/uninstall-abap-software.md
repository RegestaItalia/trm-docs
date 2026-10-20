---
title: Uninstall ABAP software with deletion transports
description: See how TRM backs up, validates, removes, rolls back, and transports the removal of ABAP package objects and customizing.
---

# Uninstall ABAP software with deletion transports

TRM removes an installed ABAP package by generating and importing SAP CTS deletion transports. It plans the exact installed content, creates backup transports, validates the generated deletion against that plan, test-imports it, imports it, and can carry the deletion through the rest of the landscape in a released transport.

This is a lifecycle operation, not a source-folder cleanup. It can cover repository objects, customizing keys, nested packages, and local packages while preserving the safeguards expected for a governed SAP landscape.

!!! warning
    Uninstall is destructive. Confirm backups, dependency impact, dirty-object handling, target-system routing, and recovery procedures before running it in a shared or productive landscape.

## What happens during uninstall

The exact steps depend on the installed release, but the guarded workflow is:

1. Find the installed package and its recorded transports and content.
2. Refuse removal when another installed package depends on it, unless that check is explicitly overridden.
3. Detect dirty or changed objects so locally modified work is not silently removed.
4. Plan repository-object, development-package, and customizing cleanup.
5. Export backups for content that can be restored.
6. Generate deletion transports for the confirmed cleanup plan.
7. Verify that the returned deletion contains nothing outside the confirmed plan.
8. Upload and test-import each deletion transport before the real import.
9. Import the deletion and update TRM's installed-package records.
10. When requested, release one landscape transport that carries the deletions to the next system.

The command-line entry point is:

```bash
trm uninstall <package-name>
```

Review the prompts and options in the [uninstall command guide](../commons/uninstall.md) before executing it.

## Why a deletion transport matters

Deleting objects directly in one development system does not by itself create a repeatable landscape operation. TRM expresses the removal as transport content so the same approved deletion can move through CTS-controlled systems.

For a landscape uninstall, the resulting transport exports deleted objects as deletion entries. Nested-package removals are folded into the parent operation, so operators receive one landscape transport rather than an unrelated set of local cleanups.

## Guardrails before deletion

TRM checks several conditions before importing a deletion:

- installed dependants can block removal;
- dirty objects require an explicit decision;
- the generated deletion is compared with the planned objects and customizing keys;
- a deletion transport is test-imported before its real import;
- import return codes of 8 or higher fail by default;
- deletion transports are available only for package releases that support managed removal.

These checks make the operation inspectable. They do not remove the need for SAP change-control, backups, authorizations, or target-system validation.

## Rollback behavior

Backups are part of the workflow because a later step can fail. If deletion import or a subsequent workflow step fails, TRM attempts to restore exported content, reverse nested operations in the opposite order, repair package records, and remove or dequeue temporary deletion requests.

A failed rollback is reported separately and requires manual inspection. Operators should keep the generated transport identifiers and command output with the change record.

## Upgrades use the same removal path

An upgrade may need to remove objects or customizing that the new version no longer ships. TRM uses the same cleanup and deletion-generation path for those differences, then includes the deletions in the upgrade's landscape transport. This avoids leaving obsolete package content behind after a successful version update.

## Implementation and test evidence

The uninstall workflow and its safety checks are public:

- [uninstall workflow](https://github.com/RegestaItalia/trm-core/tree/main/src/actions/uninstall)
- [deletion generation and validation](https://github.com/RegestaItalia/trm-core/blob/main/src/actions/commons/utils/generateDeletion.ts)
- [cleanup planning, backups, customizing, and rollback](https://github.com/RegestaItalia/trm-core/blob/main/src/actions/commons/utils/packageCleanup.ts)
- [deletion workflow tests](https://github.com/RegestaItalia/trm-core/blob/main/src/actions/uninstall/generateDeletionTransport.test.ts)
- [landscape transport tests](https://github.com/RegestaItalia/trm-core/blob/main/src/actions/uninstall/generateLandscapeTransport.test.ts)
- [TRM CLI uninstall command](https://github.com/RegestaItalia/trm-client/blob/main/src/command/implementations/Uninstall.ts)

## Continue the lifecycle

- [Install and update a package](../commons/install.md)
- [Understand SAP CTS transports in TRM](../commons/transports.md)
- [Manage package dependencies](abap-dependency-management.md)
- [Follow the package-manager quick start](quickstart.md)

*Author: TRM maintainers. Technical review: Regesta Group engineering. Last reviewed: 19 October 2026.*
