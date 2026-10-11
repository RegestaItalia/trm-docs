# Make open-source ABAP easier to adopt

Open-source ABAP succeeds only when users can install it confidently. A valuable
project can still lose potential adopters if setup begins with searching for
transport files, resolving undocumented prerequisites, and interpreting a long
README.

TRM gives maintainers a package experience familiar from other development
ecosystems while continuing to use SAP transport technology.

## Reduce the first-install barrier

A maintainer can publish a named, versioned package to the public registry. Users
install the requested release through the TRM client, and the release carries the
metadata needed to describe dependencies and prerequisites.

This improves the adoption journey:

- one package name replaces a list of files;
- semantic versions make releases understandable;
- dependencies do not have to be installed from memory;
- source-repository and license metadata can be included in the manifest;
- upgrades follow the same workflow as the initial installation.

## Improve maintainability for contributors

Clear package boundaries help contributors understand which components change
together. Maintainers can release fixes independently, reuse shared packages, and
communicate compatibility through dependency ranges rather than copying common
code into every repository.

Consumers still need to review third-party code and test it according to their
organization's policies. TRM improves delivery consistency; it does not certify
the quality or security of a package.

## Grow an ecosystem

When projects share a common publication and installation model, they become
easier to combine. A library can be consumed by several tools, and improvements
to that library can be released without repackaging every dependent project.

The result is a lower barrier for new users and a healthier reuse model for the
ABAP community.

Start with [Publish and install](../examples/1_publish_and_install.md) and review
the [manifest metadata](../commons/manifest.md) exposed with a release.
