---
title: How TRM uses SAP CTS transports
description: Learn how TRM creates, packages, imports, updates, and propagates SAP CTS transports for versioned ABAP software delivery.
---

# Transports created by TRM

TRM moves ABAP code and customizing with standard SAP transport requests. When you publish, install, update or
uninstall a package, TRM creates some transport requests on your system, and you will see them in
`SE09`/`SE10` and in the `STMS` import queues.

This page lists which transports TRM creates, what they contain, and what you should do with
each one. In short, **the only transports you move to the rest of your landscape are landscape
transports**: see [Move an installed package through the landscape](package_across_landscape.md).
TRM uses the others internally.

## How to recognize a TRM transport

The description of each transport TRM creates starts with a transport icon (`@X1@`, shown as an
icon in SAP GUI) followed by **TRM**, the package name and the version, cut to 60 characters. A
short label in brackets tells you its role:

| Description | What it is |
| --- | --- |
| `TRM @acme/tools v1.2.0` | Objects of the package |
| `TRM @acme/tools 1.2.0` | Landscape transport of an install |
| `TRM (D) @acme/tools v1.2.0` | ABAP package definitions |
| `TRM (L) @acme/tools v1.2.0` | Translations |
| `TRM (BKP) @acme/tools 1.1.0` | Backup taken before TRM changes something |
| `TRM (DELE) @acme/tools 1.1.0` | Deletion of objects or customizing, or landscape transport of an uninstall |

Customizing transports keep the description of the customizing request they come from.

Publish transports and the landscape transport of an install also carry the package name and
version inside the transport, and the package [manifest](manifest.md) in its documentation, so you
can tell which release they belong to even after they have moved through the landscape. The
landscape transport of an uninstall carries the package name and version only.

## When you publish

`trm publish` takes a snapshot of the ABAP package as transports, which make up the
[artifact](artifact.md) of the release (see [Publishing a package](publish.md)).

| Transport | Contains | Created |
| --- | --- | --- |
| **Package definitions** (`D`) | The ABAP package and its subpackages | Always |
| **Objects** | All the repository objects: programs, classes, tables, CDS views, ... | Always |
| **Translations** (`L`) | The translated texts of the objects | Unless `--no-lang-tr` |
| **Customizing** | A copy of a customizing request you chose to ship | One for each customizing request added to the release, unless `--no-cust-tr`. See [Customizing guidelines](customizing_guidelines.md) |

These are *transports of copies*, released to the transport target you choose during the publish,
so they may show up in that system's import queue. A translations or customizing transport that
ends up empty is deleted right away.

**Don't import them anywhere.** To deliver the package to another system, install it with
`trm install`: an install also checks requirements and dependencies, and keeps track of what was
installed.

## When you install or update

`trm install` runs on one system, usually the first system of your landscape. On that system, TRM
creates the following transports.

### Release transports

One transport for each part of the release that is installed: package definitions, objects,
translations and each customizing transport. TRM fills them with the content of the release and
imports them on this system.

- Package definitions are imported only when you keep the publisher's ABAP package names. When
  you install into packages with your own names, TRM creates those packages directly.
- Translations and customizing transports you choose to skip are not created.
- When you install from a `.trm` file, these transports keep the number they have in the file.

They stay in this system's import history. **Don't move them to other systems**: their content is
already in the landscape transport.

### Backup transports

Before changing anything, TRM copies what it is about to overwrite or delete:

- on an **update**, the objects and the customizing of the installed release (one backup each);
- on any install, the objects of the release that already exist on the system and would be
  overwritten.

Objects in temporary (`$`) packages can't be backed up: TRM warns, and a rollback can't restore
them.

Backups are released and stay in this system's import queue, **without being imported**. If the
install fails, TRM imports them to bring the system back to how it was. They remain in the queue
even after a successful install, so you can still restore the previous state by hand.

- **Don't import them** unless you want to go back to the state before the install.
- **Never forward them** to other systems.
- You can remove them from the queue when you no longer need a way back.

### Deletion transports

An update removes what the new release no longer needs (see
[What an update changes](install.md#what-an-update-changes)). The **registry** generates the
deletion transports from the backups, one for the objects and one for the customizing, and TRM
imports them on this system after the new release. Their deletions are also added to the landscape
transport, so you don't move them either.

If the registry can't generate them, the update continues without deleting anything and lists the
leftover objects and customizing keys for manual cleanup.

### Landscape transport

When everything is installed, TRM creates **one ordinary transport request** with:

- the ABAP packages, with the names used on this system;
- all the objects of the release;
- the namespace, when this install added it (if it is locked in another transport, TRM leaves it
  out and warns);
- the translations and customizing you imported;
- on an update, the deletions of the update.

Each dependency installed along with the package gets its own landscape transport.

**This is the transport to move** to quality and production. See
[Move an installed package through the landscape](package_across_landscape.md) for the target, the
import order, and the cases where no landscape transport is created.

### Summary

| Transport | When | Where it ends up | Move it to other systems? |
| --- | --- | --- | --- |
| Release transports | Every install | Imported on this system | No |
| Backup (`BKP`) | Updates, and installs that overwrite existing objects | Import queue of this system, not imported | No |
| Deletion (`DELE`) | Updates that remove something | Imported on this system | No |
| Landscape transport | When the system has a transport target | Import queue of the target you choose | **Yes** |

## When you uninstall

[`trm uninstall`](uninstall.md) works like an update to "nothing":

1. a **backup** (`BKP`) of the objects and, when the package has customizing, one of the
   customizing, kept in this system's import queue;
2. up to two **deletion** transports (`DELE`, objects and customizing), generated by the registry
   and imported on this system;
3. a **landscape transport** described as `TRM (DELE) <package> <version>`, with the same deletions,
   released to the transport target you choose. A single landscape transport also carries the
   deletions of the TRM packages installed inside the package.

## If something fails

TRM undoes what it already did, in reverse order. It re-imports the backups, deletes the
transports it created when SAP still allows it, and otherwise takes them out of the import queue
so they can't be imported by mistake. Backups always stay in the queue.

TRM can only change the import queue of the system it is connected to. If a transport already
reached another system's queue, the log tells you to remove it there in `STMS`.
