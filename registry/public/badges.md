# Badges

Badges provide a clean, readable way to display key package information in your project’s documentation, such as version, license, and download count.

TRM Public Registry supports badge generation via [Shields.io](https://shields.io/), a popular service for custom badge endpoints.

> Packages **must be public** to use badges. If the package is private, badge endpoints will return an error.

For more details on badge customization, see the [Shields.io badge documentation](https://shields.io/badges).

Add these badges to your repository README or docs to quickly inform users about your package status.

## Version Badge

Displays the **version** of a release.

### Example Badge

![Latest package version](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/version/trm-server?version=latest)

### Markdown Usage

```markdown
![Latest package version](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/version/trm-server?version=latest)
```

### API Details

- **Endpoint**: `https://trmregistry.com/public/shieldio/version/<package name>`
- **Query Parameters**:
  - `version` (optiona): Specific version or tag (default: 'latest')

---

## License Badge

Displays the **license** of a release.

### Example Badge

![Package license](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/license/trm-server?version=latest)

### Markdown Usage

```markdown
![Package license](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/license/trm-server?version=latest)
```

### API Details

- **Endpoint**: `https://trmregistry.com/public/shieldio/license/<package name>`
- **Query Parameters**:
  - `version` (optiona): Specific version or tag (default: 'latest')

---

## Downloads Badge

Displays the **total number of downloads** for all versions of the package.

### Example Badge

![Package downloads](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/downloads/trm-server?version=latest)

### Markdown Usage

```markdown
![Package downloads](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/downloads/trm-server?version=latest)
```

### API Details

- **Endpoint**: `https://trmregistry.com/public/shieldio/license/<package name>`
- **Query Parameters**:
  - `version` (optiona): Specific version or tag (default: 'latest')
