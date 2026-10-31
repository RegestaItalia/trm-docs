---
title: TRM Registry OpenAPI reference
description: Portable HTTP API contract for implementing a registry compatible with TRM package publishing, metadata, artifacts, and authentication.
---

# TRM Registry API

The raw OpenAPI schema is available in YAML format [here](https://raw.githubusercontent.com/RegestaItalia/trm-docs/refs/heads/main/docs/registry/openapi.yaml).

It describes the
registry protocol only: endpoint inputs, outputs, and HTTP status codes.

`{package}` is a registry package identifier. Its naming convention is
registry-defined. This is intentionally a protocol-level contract.

Call `GET /` before authenticating. Its `authentication_type` selects
unauthenticated, HTTP Basic, bearer-token, or OAuth2 authentication for
subsequent operations.

## Version: 5.0.0

### Servers

| URL |
| --- |
| https://registry.example.com/ |

### Available authorizations
#### basicAuth (HTTP, basic)
Use when ping reports `BASIC` authentication.  

#### bearerAuth (HTTP, bearer)
Supply a registry-supported credential when ping reports `TOKEN` or `OAUTH2` authentication.  

---

### [GET] /
**Get registry metadata**

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Registry capabilities and messages | **application/json**: [Ping](#ping-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

### [GET] /whoami
**Get the authenticated identity**

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Current identity | **application/json**: [WhoAmI](#whoami-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

### [POST] /auth
**Exchange an OAuth2 authorization code or refresh token**

Implement this operation only when ping reports `OAUTH2` authentication.

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [OAuthTokenRequest](#oauthtokenrequest-schema)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | OAuth2 tokens | **application/json**: [OAuthTokenResponse](#oauthtokenresponse-schema)<br> |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

### [POST] /batchCompare
**Compare requested versions with the latest available version**

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [ [VersionRequest](#versionrequest-schema) ]<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | One comparison result per supplied item | **application/json**: [ [VersionComparison](#versioncomparison-schema) ]<br> |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| None (anonymous) |  |
| basicAuth |  |
| bearerAuth |  |

### [GET] /package/{package}
**Get package metadata and an artifact download link**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |
| version | query | Release version or distribution tag. Defaults to `latest`. | No | string, <br>**Default:** latest |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Selected package release | **application/json**: [Package](#package-schema)<br> |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 404 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| None (anonymous) |  |
| basicAuth |  |
| bearerAuth |  |

### [GET] /transport/{trkorr}
**Package transport download**

Downloads the canonical transports.

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| trkorr | path | Registry transport | Yes | string |
| target | query | Optional destination transport request allocated by the target SAP system. When omitted, the canonical transport is downloaded unchanged. | No | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | The transport is ready to download | **application/json**: [TransportDownload](#transportdownload-schema)<br> |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 403 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 404 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 409 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 422 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 429 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 502 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 503 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 504 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| basicAuth |  |
| bearerAuth |  |

### [GET] /diff/{package}
**Get the differences between two releases of a package**

Optional capability. Comparing releases can take time, so a registry may
compute diffs asynchronously: while the diff is not ready it answers `202`
with a progress object whose `progress_pool_url` the client polls (the same
pattern as publication). When polling reports `current_step == steps`,
`data.diff_url` is the URL to request the diff from; `data.error` reports a
failure. A registry that does not support diffs answers `501`. A registry
may restrict diffs to some accounts: it then answers `401` to anonymous
callers and `402` to accounts whose plan does not include them; the
`progress_pool_url` follows the same rule.

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |
| from | query | Release version to compare from (the older side). | Yes | string |
| to | query | Release version to compare to (the newer side). Must differ from `from`. | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | The diff report | **application/json**: [Diff](#diff-schema)<br> |
| 202 | The diff is being computed; poll `progress_pool_url`<br>**Headers:**<br>**Retry-After**: Suggested polling delay in seconds.<br> | **application/json**: [DiffProgress](#diffprogress-schema)<br> |
| 302 | The diff report is available at the `Location` URL (a `200` response with a `Diff` body)<br> |  |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 402 | The account's plan does not include release diffs (`code` `PRO_PLAN_REQUIRED`) | **application/json**: [Error](#error-schema)<br> |
| 404 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 409 | A release cannot be compared (`code` `diff_unavailable`) | **application/json**: [Error](#error-schema)<br> |
| 422 | The comparison failed (`code` `diff_failed`) or exceeds the registry's size limits (`code` `diff_too_large`) | **application/json**: [Error](#error-schema)<br> |
| 429 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 501 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| None (anonymous) |  |
| basicAuth |  |
| bearerAuth |  |

### [POST] /delete
Endpoint for deletion transport. Its description (E07T) is the source's with the TRM kind set to DELE: `@X1@TRM [(<kind>) ]<package> <version>` becomes `@X1@TRM (DELE) <package> <version>` (60 characters at most); other descriptions are kept. trm-core names the `target` dummy with the same rule.

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **multipart/form-data**: [DeleteTransportRequest](#deletetransportrequest-schema)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | The deletion transport is ready to download, or `empty` is true because nothing remains to delete; then no download is offered. | **application/json**: [DeletionTransportDownload](#deletiontransportdownload-schema)<br> |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 402 | The account's plan does not include transport deletion (`code` `PRO_PLAN_REQUIRED`) | **application/json**: [Error](#error-schema)<br> |
| 403 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 404 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 409 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 413 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 422 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 429 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 502 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 503 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 504 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |
| basicAuth |  |
| bearerAuth |  |

### [PUT] /package/tag/{package}
**Assign a tag to a package version**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [TagAssignment](#tagassignment-schema)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 204 | Tag assigned |  |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 403 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

### [DELETE] /package/tag/{package}
**Remove a package tag**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [Tag](#tag-schema)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 204 | Tag removed |  |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 403 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

### [GET] /publish/check/{package}
**Check whether a package version can be published**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |
| version | query | Release version. | Yes | string |
| private | query | Package visibility indicator. | No | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 204 | Publishing is permitted |  |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 403 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

### [POST] /publish/{package}
**Upload a package artifact**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |
| version | query | Release version. | Yes | string |
| tags | query | Comma-separated tags to apply. Defaults to `latest`. | No | string, <br>**Default:** latest |

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **multipart/form-data**: [PublishRequest](#publishrequest-schema)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 201 | Package published successfully |  |
| 202 | Publication accepted for asynchronous processing | **application/json**: [Publish](#publish-schema)<br> |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 403 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 413 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 422 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

### [POST] /deprecate/{package}
**Mark a package release as deprecated**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |
| version | query | Release version or distribution tag. Defaults to `latest`. | No | string, <br>**Default:** latest |

#### Request Body

| Required | Schema |
| -------- | ------ |
|  Yes | **application/json**: [DeprecationRequest](#deprecationrequest-schema)<br> |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 204 | Release deprecated |  |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 403 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 404 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

### [POST] /unpublish/{package}
**Remove or yank a package release**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |
| version | query | Release version or distribution tag. Defaults to `latest`. | No | string, <br>**Default:** latest |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 204 | Release removed |  |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 401 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 403 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 404 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 409 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

---
### Schemas

#### Error Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| message | string |  | Yes |
| code | string | Optional machine-readable error code. | No |

#### Ping Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| authentication_type | string, <br>**Available values:** "NO_AUTH", "BASIC", "OAUTH2", "TOKEN" |  | Yes |
| authentication_data | [OAuth2Data](#oauth2data-schema) |  | No |
| alert_email | string (email) |  | No |
| messages | [ [Message](#message-schema) ] |  | No |

#### OAuth2Data Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| authorization_url | string (uri) |  | Yes |
| client_id | string |  | Yes |
| response_type | string |  | Yes |
| scope | string |  | No |

#### OAuthTokenRequest Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| grant_type | string, <br>**Available values:** "authorization_code", "refresh_token" |  | Yes |
| code | string |  | No |
| refresh_token | string |  | No |
| redirect_uri | string |  | No |

#### OAuthTokenResponse Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| access_token | string |  | Yes |
| token_type | string |  | Yes |
| expires_in | integer |  | Yes |
| refresh_token | string |  | No |

#### WhoAmI Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| user | string |  | Yes |
| messages | [ [Message](#message-schema) ] |  | No |

#### Message Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| type | string, <br>**Available values:** "INFO", "WARNING", "ERROR" |  | Yes |
| text | string |  | Yes |

#### VersionRequest Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| name | string | Package identifier. | Yes |
| version | string | Version to compare. | Yes |

#### VersionComparison Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| name | string |  | Yes |
| version | string |  | Yes |
| latestVersion | string |  | No |
| comparison | string, <br>**Available values:** "<", "=", ">" |  | No |
| error | string | Present when this item could not be compared. | No |

#### Package Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| name | string |  | Yes |
| dist_tags | object | Distribution tag names mapped to release versions. | Yes |
| versions | [ string ] |  | Yes |
| yanked_versions | [ string ] |  | Yes |
| manifest | { **"name"**: string, **"version"**: string, **"engines"**: object } | Package manifest supplied by the artifact. | Yes |
| deprecated | boolean |  | Yes |
| deprecated_message | string |  | No |
| changelog | string | Optional Markdown changelog supplied at publication time and sanitized by the registry before storage and response. | No |
| download_link | string (uri) | A URL that returns the package `.trm` artifact as `application/octet-stream`. RegistryV2 follows redirects when downloading it. | Yes |
| download_link_expiry | long | Unix epoch milliseconds. An expired download link returns `410 Gone` so the client can request a fresh package view. Unknown links return `404 Not Found`. | No |
| checksum | string | Base64-encoded SHA-512 digest of the exact artifact bytes returned by `download_link`. | Yes |
| transports | [ [Transport](#transport-schema) ] | Transports available in the selected release. | Yes |

#### Transport Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| trkorr | string |  | Yes |
| type | string, <br>**Available values:** "TADIR", "DEVC", "LANG", "CUST" |  | Yes |
| description | string |  | Yes |
| contents | [TransportContents](#transportcontents-schema) |  | Yes |

#### TransportContents Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| download_link | string (uri) | A URL that returns the exact parsed R3trans log JSON for this release transport. | Yes |
| download_link_expiry | long | Unix epoch milliseconds. An expired download link returns `410 Gone` so the client can request a fresh package view. Unknown links return `404 Not Found`. | Yes |
| checksum | string | Base64-encoded SHA-512 digest of the exact JSON bytes returned by `download_link`. | Yes |

#### TransportDownload Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| download_link | string (uri) | A URL that returns a ZIP containing the K and R transport files. | Yes |
| download_link_expiry | long | Unix epoch milliseconds. An expired download link returns `410 Gone` so the client can request a fresh package view. Unknown links return `404 Not Found`. | Yes |
| checksum | string | Base64-encoded SHA-512 digest of the exact ZIP bytes returned by `download_link`. | Yes |

#### DeleteTransportRequest Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| header | binary | The K/header file of the source transport. | Yes |
| data | binary | The R/data file of the source transport. | Yes |
| options | string | Optional JSON text with `DeleteTransportOptions`. Without it the whole source transport is converted into a deletion transport that keeps the source request. | No |

#### DeleteTransportOptions Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| target | string | Request the deletion transport is renamed to. Defaults to the source request. | No |
| subtract | [ string ] | Registry transports readable by the caller whose objects and keys must not be deleted, as `GET /transport/{trkorr}` resolves them. | No |
| exclude | { **"e071"**: [ [DeletedObject](#deletedobject-schema) ], **"e071k"**: [ [DeletedKey](#deletedkey-schema) ] } | Objects and customizing keys never to delete. | No |

#### DeletedObject Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| pgmid | string |  | Yes |
| object | string |  | Yes |
| objName | string |  | Yes |

#### DeletedKey Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| table | string | Table name (E071K OBJNAME). | Yes |
| tabkey | string | Table key (E071K TABKEY); a trailing `*` denotes a generic key. | Yes |

#### DeletedContent Schema

What the deletion transport deletes: object entries (CTS comments, language entries and key-based entries excluded) and the key selectors of key-based entries.

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| e071 | [ [DeletedObject](#deletedobject-schema) ] |  | Yes |
| e071k | [ [DeletedKey](#deletedkey-schema) ] |  | Yes |

#### DeletionTransportDownload Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| DeletionTransportDownload | [TransportDownload](#transportdownload-schema) & { **"deleted"**: [DeletedContent](#deletedcontent-schema) } or { **"empty"**: boolean, <br>**Available values:** true, **"deleted"**: [DeletedContent](#deletedcontent-schema) } |  |  |

#### Tag Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| tag | string |  | Yes |

#### TagAssignment Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| TagAssignment | [Tag](#tag-schema) & { **"version"**: string } |  |  |

#### PublishRequest Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| artifact | binary | Package artifact. | Yes |
| readme | binary | Optional Markdown or plain-text README. | No |
| changelog | binary | Optional Markdown or plain-text changelog for this release. | No |
| retainedCustomizing | string | JSON-encoded array of up to 100 unique CUST TRKORRs from the immediately preceding published release to retain by reference. | No |

#### Publish Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| progress_pool_url | string (uri) | URL to poll for publication progress. | Yes |
| steps | integer | Total number of publication steps. | Yes |
| current_step | integer | Current publication step. | Yes |
| current_step_message | string | Optional description of the current publication step. | No |

#### DiffProgress Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| progress_pool_url | string (uri) | URL to poll for diff progress; it answers with this same object. | Yes |
| steps | integer | Total number of steps. The diff is ready when `current_step` equals `steps`. | Yes |
| current_step | integer |  | Yes |
| current_step_message | string |  | No |
| data | { **"diff_url"**: string (uri), **"error"**: string, **"code"**: string, <br>**Available values:** "diff_failed", "diff_too_large" } |  | No |

#### Diff Schema

A `trm.transport-log-diff` report. Objects of the package are listed with
an `added`, `removed`, `modified`, `unchanged` or `indeterminate` status;
`entries` hold the changed content of each object. Clients must ignore
unknown properties and check `format` and `version`.

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| format | string |  | Yes |
| version | integer |  | Yes |
| comparison | object |  | No |
| before | object |  | No |
| after | object |  | No |
| summary | { **"objects"**: object, **"entries"**: object, **"changedEntries"**: integer } |  | Yes |
| objects | [ { **"id"**: string, **"pgmid"**: string, **"type"**: string, **"name"**: string, **"status"**: string, <br>**Available values:** "added", "removed", "modified", "unchanged", "indeterminate", **"entryIds"**: [ string ], **"fidelity"**: string, <br>**Available values:** "exact", "rendered" } ] |  | Yes |
| entries | [ { **"id"**: string, **"objectId"**: string, **"kind"**: string, **"name"**: string, **"status"**: string, <br>**Available values:** "added", "removed", "modified", "indeterminate" } ] |  | Yes |

#### DeprecationRequest Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| deprecate_note | string | Message explaining why the release is deprecated. | Yes |
