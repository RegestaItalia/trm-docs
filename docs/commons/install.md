# Installing and updating a package

Installing brings a published TRM release into the SAP system you are connected to. The same
command also updates (or downgrades) a package that is already installed.

```bash
trm install <package name> [version]
```

| Command | Use it to |
| --- | --- |
| `trm install <package> [version]` | Install a release from a registry. The version defaults to `latest`; a [distribution tag](publish.md#release-candidates-and-tags) works too. |
| `trm update <package> [version]` | Same as install, but also reinstalls the version that is already installed. |
| `trm import <file>` | Install from a local `.trm` file, for example in an [offline environment](../faq.md#can-trm-work-in-an-offline-or-restricted-customer-environment). |
| `trm clean-install <package> [version]` | Install using a [lockfile](lockfile.md), to reproduce the exact release of the package and of its dependencies. The version can be left out: it's taken from the lockfile. |

trm-server must be installed on the target system, see [Server setup](../server/setup.md).

## What happens during an install

TRM runs every check first and changes the system only once they all pass.

1. **Release checks.** TRM downloads the release and validates its manifest. When an integrity
   value is provided (for example from a [lockfile](lockfile.md)), the download must match it.
2. **Already installed?** Installing the version that is already there stops with an error,
   unless you use `--overwrite` or `trm update`. A newer version is an upgrade, an older one a
   downgrade.
3. **Dependants.** On an upgrade, TRM checks that the packages that depend on this one accept the
   new version. If one of them doesn't, the install stops and TRM tells you which package to
   upgrade first.
4. **Content checks.** TRM checks that the system supports every object type in the release, and
   that none of the objects is locked in an open transport request.
   If the release includes translations or customizing, TRM asks whether to import the translations
   and each customizing transport (the default answer is yes). To answer in advance,
   `--lang-tr` and `--cust-tr` import them, `--no-lang-tr` and `--no-cust-tr` skip them.
5. **Existing objects.** If objects of the release already exist on the system, outside of this
   package, TRM stops instead of overwriting them. See [Existing objects](#existing-objects).
6. **Requirements.** TRM checks the [SAP entries](sap_entries.md) and the [engines](engines.md)
   (software components, support packages, SAP Notes, ...) required by the release.
7. **Dependencies.** TRM lists the TRM packages the release needs that are missing or installed in
   an incompatible version, and asks before installing them. If two packages need versions of the
   same dependency that can't coexist, or the dependencies form a cycle, the install stops before
   anything is installed. See [Dependencies and conflicts](../faq.md#what-happens-when-two-packages-require-incompatible-versions-of-one-dependency).
8. **ABAP packages.** TRM decides which ABAP packages receive the objects. See
   [Choosing the ABAP packages](#choosing-the-abap-packages).
9. **Locks.** TRM [locks](action_locks.md) the package, its ABAP packages and objects, so no other
   TRM operation can change them in the meantime.
10. **Install the dependencies**, each one with the same steps.
11. **Import.** TRM creates the ABAP packages, registers the namespace if needed, and imports the
    transports.
12. **Landscape transport.** TRM collects everything it installed in a new transport request and
    releases it. See [Moving the package through the landscape](#moving-the-package-through-the-landscape).
13. **Post activities.** TRM runs the [post activities](post_activities.md) of the release, unless
    you pass `--skip-post-activities`.
14. **Record.** TRM records the installed release on the system: `trm list` shows it.

> ⚠️ Don't interrupt an install while transports are being imported or released.

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

TRM remembers the mapping: the next update installs into the same packages, so you only answer
once. Mappings you pass on an update are merged with the remembered ones.

Some rules apply:

- If one package is temporary (`$` prefix), all of them must be. Temporary packages aren't
  transported, so no landscape transport is created.
- A package can't be installed inside the ABAP packages of another installed TRM package.
- New transportable packages get the system's default transport layer. Use `-T, --transport-layer`
  to choose another one.
- If the objects use a reserved namespace (for example `/ACME/`) that doesn't exist on the system,
  TRM asks whether to import it with the repair license shipped in the release (the default answer
  is yes). Pass `--namespace` to import it without asking, or `--no-namespace` to skip it. If you
  decline, or install [without prompts](#installing-without-prompts) and without `--namespace`, the
  install stops when
  ABAP packages must be created in that namespace; add the namespace in `SE03` or rerun with
  `--namespace`.

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
- **Reinstall of the same version** (`--overwrite` or `trm update`): TRM asks for confirmation.

Bring important local changes back into the package source before updating, or they are lost.

## What an update changes

An update replaces the installed release with the new one:

- Objects that are no longer part of the release are **deleted**. TRM lists objects that are about
  to be deleted but were never part of the package (for example objects a developer created inside
  its ABAP packages) and asks before deleting them.
- **Tables keep their data** when they are still part of the release. See
  [Table updates](table_updates.md) for the details and the risky table changes.
- **Customizing** of the installed release is replaced by the customizing of the new one. See
  [Customizing guidelines](customizing_guidelines.md#customizing-on-update-and-uninstall).
- ABAP packages that become empty are deleted. The namespace is deleted only when nothing else on
  the system uses it.

Before changing anything, TRM takes a **backup** of what the update may delete. Deleted objects are
collected in a **deletion transport**: TRM imports it on the system, and adds its deletions to the
landscape transport, as described below. See [Transports](transports.md#when-you-install-or-update).

## Moving the package through the landscape

An install takes place on one system, typically the first one of your landscape (for example the
development system). TRM then prepares what the rest of the landscape needs:

- The **landscape transport** contains the ABAP packages, objects, namespace, translations and
  customizing that were installed. TRM releases it to the transport target you choose (`--landscape-tr-target`),
  and it follows your normal import route to quality and production.
- On an update, the landscape transport also contains the **deletions** of the update: importing
  it installs the new release and removes what the old one had and the new one doesn't. There is
  no separate deletion transport to move.

No landscape transport is created when:

- the system has no transport targets: TRM considers it the last system of the landscape;
- the package is installed into temporary (`$`) packages.

The following systems don't need trm-server: they receive ordinary transports. The other transports
TRM creates during the install stay on this system, see [Transports](transports.md).

For the complete operational flow—including which installation requests should not be forwarded,
what remains after a successful install or update, and the required update import order—see
[Move an installed package through the landscape](../examples/7_package_across_landscape.md).

## If something fails

When a step fails, TRM undoes the steps already completed, in reverse order: it removes imported
objects, restores the previous release on an update, deletes the transports it created, and
uninstalls the dependencies it installed. The error explains what went wrong.

Rollback is best effort. Some operations can't be fully reversed (for example a post activity, or a
transport already released to another system). When TRM can't clean something up, it says so in the
log, for example a transport to remove from an import queue in STMS. See also
[Locks](action_locks.md) if a failed run left a lock behind.

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
| Landscape transport target | Required when the system has more than one target (`--landscape-tr-target`) |
| Local changes on a reinstall of the same version | Stops |
| Extra objects deleted by an update | Deleted, with a warning in the log |
