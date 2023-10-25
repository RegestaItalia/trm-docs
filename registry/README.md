# TRM Registry

TRM relies on a registry where packages are published and downloaded.

Out of the box, it is already configured to work with the public registry, and no other action is required.

> Any TRM Registry implementation besides the [public registry](https://trmregistry.com) is considered "private".

It is, however, possible to declare multiple "private" registries.

# Public Registry

TRM Public Registry is the official TRM registry implementation.

By default, each TRM client is set up to work with the public registry.

A person may be able to download a package without the need of an account.

Restrictions on the account are based on its plan. Differences between plans can be seen [here](https://trmregistry.com/#/plans).

The public registry exposes [REST APIs](/registry/public/api.md) that may be used to perform actions programmatically.

## Roadmap

TRM Public Registry roadmap is explained [here](/registry/public/roadmap.md).

# Private registry

In order to configure a private registry, the endpoint should be provided to the end-user.

To add a private registry to your TRM local installation you can:

- Manually add the private registry
    
    Navigate to your system AppData folder and open the "trm" folder.
    
    > In order to see the "trm" folder, the cli must be installed and a command executed at least once.
    
    Open or create the `registry.ini` file.
    
    Here the registry should be declared like this:
    
    ```ini
        [<<REGISTRY_NAME>>]
        endpointUrl=<<REGISTRY_ENDPOINT>>
    ```

    Optionally to the `endpointUrl` parameter, you could also declare an `auth` property and provide, in JSON format, the authentication needed for the registry.

- Add the registry via CLI

    Run the command

    `trm addRegistry <<REGISTRY_NAME>>`
