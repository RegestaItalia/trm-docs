# Dependency Recognition

TRM can automatically detect the dependencies required by a TRM package to prevent syntax and runtime errors.

This detection is based on the types of objects used within the package. As support for additional object types may be needed over time, you can request support by opening an [incident](/incidents.md)

## Supported Object Types

This list includes objects that were tested. Other object types may also be supported, but no tests were performed.

| Object | Supported | Notes |
|--------|-----------|-------|
| CLAS   | ✅ Yes   |       |
| DTEL   | ✅ Yes   |       |
| FUGR   | ✅ Yes   |       |
| PROG   | ✅ Yes   |       |
| TABL   | ✅ Yes   |       |
| VIEW   | ✅ Yes   |       |

## SAP Objects

If a dependency is identified and the referenced object belongs to a **standard SAP package**, TRM includes the requirement as part of the **TADIR SAP entries**. This ensures that references to standard objects are properly managed without bundling SAP-owned code.