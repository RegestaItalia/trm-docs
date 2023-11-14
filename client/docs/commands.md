# Full list of commands

A full list of commands that can be used by trm-client can be found by simply typing

`trm`

in your CLI.

# System alias

Because a connection to an SAP ECC/S4 system has a quite a few parameters, connecting to a system by typing all of them via CLI can be challenging.

To solve this problem, you can create a system alias.

A system alias is an easy way to store all of the connection attributes, including login data, of an SAP ECC/S4 system.

System aliases are saved in **plain text** in the AppData `systems.ini` file.

## Manage alias

All-in-one command that lets you view, edit or check connection of an alias.

- Command `trm createAlias <<ALIAS_NAME>>`
- Options
    - `-a, --systemAlias <<systemAlias>>` - `string`

        Alias name to manage. If not provided, a list with all of you aliases will be prompted.

## Create alias

Create a new system alias.

- Command `trm createAlias <<ALIAS_NAME>>`

## Delete alias

Delete a system alias.

- Command `trm deleteAlias <<ALIAS_NAME>>`

# Info

Shows informations about the client and the client TRM dependencies on a system.

- Command `trm info`
- Options
    - `-a, --systemAlias <<SYSTEM_ALIAS>>` - `string`

        Alias of the system to connect.
    
    - `-d, --dest <<SYSTEM_ID>>` - `string`

        System ID of the system to connect.

        Ignored in conjunction with alias option.

    - `-h, --ashost <<APPLICATION_SERVER_ADDRESS>>` - `string`

        Application server address of the system to connect.

        Ignored in conjunction with alias option.

    - `-n, --sysnr <<INSTANCE_NUMBER>>` - `string`

        Instance number of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router string of the system to connect.

        Ignored in conjunction with alias option.

    - `-c, --client <<CLIENT>>` - `string`

        System logon client.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-p, --passwd <<PASSWORD>>` - `string`

        System logon user password.

        Ignored in conjunction with alias option.

> If the direct connection options are incomplete you'll be prompted to fill in the required values.

# Ping

This command lets you test a connection to a development system with trm-server installed.

If trm-server is installed, and the user is allowed, it should respond without any errors.

Use this command anytime you want to check a user can access trm-server RFC Function modules.

- Command `trm ping`
- Options
    - `-a, --systemAlias <<SYSTEM_ALIAS>>` - `string`

        Alias of the system to connect.
    
    - `-d, --dest <<SYSTEM_ID>>` - `string`

        System ID of the system to connect.

        Ignored in conjunction with alias option.

    - `-h, --ashost <<APPLICATION_SERVER_ADDRESS>>` - `string`

        Application server address of the system to connect.

        Ignored in conjunction with alias option.

    - `-n, --sysnr <<INSTANCE_NUMBER>>` - `string`

        Instance number of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router string of the system to connect.

        Ignored in conjunction with alias option.

    - `-c, --client <<CLIENT>>` - `string`

        System logon client.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-p, --passwd <<PASSWORD>>` - `string`

        System logon user password.

        Ignored in conjunction with alias option.

> If the direct connection options are incomplete you'll be prompted to fill in the required values.

# Registry

