# Frequently asked questions

## Understanding TRM

### What is TRM?

TRM (Transport Request Manager) is a package manager for SAP ABAP developments. It
packages CTS transports with release metadata so ABAP developments can be
published, versioned, installed, upgraded, and automated as named software
packages.

A TRM artifact can include workbench objects, translations, customizing, SAP
prerequisites, package dependencies, and post-install activities.

### Why use TRM instead of sharing transport files?

A transport moves changes; TRM manages a software release. It adds a package
identity, semantic version, dependency information, prerequisite checks, and a
repeatable installation workflow around CTS.

This is especially valuable when the same component is delivered to several SAP
systems or customers, or when multiple components must be kept compatible.

### Does TRM replace SAP CTS or our change-management process?

No. TRM uses SAP transport mechanisms to publish and install package content. Your
organization still controls approvals, segregation of duties, testing, and
promotion to quality and production.

### Who is TRM for?

TRM is useful for:

- SAP partners maintaining common solutions across customers;
- corporate ABAP teams modularizing shared internal developments;
- open-source maintainers who want a simple installation experience;
- delivery teams automating repeatable ABAP deployments.
- freelance ABAP developers distributing reusable tools or add-ons;

### Is TRM an SAP product?

No. TRM is not endorsed, sponsored, or affiliated with SAP. It is an independent,
open-source project funded and maintained by Regesta S.p.A. and Clarex S.r.l.

## Packages and releases

### What is inside a `.trm` file?

A `.trm` file is a portable package artifact. It contains a manifest and the
transports produced for the release. Depending on the package, those transports
can contain package definitions, workbench objects, translations, and customizing
data. It can also include serialized source when abapGit is available in the
publishing system.

See [TRM artifact](commons/artifact.md) for the format and transport types.

### How are packages versioned?

