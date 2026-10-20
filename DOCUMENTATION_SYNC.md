# Documentation synchronization

Some documentation is shared between `trm-docs` and other TRM repositories. The
repository that owns the content is the source of truth; GitHub Actions copies or
generates the corresponding files in the consuming repository.

## Overview

| Direction | Source of truth | Destination | Content |
| --- | --- | --- | --- |
| Export | `RegestaItalia/trm-docs` | `RegestaItalia/trm-server` and `RegestaItalia/trm-rest` | SAP setup instructions (`SETUP.MD` marked section) |
| Import | `RegestaItalia/trm-plugin-btp-dest` | `RegestaItalia/trm-docs` | BTP destination guide (`BTP.MD` marked section) and local images |
| Import | - | `RegestaItalia/trm-docs` | Registry OpenAPI Markdown and YAML |
| Import |- | `RegestaItalia/trm-docs` | The **Supported object types** section and its coverage chart |

Generated or synchronized content should be edited in its source-of-truth
repository. Direct edits to a destination can be overwritten by the next sync.

## Exported documentation

### trm-server and trm-rest setup

The source of truth is [`docs/server/setup.md`](docs/server/setup.md). The block
between these markers is exported:

```html
<!-- START OF SETUP.MD -->
<!-- END OF SETUP.MD -->
```

It replaces the block with the same markers in:

- `RegestaItalia/trm-server` → `README.md`
- `RegestaItalia/trm-rest` → `README.md`

The exported section describes how to set up `trm-server` and `trm-rest` in an
SAP system. Documentation-relative image paths are converted to raw GitHub URLs
so that the images also work in the destination READMEs.

The export is implemented by
[`scripts/sync_setup_readme.py`](scripts/sync_setup_readme.py) and
[`sync-server-setup.yml`](.github/workflows/sync-server-setup.yml). It runs on
every push to the `main` branch of `trm-docs` and can also be started manually.
If the marked content changed, the workflow commits the updated `README.md`
directly to the `main` branch of each destination repository.

To test the export locally with sibling checkouts:

```sh
python3 scripts/sync_setup_readme.py \
  docs/server/setup.md \
  ../trm-server/README.md \
  ../trm-rest/README.md
```

## Imported documentation

### BTP destination

The source of truth is `README.md` in
[`RegestaItalia/trm-plugin-btp-dest`](https://github.com/RegestaItalia/trm-plugin-btp-dest).
Its complete content is copied into
[`docs/client/btp_destination.md`](docs/client/btp_destination.md), between:

```html
<!-- START OF BTP.MD -->
<!-- END OF BTP.MD -->
```

Repository-local images referenced by the README are copied to
`docs/client/assets/btp_destination/`, and their links are rewritten for the
documentation site.

The import is owned by the `sync-readme-to-docs.yml` workflow and
`.github/scripts/sync_readme_to_docs.py` in `trm-plugin-btp-dest`. It runs when
`README.md` or a supported image file is pushed to that repository's `master`
branch, and it can also be started manually. Changes are committed directly to
the `main` branch of `trm-docs`.

### Registry OpenAPI reference

The source of truth is `openapi.yaml`.
The source repository's `sync-registry-openapi.yml` workflow produces:

- [`docs/registry/openapi.yaml`](docs/registry/openapi.yaml), copied from the source schema;
- [`docs/registry/openapi.md`](docs/registry/openapi.md), generated from the schema with `swagger-markdown`.

The workflow runs whenever `openapi.yaml` changes and can also be
started manually. It commits changes directly to the `main` branch of
`trm-docs`.

### Supported dependency object types

Its workflow updates:

- the **Supported object types** section in
  [`docs/commons/dependencies.md`](docs/commons/dependencies.md);
- `docs/assets/commons/test-coverage-by-object.svg`.

The section is generated from `OBJECT_TYPE_STATUS.md` and
`dependency-docs.json` by `scripts/update_dependencies_doc.py`. The chart is
generated from the dependency test results by `scripts/generate_coverage_chart.py`.

The import runs when its source data, generator scripts, or chart change,
and it can also be started manually. It currently checks out and pushes 
the `dependency-coverage` branch of `trm-docs`, so those changes must be 
merged into `main` through the repository's normal review process.
This is done to prevent publishing into main an upcoming coverage not yet released.

## Maintenance rules

- Keep each synchronized block's start and end markers exactly once in the
  destination document; the sync scripts fail when required markers are
  missing or duplicated.
- Change shared content only in the repository identified as its source of
  truth.
- Update generated OpenAPI Markdown by changing the YAML schema, not by editing
  `docs/registry/openapi.md` directly.
- Review the workflow run and its resulting commit after changing synchronized
  content, especially when a cross-repository credential or branch protection
  rule may prevent the push.
