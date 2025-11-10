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
- **Default**: [public](https://trmregistry.com/registry/) if left blank.

### `distFolder`
- **Description**: Name of the distribution folder in the `.trm` artifact (typically `dist`).

### `backwardsCompatible`
- **Description**: Reserved indicator for future use.

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
  - `registry`: Registry endpoint (optional, [public](https://trmregistry.com/registry/) is blank).

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

## Manifest in Transport Requests

TRM embeds the `manifest.json` content inside transport request documentation (viewable in transaction `SE01`).

For SAP transport documentation, the JSON is transformed into an **XML** format, making it visible directly within the transport logs after package installation.