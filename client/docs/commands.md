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

## Info

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

## Ping

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

## Registry

Out of the box, trm-client is configured to work with the [public registry](https://trmregistry.com).

It is, however, possible to add as many private registries as you want.

To learn more about private registries, [visit the documentation](https://docs.trmregistry.com).

Registry data is saved in **plain text** in the AppData `registry.ini` file.

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

### Add private registry

- Command `trm addRegistry <<REGISTRY_NAME>>`
- Options
    - `-e, --endpoint <<ENDPOINT_URL>>` - `string`

        Base url of the registry.

    - `-a, --authentication <<JSON>>` - `string`

        Authentication object.

### Remove private registry

- Command `trm removeRegistry <<REGISTRY_NAME>>`

## Packages

TRM identifies a package as the composition of its TRM transports and the manifest.

> To avoid confusion, whenever TRM refeers to SAP packages, they are called Devclasses

### Publish package from a system

- Command `trm publish <<PACKAGE_NAME>>`
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

### Unpublish package from registry

This command will only remove the package from the registry.

If installed on any of your systems, it will remain without any changes.

- Command `trm unpublish <<PACKAGE_NAME>>`
- Options
    - `-v, --version <<VERSION>>` - **required** - `string`

        Version of the release to unpublish.
        
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

### Install package on a system

- Command `trm install <<PACKAGE_NAME>>`
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

### List packages in a system

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

### View package on a system

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

### Check package on a system

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

### Compare package between multiple systems

- Command `trm compare <<PACKAGE_NAME>>`
- Options
    - `-r, --registry <<REGISTRY_NAME>>` - `string`

        If no private registries are found, it will default to the public registry.

        If one or more registries are found, and this option is not provided, it will prompt for a registry selection.

    - `-c, --connections <<JSON_ARRAY>>` - `string`

        Array of aliases to compare.
