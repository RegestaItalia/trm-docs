# Control dependencies in modular ABAP solutions

Modular design only works when teams can identify and reproduce the relationships
between modules. In ABAP delivery, those relationships are often hidden until an
import produces an activation error or a runtime call reaches a missing object.

TRM makes dependencies part of the release instead of leaving them in project
memory.

## The hidden cost of dependencies

A business application may rely on a shared framework, which relies on another
utility, which assumes specific objects. When those requirements are tracked
in spreadsheets or installation guides, every delivery depends on someone
interpreting the chain correctly.

Common consequences include:

- transports imported in the wrong order;
- incompatible library versions in one SAP system;
- missing SAP prerequisites;
- duplicated components bundled to avoid dependency risk;
- senior developers required for routine installations.

## Make the graph explicit

TRM records package dependencies as semantic version ranges. During installation,
it selects compatible releases and installs dependencies recursively. It also
checks recorded SAP objects and entries before package import.

When a tested dependency set must be reproduced exactly, a lockfile records the
selected versions and artifact integrity values. This is useful for release
qualification, customer support, and consistent pipeline runs.

Dependency detection is deterministic, not magic. TRM uses SAP's internal repository APIs
and object metadata to discover the dependencies of supported object types. The
same repository state therefore produces the same detected dependency graph; the
result does not depend on heuristics or generative analysis.

## Business value

Explicit dependencies allow teams to split large solutions without making them
harder to deliver. Shared modules can evolve independently, applications can state
their compatibility expectations, and installation failures move earlier in the
process—from production troubleshooting to prerequisite validation.

The result is safer reuse and a clearer architecture: components have owners,
versions, and declared relationships.

Review [dependency recognition](../commons/dependencies.md) and the
[lockfile example](../examples/3_install_with_a_lockfile.md).
