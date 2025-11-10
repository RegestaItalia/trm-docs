# TRM Registry

TRM uses a **registry** to publish and download packages.

By default, TRM is configured to work with the **public registry**, and no additional setup is required unless you wish to use or host a private registry.

> Any TRM registry other than the [official public registry](https://trmregistry.com) is considered a **private registry**.

---

## Public Registry

The **TRM Public Registry** is the official registry service provided by TRM.

- **Default Behavior**: All TRM clients are preconfigured to use it.
- **Anonymous Access**: Package downloads can often be done without an account.
- **Plans & Permissions**: Access levels and limits are determined by the user’s subscription plan. You can compare plans [here](https://trmregistry.com/plans).

### Roadmap

You can find the roadmap for the public registry [here](/registry/public/roadmap.md).

---

## Private Registry

You can configure one or more **private registries** to use with TRM.

### How to Add a Private Registry

You can add a private registry in two ways:

### Option 1: Manually via File

1. Navigate to your system's `AppData` folder:
   - Go to the `trm` directory (created after running any CLI command once).
2. Open or create a file named `registry.ini`.
3. Add your private registry in the following format:

```ini
[<registry name>]
endpointUrl=<registry endpoint>
```

> You may also optionally include an `auth` property containing a JSON-formatted authentication payload if your registry requires credentials.

### Option 2: Using the CLI

You can also add a registry with a single command:

```bash
trm registry add <registry name>
```

TRM will prompt you for the registry endpoint and any optional authentication configuration.