# Publish and Install

In this guide, we’ll walk through how to **publish and install** a simple TRM package.

## Coding

Let’s start by creating a new SAP package called `ZTRM_DOCS_SAMPLE`, and inside it, a class named `ZCL_TRM_DOCS_SAMPLE`.  
This will be the initial content of our TRM package.

<div style="display:flex; gap:12px; flex-wrap:wrap">
  <img src="/_media/1_1_publish_and_install.png" alt="Creating a package" style="flex:1 1 300px; max-width:100%; height:auto">
  <img src="/_media/1_2_publish_and_install.png" alt="Creating a class" style="flex:1 1 300px; max-width:100%; height:auto">
</div>

With `trm-server` installed, this is my current workspace:

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_3_publish_and_install.png" alt="Current workspace viewed in Eclipse" style="max-width:100%; height:auto; border-radius:8px;">
</div>

> Notice that my package name starts with “Z”.  
> TRM doesn’t work with temporary packages because it needs **transportable objects**.  
> You can use the “Z” namespace or other development namespaces such as “Y” or “/MYCOMPANY/”.

Now I’ll add a simple method, just to have something inside.

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_4_publish_and_install.png" alt="Adding a method" style="max-width:100%; height:auto; border-radius:8px;">
</div>

That’s it! I’m done coding and ready to make my first release. 🥳

## Publish

We’ll publish to the [public registry](https://trmregistry.com), which is the default registry included with TRM.

> When you create a release, you’re essentially **freezing the current state** of your package.  
> Each release acts as a snapshot, often bundled with a changelog or documentation so users know what’s included in that version.

To publish there, you need to be logged in first, so let’s do that:

```bash
trm login
```

> “public registry” simply means that anyone can browse it.  
> It doesn’t mean your package will automatically be visible to everyone (you’ll choose that during publish).

Now let’s publish our package using the command:

```bash
trm publish @trmsamples/doc-demo
```

> The scope `@trmsamples` corresponds to an organization named “trmsamples”.  
> If the organization doesn’t exist or you’re not a member, you’ll get an error during publishing.

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_5_publish_and_install.png" alt="Connection to SAP" style="max-width:100%; height:auto; border-radius:8px;">
</div>

TRM now asks how to connect to your SAP development system.  
I’ve already created an alias for mine, so connecting is quick.

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_6_publish_and_install.png" alt="Version proposal" style="max-width:100%; height:auto; border-radius:8px;">
</div>

Since I didn’t specify a version, TRM automatically proposes `1.0.0`.

> To explicitly set a version, run:  
> `trm publish <package name> [version]`

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_7_publish_and_install.png" alt="Package visibility" style="max-width:100%; height:auto; border-radius:8px;">
</div>

Next, TRM asks if I want to **restrict access** to specific users or make the package **publicly available**.  
For this demo, I’ll choose **public**.

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_8_publish_and_install.png" alt="Transport targets" style="max-width:100%; height:auto; border-radius:8px;">
</div>

TRM then lists all transport targets.  
When publishing, a certain number of transports are generated and released automatically to the selected target.  

If possible, create a **virtual system** so TRM can release everything without worrying about transport targets.  
Otherwise, just choose your development or another available system.

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_9_publish_and_install.png" alt="SAP Package name" style="max-width:100%; height:auto; border-radius:8px;">
</div>

When asked for the ABAP package, I’ll select the one created earlier.

> After entering the package name, TRM automatically checks for dependencies with other TRM packages, custom objects, and SAP objects.

I’ll now fill in a few optional **manifest fields**, such as a short description, license, and publisher details.

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_10_publish_and_install.png" alt="Optional steps" style="max-width:100%; height:auto; border-radius:8px;">
</div>

TRM then offers more optional steps, like editing dependencies, post install activities, or customizing.  
We’ll explore these in another example.

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_11_publish_and_install.png" alt="Package published" style="max-width:100%; height:auto; border-radius:8px;">
</div>

The green message confirms the package was successfully published!  
You can also check it on the registry website:  
[trmregistry.com/package/@trmsamples/doc-demo](https://trmregistry.com/package/@trmsamples/doc-demo)

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_12_publish_and_install.png" alt="Package viewed in registry" style="max-width:100%; height:auto; border-radius:8px;">
</div>

## Install

Now let’s start fresh: I'm an end user who wants to install the `@trmsamples/doc-demo` package.

> I’m using A4H (ABAP Developer Trial).  
> Even though the SID remains A4H, this is a clean system: everything from before is gone.

First, let’s see which packages are currently installed in the development system:

```bash
trm list
```

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_13_publish_and_install.png" alt="List installed packages" style="max-width:100%; height:auto; border-radius:8px;">
</div>

As you can see, only `trm-server` is installed, which confirms we’re starting from a blank setup.

> `trm-server` is required only in development systems.  
> In quality or production systems, transports are handled manually, the old-fashioned way.

Now let’s install our package:

```bash
trm install @trmsamples/doc-demo
```

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_14_publish_and_install.png" alt="Install command" style="max-width:100%; height:auto; border-radius:8px;">
</div>

You may notice I didn’t specify a version or tag, so TRM automatically picks the latest release.

At this point, TRM asks how I want to name the SAP package in my system, and proposes the original name chosen by the publisher.

> Just like with abapGit, the SAP package name isn’t fixed and can be changed by the end user.

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_15_publish_and_install.png" alt="Install success" style="max-width:100%; height:auto; border-radius:8px;">
</div>

Once again, the green message confirms a successful installation!  
Let’s verify it by listing and viewing the installed packages:

```bash
trm list
trm view @trmsamples/doc-demo
```

<div style="display:flex; justify-content:center;">
  <img src="/_media/1_16_publish_and_install.png" alt="List and view commands" style="max-width:100%; height:auto; border-radius:8px;">
</div>

We can now take it to the next step: let’s see how TRM handles dependencies!

➡️ Next: [Package with dependencies](/examples/2_package_with_dependencies.md)