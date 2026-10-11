# Build a commercial ABAP add-on

An ABAP solution becomes difficult to sell repeatedly when every sale creates a
new delivery project. Transport lists, installation notes, prerequisites, and
upgrade instructions quickly consume the margin earned by the product itself.

TRM gives independent developers and software vendors a repeatable distribution
model for CTS-based ABAP products.

## The challenge

A customer buying an add-on expects more than source code. They expect a defined
release, predictable installation, documented compatibility, and a credible path
for fixes and upgrades. A folder of transport files leaves important questions
unanswered:

- Which features form version `2.3.0`?
- Which shared libraries must be installed first?
- What SAP system requisites are needed?
- Can the vendor reproduce exactly what the customer received?

Answering those questions manually for every customer does not scale.

## The TRM approach

TRM packages the solution's transports and release metadata in a `.trm` artifact.
The vendor can publish named releases to a registry or provide the artifact
directly for local installation.

Each release can describe:

- its semantic version and product metadata;
- dependencies on other TRM packages;
- required SAP objects and entries;
- workbench, translation, and customizing content;
- activities to execute after installation.

The customer receives a consistent installation workflow rather than a bespoke
set of instructions. Future fixes are published as new versions of the same
package, making the upgrade path visible and intentional.

## Start small

Choose the smallest independently useful component, establish its package name,
and publish a first release from a non-production source system. Test installation
into a clean target system before adding optional customizing or post-install
automation.

Continue with [Publish and install](../examples/1_publish_and_install.md).
