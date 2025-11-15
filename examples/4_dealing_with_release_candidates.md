# Dealing with release candidates

A release candidate (RC) is a version of a package that is almost ready to become a final release.
It’s basically a “preview” version meant for testing before the official release goes out to everyone.

Release candidates are a good way to move your product from the central development system to a customer development system where there might better data to test the new features, in a stage where human tests are done before declaring the release is ready and definitive.

## Release tags

Tags are particolary useful with release candidates.
A tag is simply a label that points to a release of the package.

> We've been using tags up until now without noticing... the latest keyword is a tag itself that points to the latest release of the package!

Adding a tag to a release candidate (common tags are `rc`, `alpha`, `dev`...) allows the end user (or who is in charge of the human tests) to install the latest available release candidate.

## Publishing a release candidate

There's really not much changing in the publish steps of a release candidate, except maybe for the version of the release.
When it comes to versioning, it's good practice to indicate a prerelease by adding it to the version itself, like `1.0.3-rc.0` (release candidate build 0).
This makes it clear to end users that the release is still not ready for production.

> 💡 Tip: just like publishing without indicating a version TRM proposes an increase of the latest available version, you can also do that with prereleases, by using --prerelease and --pre-release-identifier <identifier>

Let's publish the first release candidate of `@trmsamples/doc-demo` version `1.0.3`, and tagging it `rc`.

<div style="display:flex; justify-content:center;">
  <img src="/_media/4_1_dealing_with_release_candidates.png" alt="Publishing with a tag" style="max-width:100%; height:auto; border-radius:8px;">
</div>

> Notice TRM indicates the release is tagged with `rc`

If we go to the registry website we can confirm the `rc` tag is in place:

<div style="display:flex; justify-content:center;">
  <img src="/_media/4_2_dealing_with_release_candidates.png" alt="Publishing with a tag" style="max-width:100%; height:auto; border-radius:8px;">
</div>

This clearly shows that the `latest` tag still points to version `1.0.2` and if an end user was to install the latest stable version, they'd get version `1.0.2`.
However a release candidate exists, and it's tagged with `rc` pointing to version `1.0.3-rc.0`.

## Installing a release candidate and promoting to latest

Just like any install, we can point to a specific version or to a tag. In this case, let's install the `rc` version.

<div style="display:flex; justify-content:center;">
  <img src="/_media/4_3_dealing_with_release_candidates.png" alt="Installing the prerelease" style="max-width:100%; height:auto; border-radius:8px;">
</div>

As you can see, `rc` installed `1.0.3-rc.0`.
At this point, now release candidates of version `1.0.3` can be published (`1.0.3-rc.1`, `1.0.3-rc.2` and so on) and the `rc` tag can be moved to the latest release candidate available.

Once we're ready to release `1.0.3`, we can either re-publish the latest release candidate (essentially cleaning the semantic versioning from `1.0.3-rc.0` to `1.0.3`) or simply reassign the `latest` tag and delete the `rc` tag.

<div style="display:flex; justify-content:center;">
  <img src="/_media/4_4_dealing_with_release_candidates.png" alt="Retagging the release" style="max-width:100%; height:auto; border-radius:8px;">
</div>