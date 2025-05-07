# Manifest

The **manifest** is a JSON document that contains metadata about a TRM package. It is created during publishing and is included in the `.trm` artifact under the name `manifest.json`.

Manifest values are used by registries to **index, verify, and resolve** packages.

---

## Manifest Structure

Below are the properties defined in `manifest.json`:

### `name`
- **Description**: Full name (including scope) of the package.

### `version`
- **Description**: [SemVer](https://semver.org/) compliant version string.

### `private`
- **Description**: Boolean flag indicating package visibility.
- **Usage**: Private packages are typically accessible only to specific registry users.

### `registry`
- **Description**: URL of the package registry.
- **Default**: [public](https://trmregistry.com) if left blank.

### `distFolder`
- **Description**: Name of the distribution folder in the `.trm` artifact (typically `dist`).

### `backwardsCompatible`
- **Description**: Indicates whether the current version is backwards compatible with previous versions.
- **Details**: More on [backwards compatibility](#backwards-compatibility).

### `description`
- **Description**: Short description of the package.

### `git`
- **Description**: URL of the package's source repository.

### `website`
- **Description**: Link to the project or documentation website.

### `license`
- **Description**: License identifier (must be [OSI approved](https://opensource.org/licenses/)).

### `authors`
- **Description**: List of authors.
- **Format**: Array of objects with the following fields:
  - `name`: Author's full name.
  - `email`: Contact email.

### `keywords`
- **Description**: Array of keywords to improve searchability.

### `dependencies`
- **Description**: List of required TRM packages.
- **Format**: Array of objects with the following fields:
  - `name`: Name of the dependency package.
  - `version`: Valid SemVer version or range.
  - `integrity`: SHA512 checksum of the package. [Details](#dependency-integrity-check).
  - `registry`: Registry endpoint (optional, [public](https://trmregistry.com) is blank).

### `postActivities`
- **Description**: List of activities to run automatically after installation.
- **More info**: See [post activities section](post_activities.md)

### `namespace`
- **Description**: SAP namespace in use by the TRM package.
- **Structure**:
  - `ns`: Namespace.
  - `replicense`: Namespace repair key.
  - `texts`: Array of objects with the following fields:
    - `description`: Namespace description.
    - `owner`: Namespace owner.
    - `language`: Texts language.

---

## Backwards Compatibility

The `backwardsCompatible` flag determines whether a version upgrade is safe for packages that depend on this package.

### Example

Suppose we have the following packages:

- **Package A**
  - Versions: `1.0.0`, `1.0.1`, `1.1.0`
  - No dependencies

- **Package B**
  - Version: `1.0.0`
  - Depends on: `Package A@^1.0.0`

- **Package C**
  - Version: `1.0.0`
  - Depends on: `Package A@^1.1.0`

### Installation Scenario

1. Install **Package B**:
   - Resolves `Package A` version `1.0.1` (latest in `^1.0.0` range)
2. Install **Package C**:
   - Requires at least `Package A` version `1.1.0`

Since `Package A` is already installed at `1.0.1`, upgrading to `1.1.0` is required.  
TRM checks the `backwardsCompatible` flag in version `1.1.0` to confirm the upgrade won't break existing dependencies (like Package B).

---

## Dependency Integrity Check

To ensure a dependency is:

- The same version expected by the publisher
- Uncompromised or unaltered

TRM compares the SHA512 checksum (`integrity`) of the downloaded package before installing it.

If the checksum doesn't match, the installation is **aborted** to protect against corrupted or tampered content.

---

## Manifest in Transport Requests

TRM embeds the `manifest.json` content inside transport request documentation (viewable in transaction `SE01`).

For SAP transport documentation, the JSON is transformed into an **XML** format, making it visible directly within the transport logs after package installation.