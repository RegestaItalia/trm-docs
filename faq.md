# FAQ (Frequently Asked Questions)

This document is regularly updated with common questions from the community.

Before asking general questions about TRM or the public registry, please read through this FAQ.

+ Do I need TRM? +

    TRM provides value as a versioning and packaging tool:

    - As an **SAP open-source developer**, you can use TRM to **publish** your code. For end users, installing a package becomes as simple as running a CLI command, just as it is in many modern development ecosystems.
    - As a **SAP partner**, TRM helps you **modularize your developments**. Each module can be treated as a library or product. Delivering these to customers is a one-command process using the CLI.

+ Is TRM an SAP product? +

    **No.** TRM is not endorsed, sponsored, or affiliated with SAP in any way.

+ Who owns TRM? +

    TRM is owned, funded, and actively maintained by [Regesta S.p.A.](https://www.regestaitalia.eu/) and [Clarex S.r.l.](https://www.clarex.it/).

+ I need support. Whom should I contact? +

    Check out the [incident](/incidents.md) section.

+ Is it safe to import open source ABAP packages into my customer system? +

    You should exercise caution:

    - Always check the package’s **Git repository and source code**.
    - Community feedback is a useful indicator of reliability.
    - Inspect the contents of the package's transports.

+ I'm an SAP partner and want to publish private packages. What should I do? +

    [Upgrading your plan](https://trmregistry.com/plans) allows you to publish private packages and have priority support.

+ Can I implement my own private registry? +

    Yes. TRM is open source, and you can implement your custom private registry. 

+ How does TRM handle dependencies? +

    During publishing, TRM automatically detects dependencies on other TRM packages, custom objects, and standard SAP objects.

    During installation, TRM ensures that:
        - The SAP objects used exist.
        - Required TRM packages are installed and up to date.

    More info: [Dependency recognition](/commons/dependencies.md#dependency-recognition)

+ Does TRM support cloud developments? +

    Cloud development is **not currently supported**, but research has begun and updates will follow.

+ Can I use TRM for CD (Continuous Deployment)? +

    Yes.

    - TRM supports automation through the CLI.
    - All publish/install commands support non-interactive execution.
    - For GitHub Actions, see the [CD workflow example](/examples/6_abap_github_actions_ci_cd.md).

+ Does TRM support object translations? +

    Yes, object translations are fully supported.

+ Does TRM support customizing? +

    Yes, TRM supports customizing.

+ I installed a package with dependencies, and TRM generated multiple transports. How do I determine the correct release order? +

    SAP supports defining [transport dependencies via CTS projects](https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611666.html), but TRM does not currently support this.
