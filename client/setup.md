# Client setup

**trm-client** is the client component of TRM.

It acts as the CLI bridge between the **user** and **TRM server**.

---

# Install via Npm

With [Node.js and npm](https://nodejs.org/en/download) installed, you can install [trm-client](https://www.npmjs.com/package/trm-client) via npm, as it is distributed as a Node.js package.

```bash
npm install -g trm-client
```

## Connect to SAP via RFC

If you wish to connect to an SAP system via RFC, install the requirements for [node-rfc](https://github.com/SAP-archive/node-rfc) and execute

```bash
npm install -g node-rfc
```

RFC should now be available as an option when trying to connect to a system.

## Connect to SAP via BTP

If you wish to connect to an SAP system via BTP exposed destination, install the requirements for [trm-plugin-btp-dest](https://github.com/RegestaItalia/trm-plugin-btp-dest) and execute

```bash
npm install -g trm-plugin-btp-dest
```

BTP should now be available as an option when trying to connect to a system.
