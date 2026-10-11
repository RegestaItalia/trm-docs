# GitHub Actions

TRM runs from the command line, so it fits in any CI/CD tool. This page shows how to run it in
[GitHub Actions](https://docs.github.com/actions) to publish a release or install one, without
anyone typing answers at a prompt. The same approach works in GitLab CI, Azure Pipelines, Jenkins
and similar tools.

## What the pipeline needs

| Need | How |
| --- | --- |
| A runner | A GitHub-hosted runner such as `ubuntu-latest`, when you [connect through SAP BTP](#reaching-the-sap-system). Otherwise a [self-hosted runner](https://docs.github.com/actions/hosting-your-own-runners) inside your network. |
| The TRM client | `npm install -g trm-client` on a runner with Node.js. |
| A connection to SAP | Recommended: the **BTP** connection of [trm-plugin-btp-dest](../client/btp_destination.md), through an SAP BTP destination and the Cloud Connector. On a self-hosted runner, the **REST** connection is the simplest: it only needs [trm-rest](../server/setup.md) on the SAP system. RFC also works, but the runner then needs the SAP NW RFC SDK and `node-rfc`, see [Client setup](../client/setup.md). |
| An SAP user | A technical user authorized in table `/ATRM/USERS` (see [Server setup](../server/setup.md#maintain-authorized-users)), with the authorizations to create, release and import transports. With the BTP connection, it's the user set in the destination. |
| Registry access | Recommended: [GitHub Actions trusted publishing](../registry/public/authentication.md#github-actions-trusted-publishing), with no token to store. Alternatively, a [personal access token](../registry/public/authentication.md#personal-access-tokens) with the scopes the job needs. Installing public packages needs no authentication. |

Store passwords, certificates and tokens as
[GitHub secrets](https://docs.github.com/actions/security-for-github-actions/security-guides/using-secrets-in-github-actions),
never in the workflow file.

## Reaching the SAP system

GitHub-hosted runners run in the cloud, outside your company network, so they can't reach an
on-premise SAP system directly. There are two ways around this.

**Through SAP BTP (recommended).** If the SAP system is connected to SAP BTP with the SAP Cloud
Connector, install the [trm-plugin-btp-dest](../client/btp_destination.md) plugin in the job and
connect with the `BTP` connection type. TRM reaches the system through a BTP destination, so you
can use GitHub-hosted runners and keep the SAP system closed to the internet. The BTP side needs a
[one-time setup](../client/btp_destination.md#one-time-setup): a destination, the small `trm-ssh`
app and a BTP user for the pipeline.

**With a self-hosted runner.** Install a
[self-hosted runner](https://docs.github.com/actions/hosting-your-own-runners) on a machine inside
your network that can reach the SAP system, and connect with REST (or RFC) as from any other
computer. You then maintain the runner machine yourself.

## Connecting without prompts

Three pieces of configuration replace the interactive questions.

### The SAP connection

Set the connection type and its data as environment variables:

- `TRM_CONNECTION_TYPE`: `BTP`, `REST` or `RFC`.
- `TRM_CONNECTION_ARGS`: a JSON object with the connection data.

For the **BTP** connection (plugin installed with `npm install -g trm-plugin-btp-dest`):

```json
{
  "btpEmail": "trm-ci@example.com",
  "btpPassword": "secret",
  "cfRegion": "eu10",
  "btpDestination": "SAP_DEV",
  "forwardRfcDest": "NONE"
}
```

The BTP user can also log in with an SAP Passport instead of email and password: put the `.pfx`
file, base64 encoded, in the `TRM_SAP_PASSPORT` environment variable and its passphrase in
`TRM_SAP_PASSPORT_PASSPHRASE`. All arguments are described in
[Connect through SAP BTP](../client/btp_destination.md#connect).

For a **REST** connection (self-hosted runner):

```json
{
  "endpoint": "https://sap-dev.example.com",
  "client": "100",
  "user": "TRM_CI",
  "passwd": "secret",
  "lang": "EN"
}
```

The same values can be passed as command options (`--connection-type` and `--connection-args`,
which also accepts the path of a JSON file).

### The registry

Pass the registry and how to authenticate on each command:

```bash
-E public -A '{"oidc":"github"}'
```

`{"oidc":"github"}` uses [GitHub Actions trusted publishing](#authenticating-to-the-registry):
the job needs `permissions: id-token: write`, and no secret. To use a personal access token
instead, pass `-A '{"token":"<your token>"}'`.

`public` stands for the public registry. For a private registry, use its endpoint URL instead.

### The prompts

Add `--no-prompts` to every command. TRM then never waits for an answer: it uses the options you
passed, applies safe defaults, and stops with an error when a decision is missing. The decisions
TRM can't take on its own are listed in
[Publishing without prompts](publish.md#publishing-without-prompts),
[Installing without prompts](install.md#installing-without-prompts) and
[Uninstalling without prompts](uninstall.md#uninstalling-without-prompts).

## Authenticating to the registry

The recommended way to authenticate from GitHub Actions is
[trusted publishing](../registry/public/authentication.md#github-actions-trusted-publishing) with
OpenID Connect (OIDC): instead of a long-lived token saved as a secret, each run gets a
short-lived identity token from GitHub, and the registry accepts it as the GitHub user who
triggered the run.

1. **Link your GitHub account** once: on the registry, open
   [Settings](https://trmregistry.com/settings) and press **Link GitHub** in the **GitHub account**
   card. Everyone who starts the workflow needs a linked account with the permission to publish
   the package.
2. **Allow the workflow to request the token**, in the workflow or in the job:

    ```yaml
    permissions:
      contents: read
      id-token: write
    ```

3. **Tell TRM to use it**, with `-A '{"oidc":"github"}'` on each command.

The TRM client then asks GitHub for a token issued for the registry (audience
`https://trmregistry.com`), sends it to the registry, and asks for a fresh one when a long run
needs it. The token works for everything a personal access token with `package:all` allows:
publish, install (including private packages), unpublish, deprecate and tags.

Use a [personal access token](../registry/public/authentication.md#personal-access-tokens) instead
when the workflow must act as a fixed account whoever starts it, for example for scheduled runs, or
when the people starting it don't have a linked GitHub account.

## Example: publish when a GitHub release is created

This workflow publishes a new version of the package every time a release is published in the
repository, on a GitHub-hosted runner. The tag of the GitHub release (for example `v1.4.0`)
becomes the TRM version, and the repository's `README.md` and `CHANGELOG.md` are attached to the
release. It connects to SAP through a BTP destination and authenticates to the registry as the
person who published the GitHub release.

Repository secrets used: `BTP_EMAIL` and `BTP_PASSWORD`, the BTP user of the pipeline.

```yaml
name: Publish TRM package

on:
  release:
    types: [published]

permissions:
  contents: read
  id-token: write # lets TRM authenticate to the registry with GitHub OIDC

jobs:
  publish:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install TRM client and BTP plugin
        run: npm install -g trm-client trm-plugin-btp-dest

      - name: Publish
        env:
          TRM_CONNECTION_TYPE: BTP
          TRM_CONNECTION_ARGS: >-
            {"cfRegion": "eu10", "btpDestination": "SAP_DEV", "forwardRfcDest": "NONE",
            "btpEmail": ${{ toJSON(secrets.BTP_EMAIL) }},
            "btpPassword": ${{ toJSON(secrets.BTP_PASSWORD) }}}
        run: |
          VERSION="${GITHUB_REF_NAME#v}"
          trm publish @acme/sales-tools "$VERSION" \
            --no-prompts \
            -E public -A '{"oidc":"github"}' \
            --sap-package ZACME_SALES \
            --public \
            -T QAS \
            --readme README.md \
            --changelog CHANGELOG.md
```

- `toJSON(...)` puts each secret in the JSON as a correctly quoted string, even if it contains
  quotes or backslashes.
- `--sap-package` and `--public` (or `--private`) are needed only for the first publish. Later
  releases reuse them.
- `-T` is the transport target of the publish transports; it can be left out when the system has
  only one.
- Everything else (description, license, dependencies, customizing...) is taken from the previous
  release, see [What TRM reuses from the previous release](publish.md#what-trm-reuses-from-the-previous-release).
  To stop carrying over customizing transports of the previous release, pass
  `--drop-cust <transports>` (comma separated) or `--drop-cust all`.

**With a self-hosted runner and REST**, change `runs-on: ubuntu-latest` to `runs-on: self-hosted`,
install only `trm-client`, and set the connection as in [The SAP connection](#the-sap-connection):

```yaml
        env:
          TRM_CONNECTION_TYPE: REST
          TRM_CONNECTION_ARGS: ${{ secrets.SAP_DEV_CONNECTION }} # the REST JSON shown above
```

**With a personal access token**, drop `id-token: write`, store the token as the `TRM_TOKEN`
secret, add `TRM_TOKEN: ${{ secrets.TRM_TOKEN }}` to `env`, and replace the registry options with
`-E public -A "{\"token\":\"$TRM_TOKEN\"}"`.

## Example: install the locked release on a test system

This workflow installs the package on a test system, on demand. It uses a [lockfile](lockfile.md)
committed in the repository, so the test system gets exactly the release and the dependency
versions recorded in it, every time.

```yaml
name: Install on test system

on:
  workflow_dispatch:

permissions:
  contents: read
  id-token: write # only needed for private packages

jobs:
  install:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-node@v4
        with:
          node-version: 22

      - name: Install TRM client and BTP plugin
        run: npm install -g trm-client trm-plugin-btp-dest

      - name: Install package
        env:
          TRM_CONNECTION_TYPE: BTP
          TRM_CONNECTION_ARGS: >-
            {"cfRegion": "eu10", "btpDestination": "SAP_TEST", "forwardRfcDest": "NONE",
            "btpEmail": ${{ toJSON(secrets.BTP_EMAIL) }},
            "btpPassword": ${{ toJSON(secrets.BTP_PASSWORD) }}}
        run: |
          trm clean-install @acme/sales-tools \
            --no-prompts \
            -E public -A '{"oidc":"github"}' \
            --lock-file trm-lock.json \
            --package-replacements '[{"originalDevclass":"ZACME_SALES","installDevclass":"ZTEST_SALES"}]'
```

- Without a version, `trm clean-install` installs the release recorded in the lockfile. If you
  pass a version, it must match the lockfile, or the command stops.
- To move the test system to a new release, regenerate the lockfile with `trm lock` on a system
  where that release is installed, and commit it.
- For a public package, the registry options can be just `-E public` and the `id-token`
  permission can go: anyone can download it.
- Use `trm install` without a lockfile instead to get the newest compatible versions.

## Keep approvals where they belong

A pipeline should automate the repeatable mechanics, not the decision to go live:

1. Publish a versioned release.
2. Install it on a non-production system, and run your tests.
3. Approve it with your organization's usual process.
4. Move the [landscape transport](install.md#moving-the-package-through-the-landscape) through
   quality and production along the normal transport route.

Give the pipeline's SAP user, BTP user and registry credentials only the permissions their job
needs, and use separate credentials for publishing and installing. GitHub
[environments](https://docs.github.com/actions/deployment/targeting-different-environments/using-environments-for-deployment)
can require a manual approval before a job that touches a sensitive system.

## Troubleshooting

- **The job hangs:** a value is missing and TRM is waiting for an answer. Check that `--no-prompts`
  is on every command, and that the connection arguments are complete (for BTP, include
  `forwardRfcDest`).
- **"... is required ... when interactive prompts are disabled":** pass the option named in the
  error. The first publish of a package needs `--sap-package` and `--public`/`--private`.
- **"Transport target was not declared":** the system has more than one transport target; pass
  `-T` (publish) or `--landscape-tr-target` (install, uninstall).
- **"GitHub Actions OIDC token is not available":** add `permissions: id-token: write` to the
  workflow or job.
- **"GitHub account not linked to a TRM profile":** the user who started the run hasn't
  [linked a GitHub account](../registry/public/authentication.md#link-your-github-account).
- **"Invalid connection type "BTP"":** install `trm-plugin-btp-dest` in the same
  `npm install -g` step as `trm-client`.
- **BTP login or tunnel errors:** see the [one-time setup](../client/btp_destination.md#one-time-setup)
  (Space Developer role, SSH enabled for `trm-ssh`, user without two-factor authentication).
- **Detailed logs:** add `--debug`, or use `--logger CLI_LOG --logger-out-dir <folder>` to also
  write the log to a file you can upload as a [workflow artifact](https://docs.github.com/actions/using-workflows/storing-workflow-data-as-artifacts).
