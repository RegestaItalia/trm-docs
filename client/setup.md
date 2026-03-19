# Client setup

**trm-client** is the client component of TRM.

It acts as the CLI bridge between the **user** and **TRM server**.

---

# Dockerized version (Recommended)

If you are using [Docker](https://www.docker.com/), the recommended approach is to use [trm-docker](https://github.com/RegestaItalia/trm-docker).

## Download Docker Run Script

This script is a small utility used to run TRM inside Docker. After installing the required SAP proprietary tools, the script can be moved into a directory included in your `PATH` so that it can be executed from anywhere.

1. Go to the [trm-docker repository](https://github.com/RegestaItalia/trm-docker)
2. Download the script corresponding to your operating system:
   - **Windows**: download [win.cmd](https://raw.githubusercontent.com/RegestaItalia/trm-docker/refs/heads/main/win.cmd) and rename it to `trm.cmd`
   - **macOS / Linux**: download [macos](https://raw.githubusercontent.com/RegestaItalia/trm-docker/refs/heads/main/macos), rename it to `trm`, and make it executable:
     ```bash
     chmod +x trm
     ```
3. In the same directory where you placed the script, create a folder named `init`.

This `init` folder will later contain the SAP proprietary files required by TRM.

## Download SAPCAR and SAPEXE and Extract Required Files

SAPCAR is used to extract `.SAR` archives downloaded from SAP Software Center.

### Download SAPCAR

1. Log in to the [SAP Software Center](https://me.sap.com/softwarecenter)
2. Click **SUPPORT PACKAGES & PATCHES**
3. Expand **By Alphabetical Index (A–Z)** and select **S**
4. Click **SAPCAR**
5. Choose the **latest version**
6. On the download page select your operating system:
   - **WINDOWS ON X64 64BIT**
   - **MACOS ON ARM64BIT**
   - **MACOS X 64-BIT**
7. Download:
   - **Windows** → latest `.EXE`
   - **macOS** → latest `.ZIP`
8. If using macOS, extract the archive and make the binary executable:
   ```bash
   chmod +x SAPCAR
   ```

### Download SAP Kernel Files

1. Go back to **SUPPORT PACKAGES & PATCHES**
2. Expand **By Alphabetical Index (A–Z)** and select **K**
3. Click **SAP KERNEL 64-BIT**
4. Choose the **latest version**
5. On the download page select **LINUX ON X86_64 64BIT**
6. Download the latest **SAPEXE** archive  
   (file name similar to `SAPEXE_###-########.SAR`)

### Extract the Required Files

1. Place the downloaded `SAPEXE_*.SAR` file in the same directory as `SAPCAR`.
2. Extract it:

   **Windows**
   ```bash
   SAPCAR -xvf SAPEXE_###-########.SAR
   ```

   **macOS / Linux**
   ```bash
   ./SAPCAR -xvf SAPEXE_###-########.SAR
   ```

3. After extraction, move the following files into the previously created `init` folder:

   ```
   R3trans
   libicudata##.so
   libicui18n##.so
   libicuuc##.so
   ```

4. *(Optional)* If you want RFC functionality available in TRM, also move the following files into the `init` folder:

   ```
   startrfc
   rfcexec
   libsapnwrfc.so
   libsapucum.so
   ```

# Pull docker image

With Docker running on your system, pull the [abaptrm/docker](https://hub.docker.com/r/abaptrm/docker) image:
```bash
docker pull --platform=linux/amd64 abaptrm/docker
```

# Initial Installation via Script

Once the `init` folder is populated, docker image is pulled and the `trm` script is ready, run the script from the directory where it is located.

**Windows**
```bash
trm
```

**macOS / Linux**
```bash
./trm
```

The first execution performs the initial setup of the Docker environment.\
After the installation completes, you may move the script to a directory included in your system `PATH` so it can be executed from anywhere.

**Windows**
```
C:\Windows\System32
```

**macOS / Linux**
```
/usr/local/bin
```

After this step, you can simply run:

```bash
trm
```

from any directory.

---

# Install via Npm

With [Node.js and npm](https://nodejs.org/en/download) installed, you can install [trm-client](https://www.npmjs.com/package/trm-client) via npm, as it is distributed as a Node.js package.

## TODO
