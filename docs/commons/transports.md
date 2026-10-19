# Transports created by TRM

TRM moves ABAP code and customizing with standard SAP transport requests. When you publish, install, update or
uninstall a package, TRM creates some transport requests on your system, and you will see them in
`SE09`/`SE10` and in the `STMS` import queues.

This page explains which transports TRM creates, what they contain, and what you should do with
each one. In short, **after an install or update, the only transport you move to the rest of
your landscape is the landscape transport**. TRM uses the others internally.

## How to recognize a TRM transport

The description of each transport TRM creates starts with **TRM** and a transport icon, followed by
the package name and version. A short label in brackets tells you its role:

| Description | What it is |
| --- | --- |
| `TRM @acme/tools v1.2.0` | Objects of the package |
| `TRM @acme/tools 1.2.0` | Landscape transport of an install |
| `TRM (D) @acme/tools v1.2.0` | ABAP package definitions |
| `TRM (L) @acme/tools v1.2.0` | Translations |
| `TRM (BKP) @acme/tools 1.1.0` | Backup taken before TRM changes something |
| `TRM (DELE) @acme/tools 1.1.0` | Deletion of objects or customizing that are no longer needed |

Customizing transports keep the description of the customizing request they come from.

TRM also writes the package name and version inside every transport, and the package
[manifest](manifest.md) in its documentation. That way you can tell which release a transport
belongs to even after it has moved through the landscape.

## When you publish

`trm publish` runs on the system where the package is developed. TRM takes a snapshot of the ABAP
package as transports, and uploads them to the registry (or writes them to a `.trm` file with
`trm pack`). Together, they make up the [artifact](artifact.md) of the release.

| Transport | Contains | Created |
| --- | --- | --- |
| **Package definitions** (`D`) | The ABAP package and its subpackages | Always |
| **Objects** | All the repository objects: programs, classes, tables, CDS views, ... | Always |
| **Translations** (`L`) | The translated texts of the objects | When the package has translations (`--no-lang-tr` skips it) |
| **Customizing** | A copy of a customizing request you chose to ship | One for each customizing request added to the release. See [Customizing guidelines](customizing_guidelines.md) |

These are *transports of copies*. TRM releases them to the transport target you choose during the
publish, so they may show up in that system's import queue.

What you should do:

- **Nothing.** They only exist to build the release. You don't need to import them anywhere.
- To deliver the package to another system, **install it** with `trm install`. Don't import the
  publish transports by hand: an install also checks requirements and dependencies, and keeps
  track of what was installed.
- An empty translations or customizing transport is deleted right away.
- If the publish fails before the upload, TRM deletes the transports it created. A transport that
  was already released can't be deleted, so it may stay in your transport list.

> Customizing carried over from the previous release isn't copied again: the new release reuses it.

## When you install or update

`trm install` runs on one system, usually the first system of your landscape (for example the
development system). On that system, TRM creates the following transports.

### Release transports

One transport for each part of the release that is installed: package definitions, objects,
translations and each customizing transport. TRM fills them with the content downloaded from the
registry, and imports them on this system.

- Package definitions are imported only when you keep the publisher's ABAP package names. When
  you install into packages with your own names, TRM creates those packages directly.
- Translations and customizing transports you choose to skip are not imported.
- When you install from a `.trm` file, these transports keep the number they have in the file.

They stay in this system's import history. **Don't move them to other systems**: their content is
already in the landscape transport.

### Backup transports

Before changing anything, TRM takes a copy of what it is about to overwrite or delete:

- on an **update**, the objects and customizing of the installed release (one backup for the
  objects and one for the customizing);
- on any install, the objects of the release that already exist on the system and would be
  overwritten.

Backups are released and stay in this system's import queue, **without being imported**. If the
install fails, TRM imports them to bring the system back to how it was. They remain in the
queue even after a successful install, so you can still restore the previous state by hand if
something turns out to be wrong later.

What you should do:

- **Don't import them** unless you want to go back to the state before the install.
- **Never forward them** to other systems.
- You can remove them from the queue when you no longer need a way back.

### Deletion transports

An update removes what the new release doesn't need anymore: objects that are no longer part of
the package, objects created by someone inside its ABAP packages, and customizing rows that the
new release doesn't ship. See [What an update changes](install.md#what-an-update-changes).

TRM asks the registry to build a deletion transport for them, starting from the backup (one for the
objects and one for the customizing), and imports it on this system together with the new release.
Its deletions are also added to the landscape transport, so you don't need to move it either.

### Landscape transport

When everything is installed, TRM creates **one ordinary transport request** with everything that
was installed:

- the ABAP packages, with the names used on this system;
- all the objects of the release;
- the namespace, when TRM had to add it;
- the translations and customizing you imported;
- on an update, the deletions of the update.

TRM releases it to the transport target you choose (`--landscape-tr-target`). **This is the
transport to move** to quality and production. Import it like any other transport: the following
systems don't need TRM, trm-server or access to the registry.

The landscape transport isn't created when:

- the system has no transport targets: TRM considers it the last system of the landscape;
- the package is installed into temporary (`$`) ABAP packages, which can't be transported.

See [Move an installed package through the landscape](../examples/7_package_across_landscape.md)
for the complete process.

### Summary

| Transport | When | Where it ends up | Move it to other systems? |
| --- | --- | --- | --- |
| Release transports | Every install | Imported on this system | No |
| Backup (`BKP`) | Updates, and installs that overwrite existing objects | Import queue of this system, not imported | No |
| Deletion (`DELE`) | Updates that remove something | Imported on this system | No |
| Landscape transport | When the system has a transport target | Import queue of the target you choose | **Yes** |

## When you uninstall

[`trm uninstall`](uninstall.md) works like an update to "nothing":

1. a **backup** (`BKP`) of the objects and customizing of the package, kept in this system's import queue;
2. a **deletion** transport (`DELE`), generated by the registry and imported on this system;
3. a **landscape transport** described as `TRM (DELE) <package> <version>`, with the same deletions,
   released to the transport target you choose. Move it like any other transport to remove the
   package from the following systems.

When the uninstall also removes TRM packages installed inside the package, a single landscape
transport carries all their deletions.

## Example: an update across three systems

```text
DEV  trm update @acme/tools 1.2.0
     ├─ backup        TRM (BKP) @acme/tools 1.1.0     stays in the DEV queue, not imported
     ├─ release       TRM @acme/tools v1.2.0, ...     imported on DEV
     ├─ deletion      TRM (DELE) @acme/tools 1.1.0    imported on DEV
     └─ landscape     TRM @acme/tools 1.2.0  ──────▶  QAS ──▶ PRD
```

On QAS and PRD you import a single transport: the landscape transport. It installs version 1.2.0
and removes what 1.1.0 had and 1.2.0 doesn't.

## If something fails

TRM undoes what it already did, in reverse order. It re-imports the backups, deletes the
transports it created when SAP still allows it, and otherwise takes them out of this system's import
queue so they can't be imported by mistake. Backups always stay in the queue.

TRM can only change the import queue of the system it is connected to. If a transport already
reached another system's queue, the log tells you to remove it there in `STMS`. See also
[If something fails](install.md#if-something-fails).
