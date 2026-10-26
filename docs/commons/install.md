---
title: Install and update ABAP packages with TRM
description: Install or update versioned SAP ABAP packages with requirement checks, dependency resolution, CTS transports, and landscape delivery.
---

# Installing and updating a package

Installing brings a published TRM release into the SAP system you are connected to. The same
command also updates (or downgrades) a package that is already installed.

```bash
trm install <package name> [version]
```

| Command | Use it to |
| --- | --- |
| `trm install <package> [version]` | Install a release from a registry. The version defaults to `latest`; a [distribution tag](publish.md#release-candidates-and-tags) works too. |
| `trm update <package> [version]` | Same as install, but also reinstalls the version that is already installed. Without a package name, it updates the TRM client itself. |
| `trm import <file>` | Install from a local `.trm` file, for example in an [offline environment](../faq.md#can-trm-work-in-an-offline-or-restricted-customer-environment). |
| `trm clean-install <package> [version]` | Install using a [lockfile](lockfile.md) (`-L, --lock-file`, default `trm-lock.json`), to reproduce the exact release of the package and of its dependencies. The version can be left out: it's taken from the lockfile. |

trm-server must be installed on the target system, see [Server setup](../server/setup.md).

## What happens during an install

TRM runs its checks and asks its questions before changing the system. A few questions come later,
when they depend on what was already decided (namespace, update cleanup): if anything fails after
the first change, TRM [rolls back](#if-something-fails).

1. **Release checks.** TRM picks the [landscape transport target](package_across_landscape.md#choosing-the-target-route),
   downloads the release and validates its manifest. When an integrity value is provided
   (`--integrity`, or a [lockfile](lockfile.md)), the download must match it.
2. **Already installed?** Installing the version that is already there stops with an error,
   unless you use `--overwrite` or `trm update`. A newer version is an upgrade, an older one a
   downgrade.
3. **Dependants.** On an update, TRM checks that the packages that depend on this one accept the
   new version. If one of them doesn't, the install stops and TRM tells you which package to
   upgrade first.
4. **Content checks.** TRM checks that the system supports every object type in the release, that
   none of the objects is locked in an open transport request, and that none of them belongs
   somewhere else (see [Existing objects](#existing-objects)).
   `--no-obj-types` installs objects of types the system doesn't support: TRM warns instead of
   stopping. Their import ends with return code 8 or higher, so pass `--ignore-import-errors` too.
   If the release includes translations or customizing, TRM asks whether to import the translations
   and each customizing transport (the default answer is yes). To answer in advance,
   `--lang-tr` and `--cust-tr` import them, `--no-lang-tr` and `--no-cust-tr` skip them.
5. **Requirements.** TRM checks the [SAP entries](sap_entries.md) and the [engines](engines.md)
   (software components, support packages, SAP Notes, ...) required by the release.
   `--no-sap-entries` and `--no-engines` skip these checks.
6. **Dependency conflicts.** If two packages need versions of the same dependency that can't
   coexist, or the dependencies form a cycle, the install stops. See
   [Dependencies and conflicts](../faq.md#what-happens-when-two-packages-require-incompatible-versions-of-one-dependency).
7. **ABAP packages.** TRM decides which ABAP packages receive the objects, and their transport
   layer. See [Choosing the ABAP packages](#choosing-the-abap-packages).
8. **Locks.** TRM [locks](action_locks.md) the package, its ABAP packages and objects, so no other
   TRM operation can change them in the meantime.
9. **Dependencies.** TRM lists the TRM packages the release needs that are missing or installed in
   an incompatible version, asks, and installs each one with these same steps (`--no-deps` skips
   them). Each dependency gets its own landscape transport.
10. **Namespace and ABAP packages.** TRM registers the namespace if needed and creates the ABAP
    packages.
11. **Update cleanup and backup.** On an update, TRM plans what to delete (see
    [What an update changes](#what-an-update-changes)). It then takes a
    [backup](transports.md#backup-transports) of what it is about to overwrite or delete.
12. **Import.** TRM imports the release transports and, on an update, the deletions.
13. **Landscape transport.** TRM collects everything it installed in a new transport request. See
    [Moving the package through the landscape](#moving-the-package-through-the-landscape).
14. **Post activities.** TRM runs the [post activities](post_activities.md) of the release, unless
    you pass `--skip-post-activities`.
15. **Record.** TRM records the installed release on the system: `trm list` shows it.
16. **Release.** TRM releases the landscape transport.

> ⚠️ Don't interrupt an install while transports are being imported or released.

`--simulate` runs every check and question, then shows what would change without installing.
`--ignore-import-errors` logs imports ending with return code 8 or higher as errors instead of
failing.

## Choosing the ABAP packages

A release carries the ABAP package names of the publisher, for example `ZACME_TOOLS`. On the
target system you can keep these names or install into packages of your own, to follow your
naming conventions.

- **Interactive install:** TRM asks whether to rename the packages and proposes a name for each one.
- **Keep the publisher's names:** pass `--keep-original`.
- **Explicit mapping:** pass `--package-replacements` with a JSON list (or the path of a JSON file):

```json
[
  { "originalDevclass": "ZACME_TOOLS", "installDevclass": "ZCUST_ACME_TOOLS" },
  { "originalDevclass": "ZACME_TOOLS_UI", "installDevclass": "ZCUST_ACME_TOOLS_UI" }
]
```

TRM remembers the mapping: on the next update it proposes the same names, or reuses them without
prompts. Mappings you pass on an update are merged with the remembered ones. Dependencies don't
inherit `--keep-original` or `--package-replacements`: each one asks for its own names, or uses the
original or remembered ones without prompts.

Some rules apply:

- If one package is temporary (`$` prefix), all of them must be. Temporary packages aren't
  transported, so no landscape transport is created.
- A package can't be installed inside the ABAP packages of another installed TRM package, nor
  contain the root package of one.
- New transportable packages need a transport layer that routes to the landscape transport target.
  If only one layer routes there, TRM uses it; if several do, TRM asks, proposing the system default
  first (without prompts, it uses the system default if it is routed, otherwise it stops). Use
  `-T, --transport-layer` to choose it. Without a landscape target, the system default is used.
  An existing package whose layer doesn't route to the target stops the install.
- If the objects use a reserved namespace (for example `/ACME/`) that doesn't exist on the system,
  TRM asks whether to import it with the repair license shipped in the release (the default answer
  is yes). Pass `--namespace` to import it without asking, or `--no-namespace` to skip it. If it
  isn't imported, the install stops when TRM must create ABAP packages in that namespace, and
  otherwise continues with a warning. If you rename the packages into another namespace that
  doesn't exist, add it in `SE03` first.

## Existing objects

Before importing, TRM looks for objects of the release that already exist on the system:

- **Objects of the same package**, during an update: expected, they are replaced.
- **Objects that belong somewhere else:** the install stops, so TRM never overwrites a development
  it doesn't own. The error lists the objects.
- **Objects of the installed release that someone moved** to another ABAP package: TRM asks before
  overwriting them and moving them back.

`--no-obj-check` skips this check. Use it only when you know the existing objects can be
overwritten.

## Local changes

TRM tracks changes made on the target system to the objects of an installed package (for example
a hot fix made directly in production). Such a package is called **dirty**. Run `trm dirty <package>`
to see what changed.

- **Update to another version:** TRM warns that the changes will be overwritten, then continues.
- **Reinstall of the same version** (`--overwrite` or `trm update`): TRM asks for confirmation
  (default no).

Bring important local changes back into the package source before updating, or they are lost.

## What an update changes

An update replaces the installed release with the new one:

- Objects that are no longer part of the release are **deleted**. TRM lists objects that are about
  to be deleted but were never part of the package (for example objects a developer created inside
  its ABAP packages) and asks before deleting them.
- Installed objects that someone moved out of the package and that the new release no longer ships
  are **kept**, unless you confirm their deletion (default no).
- **Tables keep their data** when they are still part of the release.
- **Customizing** follows the rules in
  [Customizing on update and uninstall](customizing_guidelines.md#customizing-on-update-and-uninstall).
- ABAP packages that become empty are deleted. The namespace is deleted only when nothing else on
  the system uses it, the new release doesn't use it, and it isn't a producer namespace.

The update stops if an object or package to delete is locked in an open transport request. The
deletions are carried by [deletion transports](transports.md#deletion-transports) and reach the
rest of the landscape inside the landscape transport.

## Moving the package through the landscape

An install takes place on one system, typically the first one of your landscape. The rest of the
landscape receives the package through the **landscape transport**, an ordinary transport request
that TRM releases to the target you choose (`--landscape-tr-target`). The following systems don't
need TRM. See [Move an installed package through the landscape](package_across_landscape.md).

## If something fails

When a step fails, TRM undoes the steps already completed, in reverse order: it removes imported
objects, restores the previous release on an update, removes the transports it created (see
[Transports](transports.md#if-something-fails)), and uninstalls the dependencies it installed or
brings them back to the version they had.

Rollback is best effort. Some operations can't be fully reversed: a post activity, a transport
already released to another system, or an upgrade of trm-server or trm-rest once imported. When TRM
can't clean something up, it says so in the log. See also [Locks](action_locks.md) if a failed run
left a lock behind.

## Installing without prompts

Pass `--no-prompts` to install from a script or a pipeline. TRM then makes these decisions on its own:

| Decision | Without prompts |
| --- | --- |
| Missing dependencies | Installed (`--no-deps` skips them) |
| Translations | Imported, unless `--no-lang-tr` |
| Customizing transports | All imported, unless `--no-cust-tr` |
| Missing reserved namespace | Imported only with `--namespace`; otherwise the install stops when ABAP packages must be created in it |
| Downgrading a dependency | Stops, unless `--allow-downgrade` |
| Existing objects | Stops, unless `--no-obj-check` |
| Objects of the installed release moved to other ABAP packages | Stops, unless `--no-obj-check` |
| ABAP package names | Kept as published, or as remembered from the previous install, unless `--package-replacements` |
| Transport layer, when several route to the target | System default if routed, otherwise stops (`-T, --transport-layer`) |
| Landscape transport target | Required when the system has more than one target (`--landscape-tr-target`) |
| Local changes on a reinstall of the same version | Stops |
| Extra objects deleted by an update | Deleted, with a warning in the log |
| Moved-out objects the new release no longer ships | Kept |
| Customizing rows the new release no longer ships | See [Customizing on update and uninstall](customizing_guidelines.md#customizing-on-update-and-uninstall) |
