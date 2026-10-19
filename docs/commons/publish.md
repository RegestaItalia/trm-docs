# Publishing a package

Publishing turns an ABAP package on your development system into a versioned TRM release.
TRM reads the package, builds the transports for it, and uploads the result to a registry, or
writes it to a local `.trm` file.

```bash
trm publish <package name> [version]
```

To write a local file instead of uploading to a registry:

```bash
trm pack <package name> <version> [file name]
```

## Before you start

- **trm-server** must be installed on the system you publish from. See [Server setup](../server/setup.md).
- The system must have **at least one transport target** configured in TMS. TRM creates real
  transport requests and releases them, so it needs somewhere to send them.
- All objects of the ABAP package must be **released**: an object still locked in an open
  transport request stops the publish.
- To publish to a registry that requires an account, log in first with `trm login`.

## What TRM asks you

When you run `trm publish` interactively, TRM guides you through the release:

| Question | What it means |
| --- | --- |
| ABAP package | The SAP package (and its subpackages) that make up the release. TRM remembers it: the next release of the same package starts from the same ABAP package. |
| Version | Leave it empty to let TRM calculate it. The first release is `1.0.0`; later releases increase the latest version by the chosen increment (`patch` by default, see `--increment`). |
| Visibility | Public or private. Asked only on the first publish; it can't be changed afterwards. |
| Dependencies | Other TRM packages your objects use. TRM finds most of them automatically, see [Dependencies](dependencies.md). |
| Customizing transports | Customizing requests to ship with the release. See [Customizing guidelines](customizing_guidelines.md). |
| Manifest values | Description, authors, license, website, Git repository, [engines](engines.md), [post activities](post_activities.md), and more. See [Manifest](manifest.md). |
| Readme and changelog | Markdown text shown on the registry page of the release. |
| Transport target | The TMS target assigned to the transports TRM creates. If the system has only one, it is picked automatically. |

## What TRM reuses from the previous release

From the second release onwards, TRM starts from the manifest of the latest release, so you
don't have to type the same values again:

- Description, authors, license, website, keywords and the other manifest values are copied.
  Values you pass explicitly replace them. Use `--no-keep-manifest` to start from scratch.
- Post activities are copied too. If you pass post activities, they replace the whole list of the
  latest release: pass every post activity the new release needs. The same class can appear more
  than once, with different parameters. Post activities whose class doesn't exist on the system are dropped.
- **Customizing transports are carried over.** The customizing of the latest release stays in the
  new release unless you remove it, either when TRM lists the customizing transports or with
  `--drop-cust`. See [Customizing guidelines](customizing_guidelines.md#customizing-across-releases).

## What happens during a publish

1. **Checks.** TRM verifies your authorization, that the version isn't already published, and that
   the ABAP package isn't part of another TRM package. A package and its subpackages can use at
   most one reserved namespace (for example `/ACME/`).
2. **Dependency detection.** TRM scans the objects and lists the TRM packages and SAP objects they
   need. TRM dependencies go into the manifest. SAP objects go into the [SAP entries](sap_entries.md).
3. **Locks.** TRM [locks](action_locks.md) the package name, the ABAP package and its objects, so
   another publish or install can't change them at the same time.
4. **Transports.** TRM creates and releases one transport per content type: the package definitions
   (`DEVC`), the workbench objects (`TADIR`), translations (`LANG`, optional), and one transport per
   customizing request (`CUST`, optional). See [Artifact](artifact.md).
5. **Upload.** The transports, the manifest, and the abapGit-serialized source code (when abapGit is
   installed) are bundled into the artifact and uploaded.
6. **Record.** TRM records the published package on the system, so `trm list` shows it and the next
   publish can reuse its data.

> ⚠️ Don't interrupt a publish once the transports are being generated. If a step fails before the
> upload, TRM deletes the transports it created. Once released, a transport can't be deleted, so
> it may remain in your transport list.

## Release candidates and tags

- `--pre-release` publishes a prerelease such as `1.1.0-rc.0`. Use `--pre-release-identifier` to
  choose the label (`alpha`, `beta`, `rc`, ...). Version ranges in dependencies don't match
  prereleases unless the range itself names one, so consumers don't receive them by accident.
- `--tag` assigns distribution tags (for example `beta`). Install a tagged release with
  `trm install <package> <tag>`.

## Publishing without prompts

Pass `--no-prompts` to publish from a script or a pipeline (in GitHub Actions, see
[GitHub Actions](github_actions.md) and [trusted publishing](../registry/public/authentication.md#github-actions-trusted-publishing),
which publishes without storing a registry token). Any value TRM would otherwise ask for
must then be supplied, or the publish stops with an error:

| Value | Option |
| --- | --- |
| ABAP package (first publish only) | `-P, --sap-package` |
| Visibility (first publish only) | `--public` or `--private` |
| Transport target (when the system has more than one) | `-T, --target` |

Everything else is optional:

| To | Option |
| --- | --- |
| Add customizing requests | `--cust <requests>` |
| Stop carrying over customizing transports of the latest release | `--drop-cust <requests>`, or `--drop-cust all` |
| Publish without any customizing | `--no-cust-tr` |
| Set manifest values | `--description`, `--license`, `--dependencies`, `--engines`, `--post-activities`, ... |

Options that take JSON or Markdown also accept a file path.

`--drop-cust` takes the transport numbers of the customizing transports of the latest release, as
`trm content <package name>` lists them under `CUST`, separated by commas. A number that isn't a
customizing transport of the latest release, or that is also passed to `--cust`, stops the publish
with an error. In an interactive publish, the dropped transports aren't listed with the customizing
transports, and you can still edit the rest.

See [GitHub Actions](github_actions.md) for a complete pipeline example.
