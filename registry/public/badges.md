# Badges

Badges can be used in your project documentation for concise and easy to read information about a release.

The public registry badges can be used in conjunction with [Shields.io](https://shields.io/).

For more details about Shields.io, read its documentation [here](https://shields.io/badges).

Packages visibility **must** be public, otherwise the endpoints will just respond with an error.

## Version

This badge can be used to display the latest published version of a package on the registry.

Usage:

```markdown
![Latest package version](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/version?package=trm-server)
```

- Endpoint: `https://trmregistry.com/public/shieldio/version`
- Example badge: ![Example](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/version?package=trm-server)
- Query parameters
    - package - **required** `string`

        Name of the package.

## License

This badge can be used to display the license of a package on the registry.

Usage:

```markdown
![Package license](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/license?package=trm-server)
```

- Endpoint: `https://trmregistry.com/public/shieldio/license`
- Example badge: ![Example](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/license?package=trm-server)
- Query parameters
    - package - **required** `string`

        Name of the package.

## Downloads counter

This badge can be used to display the amount of downloads of a package on the registry.

This value indicates the downloads of all the releases.

Usage:

```markdown
![Package downloads](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/downloads?package=trm-server)
```

- Endpoint: `https://trmregistry.com/public/shieldio/downloads`
- Example badge: ![Example](https://img.shields.io/endpoint?url=https://trmregistry.com/public/shieldio/downloads?package=trm-server)
- Query parameters
    - package - **required** `string`

        Name of the package.