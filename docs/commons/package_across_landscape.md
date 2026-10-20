---
title: Move an ABAP package across a landscape
description: Install a TRM package and promote its landscape transport through SAP development, quality, and production systems.
---

# Move an installed package through the landscape

Run `trm install` or `trm update` on the first system of a transport route. TRM installs the
release there, then releases an ordinary CTS **landscape transport** for the systems that follow
it. Move that transport through QA and production with the same STMS process you use for other
changes. For the content of the landscape transport and of every other request TRM creates, see
[Transports](transports.md).

## Choosing the target route

TRM reads the transport targets of the connected SAP system before running any check.

- With one target, it is used automatically.
- With several targets, choose one interactively or pass `--landscape-tr-target <SID>`. Without
  prompts, the option is required.
- With no target, TRM treats the connected system as the last one of the landscape and creates no
  landscape transport. Passing `--landscape-tr-target` there is an error.

Choose the immediate next system in the route: once the request is in CTS, normal transport routes
determine its later path. New transportable ABAP packages get a transport layer that routes to that
target (see [Choosing the ABAP packages](install.md#choosing-the-abap-packages)).

For a repeatable pipeline, make the target explicit:

```bash
trm install @acme/tools 2.4.0 --no-prompts --landscape-tr-target QAS
```

The same option works on `trm update`, `trm clean-install` and [`trm uninstall`](uninstall.md).

## Which requests to move

Move **only landscape transports**. Release, backup and deletion requests stay on the installation
system.

- When TRM installs or updates dependencies along with the package, each dependency gets its own
  landscape transport, released before the package's own. Import them in the order they were
  released.
- On an update, the landscape transport contains both the new release and the deletions of the
  update: importing it on QA and production installs the new version and removes the obsolete
  content. There is no separate deletion request to move.
- On an uninstall, the landscape transport carries the deletions and removes the package from the
  following systems.

The landscape transport of an install is described as `TRM <package> <version>`, without the `v`
that the imported objects transport has. Use the transport number printed by the command, or shown
in the target import queue, as the authoritative request to move.

## When no transport is generated

TRM creates no landscape transport when:

- the connected system has no transport target;
- the package is installed into temporary (`$`) ABAP packages, which are local to the system and
  can't be released through CTS;
- an uninstall has nothing to delete.

An update or uninstall of a temporary installation still cleans up locally, but its deletions don't
reach other systems. To promote the package, install it into transportable ABAP packages and make
sure the system has the correct TMS route.

## What happens on downstream systems

QA and production receive ordinary CTS imports. They don't need trm-server, registry access or the
TRM client. Don't run `trm install` again on systems of the same route: that would create separate
installations instead of promoting the tested transport.

Only the install on the first system downloads from the registry, checks dependencies and
requirements, asks questions and runs [post activities](post_activities.md). Importing the landscape
transport doesn't run post activities: if one must run on each downstream system or client, include
that step in the deployment procedure of that environment.

TRM records installed packages only on the system where `trm install` ran, so `trm list` on a
downstream system doesn't prove that the import completed. Use the STMS import history and the usual
functional checks there.

## If the release or the install fails

Releasing the landscape transport is the last step. If only the release fails, the package stays
installed (or uninstalled) and TRM tells you to release the transport manually in `SE09`, or to
check it in STMS if it was released after all.

If the install fails after a dependency was installed, TRM rolls the dependency back and removes
its landscape transport: it deletes it while SAP allows it, otherwise it takes it out of the target
queue, which it can only do when the target is the connected system. Otherwise the log tells you to
remove it manually in STMS. Do that before retrying. See also
[If something fails](install.md#if-something-fails).

## Operational checklist

After `trm install`, `trm update` or `trm uninstall` reports success:

1. Record the landscape transport numbers from the command output or the target import queue.
2. In STMS, confirm they are in the target queue.
3. Import them into QA, in release order, review the return codes and application checks, then
   promote the same requests to production.
4. Keep the requests in the normal change-management record.
