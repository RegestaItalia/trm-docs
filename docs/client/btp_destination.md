---
title: Connect TRM through an SAP BTP destination
description: Configure the TRM client to reach an SAP ABAP system securely through an SAP BTP destination and Cloud Connector.
---

<!-- START OF BTP.MD -->
# trm-plugin-btp-dest

Connect TRM to a BTP destination.

## Why use this connector

TRM normally needs a direct network route to the target SAP system (RFC or HTTP). That is often not available:

- **CI/CD pipelines** (GitHub Actions, Azure DevOps, GitLab runners, ...) run on cloud-hosted agents that cannot reach systems inside the corporate network
- Opening firewall ports or setting up a VPN just for TRM to connect is not always an option

If your on-premise SAP system is already connected to SAP BTP through the **SAP Cloud Connector**, this plugin lets TRM reuse that secure tunnel: any machine that can reach SAP BTP over the internet can reach the SAP system, without exposing it or changing network configuration.

## How it works

```
 ┌─────────────────────────┐
 │ TRM Client              │  local machine / CI runner
 │ + trm-plugin-btp-dest   │
 └───────────┬─────────────┘
             │ 1. Cloud Foundry login (API)
             │ 2. SSH tunnel (cf ssh endpoint)
             ▼
 ┌──────────────────────────────── SAP BTP (Cloud Foundry) ────┐
 │  ┌─────────────┐  3. REST calls    ┌──────────────────────┐ │
 │  │ trm-ssh app │ ────────────────▶ │ Connectivity service │ │
 │  └─────────────┘  via destination  └──────────┬───────────┘ │
 └───────────────────────────────────────────────┼─────────────┘
                                                 │ secure tunnel
                                                 ▼
 ┌──────────────────────────────── On-premise ─────────────────┐
 │  ┌──────────────────────┐  HTTP   ┌──────────────────────┐  │
 │  │ SAP Cloud Connector  │ ──────▶ │ SAP system           │  │
 │  └──────────────────────┘         │ trm-rest (REST API)  │  │
 │                                   │     │                │  │
 │                                   │     ▼                │  │
 │                                   │ trm-server           │  │
 │                                   └──────────────────────┘  │
 └─────────────────────────────────────────────────────────────┘
```

1. The plugin logs into Cloud Foundry and looks for the **trm-ssh** app
2. It opens an SSH tunnel to the app and forwards the Connectivity service proxy ports to the local machine
3. TRM calls the SAP system through the chosen BTP destination (proxy type `OnPremise`); the Connectivity service and the Cloud Connector route each call to the on-premise system
4. On the SAP system, **trm-rest** receives the HTTP calls

The connection is currently **REST only** (HTTP through the destination, no RFC).

## One-time setup

You need administrator access to the BTP subaccount and SAP Cloud Connector. The target SAP
system must have trm-server and trm-rest installed.

### 1. Expose the SAP system in Cloud Connector

In the Cloud Connector connected to your BTP subaccount, add the SAP system as an **HTTP(S)**
backend with a virtual host and port. Allow access to `/ztrmserver` (the trm-rest service),
including all of its subpaths.

### 2. Create the BTP destination

Create a destination in the BTP subaccount with these settings:

| Field | Value |
| --- | --- |
| Name | Any name, for example `SAP_DEV`; this is the value passed to TRM |
| Type | `HTTP` |
| Proxy Type | `OnPremise` |
| URL | The Cloud Connector virtual host and port, for example `http://sap-dev:443`, without a path |
| Authentication | `BasicAuthentication`, using the SAP user that TRM should run as |
| Additional property `sap-client` | The SAP client, for example `100` |

The destination's SAP user needs authorization object `ZTRM_AUTH` with `ACTVT = 16` (Execute),
as well as the authorizations required to create, release, and import transports.

### 3. Deploy the SSH enabler app