Out of the box, trm-client is configured to work with the [public registry](https://trmregistry.com).

It is, however, possible to add as many private registries as you want.

To learn more about private registries, [visit the documentation](https://docs.trmregistry.com).

Registry data is saved in **plain text** in the AppData `registry.ini` file.

## Login

This command lets you log in into the registry.

> This command will show an error message when executed on a registry that requires no authentication.

- Command `trm login`
- Options
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

    - `-f, --force` - `boolean`

        If this command is executed when you're already logged in it will prompt for confirmation before overwriting the already existing auth data.

        This flag will force the login authentication process.

    - `-a, --authentication <<AUTH_DATA>>` - `JSON`

        If the authentication process is confirmed and this option is not provided, you'll be prompted for the necessary login steps, otherwise this data will be used to automatically login.

## Current logged in user

Show the currently logged in user data in a registry.

> This command will show an error message when executed on a registry that requires no authentication.

- Command `trm whoami`
- Options
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

## Logout

Log out of the registry.

> This command will show an error message when executed on a registry that requires no authentication.

- Command `trm logout`
- Options
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

## Add private registry

- Command `trm addRegistry <<REGISTRY_NAME>>`
- Options
    - `-e, --endpoint <<ENDPOINT_URL>>` - `string`

        Base url of the registry.

    - `-a, --authentication <<JSON>>` - `string`

        Authentication object.

## Remove private registry

- Command `trm removeRegistry <<REGISTRY_NAME>>`
- Options
    - `-f, --force` - `boolean`

        Skip confirm prompt.

# Packages

TRM identifies a package as the composition of its TRM transports and the manifest.

> To avoid confusion, whenever TRM refeers to SAP packages, they are called Devclasses

## Publish package from a system

- Command `trm publish <<PACKAGE_NAME>>`
- Options
    - `-d, --devclass <<DEVCLASS>>` - `string`

        Name of the devclass on source system.
    
    - `-v, --version <<VERSION>>` - `string`

        Version to publish.

        Allowed values are either `latest` or a semver valid version.

        Default: `latest` - If the package is published for the first time, the version is set to `1.0.0` by default; if the package already exists in the registry, the latest version is fetched and the patch version is increased
    
    - `-t, --target <<TARGET>>` - `string`

        System target for transport request release.

    - `-m, --manifest <<JSON>>` - `string`

        Path to JSON file or JSON object containing manifest values.

        See [Publish package manifest](#publish-package-manifest) for the detailed explaination.

    - `-rm, --readme <<MARKDOWN>>` - `string`

        Path to MD file or markdown string containing the readme.

    - `-ci, --ci` - `boolean`

        Avoids non-blocking prompts.

        Its intended use is in pipeline contexts, where the prompts should not appear.

        Default: `false`.

    - `-fm, --forceManifest` - `boolean`

        Flag for forcing the manifest values prompt even when the values are already provided.
        
        Has no meaning if running with flag `-ci, --ci`.

        Default: `false`.

    - `-om, --overwriteManifest` - `boolean`

        Overwrite manifest values. By default, it falls back to the previously published manifest.

        Default: `false`.

    - `-sd, --skipDependencies` - `boolean`

        Skip dependencies search.
        
        Default: `false`.

    - `-ses, --skipEditSapEntries` - `boolean`

        Skip edit SAP entries prompt.

        Default: `false`.

    - `-sed, --skipEditDependencies` - `boolean`

        Skip edit dependencies prompt.
        
        Default: `false`.

    - `-srm, --skipReadme` - `boolean`

        Skip edit readme prompt.
        
        Default: `false`.

    - `-to, --releaseTimeout <timeout>` - `number`

        Timeout (in seconds) for the transports release.

        Default: `180`.

    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

    - `-a, --systemAlias <<SYSTEM_ALIAS>>` - `string`

        Alias of the system to connect.
    
    - `-d, --dest <<SYSTEM_ID>>` - `string`

        System ID of the system to connect.

        Ignored in conjunction with alias option.

    - `-h, --ashost <<APPLICATION_SERVER_ADDRESS>>` - `string`

        Application server address of the system to connect.

        Ignored in conjunction with alias option.

    - `-n, --sysnr <<INSTANCE_NUMBER>>` - `string`

        Instance number of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router string of the system to connect.

        Ignored in conjunction with alias option.

    - `-c, --client <<CLIENT>>` - `string`

        System logon client.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-p, --passwd <<PASSWORD>>` - `string`

        System logon user password.

        Ignored in conjunction with alias option.

> If the direct connection options are incomplete you'll be prompted to fill in the required values.

### Publish package manifest

The manifest is a document that contains information about a package. Its values can be defined during publishing.

The `-m, --manifest <<JSON>>` option allows you to define manifest values with a JSON string.

It can either indicate a file path or an acutal JSON string.

The expected object should have these values defined:

- `private` - **required** - `boolean`

    Defines the package visibility.

- `backwardsCompatible` - `boolean`

    Can be ignored if publishing a package for the first time.

    Defines if the release is backwards compatible with its older versions.

- `description` - `string`

    Short description of the package.

- `git` - `string`

    Link to git repository.

- `website` - `string`

    Link to project website.

- `license` - `string`

    Package license.

- `authors` - `string`

    Package authors, separated by comma.

    Valid values are:
    1. `Author 1, Author 2, Author 3...`
    2. `Author 1 <author1@email.com>, Author 2 <author2@email.com>, Author 3 <author3@email.com>...`

- `keywords` - `string`

    Package keywords, separated by comma.

- `dependencies` - `array`

    Defines a list of necessary TRM packages needed in order to avoid dependency errors.

    The array must define object with the following properties:
    - `name` - **required** - `string`

        Package full name.
    
    - `version` - **required** - `string`

        Semver valid version or range.

    - `registry` - `string`

        Registry endpoint.

        If left blank, defaults to public registry.

- `sapEntries` - `object`

    Defines the required table records needed in order to avoid runtime errors.

    Typically, indicates the TADIR dependencies with standard SAP objects.

    The object must have this structure:

    ```json
    {
        "TABLE_NAME1": [{...}],
        "TABLE_NAME2": [{...}],
        "TABLE_NAME3": [{...}]
    }
    ```

    Each table record should contain the required field/value combination needed in order to extract the required record.

The `dependencies` and `sapEntries` values of the manifest are calculated at runtime (unless running with the `-sd, --skipDependencies` flag) and values from the `-m, --manifest <<JSON>>` json are then merged.

Unless running with the `-om, --overwriteManifest` flag, release-indipendent values are kept the same, and not prompted (unless running with `-fm, --forceManifest` flag). 

## Unpublish package from registry

This command will only remove the package from the registry.

If installed on any of your systems, **it will remain without any changes**.

- Command `trm unpublish <<PACKAGE_NAME>>`
- Options
    - `-v, --version <<VERSION>>` - **required** - `string`

        Version of the release to unpublish.
        
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

## Install package on a system

- Command `trm install <<PACKAGE_NAME>>`
- Options
    - `-v, --version <<PACKAGE_VERSION>>` - `string`

        Version to get from the registy and install.

        Default: `latest` - Latest version available on the registry.

    - `-ci, --ci` - `boolean`

        Clean Install - avoids non-blocking prompts.

        Its intended use is in pipeline contexts, where the prompts should not appear.

        Default: `false`.

    - `-f, --force` - `boolean`

        Force the install when the same package and version is already installed.

        Overwritten by `-ci` flag.

        Default: `false` - Confirmation prompt.

    - `-to, --importTimeout <<TIMEOUT>>` - `number`

        Timeout (in seconds) for the package import.

        Default: `180`.

    - `-is, --ignoreSapEntries` - `boolean`

        Ignore missing SAP entries required by package.

        Default: `false` - If system has missing entries, installation will be aborted with error.

    - `-sd, --skipDependencies` - `boolean`

        Skip dependency check (and possible install) of package.

        Default: `false` - Dependencies are checked and install executed (if necessary).

    - `-k, --keepOriginalPackages` - `boolean`

        Keep same devclass (subpackages included) names of a package.

        **Use with caution**, if a package with the same name already exists on your system, it might change its hierarchy.

        See [Install package replacements](#install-package-replacements) for the detailed explaination.

        Default: `false` - Devclass names are calculated/prompted.

    - `-pr, --packageReplacements <<JSON>>` - `string`

        Path to JSON file or JSON array of package replacements.

        Ignored if `-k, --keepOriginalPackages` is used.

        See [Install package replacements](#install-package-replacements) for the detailed explaination.

    - `-swb, --skipWorkbenchTransport` - `boolean`

        Skip generation of workbench transport after install.

        Default: `false` - Transport is generated/updated.

    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

    - `-a, --systemAlias <<SYSTEM_ALIAS>>` - `string`

        Alias of the system to connect.
    
    - `-d, --dest <<SYSTEM_ID>>` - `string`

        System ID of the system to connect.

        Ignored in conjunction with alias option.

    - `-h, --ashost <<APPLICATION_SERVER_ADDRESS>>` - `string`

        Application server address of the system to connect.

        Ignored in conjunction with alias option.

    - `-n, --sysnr <<INSTANCE_NUMBER>>` - `string`

        Instance number of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router string of the system to connect.

        Ignored in conjunction with alias option.

    - `-c, --client <<CLIENT>>` - `string`

        System logon client.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-p, --passwd <<PASSWORD>>` - `string`

        System logon user password.

        Ignored in conjunction with alias option.

> If the direct connection options are incomplete you'll be prompted to fill in the required values.

### Install package replacements

Package replacements are the names of devclasses used during install of a package.

These values might be different from the published names.

If the parameter `-k, --keepOriginalPackages` is used, the original published devclass names are used during install.

This might be dangerous because if a devclass with the same name as one of the devclasses to install already exists on your system, it might change its superpackage (thus, its hierarchy).

When the `-k, --keepOriginalPackages` parameter is not used, `-pr, --packageReplacements` can be used to pass the replacement values.

The expected input is either a path to a file or a string with an array in JSON.

This array must have atleast one object, with these properties:

- `originalDevclass` - **required** - `string`

    Name of the original devclass of the package.

- `installDevclass` - **required** - `string`

    Replacement name.

Both install and original devclass names shall not exceede the 30 characters limit and, are subject to namespace validation.

If one or more package replacements are not found, a prompt asking a replacement name is shown on screen.

**Examples**

1.  Package has this devclass structure:

    - ZCUSTOM

    Using the flag `-k, --keepOriginalPackages` will result in a package named `ZCUSTOM` in the install system.

2.  Package has this devclass structure:

    - ZCUSTOM
        - ZCUSTOM_SUB

    Using the option `-pr, --packageReplacements` with the value 
    ```json
    [{
        originalDevclass: "ZCUSTOM",
        installDevclass: "ZINSTALL_CUSTOM"
    }, {
        originalDevclass: "ZCUSTOM_SUB",
        installDevclass: "ZINSTALL_CUSTOM_SUB"
    }]
    ```
    will result in a package named `ZINSTALL_CUSTOM` and a subpackage named `ZINSTALL_CUSTOM_SUB` in the install system.

3.  Package has this devclass structure:

    - ZCUSTOM
        - ZCUSTOM_SUB

    Using the option `-pr, --packageReplacements` with the value 
    ```json
    [{
        originalDevclass: "ZCUSTOM",
        installDevclass: "ZINSTALL_CUSTOM"
    }]
    ```
    will result in a package named `ZINSTALL_CUSTOM` in the install system and a prompt for devclass `ZCUSTOM_SUB`.

## List packages in a system

- Command `trm list`
- Options
    - `-a, --systemAlias <<SYSTEM_ALIAS>>` - `string`

        Alias of the system to connect.
    
    - `-d, --dest <<SYSTEM_ID>>` - `string`

        System ID of the system to connect.

        Ignored in conjunction with alias option.

    - `-h, --ashost <<APPLICATION_SERVER_ADDRESS>>` - `string`

        Application server address of the system to connect.

        Ignored in conjunction with alias option.

    - `-n, --sysnr <<INSTANCE_NUMBER>>` - `string`

        Instance number of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router string of the system to connect.

        Ignored in conjunction with alias option.

    - `-c, --client <<CLIENT>>` - `string`

        System logon client.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-p, --passwd <<PASSWORD>>` - `string`

        System logon user password.

        Ignored in conjunction with alias option.

> If the direct connection options are incomplete you'll be prompted to fill in the required values.

## View package on a system

- Command `trm view <<PACKAGE_NAME>>`
- Options
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

    - `-a, --systemAlias <<SYSTEM_ALIAS>>` - `string`

        Alias of the system to connect.
    
    - `-d, --dest <<SYSTEM_ID>>` - `string`

        System ID of the system to connect.

        Ignored in conjunction with alias option.

    - `-h, --ashost <<APPLICATION_SERVER_ADDRESS>>` - `string`

        Application server address of the system to connect.

        Ignored in conjunction with alias option.

    - `-n, --sysnr <<INSTANCE_NUMBER>>` - `string`

        Instance number of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router string of the system to connect.

        Ignored in conjunction with alias option.

    - `-c, --client <<CLIENT>>` - `string`

        System logon client.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-p, --passwd <<PASSWORD>>` - `string`

        System logon user password.

        Ignored in conjunction with alias option.

> If the direct connection options are incomplete you'll be prompted to fill in the required values.

## Check package on a system

- Command `trm check <<PACKAGE_NAME>>`
- Options
    - `-a, --systemAlias <<SYSTEM_ALIAS>>` - `string`

        Alias of the system to connect.
    
    - `-d, --dest <<SYSTEM_ID>>` - `string`

        System ID of the system to connect.

        Ignored in conjunction with alias option.

    - `-h, --ashost <<APPLICATION_SERVER_ADDRESS>>` - `string`

        Application server address of the system to connect.

        Ignored in conjunction with alias option.

    - `-n, --sysnr <<INSTANCE_NUMBER>>` - `string`

        Instance number of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router of the system to connect.

        Ignored in conjunction with alias option.

    - `-s, --sapRouter <<SAP_ROUTER>>` - `string`

        SAP Router string of the system to connect.

        Ignored in conjunction with alias option.

    - `-c, --client <<CLIENT>>` - `string`

        System logon client.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-u, --user <<USER>>` - `string`

        System logon user.

        Ignored in conjunction with alias option.

    - `-p, --passwd <<PASSWORD>>` - `string`

        System logon user password.

        Ignored in conjunction with alias option.

> If the direct connection options are incomplete you'll be prompted to fill in the required values.

## Compare package between multiple systems

- Command `trm compare <<PACKAGE_NAME>>`
- Options
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

    - `-c, --connections <<JSON_ARRAY>>` - `string`

        Array of aliases to compare.
