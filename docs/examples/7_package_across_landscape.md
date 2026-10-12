# Move an installed package through the landscape

Run `trm install` or `trm update` on the first system of a transport route. TRM imports the
release there, then creates one ordinary CTS transport for the systems that follow it. Move that
transport through QA and production with the same STMS process you use for other changes.

This page explains which requests an installation creates, which ones belong in the import queue,
and what remains on the system when the command finishes.

## The transports have different jobs

A published release can contain several source transports. TRM prepares and imports them on the
system where the command runs, but they are not the delivery unit for the rest of that system's
landscape.

| Transport | Purpose | Move it manually? |
| --- | --- | --- |
| **DEVC** | Creates the publisher's SAP package hierarchy when the original package names are kept. It is not imported when TRM creates mapped target packages instead. | No. It is an installation input. |
| **TADIR** | Contains the repository/workbench objects of the published release. | No. It is an installation input. |
| **LANG** | Contains translations, when the release has them and their import was not skipped. | No. Its imported entries are copied into the landscape transport. |
| **CUST** | Contains customizing. A release can contain more than one, and each can be accepted or skipped during an interactive install. | No. Entries from the imported transports, including their table keys, are copied into the landscape transport. |
| **Deletion transport** | On an update, removes objects and package definitions that belonged to the installed version but not to the new version. It can also remove old customizing before replacement customizing is imported. | Yes, but TRM normally puts it in the selected target's import queue for you. |
| **Landscape transport** | The consolidated transport created from what TRM actually installed: SAP packages, workbench objects, an imported namespace when available, translations, and customizing. | Yes. This is the normal delivery unit for downstream systems. |

The transport numbers used to prepare DEVC, TADIR, LANG, and CUST content can therefore remain
visible in the installation system. Depending on whether the release came from a registry or a
local `.trm` file, TRM may reuse an uploaded request number or create a local transport of copies
as a staging request. Do not add these requests to the route as well: doing so duplicates the
delivery and can lose the selection and ordering that TRM assembled in the landscape transport.

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

An update first cleans the installed version on the system where the command runs and then imports
the new release. Objects that exist in both versions are updated; tables that exist in both are
retained so their data is not dropped. Objects and now-empty SAP packages that disappeared from
the release are removed.

For a transportable installation, a successful update normally leaves two requests to move:

1. the **deletion transport**, already forwarded to the selected target's import queue;
2. the new, released **landscape transport**.

Import them in exactly that order on every system:

```text
DEV: trm update
          |
          +-- 1. deletion transport --------+
          +-- 2. landscape transport -------+--> QAS --> PRD
```

The landscape transport contains an `upgrade=<deletion transport>` marker, but TRM deliberately
does not create a CTS project dependency between the requests. The import queue order is therefore
operationally significant: deleting after importing the new version could remove an object that
the new release still expects or leave the system at the wrong package level.

Use an import-all workflow only when it preserves this order. If requests are selected manually,
select and import the deletion request first, wait for it to finish, and then import the landscape
request. Apply the same sequence at every hop; do not move only the landscape request because the
development system already looks correct.

## Choosing the target route

TRM reads the transport targets available from the connected SAP system.

- With one target, that route can be used for the generated requests.
- With several targets, choose the intended one interactively or pass
  `--landscape-tr-target <SID>`. In non-interactive runs, the option is required when the choice is
  ambiguous.
- With no target, TRM treats the connected system as the final system and creates no landscape
  transport.

The target belongs to the generated landscape request and receives the update deletion request.
Choose the immediate next system in the route, not an arbitrary later system. Once the requests
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

An update of a temporary installation can still perform local cleanup, but its deletion is not
forwarded. If you intended to promote the package, install it into transportable SAP packages and
make sure the system has the correct TMS route.

## Operational checklist

After `trm install` or `trm update` reports success:

1. Record the landscape transport number and, for an update, the deletion transport number from
   the command output or the target import queue.
2. In STMS, confirm both update requests are in the same target queue and that deletion precedes
   landscape content.
3. Do not forward the DEVC, TADIR, LANG, CUST, backup, or staging requests that may be visible on
   the installation system.
4. Import into QA, review the transport return codes and application checks, then promote the same
   request or ordered pair to production.
5. Keep the requests in the normal change-management record. The landscape request description
   and embedded manifest identify the TRM package and version.

If the command fails after a request has been released, TRM attempts to remove the landscape and
deletion requests from the target queue. It can remove them automatically only when it is connected
to that target system; otherwise the error log tells you to remove them manually in STMS. Before
retrying, check the named target queue and remove any request that the failed run explicitly marked
for cleanup. See [If something fails](../commons/install.md#if-something-fails) for the wider
rollback behavior.
