---
title: ABAP dependency management with TRM
description: Learn how TRM declares, resolves, locks, verifies, installs, and removes versioned dependencies for SAP ABAP packages.
---

# ABAP dependency management with TRM

TRM treats dependencies as part of a package's release contract. A manifest declares required TRM packages with semantic-version ranges, the installer selects compatible releases, and a lockfile can pin the exact versions and integrity values used for a repeatable installation.

This is different from an SAP object dependency. Object references help explain which repository objects rely on one another; a package dependency states which separately versioned software release must be installed.

## Dependency lifecycle

1. **Declare.** The publisher adds package names and non-empty semantic-version ranges to the manifest.
2. **Resolve.** During installation, TRM checks installed packages and available registry releases against each range. Pre-releases are selected only when the range opts into them.
3. **Verify.** TRM checks package integrity and the target's TRM, server, SAP release, and required-component constraints before import.
4. **Install.** Compatible dependencies are installed through the same guarded transport workflow as the root package.
5. **Lock.** A lockfile records the root package, its dependency graph, exact releases, registries, and integrity values.
6. **Protect.** Before uninstalling a package, TRM checks whether installed packages still depend on it.

## Manifest ranges and release selection

A dependency entry identifies a package and a semantic-version range. Ranges let a publisher express compatibility without forcing every consumer onto one build. For example, `^2.3.0` accepts compatible `2.x` releases while excluding a `3.0.0` breaking release.

TRM validates dependency ranges when a package is prepared for publishing. At install time it evaluates candidate releases in descending version order, verifies lockfile constraints when a lockfile is present, and avoids silently selecting a pre-release for a range that did not request one.

See [Declare package dependencies](../commons/dependencies.md) for the manifest shape and [Install and update](../commons/install.md) for the operational workflow.

## Lockfiles and reproducible installs

Version ranges answer “which releases are compatible?” A lockfile answers “which releases did this installation use?” It records exact versions and integrity values for the root package and resolved dependencies.

Use a committed lockfile when the same tested dependency graph must be installed across systems or rebuilt later. TRM rejects a lock entry that does not satisfy the requested dependency range and verifies that the fetched release matches its recorded integrity value.

Read [Reproducible ABAP installs with a lockfile](../commons/lockfile.md) for generation and clean-install commands.

## Package dependencies and SAP prerequisites

TRM evaluates more than TRM-to-TRM package relationships. A release can also constrain the supported TRM client/server versions, SAP release, and installed SAP components. These engine checks fail before importing an incompatible release.

That separation is intentional:

- **package dependencies** can be resolved and installed as versioned TRM releases;
- **SAP and runtime prerequisites** describe the target system and must already be satisfied;
- **repository-object dependencies** help analyze impact but are not themselves versioned packages.

## Conflict and removal behavior

If no available release satisfies a required range, installation stops instead of choosing an incompatible version. If a package is already installed, TRM checks its version against the requested constraint. A downgrade is explicit rather than an unnoticed side effect.

Uninstall performs the reverse safety check: dependants prevent removal unless the operator deliberately overrides that protection. This keeps a dependency from disappearing while installed packages still require it.

## Implementation evidence

The behavior is public and reviewable in the TRM repositories:

- [dependency release selection](https://github.com/RegestaItalia/trm-core/blob/main/src/actions/installDependency/findInstallRelease.ts)
- [dependency installation workflow and tests](https://github.com/RegestaItalia/trm-core/tree/main/src/actions/installDependency)
- [lockfile implementation and integrity checks](https://github.com/RegestaItalia/trm-core/blob/main/src/lockfile/Lockfile.ts)
- [manifest validation](https://github.com/RegestaItalia/trm-core/blob/main/src/manifest/Manifest.ts)
- [dependant protection during uninstall](https://github.com/RegestaItalia/trm-core/blob/main/src/actions/uninstall/checkDependants.ts)

## Continue the lifecycle

- [Start with a complete install example](../examples/2_package_with_dependencies.md)
- [Understand the `.trm` artifact](../commons/artifact.md)
- [See how uninstall uses deletion transports](uninstall-abap-software.md)
- [Compare ABAP delivery tools](abap-package-managers-compared.md)

*Author: TRM maintainers. Technical review: Regesta Group engineering. Last reviewed: 19 October 2026.*
