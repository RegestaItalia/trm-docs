# Engines

The `engines` property of the [manifest](manifest.md) declares **which SAP systems a TRM package can be installed on**: the TRM versions it needs (`trm-core` and `trm-server`), the release and support package of software components, installed products, implemented SAP Notes and, when nothing else fits, the content of standard SAP tables.

Just like `engines.node` in a Node.js `package.json`, engines describe the *environment* the package needs, not other packages.

This page is a hands-on guide to writing `engines` by hand in `manifest.json`.

---

## When engines are checked

- **On install**, before anything is changed on the target system (no transport is created, nothing is locked or imported). If a requirement is not met, the installation is aborted and TRM prints the requirement, the expected value and the value found on the system.
- **For dependencies too**: when a package pulls in dependencies, each dependency's engines are checked when that dependency is installed.

Engines compared with other manifest properties:

| Property | Describes | Example |
|---|---|---|
| [`dependencies`](dependencies.md) | Other **TRM packages** | `"trm-server": "^6.4.1"` |
| [`sap_entries.json`](sap_entries.md) | **Exact rows** that must exist in SAP tables | `TFDIR` row of `CONVERSION_EXIT_ALPHA_INPUT` |
| `engines` | The **SAP system**: releases, SP levels, products, notes, table conditions with operators, and the **TRM versions** used to install | `SAP_BASIS` release `>=750`, `trm-core` `>=9.4.0` |

> ⚠️ **Note**: the check can be skipped at install time, but doing so **may result in syntax errors, dumps or wrong behaviour**, exactly like skipping SAP entries.

---

## Structure at a glance

```json
{
  "name": "my-package",
  "version": "1.0.0",
  "engines": {
    "trm": {
      "trm-core": ">=9.4.0",
      "trm-server": ">=6.4.1"
    },
    "components": {
      "SAP_BASIS": { "release": ">=750", "sp": ">=5" },
      "SAP_GWFND": true,
      "S4CORE": false
    },
    "products": {
      "ABAP PLATFORM": { "version": ">=2022 <=2023" }
    },
    "notes": {
      "3284711": true,
      "1234567": { "version": ">=3" }
    },
    "tables": [
      {
        "table": "SEOCOMPODF",
        "where": [
          { "field": "CLSNAME", "op": "EQ", "value": "/UI2/CL_JSON" },
          { "field": "CMPNAME", "op": "EQ", "value": "VERSION" },
          { "field": "VERSION", "op": "EQ", "value": "1" },
          { "field": "ATTVALUE", "op": "GE", "value": "12" }
        ]
      }
    ],
    "anyOf": [
      { "components": { "UI_700": { "release": "200", "sp": ">=16" } } },
      { "components": { "SAP_UI": { "release": ">=750" } } }
    ]
  }
}
```

Every key is optional. Declare only what your package **really** needs.

### How requirements combine

| Construct | Meaning |
|---|---|
| Top-level keys (`trm`, `components`, `products`, `notes`, `tables`, `anyOf`) | **All** must be satisfied (AND) |
| Entries inside `trm`, `components`, `products`, `notes`, `tables` | **All** must be satisfied (AND) |
| An **array** as the value of a component or product | **At least one** constraint must match (OR) |
| `anyOf: [ {...}, {...} ]` | **At least one** alternative must be satisfied (OR). Each alternative is a full engines object |
| A property that is not declared | Not checked |
| A property inside a constraint that is not declared (e.g. `sp` missing) | Not checked |

`anyOf` alternatives can contain another `anyOf`, up to 3 levels deep.

---

## Range syntax

