# Client setup

**trm-client** is the client component of TRM.

It acts as the CLI bridge between the **user** and **TRM server**.

---

# Install via npm

After installing [Node.js and npm](https://nodejs.org/en/download), install [trm-client](https://www.npmjs.com/package/trm-client) from npm:

```bash
npm install -g trm-client
```

## Connect to SAP via RFC

To connect to an SAP system through RFC, install the prerequisites for [node-rfc](https://github.com/SAP-archive/node-rfc), then run:

```bash
npm install -g node-rfc
```

RFC should now be available as an option when trying to connect to a system.

## Connect to SAP via BTP

To connect to an SAP system through a destination exposed by SAP BTP, install the prerequisites for [trm-plugin-btp-dest](https://github.com/RegestaItalia/trm-plugin-btp-dest), then run:

```bash
npm install -g trm-plugin-btp-dest
```

BTP should now be available as an option when trying to connect to a system.
