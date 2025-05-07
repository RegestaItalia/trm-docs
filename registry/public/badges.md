# Badges

Badges provide a clean, readable way to display key package information in your project’s documentation — such as version, license, and download count.

TRM Public Registry supports badge generation via [Shields.io](https://shields.io/), a popular service for custom badge endpoints.

> ⚠️ Packages **must be public** to use badges. If the package is private, badge endpoints will return an error.

For more details on badge customization, see the [Shields.io badge documentation](https://shields.io/badges).

Add these badges to your repository README or docs to quickly inform users about your package status.

---

## Latest Version Badge

Displays the **latest published version** of a package from the TRM Public Registry.

### Example Badge

![Latest package version](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/version?package=trm-server)

### Markdown Usage

```markdown
![Latest package version](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/version?package=trm-server)
```

### API Details

- **Endpoint**: `https://trmregistry.com/public/shieldio/version`
- **Query Parameters**:
  - `package` (required): Name of the package (e.g., `trm-server`)

---

## License Badge

Displays the **license** declared by the package.

### Example Badge

![Package license](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/license?package=trm-server)

### Markdown Usage

```markdown
![Package license](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/license?package=trm-server)
```

### API Details

- **Endpoint**: `https://trmregistry.com/public/shieldio/license`
- **Query Parameters**:
  - `package` (required): Name of the package

---

## Downloads Badge

Displays the **total number of downloads** for all versions of the package.

### Example Badge

![Package downloads](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/downloads?package=trm-server)

### Markdown Usage

```markdown
![Package downloads](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/downloads?package=trm-server)
```

### API Details

- **Endpoint**: `https://trmregistry.com/public/shieldio/downloads`
- **Query Parameters**:
  - `package` (required): Name of the package
