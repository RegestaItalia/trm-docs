# Automate repeatable ABAP delivery

ABAP teams increasingly automate code checks and builds, yet software delivery
often ends with a manual list of transports and instructions. That gap makes the
last mile slow, inconsistent, and difficult to reproduce.

TRM provides package-oriented operations that can run non-interactively in a
delivery pipeline.

## What can be standardized

A pipeline can use TRM to publish an approved package release or install a
specific release into a target SAP system. The same workflow can define package
visibility, optional content, dependency behavior, and target mappings without
waiting for interactive answers.

This is particularly useful for:

- scheduled delivery of shared internal components;
- repeatable installation into integration systems;
- release-candidate validation;
- customer-specific deployment pipelines;
- producing a consistent package artifact for approval;

## Keep approvals where they belong

Automation does not require uncontrolled production deployment. A useful pipeline
separates repeatable mechanics from business authorization:

1. Validate and publish a versioned release.
2. Install it in a non-production SAP system.
3. Run technical and functional tests.
4. Require the organization's normal approval.
5. Promote the approved transport through the governed landscape route.

Credentials remain protected as pipeline secrets, and technical users should have
only the SAP and registry permissions their job requires.

## Business impact

Teams spend less time repeating known steps and more time evaluating the release.
The same inputs produce the same declared package operation, logs are available to
the pipeline, and delivery knowledge is encoded instead of depending on who is
available that day.

TRM therefore connects modern release engineering with SAP CTS without asking the
organization to abandon its existing controls.

See the [GitHub Actions concept](../commons/github_actions.md) and
[CI/CD example](../examples/6_abap_github_actions_ci_cd.md).
