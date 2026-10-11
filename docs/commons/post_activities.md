# Post Activities

When a TRM package is published, the publisher can define a set of **post-install activities** to be automatically executed after the package is installed.

These post activities run ABAP code directly on the **target system** (the system where the package is installed) and are useful for tasks such as:

- Client-dependent customizing
- Cache clearing or refreshing

To avoid redundant executions, each post activity typically includes a **pre-check**.

> ⚠️ **Post activities do not support rollback or uninstall.** They are intended
> for actions that run after installation and should not generate persistent
> objects or other content that would need to be removed if the package is rolled
> back or uninstalled. Keep them safe to repeat and limited to operations that do
> not require a compensating cleanup action.

They are defined in the `manifest.json` file and each entry in `postActivities` includes:
- `name`: The name of the ABAP class implementing the post activity
- `parameters`: A list of key-value (name and value) pairs passed to the class

Example:

```json
"postActivities": [
  {
    "name": "ZCL_MY_CUSTOM_TRM_PA",
    "parameters": [
      {
        "name": "ARG",
        "value": "SOME VALUE"
      }
    ]
  }
]
```

---

## Standard Post Activities

TRM provides several standard post activities that can be used out of the box.

### Activate SICF Node

The `/ATRM/CL_PA_ACTIVATE_SICF_NODE` post activity activates a SICF service node
if it is not already active.

#### Expected Parameters

| Parameter  | Required | Description                  |
|------------|----------|------------------------------|
| `url`      | **Yes**  | URL of the SICF service node |
| `hostname` | **Yes**  | SICF host name               |

---

### Regenerate SAP_ALL

The `/ATRM/CL_PA_SAP_ALL_REGEN` post activity regenerates the `SAP_ALL` profile
for all clients. It does not require any parameters.

---

### UI5 Fiori Cache Cleanup

The `ZCL_TRM_PA_FIORI_CACHE_CLEANUP` post activity is used to **clear the Fiori UI5 cache**, especially useful if the TRM package includes a BSP application.

#### Expected Parameters

| Parameter         | Required | Description                        |
|-------------------|----------|------------------------------------|
| `ui5_repository`  | No       | Name of the BSP application        |

---

## Custom Post Activities

You can define **custom post activities** in your TRM package. It's the publisher's responsibility to:

- Include the ABAP class definition within the package, or
- Declare it as a dependency in the manifest.

> ⚠️ TRM does not validate the content of custom post activities — end users must ensure they are safe.

### Requirements for a Custom Post Activity Class

- A constant flag `TRM_PA` must be defined in the public section:

```abap
CONSTANTS trm_pa TYPE flag VALUE 'X' ##NO_TEXT.
```

- A static method `EXECUTE` is required. If it includes `EXPORTING messages TYPE symsg_tab`, those messages will be shown to the user after execution.

- An optional static method `PRE` can check whether the post activity needs to
  run. It must return `execute TYPE flag`; TRM calls `EXECUTE` only when this is
  set to `'X'`. If `PRE` is not defined, the post activity runs by default. The
  method can accept the same manifest parameters as `EXECUTE` and can optionally
  return messages.

```abap
CLASS-METHODS pre
  IMPORTING
    !arg      TYPE ty_nrfrom OPTIONAL
  EXPORTING
    !execute  TYPE flag
    !messages TYPE symsg_tab.
```

### Sample Implementation

```abap
CLASS zcl_my_custom_trm_pa DEFINITION
  PUBLIC
  FINAL
  CREATE PUBLIC.

  PUBLIC SECTION.

    CONSTANTS trm_pa TYPE flag VALUE 'X' ##NO_TEXT.

    CLASS-METHODS execute
      IMPORTING
        !arg      TYPE ty_nrfrom OPTIONAL
      EXPORTING
        !messages TYPE symsg_tab.

  PROTECTED SECTION.
  PRIVATE SECTION.
ENDCLASS.

CLASS zcl_my_custom_trm_pa IMPLEMENTATION.

  METHOD execute.
    DATA: lv_message TYPE string,
          ls_message LIKE LINE OF messages.

    lv_message = 'Executed custom post activity!'.
    cl_message_helper=>set_msg_vars_for_clike( lv_message ).
    MOVE-CORRESPONDING sy TO ls_message.
    ls_message-msgty = 'S'.
    APPEND ls_message TO messages.
  ENDMETHOD.

ENDCLASS.
```

---

For reusable actions, consider creating a library of post activities shared across packages.
