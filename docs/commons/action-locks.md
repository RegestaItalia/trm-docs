# SAP action locks and manual cleanup

TRM uses persistent SAP action locks to prevent two or more processes from changing the same resource at the same time. They have no automatic expiry. A normally completed action releases its locks, including after its rollback. An abruptly terminated process or failed cleanup can leave rows behind.

## What is locked

Each lock identifies a resource type and name. TRM derives a stable hash from those values, so separate processes and the connectors contend for the same row. A row also records the action, SAP user, creation timestamp, and an internal owner token. Only that owner can perform the normal release.

| Action | Resources reserved |
| --- | --- |
| Install or update | Package identity (package name plus registry endpoint), target and previously installed SAP packages (`DEVCLASS`), transport requests (`TRANSPORT`), and imported repository objects (`OBJECT`). The payload's objects and packages are reserved **before dependency installation**. Each dependency install also acquires its own locks; parent-held locks remain until the dependency chain has finished or rolled back. |
| Publish | Package identity, source SAP package, and included workbench objects. |
| CG3Z transport upload | Transport request number (`TRKORR`). |

An install that collides with a held package, SAP package, object, or transport lock fails instead of overlapping the other operation. A lock is a concurrency guard, not evidence that the underlying SAP change succeeded or was rolled back.

## Inspect locks in SAP GUI

1. Open transaction `/ATRM/LOCK`.
2. Optionally filter by resource type, resource name, resource hash, action, SAP owner, or creation timestamp. Use the resource name and action from the failed TRM operation to narrow the list.
3. Inspect the columns **Type**, **Resource**, **Action**, **Owner**, **Created at**, and **Hash**. The hash is the internal exact-key identifier, not a separate resource.

Viewing requires authorization object `ZTRM_AUTH` with activity `16`.

## Manually remove an orphaned lock

Do this only after confirming that **no TRM process, job, or dependent install still owns the resource**. Age alone does not prove a lock is stale: a long-running install can legitimately hold it. Check the initiating process and its logs, and inspect any partially changed SAP state. Deleting a lock does **not** complete an import, undo changes, or run rollback.

1. Refresh the list and identify the exact row by its type, resource, action, owner, and creation time. If the process is still running, leave the lock in place.
2. Select the **Delete** icon on that row.
3. The report refreshes after deletion. If normal cleanup removed the row in the meantime, it reports **Lock already released; list refreshed** and continues normally. If ownership changed, it reports **Lock changed ownership; list refreshed** and does not delete the new owner's lock. Recheck the new row before taking any further action.
4. Reconcile any partial SAP changes and retry the TRM action only when the target state is safe. If the lock reappears, investigate the active owner rather than repeatedly deleting it.

Deletion additionally requires `S_TABU_NAM` activity `02` for table `/ATRM/ACT_LOCK` (as well as `ZTRM_AUTH` activity `16`). The report deletes only the selected resource type/hash **and its original owner token**, preventing a stale ALV row from deleting a newly acquired lock. Do not edit `/ATRM/ACT_LOCK` directly or use SM12 for these locks.
