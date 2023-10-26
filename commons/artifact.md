# TRM Artifact

A TRM artifact is a file with extension `.trm`.

It's an archive that bundles **transports** and the package **manifest**.

A typical artifact structure might look something like this:

```
├── dist
│   ├── TRMK100001
│   │   ├── K100001.TRM
│   │   ├── R100001.TRM
│   ├── TRMK100002
│   │   ├── K100002.TRM
│   │   ├── R100002.TRM
├── manifest.json
```

# Transport types

Transports are marked with different types in order to have a more specific publish/install procedure.

## DEVC

A DEVC transport contains R3TR objects of type DEVC.

This type of transports is not imported by TRM because it only contains devclasses, which are instead generated.

## TADIR

A TADIR transport contains all of the objects of a package (and its subpackages) excluding DEVCs (included in [DEVC](#devc)).

Transports also include two comments (object type **ZTRM**) that indicate the package manifest keys (name and version).