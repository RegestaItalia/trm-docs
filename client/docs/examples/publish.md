# Publish TRM packages

In this tutorial we're going to see how to publish a package to a registry.

**Prerequisite**
- Logged into [public registry](https://docs.trmregistry.com/#/registry/public/authentication)/Custom registry implemented
- Development system with
    - trm-server installed
    - Custom package with objects created



# Packages with dependencies

When publishing packages (unless specified) TRM will check all the dependency objects.

If one or more TRM packages are found, they are automatically added to the dependency list.

This means that, next time someone tries to install the package, they will install all the required dependencies too.

> Automatic dependency recognition is subject to the dependency object type. To check if an object dependency is recognized automatically, [check this table](https://docs.trmregistry.com/#/commons/dependencies?id=dependency-recognition).

## Publish with dependencies example

In this example, we're publishing package A that uses a class from package B, and package B **is not** a TRM package (not yet published).

This means package A is the **dependant** and package B is the **dependency**.

If we run the publish command on package A, it will result in an error:

<p align="center">
  <img src="/_media/sample_dependency_error.png" />
</p>

The error is telling us that in order to publish package A **we first must publish package B**.

After doing so, publishing package A will tell us that the dependency with package B has been found:

<p align="center">
  <img src="/_media/sample_dependency_success.png" />
</p>

Its [manifest](https://docs.trmregistry.com/#/commons/manifest) will have a dedicated section that looks like this:

```json
"dependencies": [
    {
      "name": "trm-dependency",
      "version": "^1.0.0",
      "integrity": "..."
    }
]
```

- `name` - **required** - `string`

    Dependency package full name.

- `version` - **required** - `string`
    
    Semver valid version or range of the dependency package.

- `integrity` - **required** - `string`

    SHA512 of the dependency package.

- `registry` - `string`
    
    Registry endpoint of the dependency.