Releases, SP levels and versions are written as **ranges**, with a syntax close to SemVer ranges (`trm` is the exception: it uses real SemVer ranges, see [below](#trm-trm-versions)):

| Syntax | Meaning | Example |
|---|---|---|
| `value` or `=value` | Exact match | `"758"` |
| `>=value`, `>value`, `<=value`, `<value` | Comparison | `">=750"` |
| `A B` (space) | Both A **and** B | `">=750 <=758"` |
| `A \|\| B` | A **or** B | `"740 \|\| >=752"` |

A space between the operator and the value is allowed (`">= 750"`). Ranges are always **strings** in JSON: write `"758"`, not `758`.

### How values are compared

Each property compares values in its own way:

| Property | Compared as | Notes |
|---|---|---|
| `components.*.release` | **Release** | Numbers are compared numerically (`750 < 758 < 2020`). Alphanumeric releases, such as `SAP_ABA` `75I`, are compared character by character (`0-9` come before `A-Z`, so `758 < 75A < 75I`) when they have the same length. Values that can't be compared (e.g. `DEV` against `2020`) never satisfy the range. |
| `components.*.sp` | **Integer** | `0000000002` on the system is SP `2`. |
| `products.*.version` | **Dotted version** | `7.52 < 2022 < 2023`, `2.0 = 2`. |
| `notes.*.version` | **Integer** | `0009` on the system is version `9`. |

Do **not** strip letters from releases: `75I` is a valid `SAP_ABA` release (and it is newer than `758`).

### Valid and invalid ranges

| Range | Valid? | Why |
|---|---|---|
| `">=750"` | ✅ | |
| `"758"` | ✅ | Exact match |
| `">=750 <=758"` | ✅ | Window |
| `"750 \|\| >=752"` | ✅ | Alternatives |
| `">=75I"` (release) | ✅ | Alphanumeric release |
| `">=7.52"` (product version) | ✅ | Dotted version |
| `758` | ❌ | Must be a string |
| `"^750"`, `"~750"` | ❌ | Caret and tilde are not supported |
| `">=SP05"` (sp) | ❌ | SP levels are plain numbers: `">=5"` |
| `">=2023 FPS01"` (product version) | ❌ | FPS is not a product version, see [below](#feature-package-stacks-fps-and-sp-stacks) |
| `">=750 \|\|"` | ❌ | Empty alternative |

---

## `trm`: TRM versions

Checks the TRM versions involved in the installation. Unlike the other checks, it is not about SAP software but about TRM itself: use it when your package relies on a feature (for example a manifest property or a post activity behaviour) that only exists from a certain TRM version.

```json
"trm": {
  "trm-core": ">=9.4.0",
  "trm-server": "^6.4.1"
}
```

| Key | Checks |
|---|---|
| `trm-core` | The version of **trm-core** running the installation (the one used by TRM Client, TRM GUI or the CI action) |
| `trm-server` | The version of **trm-server** installed on the target system. If trm-server is not installed, the requirement fails |

These are the **only two** keys allowed in `trm`: any other key (for example `trm-client` or `TRM-CORE`) makes the declaration invalid. At least one of the two must be declared.

Values are standard [SemVer ranges](https://github.com/npm/node-semver#ranges), the same used by [`dependencies`](dependencies.md): `^`, `~`, `x` ranges, hyphen ranges and `||` are all allowed. Pre-release versions in use (e.g. `10.0.0-beta.1`) are compared too, so `>=9.4.0` is satisfied by `10.0.0-beta.1`.

### Prefilled on publish

Engines are optional, and when publishing TRM asks whether to declare them (default *no*). If you choose to declare engines for a package that has none yet, `trm` is **already populated** with the trm-core version used to publish, as "this version or newer":

```json
"trm": { "trm-core": ">=9.4.0" }
```

Keep it, raise or relax it, or remove it if your package works with any TRM version. `trm-server` is never prefilled.

### Common mistakes

- Using `trm` for the TRM packages your package calls at runtime: if your ABAP code needs trm-server objects, declare trm-server in [`dependencies`](dependencies.md) instead, so it is installed together with your package. `trm.trm-server` only *checks* the installed version, it never installs it.
- Writing SAP-style ranges such as `">=9.4"`: SemVer accepts partial versions, but write the full version (`">=9.4.0"`) to avoid surprises.

---

## `components`: software components

Checks the software components installed on the system.

```json
"components": {
  "SAP_BASIS": { "release": ">=750", "sp": ">=5" },
  "SAP_GWFND": true,
  "S4CORE": false,
  "SAP_UI": [
    { "release": "750", "sp": ">=17" },
    { "release": ">=752" }
  ]
}
```

| Value | Meaning |
|---|---|
| `true` | The component must be installed, any release |
| `false` | The component must **not** be installed |
| `{ "release": "...", "sp": "..." }` | The component must be installed and match both ranges (either can be omitted) |
| `[ {...}, {...} ]` | The component must be installed and match **at least one** of the constraints |

Component names are case-insensitive (`sap_basis` is stored as `SAP_BASIS`).

### How to find the values on your system

- **System → Status → Component information** (the magnifying glass next to *Product Version*): shows each component with its **Release**, **SP Level** and **Support Package** name.
- Transaction **SPAM → Package level**.
- Transaction **SE16** on table **`CVERS`**:
  - `COMPONENT` is the key you write in `components`.
  - `RELEASE` is compared with `release`.
  - `EXTRELEASE` is the SP level compared with `sp` (`0000000002` is SP `2`).

Example from an ABAP Platform 2023 system:

| COMPONENT | RELEASE | EXTRELEASE |
|---|---|---|
| SAP_BASIS | 758 | 0000000002 |
| SAP_ABA | 75I | 0000000002 |
| SAP_UI | 758 | 0002 |
| S4FND | 108 | 0000000002 |

### Common recipes

Minimum NetWeaver 7.50:

```json
"components": { "SAP_BASIS": { "release": ">=750" } }
```

Exact release with a minimum SP:

```json
"components": { "SAP_BASIS": { "release": "758", "sp": ">=2" } }
```

ECC only (not S/4HANA):

```json
"components": { "S4CORE": false, "SAP_APPL": true }
```

S/4HANA only:

```json
"components": { "S4CORE": true }
```

A minimum SP that depends on the release (a common pattern in SAP Notes):

```json
"components": {
  "SAP_UI": [
    { "release": "750", "sp": ">=17" },
    { "release": "752", "sp": ">=9" },
    { "release": ">=753" }
  ]
}
```

### Common mistakes

- Writing `"sp": ">=SP05"` or `"sp": "SAPK-75005INSAPUI"`: use the plain number, `">=5"`.
- Forgetting newer releases: `{ "release": "750", "sp": ">=17" }` alone **rejects** a 752 system. Add `{ "release": ">=752" }` as an alternative when newer releases are fine.
- A single constraint with `"sp"` but no `"release"`: SP levels restart at every release, so `sp >=5` on its own is rarely what you mean.

---

## `products`: product versions

Checks the product versions installed on the system (table `PRDVERS`, installed versions only).

```json
"products": {
  "ABAP PLATFORM": { "version": ">=2022" },
  "SAP S/4HANA FOUNDATION": true,
  "SLT": false
}
```

| Value | Meaning |
|---|---|
| `true` | The product must be installed, any version |
| `false` | The product must **not** be installed |
| `{ "version": "..." }` | An installed version of the product must match the range |
| `[ {...}, {...} ]` | An installed version must match **at least one** of the constraints |

Product names are case-insensitive and repeated spaces are ignored.

### How to find the values on your system

- **System → Status → Component information → Installed Product Versions** tab.
- Transaction **SE16** on table **`PRDVERS`**:
  - `NAME` is the key you write in `products` (e.g. `ABAP PLATFORM`).
  - `VERSION` is compared with `version` (e.g. `2023`, `7.52`).
  - Only rows with `INSTSTATUS = +` are installed. The table also lists older versions the system was upgraded from, with `-`.

### Feature package stacks (FPS) and SP stacks

The FPS or SP stack of a product ("S/4HANA 2023 **FPS03**") is **not stored** in any table: SAP derives it from the SP levels of the product's software components. For this reason `products` only checks the product version. To require a minimum FPS, write it as the SP level of the product's main component. See [Translating SAP documentation into engines](#translating-sap-documentation-into-engines).

---

## `notes`: SAP Notes

Checks that SAP Notes are implemented with SNOTE (tables `CWBNTCUST` and `CWBNTHEAD`).

```json
"notes": {
  "3284711": true,
  "2934135": { "version": ">=5" }
}
```

| Value | Meaning |
|---|---|
| `true` | The note must be implemented |
| `{ "version": "..." }` | The note must be implemented, and the implemented version must match the range |

A note satisfies the requirement when its implementation status is:

- **Completely implemented** (`E`).
- **Obsolete** (`O`): the correction is already contained in the system's support package level.

Any other status fails the requirement, as does a note that was never downloaded: *Can be implemented* (`N`), *Incompletely implemented* (`U`), *Obsolete version implemented* (`V`), *Cannot be implemented* (`-`).

Note numbers can be written with or without leading zeros (`"0003284711"` is the same as `"3284711"`).

### How to find the values on your system

- Transaction **SNOTE**: the note's *Implementation Status* and *Version*.
- Transaction **SE16** on **`CWBNTCUST`** (`NUMM` is the note number with leading zeros, `PRSTATUS` is the status) and **`CWBNTHEAD`** (`VERSNO` holds the downloaded versions, and the latest one is the implemented version).

### Common mistakes

- **A note that is contained in a support package but was never downloaded** does not appear in SNOTE, so it fails the check. If the correction is also delivered with an SP, accept both paths with `anyOf`:

  ```json
  "anyOf": [
    { "notes": { "3284711": true } },
    { "components": { "SAP_BASIS": { "release": "758", "sp": ">=3" } } }
  ]
  ```

---

## `tables`: table conditions

When no other check fits (a class constant, a system setting, the presence of a standard object), check that **at least one row** of a table matches all the conditions.

```json
"tables": [
  {
    "table": "SEOCOMPODF",
    "where": [
      { "field": "CLSNAME", "op": "EQ", "value": "/UI2/CL_JSON" },
      { "field": "CMPNAME", "op": "EQ", "value": "VERSION" },
      { "field": "VERSION", "op": "EQ", "value": "1" },
      { "field": "ATTVALUE", "op": "GE", "value": "12" }
    ]
  }
]
```

| Property | Required | Description |
|---|---|---|
| `table` | ✅ | Table name (max 30 characters: `A-Z`, `0-9`, `_`, `/`) |
| `where` | ✅ | Non-empty list of conditions, all must match (AND) |
| `where[].field` | ✅ | Field name (max 30 characters: `A-Z`, `0-9`, `_`, `/`) |
| `where[].op` | | One of `EQ` (default), `NE`, `LT`, `LE`, `GT`, `GE`, `LIKE` |
| `where[].value` | ✅ | Value as a string, max 32 characters. Single quotes are escaped automatically. It must not contain ` AND ` or ` OR `. |

With `LIKE`, use the ABAP SQL wildcards `%` (any string) and `_` (any character), e.g. `{ "field": "OBJ_NAME", "op": "LIKE", "value": "/UI2/CL_JSON%" }`.

The requirement **fails** (it is never skipped) when the installing user can't read the table, or when the table doesn't exist.

### Recipes

A class constant with a minimum value, e.g. `/UI2/CL_JSON=>VERSION >= 12`. Class attributes are stored in `SEOCOMPODF`: `CLSNAME` is the class, `CMPNAME` the attribute, `VERSION` `1` the active version, `ATTVALUE` the initial value.

```json
"tables": [{
  "table": "SEOCOMPODF",
  "where": [
    { "field": "CLSNAME", "value": "/UI2/CL_JSON" },
    { "field": "CMPNAME", "value": "VERSION" },
    { "field": "VERSION", "value": "1" },
    { "field": "ATTVALUE", "op": "GE", "value": "12" }
  ]
}]
```

A standard object exists (prefer [`sap_entries.json`](sap_entries.md) for plain existence checks):

```json
"tables": [{
  "table": "TADIR",
  "where": [
    { "field": "PGMID", "value": "R3TR" },
    { "field": "OBJECT", "value": "CLAS" },
    { "field": "OBJ_NAME", "value": "/UI2/CL_JSON" }
  ]
}]
```

A system-wide setting or customizing entry, e.g. currency `EUR` exists:

```json
"tables": [{
  "table": "TCURC",
  "where": [{ "field": "WAERS", "value": "EUR" }]
}]
```

### Common mistakes

- **`GT`/`GE`/`LT`/`LE` on character fields compare text, not numbers.** `ATTVALUE` is a character field, so `'100' GE '12'` is **false** (`'0' < '2'`) and `'9' GE '12'` is **true**. This is fine while the values have the same number of digits (`12` to `99`). If the value can grow to more digits, list the accepted values with `anyOf`, or use `LIKE`.
- Lowercase or quoted values: write the value as it is stored in the table, without quotes. `'` is escaped for you.
- Using `tables` for software components or notes: use `components` and `notes` instead. Their results are clearer and they compare releases correctly.

---

## Translating SAP documentation into engines

### From a support package name

SAP documentation often lists minimum support packages by name, e.g. `SAPK-75017INSAPUI`:

| Part | Meaning |
|---|---|
| `SAPK-` | Support package prefix |
| `750` | Component release |
| `17` | Support package level |
| `INSAPUI` | "in component SAP_UI" |

This becomes:

```json
"components": { "SAP_UI": { "release": "750", "sp": ">=17" } }
```

Other examples: `SAPK-20016INUI700` → `UI_700` release `200` sp `>=16`, and `SAPKB75017` → `SAP_BASIS` release `750` sp `>=17`.

### From a product version and FPS

Product versions map to a main software component. The FPS or SP stack is that component's SP level:

| Product version | Main component and release |
|---|---|
| SAP S/4HANA 2020 | `S4CORE` `105` |
| SAP S/4HANA 2021 | `S4CORE` `106` |
| SAP S/4HANA 2022 | `S4CORE` `107` |
| SAP S/4HANA 2023 | `S4CORE` `108` |
| ABAP Platform 2022 | `SAP_BASIS` `757` |
| ABAP Platform 2023 | `SAP_BASIS` `758` |
| SAP NetWeaver 7.50 | `SAP_BASIS` `750` |

Always double-check the mapping and the SP level in the SAP release information of the FPS, or in **Component information** on a system at that level.

Example: *"S/4HANA from 2020 FPS02 up to 2023 FPS03"*:

```json
"components": {
  "S4CORE": [
    { "release": "105", "sp": ">=2" },
    { "release": ">=106 <=107" },
    { "release": "108", "sp": "<=3" }
  ]
}
```

To only require the product version, without the FPS:

```json
"products": { "SAP S/4HANA FOUNDATION": { "version": ">=2020 <=2023" } }
```

### Case study: a library with a minimum SP table

Suppose a library's documentation says:

> Requires one of the following minimum support packages:
>
> | Software Component | Release | Minimum Support Pack |
> |---|---|---|
> | UI_700 | 200 | SAPK-20016INUI700 |
> | SAP_UI | 750 | SAPK-75016INSAPUI |
> | SAP_UI | 752 | SAPK-75209INSAPUI |
> | SAP_UI | 753 | SAPK-75306INSAPUI |
> | SAP_UI | 754 | SAPK-75402INSAPUI |
>
> and `/UI2/CL_JSON` version 12 or higher.

**Step 1: decode each support package** into component, release and SP (see [above](#from-a-support-package-name)).

**Step 2: group rows by component.** Several releases of the same component become one array (OR):

```json
"SAP_UI": [
  { "release": "750", "sp": ">=16" },
  { "release": "752", "sp": ">=9" },
  { "release": "753", "sp": ">=6" },
  { "release": "754", "sp": ">=2" }
]
```

**Step 3: decide about newer releases.** The table stops at 754, but a 755+ system already contains the fix. Add `{ "release": ">=755" }`, or the package won't install on newer systems.

**Step 4: rows for different components are alternatives**, so use `anyOf`.

**Step 5: add the class constant** as a `tables` check. It is at the top level, so it is required in every case.

Result:

```json
"engines": {
  "anyOf": [
    { "components": { "UI_700": { "release": "200", "sp": ">=16" } } },
    {
      "components": {
        "SAP_UI": [
          { "release": "750", "sp": ">=16" },
          { "release": "752", "sp": ">=9" },
          { "release": "753", "sp": ">=6" },
          { "release": "754", "sp": ">=2" },
          { "release": ">=755" }
        ]
      }
    }
  ],
  "tables": [{
    "table": "SEOCOMPODF",
    "where": [
      { "field": "CLSNAME", "value": "/UI2/CL_JSON" },
      { "field": "CMPNAME", "value": "VERSION" },
      { "field": "VERSION", "value": "1" },
      { "field": "ATTVALUE", "op": "GE", "value": "12" }
    ]
  }]
}
```

If only `SAP_UI` matters to you (no `UI_700` systems), drop `anyOf` and keep `components.SAP_UI` at the top level.

### Nested alternatives

*"Either S/4HANA with S/4HANA Foundation 2021 or later, or ECC EHP8 SP10 or later"*:

```json
"engines": {
  "anyOf": [
    {
      "components": { "S4CORE": true },
      "products": { "SAP S/4HANA FOUNDATION": { "version": ">=2021" } }
    },
    {
      "components": { "S4CORE": false, "SAP_APPL": { "release": "618", "sp": ">=10" } }
    }
  ]
}
```

---

## Validation and errors

### On publish

The registry rejects a package whose engines are not formally valid. The error names the path of the first problem, for example:

| Error | Cause |
|---|---|
| `The engines declaration is invalid: engines.component: unknown engine check.` | Typo in a top-level key (`component` instead of `components`) |
| `...: engines.components.SAP_BASIS: unknown property "patch".` | Only `release` and `sp` are allowed |
| `...: engines.trm.trm-client: unknown TRM package, expected one of trm-core, trm-server.` | `trm` only accepts `trm-core` and `trm-server`. This is an error even outside publish |
| `...: engines.trm.trm-core: invalid range "abc".` | The value is not a valid SemVer range |
| `...: engines.components.SAP_BASIS.release: invalid range "750".` | The range is a number instead of a string, or has an invalid syntax |
| `...: engines.notes.abc: invalid SAP Note number.` | Note numbers are digits only |
| `...: engines.tables[0].where[0].op: invalid operator "IN", ...` | Unsupported operator |
| `...: engines.tables[0].where[0].value: expected a string (max 32 characters).` | The value is too long, or not a string |
| `...: engines.anyOf: maximum nesting depth (3) exceeded.` | Too many nested `anyOf` |

Structural errors (for example a range that isn't a string) are already reported locally when the manifest is read, as `Invalid engines declaration: ...`.

### On install

Each requirement is evaluated and reported:

```
Engine requirement trm.trm-core not met: expected version >=10.0.0, found version 9.4.0
Engine requirement components.SAP_BASIS not met: expected release >=758, found release 750, sp 12
Engine requirement tables[0] not met: expected SEOCOMPODF where CLSNAME EQ '/UI2/CL_JSON' AND ... (Cannot read table SEOCOMPODF: ...)
Install aborted. 3 engine requirements are not met!
```

In the error messages, requirements inside `anyOf` alternatives are reported only through their `anyOf`, which fails when no alternative is satisfied. The detailed results (including every alternative) are available in the install log.

### Forward compatibility

New kinds of checks may be added to engines in the future. If a package declares a check that your TRM version doesn't know, the installation **fails** with `Unsupported engine check "<name>", update TRM to verify it`, because a requirement that can't be verified is never treated as met. Update TRM to install the package.

---

## Authorizations

The engines check reads tables with the installing user. The user needs read access to:

- the trm-server objects (`TADIR` and the trm-server API) for `trm.trm-server`
- `CVERS` for `components`
- `PRDVERS` for `products`
- `CWBNTCUST` and `CWBNTHEAD` for `notes`
- every table named in `tables`

If a table can't be read, the requirement is reported as not met, with the reason, and the installation stops.

---

## Cheat sheet

| I need... | Engines |
|---|---|
| trm-core 9.4.0 or later | `"trm": { "trm-core": ">=9.4.0" }` |
| trm-server 6.x, from 6.4.1 | `"trm": { "trm-server": "^6.4.1" }` |
| NetWeaver 7.50 or later | `"components": { "SAP_BASIS": { "release": ">=750" } }` |
| ABAP Platform 2023 SP02 or later | `"components": { "SAP_BASIS": [{ "release": "758", "sp": ">=2" }, { "release": ">=759" }] }` (with `{ "release": ">=758", "sp": ">=2" }` alone, a newer release at SP00/SP01 would be rejected, because `release` and `sp` must both match) |
| NetWeaver 7.40 up to 7.58 | `"components": { "SAP_BASIS": { "release": ">=740 <=758" } }` |
| S/4HANA only | `"components": { "S4CORE": true }` |
| ECC only | `"components": { "S4CORE": false, "SAP_APPL": true }` |
| Gateway installed | `"components": { "SAP_GWFND": true }` |
| ABAP Platform 2022 or later | `"products": { "ABAP PLATFORM": { "version": ">=2022" } }` |
| SAP Note implemented | `"notes": { "3284711": true }` |
| SAP Note, version 5 or later | `"notes": { "3284711": { "version": ">=5" } }` |
| Note **or** the SP that contains it | `"anyOf": [{ "notes": { "3284711": true } }, { "components": { "SAP_BASIS": { "release": "758", "sp": ">=3" } } }]` |
| Class constant ≥ value | `"tables": [{ "table": "SEOCOMPODF", "where": [{ "field": "CLSNAME", "value": "<CLASS>" }, { "field": "CMPNAME", "value": "<CONSTANT>" }, { "field": "VERSION", "value": "1" }, { "field": "ATTVALUE", "op": "GE", "value": "<MIN>" }] }]` |
