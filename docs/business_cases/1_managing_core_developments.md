# Turn reusable ABAP into a product

Most ABAP teams reuse more than source code. They reuse frameworks, integration
components, utilities, industry solutions, customizing, translations, and the
knowledge required to install everything correctly.

Without a delivery model, every reuse becomes another small implementation
project. Developers identify the right transports, check prerequisites, import
them in the right order, repeat manual setup, and later try to determine which
version each SAP system contains.

TRM turns that repeated work into a versioned package that can be published once
and installed consistently wherever it is needed.

## The business problem

A transport request is an effective SAP change vehicle, but it is not a product
catalog. On its own, it does not answer the questions a reusable solution raises:

- Which release is approved for this customer?
- Which other components does it require?
- Are the required SAP objects and customizing entries available?
- What must run after the import?
- Can the same release be installed again in a predictable way?
- How do we update ten customer systems without maintaining ten procedures?

As the customer base grows, these questions consume senior developer time and
make delivery dependent on individual knowledge. The technical asset may be
reusable, but the delivery process is not.

## What TRM changes

TRM adds a package lifecycle around SAP CTS. A release is distributed as a `.trm`
artifact containing its transports and a manifest that describes the package,
version, dependencies, prerequisites, and optional post-install activities.

That creates a repeatable workflow:

1. Develop and test the component in its source SAP system.
2. Publish a named, semantically versioned release.
3. Install that release in another SAP system through the TRM client.
4. Let TRM validate prerequisites, resolve compatible dependencies, and import
   the package content.
5. Promote the generated landscape transport through the customer's normal SAP
   change process when required.

TRM does not replace CTS or the customer's governance. It makes CTS-based
software delivery easier to package, repeat, and automate.

## For freelance ABAP developers

Reusable code can become a maintainable offering instead of a collection of
transport files.

With TRM, an independent developer can:

- publish a utility, add-on, or accelerator under a clear package name;
- release fixes and features using semantic versions;
- declare dependencies instead of documenting them in a readme;
- provide one repeatable installation path to every customer;
- distribute through a registry;
- include translations, customizing transports, and installation activities;
- make upgrades explicit without rebuilding delivery instructions for each
  engagement.

The result is a more professional handover and less unpaid time spent diagnosing
inconsistent releases, or forgotten setup steps.

## For SAP partners and product teams

Partners often maintain a common solution layer across many customer landscapes:
logging frameworks, interfaces, compliance features, templates, industry
processes, or complete add-ons. Manual distribution makes each additional
customer increase the maintenance burden.

TRM lets the partner manage these assets as a portfolio of packages:

- **Modular delivery:** split a large solution into independently versioned
  components.
- **Dependency management:** declare relationships between components and let
  TRM select compatible releases.
- **Release visibility:** identify installed package versions in SAP systems
  instead of reconstructing them from transport history.
- **Controlled upgrades:** release a fix once and let each customer adopt it on
  an agreed schedule.
- **Automation:** run non-interactive client operations from delivery pipelines.
- **Landscape continuity:** create a transport containing the installed changes
  for onward movement through the target customer's landscape.

This separates product maintenance from customer-specific implementation. The
same tested release can be delivered repeatedly while customer teams retain
control over approvals and promotion.

## A practical example

Consider a partner that maintains an integration framework used by twelve
customers. The framework depends on a logging library and requires a small set of
customizing entries.

Without TRM, a patch can mean twelve transport handovers, twelve dependency
checks, twelve sets of instructions, and twelve opportunities to install the
wrong combination.

With TRM, the partner publishes a new framework version that declares the logging
library version range and includes the required delivery content. Each customer
installs the named release. TRM checks the system, resolves the dependency, and
executes the same installation workflow. If exact dependency versions must be
reproduced, the team can use a lockfile with integrity verification.

The partner still decides when a release is approved, which systems receive it,
and how it moves to quality and production. TRM removes the avoidable mechanics
around that decision.

## Where to start

Choose one component that is already reused across systems and has a clear owner.
Package it, publish an initial semantic version, and install it in a non-production
SAP system. Once that path is repeatable, separate its shared dependencies and add
automation where it creates measurable value.

See [Publish and install](../examples/1_publish_and_install.md) for a guided first
release, or start with the [server](../server/setup.md) and
[client](../client/setup.md) setup guides.
