# Server setup

**trm-server** is the server-side component of TRM.

It acts as the secure bridge between the **SAP application server** and the **TRM client**.

It exposes the APIs that allow TRM to import and export transports. Consequently, it must be installed **only** on source and target systems; it is not required on any other system in the landscape.

## First Installation

The first installation must be performed using the [standalone installer](https://raw.githubusercontent.com/RegestaItalia/trm-server/refs/heads/main/ztrm_installer.prog.abap).

The **standalone installer** is a self-contained ABAP report that allows the installation of **trm-server** and **trm-rest**.\
The installer imports trm-server transports (and trm-rest transports, if necessary) into your system and automatically moves their objects into the temporary package `$TRM`, which it also creates.\
The installer does not import the **/ATRM/** namespace because trm-server and trm-rest are intended to be used as-is. If you need to modify their objects, consider [installing them via abapGit](#install-with-abapgit) instead.

After the initial installation, we recommend installing subsequent updates through TRM.

1. Download the report source code from [here](https://raw.githubusercontent.com/RegestaItalia/trm-server/refs/heads/main/ztrm_installer.prog.abap)
2. Open transaction `SE38` and create a new report called `ZTRM_INSTALLER`

<p align="center">
    <img src="https://docs.trmregistry.com/server/images/se38_1.png" alt="SE38">
</p>

3. Give it a title and set the type to "Executable program"

<p align="center">
    <img src="https://docs.trmregistry.com/server/images/se38_2.png" alt="SE38">
</p>

4. Save as a local object (or in temporary package `$TMP`)

<p align="center">
    <img src="https://docs.trmregistry.com/server/images/se38_3.png" alt="SE38">
</p>

5. Paste or upload the report's source code, then activate it

<p align="center">
    <img src="https://docs.trmregistry.com/server/images/se38_4.png" alt="SE38">
</p>

### Release file install (From file)

#### Download the releases

1. Go to [https://trmregistry.com](https://trmregistry.com) and search for [trm-server](https://trmregistry.com/package/trm-server)
2. On the release page, select **Download**
3. Download [trm-rest](https://trmregistry.com/package/trm-rest) too, if needed
4. Open SE38 and run `ZTRM_INSTALLER`
5. Select the file(s) downloaded
6. Execute the report and wait for the installation to complete (approximately five minutes)

<p align="center">
    <img src="https://docs.trmregistry.com/server/images/offline.png" alt="ZTRM_INSTALLER">
</p>

<details>
  <summary>Online install (From registry)</summary>

### Online install

The online installation is only possible if your system is allowed to connect to the external server [https://trmregistry.com](https://trmregistry.com).

#### Download the certificate files

*This paragraph is courtesy of abapGit.org*

##### Option A - Chrome

1. Use Google Chrome to go to [https://trmregistry.com](https://trmregistry.com)
2. Select the lock icon near the address bar, then select "Connection is secure"
3. On the Security tab, select "Certificate is valid"
4. Go to the "Details" tab and select "Export..." to download the certificate
5. In the "Certification hierarchy" box, select the parent node of the GitHub certificate and export it as well. Repeat the same with the root node.

<p align="center">
    <img src="https://docs.abapgit.org/img/ssl_setup_chrome.gif" alt="Courtesy of abapGit">
</p>

##### Option B - Firefox

1. Use Firefox to go to [https://trmregistry.com](https://trmregistry.com)
2. Select the lock icon, then "More Information..." and "View Certificate"
3. Switch to the Details tab, choose the first certificate in the hierarchy, and select "Export"
4. Do the same for the next certificate in the hierarchy

##### Option C - Safari

1. Use Safari to go to [https://trmregistry.com](https://trmregistry.com)
2. Select the lock icon and then "View Certificate"
3. In the certificate hierarchy, select the root certificate
4. Holding down the Option key (⌥), drag the large certificate icon into a text editor
5. Save the document as a `.PEM` file

#### Install the Certificate Files

*This paragraph is courtesy of abapGit.org*

1. Open transaction `STRUST`
2. Open the "SSL Client (Anonymous)" folder

<p align="center">
    <img src="https://docs.trmregistry.com/server/images/strust_1.png" alt="STRUST">
</p>

3. Select "Change"
4. In the third box, labeled "Certificate," select "Import certificate" in the bottom-left corner to import the certificate
5. Select "Add to certificate list"
6. Repeat the process for all downloaded certificates

<p align="center">
    <img src="https://docs.trmregistry.com/server/images/strust_2.png" alt="STRUST">
</p>

7. Save

#### Execute TRM Installer online

1. Open SE38 and run `ZTRM_INSTALLER`
2. In the report, configure the connection settings if needed and choose whether to install `trm-rest`
3. Execute the report and wait for the installation to complete (approximately five minutes)

<p align="center">
    <img src="https://docs.trmregistry.com/server/images/online.png" alt="ZTRM_INSTALLER">
</p>

</details>

### Maintain Authorized Users

1.  Execute transaction `SE16`
2.  Create a new record in table `/ATRM/USERS`

> For security reasons, by default, TRM does not allow any user to execute RFC functions unless explicitly authorized.

### Verify RFC Authorization

To verify that a user has access to RFC functions:

1.  Log into the system as the user you want to test
2.  Execute function module `/ATRM/PING`

If the user is authorized, no errors should occur. If not authorized,
access will be denied.

## Install with abapGit

Because this package uses the **/ATRM/** namespace, installation through [abapGit](https://docs.abapGit.org/) requires a system with this namespace installed.

### Demo systems

If you are running a **demo system**, you can use the following keys:

**Development key**: 18531191373370851361\
**Repair key**: 00211665563784583720

### Other systems

For abapGit to work, you need to generate a valid developer key using the [Development Namespace Application](https://me.sap.com/namespaces/opensource).
