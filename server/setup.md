# Server setup

**trm-server** is the server-side component of TRM.

It acts as the secure bridge between the **SAP application server** and the **TRM client**.

It exposes the APIs that allow TRM to import/export transports, and, as a consequence, it must be installed **only** on source and target systems, as its not required on any other system in the landscape.

## First Installation

The first installation must be performed using the [standalone installer](https://raw.githubusercontent.com/RegestaItalia/trm-server/refs/heads/main/ztrm_installer.prog.abap).

The **standalone installer** is a self-contained ABAP report that allows the installation of **trm-server** and **trm-rest**.\
The installer will import trm-server transports (and eventually trm-rest transports too, if needed) into your system and automatically move its objects into the temporary package `$TRM` (which will also be generated).

After the initial installation, it is recommended to install subsequent theit updates via TRM.

1. Download the report source code from [here](https://raw.githubusercontent.com/RegestaItalia/trm-server/refs/heads/main/ztrm_installer.prog.abap)
2. Open transaction `SE38` and create a new report called `ZTRM_INSTALLER`

<p align="center">
    <img src="/server/images/se38_1.png" alt="SE38">
</p>

3. Give it a title and make sure to set the type to "Executable program"

<p align="center">
    <img src="/server/images/se38_2.png" alt="SE38">
</p>

4. Save as a local object (or in temporary package `$TMP`)

<p align="center">
    <img src="/server/images/se38_3.png" alt="SE38">
</p>

5. Copy and paste the source code of the report (or upload) and activate

<p align="center">
    <img src="/server/images/se38_4.png" alt="SE38">
</p>

### Online install

The online installation is only possible if your system is allowed to connect to the external server [https://trmregistry.com](https://trmregistry.com).

#### Download the certificate files

*This paragraph is courtesy of abapGit.org*

##### Option A - Chrome

1. Using Google Chrome to go to [https://trmregistry.com](https://trmregistry.com)
2. Click on the lock icon near the address bar, then click on "Connection is secure"
3. On the Security tab, click on "Certificate is valid"
4. Go to the "Details" tab and select "Export..." to download the certificate to a file
5. In the "Certification hierarchy" box, select the parent node of the GitHub certificate and export it as well. Repeat the same with the root node.

<p align="center">
    <img src="https://docs.abapgit.org/img/ssl_setup_chrome.gif" alt="Courtesy of abapGit">
</p>

##### Option B - Firefox

1. Use Firefox to go to [https://trmregistry.com](https://trmregistry.com)
2. Click on the lock icon and then "More Information ..." and there "View Certificate"
3. Switch to the Details Tab, choose the first certificate of the hierarchy and click Export
4. Do the same for the next certificate in the hierarchy

##### Option C - Safari

1. Use Safari to go to [https://trmregistry.com](https://trmregistry.com)
2. Click on the lock icon and then "View Certificate"
3. In the certificate hierarchy, select the root certificate
4. Holding down the Option key (⌥), drag the large certificate icon into a text editor
5. Save the document as a `.PEM` file

#### Install the Certificate Files

*This paragraph is courtesy of abapGit.org*

1. Install the certificates in transaction `STRUST`:
2. Open the "SSL client Client SSL Client (Anonymous)" folder

<p align="center">
    <img src="/server/images/strust_1.png" alt="STRUST">
</p>

3. Click on the Change button
4. In the third box called "Certificate", click on the bottom-left button "Import certificate" to bring the certificate into the system
5. Select "Add to certificate list"
6. Repeat the process for all downloaded certificates

<p align="center">
    <img src="/server/images/strust_2.png" alt="STRUST">
</p>

7. Save

#### Execute TRM Installer online

1. Open SE38 and run `ZTRM_INSTALLER`
2. In the report you can configure connection settings (if needed) and select/deselect `trm-rest` install
3. Execute

<p align="center">
    <img src="/server/images/online.png" alt="ZTRM_INSTALLER">
</p>

### Offline install

#### Download the releases

1. Go to [https://trmregistry.com](https://trmregistry.com) and search for `trm-server`
2. In the release page, press the **Download** button
3. Download `trm-rest` too, if needed
4. Open SE38 and run `ZTRM_INSTALLER`
5. Open the **Offline** tab and select the file(s) downloaded
6. Execute

<p align="center">
    <img src="/server/images/offline.png" alt="ZTRM_INSTALLER">
</p>

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

Because this package is in namespace **/ATRM/**, install via [abapGit](https://docs.abapgit.org/) needs a system with this namespace installed.

### Demo systems

If you are running a **demo system**, you can use the following keys

**Development key**: 18531191373370851361\
**Repair key**: 00211665563784583720

### Other systems

For abapGit to work, you need to generate a valid developer key using the [Development Namespace Application](https://me.sap.com/namespaces/opensource).
