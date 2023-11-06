# trm-client Requirements

This documentation will guide you through the installation of the required software in order to run trm-client.

## Node.Js & Npm

To install both NodeJs and npm, follow [this guide](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm#using-a-node-version-manager-to-install-nodejs-and-npm).


After installing NodeJs and npm, make sure to have the following environment variable set in your system:
- Windows

    - [Open the Enviroment Variables settings and view the PATH variable](https://learn.microsoft.com/en-us/previous-versions/office/developer/sharepoint-2010/ee537574(v=office.14))

    - Check if the path `C:\Users\<<YOUR_USER>>\AppData\Roaming\npm` is in the list, if not, add it

Running the command `npm` in your system CLI should output all of the possible commands.

## SAP NW RFC SDK
TRM Client communicates with SAP systems through RFC.

For this reason, it's necessary to have the RFC SDK installed on your system.

A guide on installing the SDK can be found [here](https://github.com/SAP/node-rfc/blob/main/doc/installation.md#sap-nwrfc-sdk-installation).

To sum up the installation:

- Download the RFC SDK from the SAP® Support Portal (follow the updated link of the note in [this section](https://support.sap.com/en/product/connectors/nwrfcsdk.html?anchorId=section_1291717368))

> **TRM DOESN'T PROVIDE THE REQUIRED SDK, IT CAN AND SHOULD ONLY BE DOWNLOADED FROM OFFICIAL SOURCES**

- On Windows
    - Create the folder `C:\nwrfcsdk`
    - Place the content downloaded into this folder (extract if needed)

    - Make sure `C:\nwrfcsdk\bin` exists

    - Make sure the libraries are also included in the bin folder (`C:\nwrfcsdk\bin\icudt50.dll` ...), if not, copy the content of the folder `C:\nwrfcsdk\bin\lib` into `C:\nwrfcsdk\bin`

    - Running the command `rfcexec` through cmd, in the folder `C:\nwrfcsdk\bin`, should list the mandatory fields of the command

    - Create an enviroment variable named `SAPNWRFC_HOME`, with the path `C:\nwrfcsdk`

    - Add `C:\nwrfcsdk\lib` to the PATH variable (same procedure done earlier for checking the npm install)

## R3Trans program

For this step, installing [SAP NW RFC SDK](#SAP-NW-RFC-SDK) is necessary.

The R3Trans program is used by TRM Client to unpack the packages downloaded from a registry.

For this reason, it's necessary to have the R3Trans program on your system.

A guide on installing the program can be found [here](https://github.com/RegestaItalia/node-r3trans#installation) (The command `npm install node-r3trans` should be skipped from the linked guide).

To sum up the installation:

- Download the RFC SDK from [SAP® Software Download Center](https://support.sap.com/en/my-support/software-downloads.html)

> **TRM DOESN'T PROVIDE THE R3TRANS PROGRAM, IT CAN AND SHOULD ONLY BE DOWNLOADED FROM OFFICIAL SOURCES**

- On Windows

    - Create the folder `C:\R3Trans`

    - Place the content downloaded into this folder (extract if needed)

    - Make sure `C:\R3Trans\R3trans.exe` exists

    - Make sure `C:\nwrfcsdk\lib` is in the list of your PATH enviroment variable

    - Running the command `R3trans` through cmd, in the folder `C:\R3Trans`, should list possible commands

    - Create an enviroment variable named `R3TRANS_HOME`, with the path `C:\R3Trans`

# trm-client Install

For this step, installing [all of the requirements](#trm-client-requirements) is necessary.

Before executing this step, it's recommended to close and reopen the CLI (if the same instance was used for setting environment variables, they might be ineffective until reloading).

Run this command in your system CLI:

`npm install trm-client -g`

this will install the [trm-client package](https://www.npmjs.com/package/trm-client) in your system.

If all of the requirements are met, running the command

`trm`

in your CLI should output all of the possible commands.

# Virtual System (Recommended)

It's highly recommended to make use of Virtual Systems in order to release transports without worrying about leaving them in queues.

Ideally, you should setup the Virtual System on your central development system, and every time you publish, the Virtual System should be targeted.

Here's a guide on how to [setup a Virtual System](https://help.sap.com/doc/saphelp_nw73ehp1/7.31.19/en-us/44/b4a0db7acc11d1899e0000e829fbbd/content.htm?no_cache=true).

The setup should be performed by your BASIS team.