TRM releases use [Semantic Versioning](https://semver.org/). Dependencies can
declare compatible version ranges, allowing publishers to communicate whether a
release is a patch, a backward-compatible feature, or a breaking change.

Version numbers communicate compatibility; they do not replace testing or an
organization's release approval process.

### Can TRM install a package into a different ABAP package name?

Yes. During installation, TRM can map the source package hierarchy to packages in
the target system. This supports customer naming conventions and transport-layer
requirements without rebuilding the release for every target.

Existing target objects are protected by installation checks, and TRM asks for
confirmation before overwriting a modified package in interactive workflows.

### Does TRM support translations and customizing?

Yes. A release can include a translation transport and one or more customizing
transports. Customizing must be designed for safe, repeatable delivery, especially
when values are client-dependent or differ between customer environments.

Language and customizing transports are optional.

### Can a package perform setup after installation?

Yes. A manifest can declare post-install activities implemented by ABAP classes.
They are suitable for repeatable tasks such as refreshing caches or regenerating roles.

Post-install activities execute code in the target SAP system. See [Post activities](commons/post_activities.md).

## Dependencies and reproducibility

### How does dependency management work?

During publication, TRM analyzes package contents to identify dependencies. Other
TRM packages become versioned package dependencies; required SAP objects and
table entries are recorded as SAP prerequisites.

During installation, TRM verifies those prerequisites and installs compatible TRM
dependencies recursively. Detection coverage varies by ABAP object type and
cannot reliably discover dynamic or string-based references. Review the current
[dependency recognition coverage](commons/dependencies.md) and declare anything
that cannot be inferred.

### What happens when two packages require incompatible versions of one dependency?

An SAP system can contain only one installed version of a given TRM package at a
time. ABAP repository objects are active in a shared system; they are
not isolated into a separate dependency tree for every consuming application.

This does **not** make TRM any less of a package manager. Package management
describes how software is named, versioned, published, resolved, installed, and
upgraded. It does not require the target runtime to keep several versions of the
same package active side by side. Many package-management models resolve one
version for a given environment.

A useful analogy is to view the SAP system as a deployment target such as a CDN:
the registry can retain and distribute many releases, while a particular target
serves one deployed version. TRM manages which release reaches that target and
which compatibility rules must be satisfied. SAP determines how the deployed
ABAP objects exist and execute.

If package `A` requires `shared-library` version `^1.0.0` and package `B` requires
`^2.0.0`, those ranges do not overlap. Installing both requirements into the same
SAP system would demand two active versions of `shared-library`, so TRM reports a
conflict instead of silently choosing a version that violates one package's
contract.

The solution is to make the dependency graph compatible. Package owners can
broaden a supported range after testing, upgrade the consuming package, or ship a
new major release that works with the shared version selected for that SAP
system. If true side-by-side behavior is required, it must be designed at the
ABAP architecture level—for example, as separately named components—not assumed
from the use of a package manager.

### What is a lockfile for?

A lockfile records the exact dependency releases and their integrity values. Use
it when the same dependency graph must be reproduced across developers, systems,
or pipeline runs.

Without a lockfile, TRM selects the newest available releases that satisfy the
declared ranges. With one, TRM uses the locked versions and verifies that the
downloaded artifacts match. See
[Install with a lockfile](examples/3_install_with_a_lockfile.md).

## Registries and connectivity

### Do I have to use the public TRM Registry?

No. TRM supports the official public registry, compatible private registries, and
local `.trm` files. A registry is convenient for discovery, access control, and
centralized releases; a local artifact is useful for local tests.

### Why use the official TRM Registry?

The official registry is already configured in the TRM client, so teams can
publish and consume packages without deploying registry infrastructure first. It
provides one place for package names, versions, metadata, release artifacts, and
access control.

For an open-source maintainer, that means a shorter path from a Git repository to
an installable ABAP package. For a company or SAP partner, it means spending less
time operating distribution infrastructure and more time maintaining the
software being delivered.

### Is the TRM Registry free?

Publishing public packages is free. This makes the registry suitable for
open-source projects, community libraries, examples, and packages intended for
unrestricted reuse.

Private packages are a paid service. They are designed for proprietary software
whose releases must only be available to authorized users or customers. Current
options are listed on the [TRM Registry plans page](https://trmregistry.com/plans).

### Why would a company publish private packages?

Most corporate ABAP is valuable precisely because it is private: internal
frameworks, integration assets, industry solutions, customer-specific products,
and intellectual property developed by SAP partners.

A private registry package keeps the benefits of package management without
making that software public. The organization can maintain named releases,
semantic versions, dependencies, and a repeatable installation workflow while
limiting artifact access to authorized consumers.

This is often simpler than distributing transport files through email, shared
drives, or a different customer portal for every engagement. The delivery method
becomes consistent even when the code must remain confidential.

### Why pay for private packages instead of using a file share?

A file share stores files. A registry understands packages and releases. It gives
the TRM client a consistent way to locate versions, retrieve package metadata,
resolve dependencies, authenticate consumers, and download the selected artifact.

Local `.trm` files remain valuable for one-off or offline delivery. A private
registry becomes more valuable when a company maintains several products,
supports multiple customers, publishes updates regularly, or wants delivery
automation that does not depend on manually exchanging files.

### Do we have to operate our own registry to keep packages private?

No. Private packages can be hosted on the official TRM Registry through a paid
plan, avoiding the deployment, monitoring, updates, availability, and API
maintenance associated with running another service.

Organizations that require infrastructure under their own control can implement
a compatible private registry using the published
[Registry API](registry/openapi.md). TRM deliberately supports both models: a
managed service for teams that want to move quickly and an open contract for
teams with specific hosting requirements.

### Can one solution use packages from different registries?

Yes. Each dependency can identify its registry, allowing a solution to combine,
for example, an internal private package with a public community dependency.
Access to every required registry must be configured in the installation
environment, and the complete dependency chain should be reviewed under the
organization's software-supply policies.

### Can TRM work in an offline or restricted customer environment?

Yes. Publish or obtain the `.trm` artifact outside the restricted environment,
transfer it through the customer's approved process, and install it from the
local file. The target still needs the TRM server component and the SAP
authorizations required for installation.

Package dependencies also need to be available to the installation process. Plan
and stage the complete dependency set when the target cannot reach a registry.

### Does TRM support SAP BTP and ABAP Cloud?

These are separate questions:

- The TRM client can connect through an SAP BTP destination when the appropriate
  client plugin is installed.
- That connectivity option does not mean TRM supports ABAP Cloud development or
  the cloud ABAP language and extensibility model. TRM currently targets
  CTS-based ABAP systems.

See [Client setup](client/setup.md) for the available connection options.

## Security and operations

### Is it safe to install a package from a registry?

A registry is a delivery channel, not a substitute for software assurance. Before
installing third-party software:

- verify the publisher and package source;
- review the manifest, dependencies, transports, and post-install activities;
- pin or lock approved versions where reproducibility matters;
- test in a non-production system;
- apply your normal code review, security, and change-management controls.

Treat a `.trm` artifact with the same care as any other executable ABAP delivery.

### What SAP access does TRM require?

TRM needs its server component in each source or target SAP system with which it
interacts. The connecting SAP user must be explicitly allowed by TRM and must
have the authorizations required for the requested transport and repository
operations.

Keep technical users least-privileged, separate publishing and installation
credentials where appropriate, and protect registry and SAP credentials as
secrets. See [Server setup](server/setup.md) for the initial authorization step.

### Can TRM be used in CI/CD pipelines?

Yes. Publishing and installation can run non-interactively, making TRM suitable
for release pipelines and repeatable delivery automation. Pipeline credentials,
package visibility, optional transports, target mappings, and approvals must be
provided explicitly so the run does not depend on interactive prompts.

Automation should complement—not bypass—the controls required by the target SAP
landscape.

### Does TRM automatically roll back every failed installation?

With CTS, rollbacks are always a bit of a challenge, and TRM cannot always
guarantee a clean rollback. TRM performs validation before import and restores
transports and system state as best as possible, but some operations are intentionally
not reversible. Custom post-install activities can also have their own side effects.

### How do I know which transport to move through the rest of the landscape?

After a successful package install, TRM creates the request that collects the
changes for onward movement. For an update that also removes obsolete objects,
the deletion transport must be imported before the landscape transport.

Follow the target organization's normal release and import-order controls; do not
infer the sequence from transport numbers alone.

## Support and contribution

### Where can I report a problem or request support?

Start with [Incidents and support](incidents.md). Include the TRM client, core, and
server versions; the connection type; the command or operation; relevant logs;
and the smallest reproducible example you can share without exposing secrets or
customer data.

### Can I contribute to TRM?

Yes. TRM's core projects are open source. Read the
[contribution guidelines](CONTRIBUTING.md), open an issue before substantial
changes, and follow the contribution rules of the repository you intend to
change.
