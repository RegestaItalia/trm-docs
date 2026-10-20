---
title: Set up TRM Server in SAP
description: Install and configure trm-server in an SAP ABAP system for package publishing, installation, updates, and transport-based removal.
---

# Server setup

**trm-server** is the server-side component of TRM.

It acts as the secure bridge between the **SAP application server** and the **TRM client**.

It exposes the APIs that allow TRM to import and export transports. Consequently, it must be installed **only** on source and target systems; it is not required on any other system in the landscape.

## First Installation

The first installation must be performed using the [standalone installer](https://raw.githubusercontent.com/RegestaItalia/trm-server/refs/heads/main/ztrm_installer.prog.abap).

The **standalone installer** is a self-contained ABAP report that allows the installation of **trm-server** and **trm-rest**.<br>
The installer imports trm-server transports (and trm-rest transports, if necessary) into your system and automatically moves their objects into the temporary package(s) `$TRM`/`$TRM_*`, which it also creates.<br>
The installer does not import the **/ATRM/** namespace because trm-server and trm-rest are intended to be used as-is. If you need to modify their objects, consider [installing them via abapGit](#install-with-abapgit) instead.

After the initial installation, we recommend installing subsequent updates through TRM.

1. Download the report source code from [here](https://raw.githubusercontent.com/RegestaItalia/trm-server/refs/heads/main/ztrm_installer.prog.abap)
2. Open transaction `SE38` and create a new report called `ZTRM_INSTALLER`

<p align="center">
    <img src="../assets/server/se38_1.png" alt="SE38">
</p>

3. Give it a title and set the type to "Executable program"

<p align="center">
    <img src="../assets/server/se38_2.png" alt="SE38">
</p>

4. Save as a local object (or in temporary package `$TMP`)

<p align="center">
    <img src="../assets/server/se38_3.png" alt="SE38">
</p>

5. Paste or upload the report's source code, then activate it

<p align="center">
    <img src="../assets/server/se38_4.png" alt="SE38">
</p>

### Release file install (From file)

#### Download the releases

1. Go to [https://trmregistry.com](https://trmregistry.com) and search for [trm-server](https://trmregistry.com/package/trm-server)
2. On the release page, select **Download**
3. Download [trm-rest](https://trmregistry.com/package/trm-rest) too, if needed
4. Open SE38 and run `ZTRM_INSTALLER`
5. Select the file(s) downloaded
6. Execute the report and wait for the installation to complete (approximately 10 minutes)

<p align="center">
    <img src="../assets/server/offline.png" alt="ZTRM_INSTALLER">
</p>

Installation of either package can be performed at any time through this report. However, you should consider using a TRM client when upgrading `trm-server` or `trm-rest`.

<details>
  <summary>Online install (From registry)</summary><br>
The online installation is only possible if your system is allowed to connect to the external server <a href="https://trmregistry.com">https://trmregistry.com</a>.

<p align="center">
    <img src="../assets/server/online.png" alt="ZTRM_INSTALLER">
</p>

If you see the "Install certificates" button, then your system is missing the required certificates to trust <a href="https://trmregistry.com">https://trmregistry.com</a>.<br>
You should either install them manually (via STRUST) or let the report install them by pressing that button.<br>

Once certificates are installed, you can proceede with the install.

Installation of either package can be performed at any time through this report. However, you should consider using a TRM client when upgrading `trm-server` or `trm-rest`.<br>
</details>

### Authorize Users

Grant each SAP user who needs to use TRM authorization object `ZTRM_AUTH` with activity
`ACTVT = 16` (Execute), typically through an assigned role.

> For security reasons, TRM does not allow a user to execute its functions unless the user has this authorization.

### Verify RFC Authorization

To verify that a user has access to RFC functions:

1.  Log into the system as the user you want to test
2.  Execute function module `/ATRM/PING`

If the user is authorized, no errors should occur. If not authorized,
access will be denied.

## Install with abapGit

Because this package uses the **/ATRM/** namespace, installation through [abapGit](https://docs.abapGit.org/) requires a system with this namespace installed.

Installing via abapGit is **not recommended** unless you are planning to contribute new features or bug fixes.

### Demo systems

If you are running a **demo system**, you can use the following keys:

**Development key**: 18531191373370851361<br>
**Repair key**: 00211665563784583720

### Other systems

For abapGit to work, you need to generate a valid developer key using the [Development Namespace Application](https://me.sap.com/namespaces/opensource).
