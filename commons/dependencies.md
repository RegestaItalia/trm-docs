# Dependency recognition

TRM is capable to automatically detect the necessary TRM package dependencies in order to avoid syntax and runtime errors.

This automatic recognition is subject to the type of objects used inside of the package.

Support for more object types can be requested with and issue [here](https://github.com/RegestaItalia/trm-core/issues).

| Object | Supported | Notes |
| ------ | --------- | ----- |
| CLAS   | Yes       |       |
| DTEL   | Yes       |       |
| FUGR   | Yes       |       |
| PROG   | Yes       |       |
| TABL   | Yes       |       |
| VIEW   | Yes       |       |
| VIEW   | Yes       |       |

## SAP Objects

Whenever a dependency with an object is detected and its package is standard (SAP), the dependency will be included in the TADIR SAP entries requirements.