---
title: Uninstall ABAP packages with deletion transports
description: Learn how TRM removes ABAP package objects and customizing with backups, rollback, deletion transports, and landscape propagation.
---

# Uninstalling a package

Uninstalling removes an installed TRM package from the SAP system you are connected to: its
objects, its ABAP packages, its customizing, and its TRM record. TRM can also carry the removal
through the rest of your landscape.

```bash
trm uninstall <package name>
```

## Before you start

- The package must be installed on the connected system: `trm list` shows the installed packages.
- The **registry the package was installed from must be reachable**. TRM asks the registry to
  generate the transport that deletes the objects, so an uninstall can't run fully offline. A
  package installed from a `.trm` file is uninstalled through the registry it was published to.
- trm-server and trm-rest can't be uninstalled: TRM needs them.
- Objects of the package must not be locked in open transport requests.

## What happens during an uninstall

1. **Local changes.** If the package is [dirty](install.md#local-changes) (its objects were changed
   on this system), TRM lists the changes and asks before deleting them. `--ignore-dirty` continues
   without asking.
2. **Dependants.** If other installed packages depend on this one, TRM lists them and asks before
   continuing: they might stop working. `--no-dependants` skips this check.
3. **Packages installed inside it.** If other TRM packages are installed inside the ABAP packages of
   this one, they would be deleted with it. TRM lists them and asks, then uninstalls each of them
   first, with the same options.
4. **Locks.** TRM [locks](action_locks.md) the package, its ABAP packages and its transport.
5. **Backup and deletion transport.** TRM backs up what it is about to delete, builds a transport
   that deletes the objects of the installed release, and imports it on the system. See
   [What is deleted](#what-is-deleted) and [Transports](transports.md#when-you-uninstall).
6. **Record.** TRM removes the package from its records: `trm list` no longer shows it.
7. **Landscape.** TRM copies the deletions into a landscape transport and releases it to the
   transport target, so the package is removed from the following systems too. See
   [Removing the package from the landscape](#removing-the-package-from-the-landscape).

> ⚠️ Don't interrupt an uninstall while the deletion transport is being imported.

## Removing the package from the landscape

When you installed the package, TRM released a [landscape transport](install.md#moving-the-package-through-the-landscape)
that carried it to your quality and production systems. The uninstall does the opposite: it
releases a landscape transport described as `TRM (DELE) <package> <version>`, containing the
deletions, to the transport target you choose (`--landscape-tr-target`). Import it like any other
transport, and the package disappears from the following systems too. When the uninstall also
removes TRM packages installed inside this one, the same transport carries their deletions.

No landscape transport is created when the system has no transport targets (TRM considers it the
last system of the landscape), when the package was installed into temporary (`$`) packages, or
when nothing was deleted.

> The TRM record is removed only on the system where you run the uninstall. Following systems
> don't record TRM packages: they only receive transports.

## If something fails

TRM undoes the completed steps: it re-imports the backup of the deleted objects, restores the TRM
record, reinstalls the nested packages it uninstalled, and removes the deletion transport from the
import queue of the connected system.

Releasing the landscape transport is the last step: if only the release fails, the package stays
uninstalled and TRM tells you to release the transport manually in `SE09`.

## Uninstalling without prompts

With `--no-prompts`, TRM stops instead of asking in the risky cases:

| Situation | Without prompts |
| --- | --- |
| Local changes | Stops, unless `--ignore-dirty` |
| Installed packages depend on it | Stops, unless `--no-dependants` |
| Other TRM packages installed inside it | Uninstalled too, with a warning in the log |
| Objects created inside its ABAP packages | Deleted, with a warning in the log |
| Objects moved to other ABAP packages | Kept |
| Customizing rows to delete | Deleted, with a warning in the log |
| Transport target | Required when the system has more than one target (`--landscape-tr-target`) |
