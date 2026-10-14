# Authentication

Anyone can browse the [public registry](https://trmregistry.com) and download public packages
without an account. To publish, manage your packages, or download private ones, TRM has to prove
who you are. There are two ways to do it:

| Method | Use it for | Secret to store |
| --- | --- | --- |
| [Personal access token](#personal-access-tokens) | Your computer, and any CI/CD tool | A long-lived token (`trm_...`) |
| [GitHub Actions trusted publishing](#github-actions-trusted-publishing) | Workflows running in GitHub Actions | None |

## Personal access tokens

A personal access token (PAT) is a key that acts as you. Each token has an expiration date and a
set of **scopes**, the actions it allows:

| Scope | Allows |
| --- | --- |
| `package:read` | Download and view packages. |
| `package:publish` | Publish packages and manage their tags. |
| `package:unpublish` | Unpublish packages. |
| `package:deprecate` | Deprecate packages. |
| `package:all` | All of the above. |

A token can never do more than your account can: publishing a package of an organization still
requires your account to be allowed to publish it.

### Generate a token

1. Log in to the [public registry](https://trmregistry.com).
2. Go to the [personal access tokens page](https://trmregistry.com/pat).
3. Press **Generate new token**.
4. Select an expiration date (or no expiration) and the scopes you need.
5. Press **Generate token**.

!!! warning
    This is your **only chance** to copy the token. Store it somewhere safe, for example in a
    password manager or as a CI/CD secret. If you lose it, revoke it and generate a new one.

### Use the token

On your computer, log in once; TRM asks for the token and remembers it:

```bash
trm login
```

In a script or pipeline, pass the token on each command instead:

```bash
trm publish ... -E public -A '{"token":"trm_..."}'
```

`-A` also accepts the path of a JSON file with the same content.

## GitHub Actions trusted publishing

With trusted publishing, a [GitHub Actions](../../commons/github_actions.md) workflow logs in to
the registry **as the GitHub user who started it**, without any token saved in the repository. It
is the recommended way to publish from GitHub Actions.

### How it works

1. You link your GitHub account to your registry account, once.
2. When a workflow runs, GitHub gives the job a short-lived, signed identity token
   ([OpenID Connect](https://docs.github.com/actions/security-for-github-actions/security-hardening-your-deployments/about-security-hardening-with-openid-connect)).
   The token says, among other things, which GitHub user triggered the run, and is issued for the
   registry only (its audience is `https://trmregistry.com`).
3. The TRM client sends that token to the registry instead of a personal access token.
4. The registry checks the token's signature with GitHub, finds the TRM account linked to that
   GitHub user, and handles the request as that account.

The token expires after a few minutes and is accepted only by the registry, so there is nothing
long-lived that can leak. When a job runs longer, the TRM client asks GitHub for a fresh token.

### Link your GitHub account

1. Log in to the [public registry](https://trmregistry.com) and open
   [**Settings**](https://trmregistry.com/settings).
2. In the **GitHub account** card, press **Link GitHub**.
3. GitHub asks you to authorize the **TRM Registry** app. The app only learns who you are on
   GitHub: it gets no access to your repositories, and the registry doesn't keep any GitHub token.
4. You are sent back to Settings, where the card shows your `@username`.

A GitHub account can be linked to only one TRM account. To stop workflows from acting as you,
press **Unlink** in the same card; you can link again at any time.

### What a workflow can do as you

There is no per-repository or per-workflow configuration: the link itself is the trust.

- **Who:** the run acts as the GitHub user who triggered it (the run's *actor*). For a workflow
  that starts when a release is published, that is the person who published the release.
- **Where:** any workflow run you trigger, in any repository, can act as you, as long as the
  workflow is allowed to request the identity token (`permissions: id-token: write`).
- **What:** the same as a personal access token with `package:all` (read, publish, unpublish,
  deprecate), limited, as always, by what your account may do on each package.

!!! warning
    Link your GitHub account only if you are comfortable with the workflows you trigger acting as
    you on the registry. If a teammate starts the workflow, the run acts as **their** TRM account:
    they need their own linked account and the permission to publish the package.

### Use it in a workflow

The job needs permission to request the identity token. When no registry authentication is passed,
the TRM client (13.3.0 or later) detects GitHub Actions and uses it automatically:

```yaml
permissions:
  contents: read
  id-token: write

steps:
  - run: trm publish ... -E public
```

To ask for it explicitly, for example with an older client, pass `-A '{"oidc":"github"}'`.

See [GitHub Actions](../../commons/github_actions.md) for complete workflows.

!!! note
    The identity token lives only a few minutes, so `trm login` can't save it, and `trm login` and
    `trm logout` never use it automatically.

### Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `GitHub Actions OIDC token is not available` | `-A '{"oidc":"github"}'` was passed but the job can't request the identity token. | Add `permissions: id-token: write` to the workflow or job. |
| `Unauthorized` | No authentication was passed and the job can't request the identity token, so the command ran as anonymous. | Add `permissions: id-token: write` to the workflow or job. |
| `GitHub account not linked to a TRM profile` | The user who triggered the run hasn't linked a GitHub account. | [Link the GitHub account](#link-your-github-account), or have a linked user start the run. |
| `Insufficient permissions` | The linked account can't do this on this package (for example, it isn't allowed to publish in the organization that owns it). | Give the account the needed rights on the package or organization. |
