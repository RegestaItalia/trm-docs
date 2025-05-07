# 📘 TRM Public Registry API Documentation

The **TRM Public Registry** exposes a set of RESTful APIs that allow developers to perform actions programmatically, such as managing users, packages, and tokens.

- 🔐 All endpoints **require authentication**. See the [authentication guide](registry/public/authentication.md).
- 🧾 The API base URL is:

```
https://www.trmregistry.com/api
```

> ⚠️ Some error codes may not be explicitly documented and should be handled as generic errors by default.

---

## `/updateUser`

Allows the currently authenticated user to update one or more of their profile properties.

> ⚠️ If a property is left empty or has an invalid value, it will not be updated.

- **Method**: `POST`  
- **Content-Type**: `multipart/form-data`

### Request Body Parameters

| Field         | Type     | Description                                               |
|---------------|----------|-----------------------------------------------------------|
| `contactEmail`| `string` | Public contact email                                      |
| `website`     | `string` | Personal or professional website URL                      |
| `github`      | `string` | GitHub profile URL                                        |
| `linkedin`    | `string` | LinkedIn profile URL                                      |
| `sapblog`     | `string` | SAP Blog profile URL                                      |
| `removeAvatar`| `boolean`| If `true`, removes the user's avatar                      |
| `avatar`      | `file`   | Uploads a new avatar (ignored if `removeAvatar` is true)  |

### Response

- `200 OK`: User data updated
- `304 Not Modified`: No changes applied

---

## `/updatePackage`

Allows maintainers with appropriate permissions to update package metadata.

- **Method**: `POST`  
- **Content-Type**: `application/json`

### Request Body

```json
{
  "readme": "string", // Valid Markdown content
  "packageMaintainers": [
    {
      "username": "string",
      "remove": "boolean",
      "canEditReleases": "boolean",
      "canEditPackage": "boolean",
      "canEditUsers": "boolean"
    }
  ]
}
```

- `readme`: New package README (Markdown format)
- `packageMaintainers`: List of users with optional permission flags

### Response

- `200 OK`: Package updated

---

## `/revokeToken`

Revokes a TRM token owned by the authenticated user.

- **Method**: `POST`  
- **Content-Type**: `application/json`

### Request Body

```json
{
  "tokenId": "string" // Required: ID of the token to revoke
}
```

### Response

- `200 OK`: Token revoked successfully

---

## `/deleteUser`

Permanently deletes the currently authenticated user.

> ⚠️ **This action is irreversible. Use with extreme caution.**

- **Method**: `POST`  
- **Response Type**: `application/json`

### Response

- `200 OK`: User deleted permanently

---

## `/deletePackage`

Deletes a specific package **version** from the registry.

> ⚠️ **This action is permanent and cannot be undone. Only individual versions can be removed.**

- **Method**: `POST`  
- **Content-Type**: `application/json`

### Request Body

```json
{
  "package": "string",  // Required: Full package name (e.g., "@scope/package-name")
  "version": "string"   // Required: Specific version to delete (e.g., "1.2.3")
}
```

### Response

- `200 OK`: Release deleted