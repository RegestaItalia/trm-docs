---
title: Package SAP customizing safely with TRM
description: Design SAP customizing content for safe, repeatable package installation, updates, client-dependent delivery, and uninstall.
---

# Customizing Guidelines

Besides ABAP objects, a TRM package can ship **customizing**: rows of configuration tables that
the package needs to work, such as default settings, value lists or mappings. This page explains
how TRM handles customizing, and how to design it so that installs, updates and uninstalls stay
predictable.

## How customizing travels in a package

You maintain customizing on your development system as usual, recording it in **customizing
requests**. When you publish, you tell TRM which requests belong to the release:

```bash
trm publish <package name> --cust DEVK900123,DEVK900124
```

or add them when TRM asks, interactively.

For each request, TRM creates a `CUST` transport in the release, a copy of the request listing the
same table entries, and releases it. Some things to know:

- **The content is read when you publish.** TRM exports the rows as they are in the tables at that
  moment, not as they were when the original request was released.
- **Connect to the right client.** Client-dependent tables are read from the client you are logged
  on to. Publish from the client where the customizing is maintained.
- **Only table content is accepted.** A customizing request is fine. A workbench request is accepted
  only if every entry in it is table content; a request containing repository objects (classes,
  tables, ...) is rejected, because those belong to the workbench part of the package.
- **Empty requests are rejected**, and a copy that ends up empty isn't shipped.
- Each `CUST` transport gets a description that installers see: by default the one of the original
  request, at most 60 characters. Make it explain what the customizing is for.

## Where customizing lands

On installation, customizing is imported into the **client the installer is logged on to**:

- **Client-independent** tables are the same for every client, so the rows are visible everywhere.
- **Client-dependent** tables receive the rows only in that client. If the package needs them in
  other clients too, the customer has to copy them (for example with `SCC1`), or you can provide a
  [post activity](post_activities.md) that fills them.

Installers choose which customizing transports to import (see
[What happens during an install](install.md#what-happens-during-an-install)). Only the imported
ones are added to the [landscape transport](install.md#moving-the-package-through-the-landscape),
so they move on to quality and production with the rest of the package.

## Customizing across releases

When you publish a new release to a registry, the customizing transports of the latest release
(the one tagged `latest`) are **carried over** automatically. You don't need to add them again; the
new release ships them alongside any new request you add. `trm pack` doesn't carry anything over.

- A carried-over transport is shipped exactly as it was first published, with its description. It
  isn't read again from the system.
- To ship changed values, add a new customizing request with the changed rows.
- To stop shipping the customizing of an earlier release, remove its transport when TRM lists the
  customizing transports, or pass its number to `--drop-cust` (`--drop-cust all` drops every
  carried-over transport). The number is the one of the `CUST` transport of the release, as
  `trm content <package name>` lists it under `CUST`, not the one of your original request. A number
  that isn't a carried-over `CUST` transport, that is also passed to `--cust`, or `all` combined
  with numbers stops the publish. `--drop-cust` also works with `--no-prompts`.
- Adding the original request again ships a new copy, read from the current table content.
- `--no-cust-tr` publishes a release without any customizing.

Avoid shipping the same row in two transports of a release: don't rely on the import order to
decide which value wins.

## Customizing on update and uninstall

TRM records which customizing transports it imported for each installed package. It uses that
record to clean up:

- **On update**, rows the new release ships again are overwritten **with the values of the new
  release**. Rows it no longer ships are deleted: TRM lists them and asks (default yes; without
  prompts, they are deleted).
- **On uninstall**, all the rows shipped by the package are deleted, after the same confirmation.
- **When the update skips customizing** with `--no-cust-tr`, the customizing of the installed
  release is kept as it is. Declining a single customizing transport at the prompt only keeps the
  installed rows that this transport ships; the other rows follow the update rules above.

Rows are deleted **by key**. When a request uses a **generic key** (for example `ZACME_CONFIG 100*`)
or contains a whole table, the deletion removes every matching row, including rows the customer
added. TRM lists these entries and asks for confirmation, with "no" as the default; without prompts,
they are kept.

Deleted customizing is backed up first, and the deletions travel to the rest of the landscape in the
landscape transport (see [Transports](transports.md)).

> If someone deletes the customizing transport of an installed release from the system, TRM can no
> longer read its keys: it warns, and leaves those rows in place. After an update, those rows are
> no longer tracked.

## Guidelines

**Ship only what the package needs.** Customizing that belongs to the customer's business (company
codes, organizational units, number range intervals of SAP applications, ...) should be maintained
by the customer, not delivered.

**Prefer tables you own.** Rows in your own configuration tables are safe to deliver and to delete.
Rows in SAP standard tables are shared with everything else on the system: an update or an
uninstall deletes them too.

**Use full keys.** Record individual rows, not generic keys or whole tables. A full key deletes exactly
the row you shipped; a generic key can wipe customer data on update or uninstall.

**Ship defaults, not environment-specific values.** RFC destinations, host names, user names and
similar values differ on every system. Leave them to the customer, or set them with a
[post activity](post_activities.md) that reads them from parameters.

**Expect your values to win on update.** Rows you ship are rewritten with the values of each new
release, so changes the customer made to them are overwritten. If customers are expected to adjust a
value, deliver it once and let them own it, or keep their settings in a separate table that you
don't ship.

**Split customizing by purpose.** One request per purpose (for example "Default settings" and "Demo
data") with a clear description makes the content of a release easy to understand.