This repository contains a build of **trm-ssh**, a simplified version of the app in
[jowavp/sap-cf-proxy](https://github.com/jowavp/sap-cf-proxy).

Download [trm-proxy_0.0.1.mtar](https://github.com/RegestaItalia/trm-plugin-btp-dest/blob/main/trm-ssh/mta_archives/trm-proxy_0.0.1.mtar),
log in to the target Cloud Foundry space with the [cf CLI](https://docs.cloudfoundry.org/cf-cli/),
and deploy it:

```sh
cf deploy trm-proxy_0.0.1.mtar
```

The deployment creates the `trm-ssh` app and binds the Destination and Connectivity services to
it. Make sure SSH is allowed in the space, then enable it for the app and restart the app:

```sh
cf enable-ssh trm-ssh
cf restart trm-ssh
```

The cf CLI is needed only for deployment; the TRM client does not use it.

### 4. Configure the BTP user

The plugin logs in to BTP and Cloud Foundry as a user who must be a member of the Cloud Foundry
space where `trm-ssh` runs. Assign the user the **Space Developer** role so the plugin can inspect
the app and open the SSH tunnel.

The user can authenticate with either:

- Email and password, if two-factor authentication is not enabled
- An SAP Passport (`.pfx` client certificate) instead of email and password

Use a dedicated technical user for pipelines.

## Install plugin

Install the plugin next to trm-client:

```sh
npm install -g trm-client trm-plugin-btp-dest
```

You should now see **BTP** as a connection type in the TRM client.

## Interactive usage

Choose **BTP** when TRM asks for the connection type. It prompts for the BTP login, global account
and subaccount (unless a Cloud Foundry region is supplied), BTP destination, and forward RFC
destination. You can save the connection as a system alias like any other TRM connection.

## Non-interactive usage (CI/CD)

Every prompt can be skipped by passing connection arguments from the TRM client:

- `--connection-type BTP` (or env `TRM_CONNECTION_TYPE`) selects this connection
- `--connection-args <JSON or path to JSON file>` (or env `TRM_CONNECTION_ARGS`) passes the arguments below

| Argument           | Description                                                                          |
| ------------------ | ------------------------------------------------------------------------------------ |
| `btpEmail`         | BTP user email                                                                       |
| `btpPassword`      | BTP user password                                                                    |
| `btpPassport`      | SAP Passport (`.pfx`) file path or base64 content, replaces `btpEmail` and `btpPassword` (env `TRM_SAP_PASSPORT`) |
| `btpPassportPassphrase` | SAP Passport passphrase (env `TRM_SAP_PASSPORT_PASSPHRASE`); prompted when missing, none with `--no-prompts` |
| `cfRegion`         | Cloud Foundry region (e.g. `eu10`); when set, global account and subaccount are skipped |
| `btpGlobalAccount` | Global account subdomain or display name (only without `cfRegion`)                   |
| `btpSubaccount`    | Subaccount subdomain, id, technical name or display name (only without `cfRegion`)   |
| `btpDestination`   | Name of the destination (proxy type `OnPremise`)                                     |
| `forwardRfcDest`   | RFC destination trm-rest forwards calls to, same as client option `-x <destination>`; `NONE` (default) for no forward. Prompted when missing, `NONE` when `--connection-type` or `--no-prompts` is used |

Arguments not provided are prompted as usual. With `--no-prompts` nothing is prompted: a missing required argument stops the command with an error naming it. Required are:

- the BTP login: `btpEmail` and `btpPassword`, or `btpPassport`
- `cfRegion`, or `btpGlobalAccount` and `btpSubaccount`
- `btpDestination`

In CI the user must be able to log in with email and password (no two-factor authentication), or with a SAP Passport. Use `cfRegion` when possible: it's shown in the subaccount overview of the BTP cockpit (`cf-eu10` means `eu10`), and it skips the BTP login used only to read global accounts and subaccounts.

Example:

```sh
export TRM_CONNECTION_TYPE=BTP
export TRM_CONNECTION_ARGS='{"btpEmail":"trm-ci@example.com","btpPassword":"secret","cfRegion":"eu10","btpDestination":"SAP_DEV","forwardRfcDest":"NONE"}'
trm install <package> --no-prompts
```

For GitHub Actions and other pipelines see [GitHub Actions](https://docs.trmregistry.com/commons/github_actions/) in the TRM documentation.

### SAP Passport

A SAP Passport (client certificate issued by SAP, `.pfx`) can be used instead of email and password: when `btpPassport` is set, email and password are not asked and the login to BTP and Cloud Foundry is done with the certificate at the SAP ID service (same as `btp login --sso` and `cf login --sso` in a browser with the passport installed).

You can create your own [SAP Passport here](https://support.sap.com/en/my-support/single-sign-on-passports.html).

```sh
export TRM_SAP_PASSPORT=/path/to/passport.pfx   # or its base64 content, e.g. from a CI secret
export TRM_SAP_PASSPORT_PASSPHRASE=...
trm <command> --connection-type BTP --connection-args '{"cfRegion":"eu10","btpDestination":"MY_DEST"}'
```

The passport is never saved with the connection data: when the saved Cloud Foundry session expires, it is read again from the arguments/environment (or email and password are prompted).
<!-- END OF BTP.MD -->