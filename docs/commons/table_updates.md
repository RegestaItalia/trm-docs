# Tables and package updates

When you update a TRM package to a newer (or older) release, TRM removes what the previous release installed and then installs the new one. This page explains what happens to the **data stored in the package's tables** during an update, and what to keep in mind before updating.

## In short

- Tables that are **still part of the new release keep their data**.
- Tables that the new release **no longer includes are removed, together with their data**.
- If the update fails and TRM rolls it back, the tables return to their previous definition and their data is kept, as long as it still fits the previous definition.

## What happens to your tables

| Situation | Result |
| --- | --- |
| The table is in both the old and the new release, unchanged | Data is kept. |
| The table is in both releases, with small changes (for example, new fields added) | Data is kept. New fields start empty. |
| The table is in both releases, with major changes (see below) | Data may be partially lost, or the update may need manual work in SAP. |
| The table was removed in the new release | The table and its data are deleted. |
| The table was renamed in the new release | It counts as removed and replaced by a new table: the old data is deleted and the new table starts empty. |
| The table is new in the new release | It is created empty. |

## Changes that need extra care

Some changes to a table's structure can't be applied to existing data automatically. If the new release includes any of these, the update can take longer, fail, need an SAP administrator to finish adjusting the table, or lose part of the data:

- Changing which fields identify a record (the table key).
- Making a field shorter, or changing what kind of value it holds.
- Removing fields: the data in those fields is lost.
- Changing the kind of table (for example, from a database table to a structure).

TRM doesn't warn about these changes before the update yet.

> **Tip for package publishers:** add new fields instead of changing or removing existing ones. When a major change can't be avoided, mention it clearly in the release notes so users can back up their data first.

## If the update fails

When an update fails partway, TRM tries to put the system back as it was before the update:

- The previous release's objects are restored.
- Tables that were kept go back to their previous definition and keep their data.
- **Data stored in fields that only the new release added is lost**, because those fields no longer exist in the previous definition.

After a rollback, an extra transport request may remain in the system's transport list. It is safe to ignore.

## Other things to know

- **Only tables keep their data.** Other objects that hold values are still reset on update. For example, number ranges restart from their initial values.
- **Customizing content** is delivered separately through customizing transports and isn't affected by what this page describes.
- **All clients are affected the same way.** Because the table isn't recreated, the data of every client is kept, including test data.
- **Objects that depend on a table**, such as views, maintenance dialogs or extensions from other packages, may need to be checked after a major table change.

## Before updating: checklist

1. Read the release notes of the new version and look for table changes.
2. If tables are removed, renamed, or have major changes, **back up their data** with your usual SAP tools.
3. For large tables with major changes, plan the update for a quiet moment: adjusting the data can take time.
4. After the update, check that the package's tables contain the expected data.
