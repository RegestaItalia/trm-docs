---
title: Move an ABAP package across a landscape
description: Install a TRM package and promote its landscape transport through SAP development, quality, and production systems.
---

# Move an installed package through the landscape

Run `trm install` or `trm update` on the first system of a transport route. TRM imports the
release there, then creates one ordinary CTS transport for the systems that follow it. Move that
transport through QA and production with the same STMS process you use for other changes.

This page explains how to choose the route, identify the request to promote, and handle it on
downstream systems. For the contents and lifecycle of every request TRM creates, see
[Transports](transports.md).

## Move only the landscape transport

TRM may leave release, backup, deletion, or staging requests visible on the installation system.
Do not add them to the route. The released landscape transport consolidates what TRM actually
installed, including the selected translations and customizing and, for an update, any deletions.
It is the only request to import into the systems that follow.

## What remains after a successful first install

On the system where `trm install` ran, you are left with:

- the installed ABAP packages and repository objects;
- any translations and customizing that you chose to import;
- the namespace registration, if TRM had to add one;
- a released landscape transport in the selected target system's import queue;
- TRM's local installation record, including the manifest, version, checksum, registry, root SAP
  package, package-name mappings, and the imported LANG and CUST transport numbers.

The landscape request has a description similar to `TRM <package> <version>`. TRM also writes the
package name, version, and manifest into the request. Those details make the request identifiable;
operators should still use the transport number printed by the successful command or shown in
the target import queue as the authoritative request to move.

TRM records the landscape transport as the installation transport. If no landscape transport is
created, it records the imported TADIR transport instead. The LANG and CUST request numbers are
stored separately because a later update or uninstall needs to identify their installed content,
especially customizing table keys.

## What remains after an update

An update first backs up what it may delete on the system where the command runs, then imports the
new release and removes what the installed version had and the new one doesn't. Objects that exist
in both versions are updated; tables that exist in both are retained so their data is not dropped.
Objects and now-empty SAP packages that disappeared from the release are removed.

For a transportable installation, the new released landscape transport contains both the new
release and the update's deletions. Importing that one request on QA and production installs the
new version and removes the obsolete content, so there is no separate import order to maintain.

## Choosing the target route

TRM reads the transport targets available from the connected SAP system.

- With one target, that route can be used for the generated requests.
- With several targets, choose the intended one interactively or pass
  `--landscape-tr-target <SID>`. In non-interactive runs, the option is required when the choice is
  ambiguous.
- With no target, TRM treats the connected system as the final system and creates no landscape
  transport.

The target belongs to the generated landscape request. Choose the immediate next system in the route, not an arbitrary later system. Once the requests
are in CTS, normal transport routes determine their later path.

For a repeatable pipeline, make the target explicit:

```bash
trm install @acme/tools 2.4.0 --no-prompts --landscape-tr-target QAS
```

Use the same option on `trm update` and `trm clean-install` when applicable.

## What happens on downstream systems

QA and production receive ordinary CTS imports. They do not need `trm-server`, registry access, or
the TRM client just to import the generated requests. Do not run `trm install` again on each system
when those systems belong to the same route: that would create separate installations instead of
promoting the tested transport.

Only the first-system install performs TRM's registry download, dependency and requirement checks,
interactive choices, and post-install activities. A post activity is not automatically replayed
by importing the landscape request. If an activity must run separately in each downstream system
or client, include that step in the deployment procedure or automation for that environment.

Likewise, `trm list` describes packages installed directly through TRM on the connected system; do
not use it as the sole proof that an ordinary downstream CTS import completed. Use STMS import
history and the usual functional checks there.

## When no transport is generated

TRM skips the landscape transport in two cases:

- the connected system has no transport target, so it is treated as the last system;
- every installation package is temporary (its name starts with `$`). Temporary objects are local
  to that system and cannot be released through CTS.

An update of a temporary installation can still perform local cleanup, but its deletions don't
reach other systems. If you intended to promote the package, install it into transportable SAP packages and
make sure the system has the correct TMS route.

## Operational checklist

After `trm install` or `trm update` reports success:

1. Record the landscape transport number from the command output or the target import queue.
2. In STMS, confirm the landscape transport is in the target queue.
3. Do not forward the DEVC, TADIR, LANG, CUST, backup, deletion or staging requests that may be
   visible on the installation system.
4. Import into QA, review the transport return codes and application checks, then promote the same
   request to production.
5. Keep the request in the normal change-management record. The landscape request description
   and embedded manifest identify the TRM package and version.

Releasing the landscape transport is the last step. If only the release fails, the package stays
installed on the installation system and TRM tells you to release the transport manually in `SE09`.
If the install fails while it installs a dependency, TRM also removes that dependency's landscape
transport from the target queue. It can remove it automatically only when it is connected to that
target system; otherwise the error log tells you to remove it manually in STMS. Before retrying,
check the named target queue and remove any request that the failed run explicitly marked for
cleanup. See [If something fails](install.md#if-something-fails) for the wider rollback
behavior.
