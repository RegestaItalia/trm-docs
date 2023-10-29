# Manifest

The manifest is a document that contains information about a package. Its values can be defined during publishing.

Manifest values are used by registries to **index packages**, and its bundled inside the `.trm` artifact with the name `manifest.json`.

A manifest has the following properties:

- `name`

    Full name of the package.

- `version`

    Semver valid version of the package

- `private`

    Indicates package visibility.

    A private package is typically visible to a restricted group of members of a registry.

- `registry`

    Package registry endpoint.

    When blank, TRM defaults to [the public registry](https://trmregistry.com).

- `distFolder`

    Indicates the name of the dist folder in the `.trm` artifact.

- `backwardsCompatible`

    Indicates if the current version of the package is backwards compatible with other package versions.

    More on backwards compatibility [here](#backwards-compatibility)

- `description`

    Short description of the package.

- `git`

    Link to the package git repository, typically containing its source code.

- `website`

    Link to project website.

- `license`

    Package license.

    Allowed values from [OSI Approved Licenses](https://opensource.org/licenses/).

- `authors`

    Package authors.

    Represented as an array of objects with the following properties:
    -  `name`

        Name of the author.

    - `email`

        Contact email of the author.

- `keywords`

    Package keywords.

    Represented as an array of strings.

- `dependencies`

    List of the necessary TRM packages needed in order to avoid dependency errors.

    Represented as an array of objects with the following properties:
    - `name`

        Dependency package full name.
    
    - `version`

        Semver valid version or range of the dependency package.

    - `registry`

        Registry endpoint of the dependency.


- `sapEntries`

    List of required table records needed in order to avoid runtime errors.

    Typically, indicates the TADIR dependencies with standard SAP objects.

    Represented as an objects with properties matching the requires SAP DDIC table names.

    The value of each of these properties is an array containing object, with the field and its value.

    More on SAP Entries [here](#sap-entries)

## Backwards compatibility

Backwards compatibility is a flag inside the `manifest.json` file that indicates if the current release is compatible with its previous releases.

This flag is foundamental for TRM package dependants, take a look at this example:

suppose we have the following situation with

- Package A

    Available releases: 1.0.0, 1.0.1, 1.1.0

    Dependencies: **None**

- Package B

    Available releases: 1.0.0

    Dependencies:

    | Dependency name | Version |
    | --------------- | ------- |
    | Package A       | ^1.0.0  |

- Package C

    Available releases: 1.0.0

    Dependencies:

    | Dependency name | Version |
    | --------------- | ------- |
    | Package A       | ^1.1.0  |

When we attempting to install **Package B** (version 1.0.0) its dependencies are checked and the registry is asked to retrieve a **Package A** version matching the **^1.0.0** range defined in Package B manifest.

The registry will respond with Package A version **1.0.1** as it's **the latest matching version** of range ^1.0.0.

The system now has:

| Package name | Version |
| ------------ | ------- |
| Package B    | 1.0.0   |
| Package A    | 1.0.1   |

Now, attempting to install **Package C** (version 1.0.0) will act the same as before; the registry is asked to retrieve a **Package A** version matching the **^1.1.0** range defined in Package C manifest.

The registry will respond with Package A version **1.1.0**.

Remember, Package A is already installed in the system, with version **1.0.1**.

This means that, if we want to install Package C, **we need to update** to atleast version 1.1.0: in order to guarantee Package B won't have drawbacks from this upgrade, the `backwardsCompatible` flag inside Package A manifest is checked.

Having this flag set to `true` means that between version 1.0.1 and 1.1.0, Package A doesn't have destructive changes.

## SAP Entries

The property `sapEntries` is used to indicate the necessary entries in tables in order to avoid runtime or syntax errors.

Suppose we want to publish a package with a report that calls the standard function module `CONVERSION_EXIT_ALPHA_INPUT`, function group `ALFA`.

To inform users that the package makes use of that function module, we can define `sapEntries`:

```json
    {
        "TADIR": {
            "PGMID": "R3TR",
            "OBJECT": "FUGR",
            "OBJ_NAME": "ALFA"
        }
    }
```

or, if you want to be more specific:

```json
    {
        "TFIDR": {
            "FUNCNAME": "CONVERSION_EXIT_ALPHA_INPUT",
            "PNAME": "SAPLALFA"
        }
    }
```

before install, TRM will check if the system contains this record in its table.

This check can be skipped by the user, but might lead to inconsistencies.

## Manifest and transport request

TRM makes use of transport requests **documentations** to store the package manifest.

You can execute transaction `SE01` and open a TRM transport (generated after install) to see the package manifest.

In transport request documentations, the `manifest.json` file is transformed into XML.