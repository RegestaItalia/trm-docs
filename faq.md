# FAQ (Frequently Asked Questions)

This document will be updated with the most frequently asked question by the community.

Before asking general questions about TRM or the public registry, read this document.

+ Do I need TRM? +

    Depending on who you are, TRM can be used in different ways.

    If you are an **SAP Open Source developer**, you can make your software and use TRM for **publishing**. With TRM, installing a package is as easy as running a CLI command like most of the other software development languages.

    If you are an **SAP partner** with customers, TRM is useful for **modularizing your developments**. Each of your modules is a library or a product and **delivering** one or more of these modules to your customers is still a CLI one-command job.

    If you are none of these options, it's still a good idea to always **make releases** of your software once it reaches a stable state.

+ Im not sure I want to invest time into TRM, what's the roadmap? +

    There are two separated roadmaps:
    1. [Roadmap for the project](/commons/roadmap.md)
    2. [Roadmap for the public registry](/registry/public/roadmap.md)

+ Is TRM an SAP product? +

    **No, TRM is not endorsed, sponsored or affiliated by or with SAP**.

+ I want to request a new feature or requerst a bug fix, what should I do? +

    You can open an issue on the appropriate Github repository.

    If you are not sure, you can contact us directly [support@trmregistry.com](mailto:support@trmregistry.com).

+ Is it safe to download packages from the public registry? +

    A package owned by an unverified published is clearly stated in its overview page.

    Verified publishers are deemed as safe by TRM maintainers.
    
    If you intend to install a package from the public registry, you should always **check its git repository** and have a look at its **source code**.
    
    Community feedback about the package are indicators of safe content.

    It's also good practice to run the R3Trans program and check its content.

+ I want to use TRM in my organization, can I publish private packages? +

    Yes you can either use the public registry or build your own private registry.

    If you want to use the public registry, to publish private registries you first must upgrade your plan.

+ Can I use a private registry instead of the public registry? +

    Yes, TRM is an open source project, and for this reason you can define a private registry and the documentation of what needs to be implemented is [here](/registry/private/README.md).

+ Are dependencies handled? +

    Yes, **TRM can handle dependencies**.

    Dependencies can be other TRM packages, SAP standard objects or customizing table records.

    Whenever a package is published, TRM will automatically detect the required dependencies, however not all objects are supported. Check the automatic dependency objects that can be detected [here](/commons/dependencies.md#dependency-recognition).
    Before publishing a package, dependencies can also be manually edited.

    Whenever a package is installed, TRM will check that the required SAP standard objects/customizing table records are available on the target system, and TRM package dependencies are installed/updated.

+ Does TRM support cloud developments? +
    
    TRM does not support cloud and, at the moment, there is **no plan to support cloud**.

+ How can I secure the RFC functions exposed by trm-server? +
    
    Some of the RFC enabled function modules exposed by trm-server can damage the system is used imporperly.
    
    trm-server should only be used by a set of authoried users.
    
    To do this, [follow the user maintenance guide](https://docs.trmregistry.com/#/server/docs/setup?id=user-authorization-maintenance).

+ Can I manually install a TRM package? +
    
    Although **not recommended**, it's possible, but there's alot of **manual steps** that need to be done in order to say the package is installed properly for TRM.

    The required manual steps are not documented.

+ Can I use TRM for CD (Continuous Deployment)? +

    Yes you can.

    The documentation of the publish and install commands will tell you all the options available in order to avoid human interaction with the CLI.

    If running in Github, there's an example of CD workflow [here](/client/docs/examples/githubActions.md).

+ Does TRM support object translations? +

    Yes, translation is supported.

 + Does TRM support customizing? +

    Not yet, but it's planned.

    Check out the [Roadmap for the project](/commons/roadmap.md).

 + I installed a package with dependencies, and TRM correctly generated a transport for each of the dependencies. How do I figure out the transport release order? +
    
    SAP does have a standard way for [defining dependencies between transports](https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611666.html), but because CTS Projects must be defined, TRM does **not** support it.

    It is planned, for the future, a command that will tell you the correct release order.

    Check out the [Roadmap for the project](/commons/roadmap.md).

 + Are there any USER EXITs I can use to extend TRM? +
    
    Not yet, but it's planned.

    Check out the [Roadmap for the project](/commons/roadmap.md).

 + How do I compare a package between multiple systems? +
    
    You can use the [compare command](/client/docs/commands.md#compare-package-between-multiple-systems).

    This command can be used to check which version is installed on which system, and it works without the need of trm-server (it can be used to **compare packages between development and productive systems**).