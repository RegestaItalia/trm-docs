# Hello world!

In this demo we're going to install the sample package [hello-world](https://www.trmregistry.com/#/package/hello-world).

This package contains a simple report that, when executed, will print an hello world string.

You can check out the package source code in its Github repository [here](https://github.com/RegestaItalia/trm-hello-world).

> This package is the perfect candidate for seeing TRM in action for your first time.

# Part 1: Install

## Prerequisites

For this demo you need to have an ECC/S4 development system, with a user allowed to make developments.

You'll also need to have [trm-server](https://docs.trmregistry.com/#/server/README) installed on that system and [trm-client](https://docs.trmregistry.com/#/client/README) on your computer.

## Installing

This package is publicly available on [the public registry](https://trmregistry.com/#/package/hello-world).

To start, run [the command](/client/docs/commands.md#install-package-on-a-system):

`trm install hello-world`

you'll be prompted with

1. System connection

    Here you should select how to connect to your development system.

    For this demo, select **Manual input**.

    Here, insert the connection values of your development system, as well as the logon data.

2. Input name for package

    The connection to the development system was successfull, and the packages has been retrieved from the registry.

    Now, you should input the name of the devclass (SAP Package) that will be created on your development system. Inside, the content of the sample package will be placed.

    For this demo, you can use a temporary package named **$TRM_HELLOWORLD**.

The `hello-world` package should now be installed into your system.

<p align="center">
  <img src="/_media/sample_install.png" />
</p>

You can view it with transaction `SE80`, and test the program `ZTRM_HELLOWORLD` with transaction `SE38`.

<p align="center">
  <img src="/_media/sample_install_se80.png" />
</p>

## List and view command

Other commands you can try after installing the `hello-world` package are **list** and **view**.

- With the [list command](https://docs.trmregistry.com/#/client/commands?id=list-packages-in-a-system) you can see all the packages installed in your system.

    Simply run `trm list`

    After connecting to the system (like we did earlier) you should see the list of packages.

    <p align="center">
        <img src="/_media/sample_list.png" />
    </p>

- With the [view command](https://docs.trmregistry.com/#/client/commands?id=view-package-on-a-system) you'll have more details about a package, like its manifest values.

    Run `trm view hello-world`

    and connect to your development system again to see the command in action.

    <p align="center">
        <img src="/_media/sample_view.png" />
    </p>

    Notice how it's also comparing the installed version with the latest available on the registry.

# Part 2: TRM in your landscape

Suppose you install a package, usually it's destined to be transported across your landscape (typically DEV-> QUA-> PRD).

## Prerequisites

For this demo you'll need [step 1](#part-1-install) completed and atleast another system in your landscape.

If you want to run this demo, make sure you installed the *hello-world* package with a namespace (**NOT $**) because, obviously, you can't transport a temporary package.

> Packages can be re-installed, and the devclass can be changed.

### Do I need trm-server?

For all the systems in your landscape that **are not development**, trm-server is not needed.

Once a package is installed with TRM, the transports across the landscape is **done manually**, and trm-server is won't be used.

## Transporting

Take a look at the install log and you'll see that a new transport has been generated.

<p align="center">
    <img src="/_media/sample_reinstall.png" />
</p>

> If you've lost the install log, check transaction `SE01`

It contain all of the objects in the TRM package and it can be used for transport across the landscape.

Before releasing, **make sure the package transport layers are correct and manually change the transport target system if necessary**.

1. Release and import the transport into your QUA system.

<p align="center">
    <img src="/_media/sample_transport.png" />
</p>

2. Run the list or view command with QUA system connection.

<p align="center">
    <img src="/_media/sample_view_after_transport.png" />
</p>

You'll notice that, although trm-server is not installed into QUA, TRM is capable of detecting that the `hello-world` package is installed.

## Compare command

The [compare command](https://docs.trmregistry.com/#/client/commands?id=compare-package-between-multiple-systems) can be used to compare the same packages between 2 or more systems.

In this case, run `trm compare hello-world` and, when asked, connect to both DEV and QUA.

<p align="center">
    <img src="/_media/sample_compare.png" />
</p>

You should see that in both systems you have the same version of `hello-world` installed.

> Try comparing other packages too!

# Install with dependencies

In this demo we're going to install the sample package [trm-dependant](https://www.trmregistry.com/#/package/trm-dependant).

This package contains a simple report that, when executed, will print a string returned from a class method of another TRM package ([trm-dependency](https://www.trmregistry.com/#/package/trm-dependency)).

You can check out both packages source code in their Github repositories:
- [trm-dependant](https://github.com/RegestaItalia/trm-dependant)
- [trm-dependency](https://github.com/RegestaItalia/trm-dependency)

> This package is the perfect candidate for seeing how TRM handles dependencies during install.ù

## Installing

This package is publicly available on [the public registry](https://trmregistry.com/#/package/trm-dependant).

To start, run [the command](https://docs.trmregistry.com/#/client/commands?id=install-package-on-a-system)
`
trm install trm-dependant
`

just like before, you'll be asked the target system connection details.

This time, you'll see that a dependency is detected and a confirm action (confirm install of the dependency) is expected.

<p align="center">
    <img src="/_media/sample_dependency_install.png" />
</p>

Confirming, will **first** install `trm-dependency` and **then** continue with the install of `trm-dependant`.

## List and view command

Running the `list` command now should show both `trm-dependency` and `trm-dependant` packages installed into your system.

## Transporting

If you check transaction `SE01` you should see two new transports, one for each of the TRM packages installed (installed as transportable):

<p align="center">
    <img src="/_media/sample_dependency_se01.png" />
</p>

To transport `trm-dependant`, you should transport `trm-dependency` first, to avoid any syntax errors or create a new transport of copies that includes both transports contents.