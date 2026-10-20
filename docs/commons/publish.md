---
title: Publish a versioned ABAP package
description: Publish an SAP ABAP development as a versioned TRM artifact with a manifest, transports, dependencies, prerequisites, and registry metadata.
---

# Publishing a package

Publishing turns an ABAP package on your development system into a versioned TRM release.
TRM reads the package, builds the transports for it, and uploads the result to a registry, or
writes it to a local `.trm` file.

```bash
trm publish <package name> [version]
```

To write a local file instead of uploading to a registry:

```bash
trm pack <package name> [version] [file name]
```

`trm pack` (alias `trm export`) writes `<package name>.trm` in the current folder unless you give a
file name. A packed release is always private, and `pack` doesn't ask for a readme or changelog,
doesn't reuse a previous release, and doesn't accept the options that only make sense on a registry
(`--increment`, `--pre-release`, `--tag`, `--public`/`--private`, `--readme`, `--no-keep-manifest`,
`--drop-cust`).

## Before you start

- **trm-server** must be installed on the system you publish from. See [Server setup](../server/setup.md).
- The system must have **at least one transport target** configured in TMS. TRM creates real
  transport requests and releases them, so it needs somewhere to send them.
- All objects of the ABAP package must be **released**: an object still locked in an open
  transport request stops the publish. Objects excluded by the abapGit `ignore` aren't checked.
- To publish to the public registry, log in first with `trm login`.

## What TRM asks you

When you run `trm publish` interactively, TRM guides you through the release:

| Question | What it means |
| --- | --- |
| ABAP package | The SAP package (and its subpackages) that make up the release. TRM remembers it on the system: the next release of the same package starts from the same ABAP package. |
| Version | When you don't pass one, TRM calculates it and asks you to confirm or type another one. The first release is `1.0.0`; later releases increase the latest version by the chosen increment (`-i, --increment`, `patch` by default). |
| Visibility | Public or private. Asked only on the first publish; the public registry doesn't allow changing it afterwards. |
| Transport target | The TMS target assigned to the transports TRM creates. If the system has only one, it is picked automatically. |
| Dependencies | Other TRM packages your objects use. TRM finds most of them automatically, see [Dependencies](dependencies.md). |
| Customizing transports | Customizing requests to ship with the release. See [Customizing guidelines](customizing_guidelines.md). |
| Manifest values | Description, authors, license, website, Git repository, [engines](engines.md), [post activities](post_activities.md), and more. See [Manifest](manifest.md). |
| Readme and changelog | Markdown text shown on the registry page of the release. |

## What TRM reuses from the previous release

From the second release onwards, TRM starts from the manifest of the latest release, so you
don't have to type the same values again (`--no-keep-manifest` starts from scratch):

- Description, license, website, Git repository and engines are copied; values you pass replace
  them. Authors and keywords you pass are added to the copied ones.
- Post activities are copied too. If you pass post activities, they replace the whole list of the
  latest release: pass every post activity the new release needs. The same class can appear more
  than once, with different parameters. Post activities whose class doesn't exist on the system are dropped.
- Customizing transports are carried over, see
  [Customizing across releases](customizing_guidelines.md#customizing-across-releases).

Dependencies and SAP entries aren't copied: they are detected again on every publish. The readme
and the changelog are written anew.

## What happens during a publish

1. **Checks.** TRM verifies your authorization, that the version isn't already published (or
   yanked), and that the ABAP package isn't empty, isn't part of another TRM package and doesn't
   contain one. A package and its subpackages can use at most one reserved namespace (for example
   `/ACME/`), which must be readable on the system.
2. **Dependency detection.** TRM scans the objects and lists the TRM packages and SAP objects they
   need. TRM dependencies go into the manifest, with the range `^<installed version>`. SAP objects
   go into the [SAP entries](sap_entries.md). The publish stops if the objects use customer ABAP
   packages that aren't part of a TRM package, or TRM packages installed from a `.trm` file.
3. **Locks.** TRM [locks](action_locks.md) the package name, the ABAP package and its objects, so
   another publish or install can't change them at the same time.
4. **Transports.** TRM creates and releases the [publish transports](transports.md#when-you-publish).
5. **Upload.** The transports, the manifest, and the abapGit-serialized source code (when abapGit is
   installed) are bundled into the [artifact](artifact.md) and uploaded.
6. **Record.** TRM records the published package on the system, so `trm list` shows it and the next
   publish can reuse its data. If only this step fails, the release is published anyway: TRM tells
   you to install that version to bring the system back in sync.

> ⚠️ Don't interrupt a publish once the transports are being generated. If a step fails, TRM
> deletes the transports it created. Once released, a transport can't be deleted, so it may remain
> in your transport list.

`--simulate` runs every check and question, then shows what the publish would do without creating
transports or publishing.

## Release candidates and tags

- `--pre-release` publishes a prerelease of the version you pass, or of the calculated one. With
  `--pre-release-identifier rc`, `trm publish <package> 1.1.0 --pre-release` publishes `1.1.0-rc.0`,
  then `1.1.0-rc.1` the next time. Without an identifier, it publishes `1.1.0-0`.
- When TRM picks a release to install, version ranges don't match prereleases unless the range
  itself names a prerelease of the same version, so consumers don't receive them by accident.
- `--tag` assigns distribution tags, separated by commas (for example `beta`). Install a tagged
  release with `trm install <package> <tag>`.

## Publishing without prompts

Pass `--no-prompts` to publish from a script or a pipeline (in GitHub Actions, see
[GitHub Actions](github_actions.md) and [trusted publishing](../registry/public/authentication.md#github-actions-trusted-publishing),
which publishes without storing a registry token). The calculated version is used without
confirmation. Any other value TRM would otherwise ask for must then be supplied, or the publish
stops with an error:

| Value | Option |
| --- | --- |
| ABAP package (when the system has no record of the package, for example on the first publish) | `-P, --sap-package` |
| Visibility (first publish only) | `--public` or `--private` |
| Transport target (when the system has more than one) | `-T, --target` |

Everything else is optional:

| To | Option |
| --- | --- |
| Add customizing requests | `--cust <requests>` |
| Stop carrying over customizing transports of the latest release | `--drop-cust <transports>`, or `--drop-cust all` |
| Publish without translations or customizing | `--no-lang-tr`, `--no-cust-tr` |
| Skip automatic dependency detection | `--no-auto-deps` |
| Set manifest values | `--description`, `--authors`, `--keywords`, `--license`, `--website`, `--git`, `--backwards-compatible`, `--dependencies`, `--sap-entries`, `--engines`, `--post-activities` |
| Set the readme and changelog | `--readme`, `--changelog` |

Options that take JSON or Markdown also accept a file path. Invalid JSON stops the command with an
error.

See [GitHub Actions](github_actions.md) for a complete pipeline example.
