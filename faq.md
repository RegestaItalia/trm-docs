# FAQ (Frequently Asked Questions)

This document is regularly updated with common questions from the community.

Before asking general questions about TRM or the public registry, please read through this FAQ.

+ Do I need TRM? +

    Depending on who you are, TRM can be useful in different ways:

    - If you are an **SAP open source developer**, you can use TRM to **publish** your software. Installing a package becomes as simple as running a CLI command—just like in many modern development ecosystems.
    - If you are an **SAP partner**, TRM helps you **modularize your developments**. Each module can be treated as a library or product. Delivering these to customers is a one-command process using the CLI.
    - Even if you don’t fit the above categories, TRM still provides value as a versioning and packaging tool — you can **release stable versions** of your code with minimal effort.

+ I'm not sure I want to invest time into TRM. What's the roadmap? +

    You can view the [public registry roadmap](/registry/public/roadmap.md).

+ Is TRM an SAP product? +

    **No.** TRM is not endorsed, sponsored, or affiliated with SAP in any way.

+ I want to request a new feature or report a bug. What should I do? +

    You can open an issue in the appropriate GitHub repository.  
    If you're unsure where to report, feel free to email us at [support@trmregistry.com](mailto:support@trmregistry.com).

+ Is it safe to download packages from the public registry? +

    Yes, but you should exercise caution:

    - Packages published by **unverified users** are clearly marked.
    - **Verified publishers** are vetted by TRM maintainers.
    - Always check the package’s **Git repository and source code**.
    - Community feedback is a useful indicator of reliability.
    - For additional safety, consider running the `R3Trans` program to inspect the package content.

+ I want to use TRM in my organization. Can I publish private packages? +

    Yes. You can either:
    
    - Use the **public registry** (a subscription upgrade is required for private packages), or  
    - Set up your **own private registry**.

+ Can I use a private registry instead of the public one? +

    Yes. TRM is open source, and you can configure a private registry.  
    See the implementation guide [here](/registry/private/README.md).

+ Are dependencies handled? +

    Yes, **TRM handles dependencies** automatically and manually.

    - Dependencies can include TRM packages, SAP standard objects, and customizing records.
    - During publishing, TRM detects dependencies automatically (based on supported object types).
    - You can also manually edit the detected dependencies.
    - During installation, TRM ensures that:
        - SAP objects/customizing records are present.
        - Required TRM packages are installed and up to date.

    More info: [Dependency recognition](/commons/dependencies.md#dependency-recognition)

+ Does TRM support cloud developments? +

    No. TRM does **not** currently support cloud-based development, and there are **no plans to support cloud** at this time.

+ How can I secure the RFC functions exposed by `trm-server`? +

    Some RFC-enabled function modules can be misused if not secured.

    - `trm-server` should only be accessible to **authorized users**.
    - Follow the [user authorization setup guide](https://docs.trmregistry.com/#/server/docs/setup?id=user-authorization-maintenance) for best practices.

+ Can I manually install a TRM package? +

    Although it's **possible**, manual installation is **not recommended** due to the complexity and number of steps involved.

    Manual installation steps are not documented, and proper integration with TRM features may not be guaranteed.

+ Can I use TRM for CD (Continuous Deployment)? +

    Yes.

    - TRM supports automation through the CLI.
    - All publish/install commands support non-interactive execution.
    - For GitHub Actions, see the [CD workflow example](/client/docs/examples/githubActions.md).

+ Does TRM support object translations? +

    Yes, object translations are fully supported.

+ Does TRM support customizing? +

    Yes, TRM supports customizing data.

+ I installed a package with dependencies, and TRM generated multiple transports. How do I determine the correct release order? +

    SAP supports defining [transport dependencies via CTS projects](https://help.sap.com/docs/SUPPORT_CONTENT/basis/3354611666.html), but TRM does **not** currently support this.

    A future CLI command is planned to assist in determining the correct release order.

+ Are there any USER EXITs I can use to extend TRM? +

    Not yet, but this is a planned feature.

+ How do I compare a package across multiple systems? +

    Use the `compare` command to check package versions across systems.

    See: [Compare command documentation](/client/docs/commands.md#compare-package-between-multiple-systems)

    - It works without `trm-server`
    - Ideal for comparing development and production systems
