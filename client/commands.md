# Commands

A full list of commands that can be used by trm-client can be found by simply typing

`trm`

in your CLI.

## System alias

Because a connection to an SAP OnPremise system has a quite a few parameters, connecting to a system by typing all of them via CLI can be challenging.

To solve this problem, you can create a system alias.

A system alias is an easy way to store all of the connection attributes, including login data, of an SAP OnPremise system.

System aliases are saved in **plain text** in the AppData `systems.ini` file.

### Manage alias

All-in-one command that lets you view, edit or check connection of an alias.

- Command `trm createAlias <<ALIAS_NAME>>`
- Options
    - `-a, --systemAlias <<systemAlias>>` - `string`

        Alias name to manage. If not provided, a list with all of you aliases will be prompted.

### Create alias

Create a new system alias.

- Command `trm createAlias <<ALIAS_NAME>>`

### Delete alias

Delete a system alias.

- Command `trm deleteAlias <<ALIAS_NAME>>`

## Registry

Out of the box, trm-client, is configured to work by default with the public registry, however it is possible to add as many custom (or private) registries as you want.

Registries data are saved in **plain text** in the AppData `registry.ini` file.

### Login

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

### Current logged in user

Show the currently logged in user data in a registry.

> This command will show an error message when executed on a registry that requires no authentication.

- Command `trm whoami`
- Options
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

### Logout

Log out of the registry.

> This command will show an error message when executed on a registry that requires no authentication.

- Command `trm logout`
- Options
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

## Publishing packages

### Publish package from a system

- Command `trm publish <<PACKAGE_NAME>>`

## Installing packages

- Command `trm install <<PACKAGE_NAME>>`

### Install package on a system

## View packages

### View on one system

- Command `trm view <<PACKAGE_NAME>>`

### Compare between multiple systems

- Command `trm compare <<PACKAGE_NAME>>`