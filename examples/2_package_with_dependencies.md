# Package with dependencies

In the last post, we published and installed a simple package.
If you remember, we have an empty method without implementation, so now we're not only implementing it but also create a dependency with another TRM package.

## Coding

I'll now create a new SAP package and, inside, create an utility class.

<div style="display:flex; gap:12px; flex-wrap:wrap">
  <img src="/_media/2_1_package_with_dependencies.png" alt="Creating a package" style="flex:1 1 300px; max-width:100%; height:auto">
  <img src="/_media/2_2_package_with_dependencies.png" alt="Creating a class" style="flex:1 1 300px; max-width:100%; height:auto">
</div>

Just like last time, let's check what's currently in my workspace:

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_3_package_with_dependencies.png" alt="Current workspace viewed in Eclipse" style="max-width:100%; height:auto; border-radius:8px;">
</div>

And here's the utility class implemented:

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_4_package_with_dependencies.png" alt="Current workspace viewed in Eclipse" style="max-width:100%; height:auto; border-radius:8px;">
</div>

I'll now go back to the `ZCL_TRM_DOCS_SAMPLE` class (which is in SAP package `ZTRM_DOCS_SAMPLE`, TRM package `@trmsamples/doc-demo`) and make use of that utility class

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_5_package_with_dependencies.png" alt="Utility class" style="max-width:100%; height:auto; border-radius:8px;">
</div>

> Even a simple use of another class (in this case creating an instance) is considered a dependency with another object

## Publish with dependency

I'll now try to publish a new release of package `@trmsamples/doc-demo`, as an change to class `ZCL_TRM_DOCS_SAMPLE` was performed.

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_6_package_with_dependencies.png" alt="Failed publish" style="max-width:100%; height:auto; border-radius:8px;">
</div>

...problems! As you can see I got an error message: clearly I messed up!

Like explained earlier, even a simple reference to another class is a dependency with it, and if `ZCL_TRM_DOCS_UTILITY` was within SAP package `ZTRM_DOCS_SAMPLE` I wouldn't have any problem, but as the CLI states, it's in package `ZTRM_DOCS_UTILITY`.

Imagine what would happen if I were to bypass that error: version `1.0.1` of `@trmsamples/doc-demo` would be released and next end user to install it would have a syntax error in class `ZCL_TRM_DOCS_SAMPLE` because `ZCL_TRM_DOCS_UTILITY` (and its package `ZTRM_DOCS_UTILITY`) doesn't exist.

To solve this, we first have to publish `ZTRM_DOCS_UTILITY` (as `@trmsamples/doc-utility`) so that it becomes a TRM package, then retry the publish of `@trmsamples/doc-demo`.

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_7_package_with_dependencies.png" alt="Utility publish" style="max-width:100%; height:auto; border-radius:8px;">
</div>

With `@trmsamples/doc-utility` published, let's now retry the publish of `@trmsamples/doc-demo`.

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_8_package_with_dependencies.png" alt="Successful publish" style="max-width:100%; height:auto; border-radius:8px;">
</div>

There we go! The new release is published. Few things to notice:
- TRM automatically proposed version 1.0.1 -> I didn't specify a version during publish, so patch of the latest version at the time (1.0.0) was incremented by one, generating 1.0.1
- The dependency with another TRM package is picked up -> We'll confirm this in the registry website, but it clearly says "1 TRM package dependency"
- Some values were proposed as defaults, like the SAP package name or the manifest values

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_9_package_with_dependencies.png" alt="Release on registry" style="max-width:100%; height:auto; border-radius:8px;">
</div>

Here's the release on the registry confirming there's a dependency with `@trmsamples/doc-utility`.

## Install with dependencies

Let's start fresh again and install (or update) `@trmsamples/doc-demo` to the latest version (1.0.2), just like an end user would do.

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_10_package_with_dependencies.png" alt="Confirm install dependency" style="max-width:100%; height:auto; border-radius:8px;">
</div>

As you can see the user is first prompted with a confirm on the install of the dependency `@trmsamples/doc-utility`.
Behind the scenes, TRM looked for `@trmsamples/doc-demo` and found out it's not installed on the end user development system.

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_11_package_with_dependencies.png" alt="Install of dependency and package" style="max-width:100%; height:auto; border-radius:8px;">
</div>

After confirm, the install of both packages continued as normal.

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_12_package_with_dependencies.png" alt="List command" style="max-width:100%; height:auto; border-radius:8px;">
</div>

A list command also confirms both packages are installed.

## Publish with SAP entries

On every publish, TRM automatically looks for dependencies with custom packages (and TRM packages) and SAP standard objects.
As such, the SAP standard objects used by a TRM package basically become requirements of the end user development system in order to install the TRM package without any syntax error.
Even a simple use of a standard data element, for example, is a dependency (listed in TRM SAP entries).

To clear things even more, let's publish a new version of `@trmsamples/doc-demo`, this time we're going to use a standard SAP function module call to see what TRM will list in its SAP entries.

<div style="display:flex; justify-content:center;">
  <img src="/_media/2_13_package_with_dependencies.png" alt="List command" style="max-width:100%; height:auto; border-radius:8px;">
</div>

As you can see, I've added a new method which uses the standard SAP function module `SPELL_AMOUNT`.
Let's publish this new release of `@trmsamples/doc-demo`.