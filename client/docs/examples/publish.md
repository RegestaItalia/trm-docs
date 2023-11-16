# Publish TRM packages

In this tutorial we're going to see how to publish a package to a registry.

## Prerequisite
- [trm-client](/client/docs/setup.md) installed on your pc
    - Logged into [public registry](https://docs.trmregistry.com/#/registry/public/authentication)/Custom registry implemented
- Development system with
    - [trm-server](/server/docs/setup.md) installed
    - Custom Z package with objects

## Login

> This step may be skipped depending on the registry.

If you haven't done it already, log into the registry.

Open you CLI and run [the command](/client/docs/commands.md#login):

`trm login`

and, if asked, select the desired registry.

To check your login was successfull, run [the command](/client/docs/commands.md#current-logged-in-user):

`trm whoami`

## Publish

Now we're ready to publish our custom developments.

Open you CLI and run [the command](/client/docs/commands.md#publish-package-from-a-system):

`trm publish {{PACKAGE_NAME}}`

where PACKAGE_NAME is the name of the TRM package you want to publish.

In this example, the package name will be `@simonegaffurini/test-publish`.

you'll be prompted with

1. System connection

    Here you should select how to connect to your development system.

    For this demo, select **Manual input**.

    Here, insert the connection values of your development system, as well as the logon data.

2. Package devclass

    This is where the name of your custom package on the SAP system should be typed.

3. Transport request target

    TRM will generate a transport of copies on the development system, so a target should be specified for release.

    If you followed the recommendations, you should [use a virtual system](/client/docs/setup.md#virtual-system-recommended).

4. Dependencies

    Dependencies (with other TRM packages or SAP standard objects) are now automatically checked, but if something is missing they can be manually edited.

5. Package visibility

    The visibility of the package determines who is able to see and install the package you're about to publish.

    > The public registry, in the current alpha stage, doesn't allow private packages, as they require an account paid plan.

6. Manifest

    Since it's the first publish of the package, you'll be prompted with some optional manifest values.

    Manifests are descriptors of the content of a package.

    Some of the possible properties are a short description, authors contacts and license.

The package should now be published.

<p align="center">
  <img src="/_media/sample_publish.png" />
</p>

You'll notice that **version 1.0.0 has been automatically assigned**: this is because we haven't specified a version.

When no version is specified during publish, the default values if **latest** which means:
- When it's the first publish -> version 1.0.0
- When it's already published -> latest release version patch increased

You can open the [public registry website](https://trmregistry.com/) and search for your package there.

<p align="center">
  <img src="/_media/sample_publish_registry.png" />
</p>

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