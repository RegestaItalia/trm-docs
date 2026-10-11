# SAP Entries

The `sap_entries.json` file (formerly the `sapEntries` property in the manifest) is used to declare necessary SAP system entries that must exist to avoid runtime or syntax errors.

These entries typically reference dependencies on **standard SAP objects**, which lack versioning and therefore cannot be tracked like custom TRM packages.

## Why SAP Entries are needed

Standard SAP objects (e.g., function modules, function groups) cannot be versioned or bundled directly in a TRM package. To ensure a TRM package works correctly when it relies on SAP-delivered functionality, you must declare such dependencies explicitly using `sap_entries.json`.

---

## Example scenario

Suppose you're publishing a package that uses the standard function module `CONVERSION_EXIT_ALPHA_INPUT`, which belongs to the function group `ALFA`.

To indicate this dependency, you can define the `sap_entries.json` file as follows:

```json
{
  "TADIR": {
    "PGMID": "R3TR",
    "OBJECT": "FUGR",
    "OBJ_NAME": "ALFA"
  }
}
```

or even more precisely:

```json
{
  "TFDIR": {
    "FUNCNAME": "CONVERSION_EXIT_ALPHA_INPUT",
    "PNAME": "SAPLALFA"
  }
}
```

Before installing a TRM package, the system will verify whether the SAP entries declared in `sap_entries.json` exist in the target system. If any are missing, the installation may be aborted to prevent unstable or broken behavior.

> ⚠️ **Note**: This verification can be skipped by the user, but doing so **may result in inconsistencies or runtime errors**.

> For best results, always declare critical SAP dependencies explicitly in `sap_entries.json`.