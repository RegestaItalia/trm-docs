# Connect through SAP BTP

TRM normally needs a direct network route to the SAP system, over RFC or HTTP. That route often
doesn't exist outside the company network: a laptop at home, or a cloud CI/CD runner such as the
ones GitHub Actions provides, can't reach an on-premise system.

If your SAP system is already connected to SAP BTP through the **SAP Cloud Connector**, the
[trm-plugin-btp-dest](https://github.com/RegestaItalia/trm-plugin-btp-dest) plugin lets TRM reuse
that secure tunnel. Any machine that can reach SAP BTP over the internet can then reach the SAP
system, without opening firewall ports or setting up a VPN.

## How it works

```
TRM client + plugin  ──▶  SAP BTP, Cloud Foundry  ──▶  Cloud Connector  ──▶  SAP system
 (your PC or runner)      trm-ssh app, Connectivity     (on-premise)         trm-server + trm-rest
                          and Destination services
```

1. The plugin logs in to Cloud Foundry with a BTP user and finds a small helper app, **trm-ssh**,
   that you deploy once in your subaccount.
2. It opens an SSH tunnel to that app, so the client can use the BTP Connectivity service.
3. Each TRM call goes through a **BTP destination** you choose; the Connectivity service and the
   Cloud Connector route it to the SAP system.
4. On the SAP system, [trm-rest](../server/setup.md) answers the calls, as with a direct REST
   connection.

The connection is **REST only**: the SAP system needs both trm-server and trm-rest.

## One-time setup

You need someone with admin rights on the BTP subaccount and on the Cloud Connector.

### 1. Expose the SAP system in the Cloud Connector

In the Cloud Connector connected to your BTP subaccount, add the SAP system as an **HTTP(S)**
backend with a virtual host and port, and allow access to the path `/ztrmserver` (the trm-rest
service) with all its sub-paths.

### 2. Create the destination

In the BTP cockpit, create a destination in the subaccount:

| Field | Value |
| --- | --- |
| Name | Any name, for example `SAP_DEV`. You pass it to TRM. |
| Type | `HTTP` |
| Proxy Type | `OnPremise` |
| URL | The virtual host and port from the Cloud Connector, for example `http://sap-dev:443`, without a path. |
| Authentication | `BasicAuthentication`, with the SAP user TRM works with. |
| Additional property `sap-client` | The SAP client, for example `100`. |

The SAP user in the destination is the one TRM works with on the SAP system, so it must be
authorized in table `/ATRM/USERS` (see [Server setup](../server/setup.md#maintain-authorized-users))
and have the authorizations to create, release and import transports.

### 3. Deploy the trm-ssh app

Download [trm-proxy_0.0.1.mtar](https://github.com/RegestaItalia/trm-plugin-btp-dest/blob/main/trm-ssh/mta_archives/trm-proxy_0.0.1.mtar),
log in to the Cloud Foundry space with the [cf CLI](https://docs.cloudfoundry.org/cf-cli/), and
deploy it:

```bash
cf deploy trm-proxy_0.0.1.mtar
```

The deployment creates the `trm-ssh` app and binds the Destination and Connectivity services to
it. SSH must be enabled for the app (and allowed in the space):

```bash
cf enable-ssh trm-ssh
cf restart trm-ssh
```

The cf CLI is needed only for this step; the TRM client doesn't use it.

### 4. Choose the BTP user

The plugin logs in to BTP and Cloud Foundry with a user that must be a member of the Cloud Foundry
space where `trm-ssh` runs, with the **Space Developer** role (needed to read the app and open the
SSH tunnel). It can log in with:

- **email and password**, for a user without two-factor authentication, or
- an **SAP Passport** (a `.pfx` client certificate issued by SAP), instead of email and password.

For pipelines, use a technical user dedicated to TRM.

## Install the plugin

Install the plugin next to the TRM client:

```bash
npm install -g trm-client trm-plugin-btp-dest
```

**BTP** is now one of the connection types the client offers. The plugin needs trm-client 11.3.0
or later.

## Connect

Interactively, choose **BTP** when TRM asks for the connection: it asks for the BTP login, the
global account and subaccount, the destination and the forward RFC destination. You can save the
connection as a system alias like any other.

Without prompts, for example in a pipeline, set the connection type to `BTP` and pass the
connection arguments as JSON, with the `--connection-type`/`--connection-args` options or the
`TRM_CONNECTION_TYPE`/`TRM_CONNECTION_ARGS` environment variables:

```bash
export TRM_CONNECTION_TYPE=BTP
export TRM_CONNECTION_ARGS='{
  "btpEmail": "trm-ci@example.com",
  "btpPassword": "secret",
  "cfRegion": "eu10",
  "btpDestination": "SAP_DEV",
  "forwardRfcDest": "NONE"
}'
trm info
```

| Argument | Description |
| --- | --- |
| `btpEmail` | BTP user email. |
| `btpPassword` | BTP user password. |
| `btpPassport` | SAP Passport: the `.pfx` file path or its base64 content. Replaces email and password. Also read from the `TRM_SAP_PASSPORT` environment variable. |
| `btpPassportPassphrase` | Passphrase of the SAP Passport. Also read from `TRM_SAP_PASSPORT_PASSPHRASE`. |
| `cfRegion` | Cloud Foundry region of the subaccount, for example `eu10`. When set, global account and subaccount aren't needed. |
| `btpGlobalAccount` | Global account subdomain or display name. Only without `cfRegion`. |
| `btpSubaccount` | Subaccount subdomain, ID, technical name or display name. Only without `cfRegion`. |
| `btpDestination` | Name of the destination (proxy type `OnPremise`). |
| `forwardRfcDest` | RFC destination trm-rest forwards the calls to, like the `-x` option of a REST connection. `NONE` for no forwarding. When missing, it defaults to `NONE` if the connection type is passed (`--connection-type` or `TRM_CONNECTION_TYPE`); otherwise TRM asks for it. |

`cfRegion` is the simplest choice: the region is shown in the subaccount overview of the BTP
cockpit (for example `cf-eu10` means `eu10`).

## See also

- [GitHub Actions](../commons/github_actions.md): run TRM on GitHub-hosted runners with this
  connection.
- [trm-plugin-btp-dest on GitHub](https://github.com/RegestaItalia/trm-plugin-btp-dest).
