# TRM Registry API
It describes the
registry protocol only: endpoint inputs, outputs, and HTTP status codes.

`{package}` is a registry package identifier. Its naming convention is
registry-defined. This is intentionally a protocol-level contract.

Call `GET /` before authenticating. Its `authentication_type` selects
unauthenticated, HTTP Basic, bearer-token, or OAuth2 authentication for
subsequent operations.

## Version: 4.0.0

### Servers

| URL |
| --- |
| https://registry.example.com/ |

### Available authorizations
#### basicAuth (HTTP, basic)
Use when ping reports `BASIC` authentication.  

#### bearerAuth (HTTP, bearer)
Use when ping reports `TOKEN` or `OAUTH2` authentication.  

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

| basicAuth |  |
| bearerAuth |  |

### [GET] /package/contents/{package}
**Get the extracted contents of a package release**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |
| version | query | Release version or distribution tag. Defaults to `latest`. | No | string, <br>**Default:** latest |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Content entries, grouped by registry-defined type | **application/json**: [PackageContents](#packagecontents-schema)<br> |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 404 | Request failed | **application/json**: [Error](#error-schema)<br> |
| default | Request failed | **application/json**: [Error](#error-schema)<br> |

##### Security

| Security Schema | Scopes |
| --------------- | ------ |

| basicAuth |  |
| bearerAuth |  |

### [GET] /package/deltaCustomizing/{package}
**Get delta-customizing values for a release**

#### Parameters

| Name | Located in | Description | Required | Schema |
| ---- | ---------- | ----------- | -------- | ------ |
| package | path | A package identifier appended exactly as supplied by RegistryV2. It may contain path separators; do not percent-encode `/` within the identifier. | Yes | string |
| version | query | Release version. | Yes | string |

#### Responses

| Code | Description | Schema |
| ---- | ----------- | ------ |
| 200 | Delta-customizing values | **application/json**: [ string ]<br> |
| 400 | Request failed | **application/json**: [Error](#error-schema)<br> |
| 404 | Request failed | **application/json**: [Error](#error-schema)<br> |
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

#### Ping Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| authentication_type | string, <br>**Available values:** "NO_AUTH", "BASIC", "OAUTH2", "TOKEN" | *Enum:* `"NO_AUTH"`, `"BASIC"`, `"OAUTH2"`, `"TOKEN"` | Yes |
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
| grant_type | string, <br>**Available values:** "authorization_code", "refresh_token" | *Enum:* `"authorization_code"`, `"refresh_token"` | Yes |
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
| type | string, <br>**Available values:** "INFO", "WARNING", "ERROR" | *Enum:* `"INFO"`, `"WARNING"`, `"ERROR"` | Yes |
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
| comparison | string, <br>**Available values:** "<", "=", ">" | *Enum:* `"<"`, `"="`, `">"` | No |
| error | string | Present when this item could not be compared. | No |

#### Package Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| name | string |  | Yes |
| dist_tags | object | Distribution tag names mapped to release versions. | Yes |
| versions | [ string ] |  | Yes |
| yanked_versions | [ string ] |  | Yes |
| manifest | { **"name"**: string, **"version"**: string } | Package manifest supplied by the artifact. | Yes |
| deprecated | boolean |  | Yes |
| deprecated_message | string |  | No |
| changelog | string | Optional Markdown changelog supplied at publication time and sanitized by the registry before storage and response. | No |
| download_link | string (uri) | A URL that returns the package `.trm` artifact as `application/octet-stream`. RegistryV2 follows redirects when downloading it. | Yes |
| download_link_expiry | long | Unix epoch milliseconds. | No |
| checksum | string | Base64-encoded SHA-512 digest of the exact artifact bytes returned by `download_link`. | Yes |

#### PackageContents Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| tdevc | [PackageContentsEntries](#packagecontentsentries-schema) |  | Yes |
| tdevct | [PackageContentsEntries](#packagecontentsentries-schema) |  | Yes |
| tadir | [PackageContentsEntries](#packagecontentsentries-schema) |  | Yes |
| e071 | [PackageContentsEntries](#packagecontentsentries-schema) |  | Yes |

#### PackageContentsEntries Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| PackageContentsEntries | [ object ] |  |  |

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

#### Publish Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| progress_pool_url | string (uri) | URL to poll for publication progress. | Yes |
| steps | integer | Total number of publication steps. | Yes |
| current_step | integer | Current publication step. | Yes |
| current_step_message | string | Optional description of the current publication step. | No |

#### DeprecationRequest Schema

| Name | Type | Description | Required |
| ---- | ---- | ----------- | -------- |
| deprecate_note | string | Message explaining why the release is deprecated. | Yes |
