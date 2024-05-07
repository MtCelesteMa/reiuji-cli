# Reiuji CLI

**Usage**:

```console
$ reiuji [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.

**Commands**:

* `convert`: Commands for converting JSON blueprints to...
* `design`: Commands for invoking Reiuji's Designer.
* `list`: List the components for a multiblock.

## `reiuji convert`

Commands for converting JSON blueprints to .schematic files.

**Usage**:

```console
$ reiuji convert [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `overhauled`: Commands for converting NuclearCraft:...
* `qmd`: Commands for converting QMD blueprints.

### `reiuji convert overhauled`

Commands for converting NuclearCraft: Overhauled blueprints.

**Usage**:

```console
$ reiuji convert overhauled [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `turbine`: Convert a NuclearCraft: Overhauled turbine...

#### `reiuji convert overhauled turbine`

Convert a NuclearCraft: Overhauled turbine blueprint to a .schematic file.

**Usage**:

```console
$ reiuji convert overhauled turbine [OPTIONS] ROTOR_FILE DYNAMO_FILE
```

**Arguments**:

* `ROTOR_FILE`: Path to the rotor JSON blueprint file.  [required]
* `DYNAMO_FILE`: Path to the dynamo JSON blueprint file.  [required]

**Options**:

* `-w, --shaft-width INTEGER`: The width of the rotor shaft in blocks.  [required]
* `-O, --output PATH`: Path to the output .schematic file.  [required]
* `-t, --transparent`: Whether the turbine should have transparent casing.
* `-f, --facing [x|z]`: The facing of the rotor.  [default: x]
* `--help`: Show this message and exit.

### `reiuji convert qmd`

Commands for converting QMD blueprints.

**Usage**:

```console
$ reiuji convert qmd [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `accelerator`: Convert a QMD accelerator blueprint to a...
* `nucleosynthesis`: Convert a QMD nucleosynthesis reactor...

#### `reiuji convert qmd accelerator`

Convert a QMD accelerator blueprint to a .schematic file.

**Usage**:

```console
$ reiuji convert qmd accelerator [OPTIONS] BLUEPRINT_FILE
```

**Arguments**:

* `BLUEPRINT_FILE`: Path to the accelerator JSON blueprint file.  [required]

**Options**:

* `-O, --output PATH`: Path to the output .schematic file.  [required]
* `-t, --transparent`: Whether the accelerator should have transparent casing.
* `--help`: Show this message and exit.

#### `reiuji convert qmd nucleosynthesis`

Convert a QMD nucleosynthesis reactor blueprint to a .schematic file.

**Usage**:

```console
$ reiuji convert qmd nucleosynthesis [OPTIONS] BLUEPRINT_FILE
```

**Arguments**:

* `BLUEPRINT_FILE`: Path to the nucleosynthesis JSON blueprint file.  [required]

**Options**:

* `-O, --output PATH`: Path to the output .schematic file.  [required]
* `-t, --transparent`: Whether the nucleosynthesis chamber should have transparent casing.
* `-f, --facing [x|z]`: The facing of the nucleosynthesis chamber.  [default: x]
* `--help`: Show this message and exit.

## `reiuji design`

Commands for invoking Reiuji's Designer.

**Usage**:

```console
$ reiuji design [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `overhauled`: Commands for designing NuclearCraft:...
* `qmd`: Commands for designing QMD multiblocks.

### `reiuji design overhauled`

Commands for designing NuclearCraft: Overhauled multiblocks.

**Usage**:

```console
$ reiuji design overhauled [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `turbine-dynamo`: Designs a NuclearCraft: Overhauled turbine...
* `turbine-rotor`: Designs a NuclearCraft: Overhauled turbine...

#### `reiuji design overhauled turbine-dynamo`

Designs a NuclearCraft: Overhauled turbine dynamo configuration.

**Usage**:

```console
$ reiuji design overhauled turbine-dynamo [OPTIONS] SIDE_LENGTH [SHAFT_WIDTH]
```

**Arguments**:

* `SIDE_LENGTH`: The side length of the dynamo configuration in blocks.  [required]
* `[SHAFT_WIDTH]`: The width of the rotor shaft in blocks.  [default: 1]

**Options**:

* `-X`: Whether to enforce symmetry along the horizontal axis.
* `-Y`: Whether to enforce symmetry along the vertical axis.
* `-C, --components PATH`: The path to the file containing a list of components.
* `-L, --limits PATH`: The path to the file containing a list of component limits.
* `-T, --timeout FLOAT`: The maximum time to spend designing the structure in seconds.
* `-O, --output PATH`: The path(s) to output the designs to.
* `--help`: Show this message and exit.

#### `reiuji design overhauled turbine-rotor`

Designs a NuclearCraft: Overhauled turbine rotor sequence.

**Usage**:

```console
$ reiuji design overhauled turbine-rotor [OPTIONS] LENGTH
```

**Arguments**:

* `LENGTH`: The length of the rotor shaft in blocks.  [required]

**Options**:

* `-e, --expansion FLOAT`: The optimal expansion of the input fluid.  [required]
* `-C, --components PATH`: The path to the file containing a list of components.
* `-L, --limits PATH`: The path to the file containing a list of component limits.
* `--qmd`: Whether to include QMD-only components. Only has effect if -C is not specified.
* `-T, --timeout FLOAT`: The maximum time to spend designing the structure in seconds.
* `-O, --output PATH`: The path(s) to output the designs to.
* `--help`: Show this message and exit.

### `reiuji design qmd`

Commands for designing QMD multiblocks.

**Usage**:

```console
$ reiuji design qmd [OPTIONS] COMMAND [ARGS]...
```

**Options**:

* `--help`: Show this message and exit.

**Commands**:

* `decelerator`: Designs a QMD decelerator.
* `linear`: Designs a QMD linear accelerator.
* `nucleosynthesis`: Designs a QMD nucleosynthesis chamber.
* `synchrotron`: Designs a QMD synchrotron.

#### `reiuji design qmd decelerator`

Designs a QMD decelerator.

**Usage**:

```console
$ reiuji design qmd decelerator [OPTIONS] SIDE_LENGTH
```

**Arguments**:

* `SIDE_LENGTH`: The side length of the decelerator in blocks.  [required]

**Options**:

* `-e, --min-energy INTEGER`: The minimum energy of the input in MeV.  [required]
* `-E, --max-energy INTEGER`: The maximum energy of the input in MeV.  [required]
* `-F, --target-focus FLOAT`: The target focus of the output.  [required]
* `-q, --charge FLOAT`: The charge of the particles in the decelerator.  [required]
* `-m, --mass FLOAT`: The mass of the particles in the decelerator in MeV/c^2.  [required]
* `-s, --beam-strength INTEGER`: The strength of the beam in the decelerator in pu/t.  [required]
* `-f, --initial-focus FLOAT`: The focus of the beam entering the decelerator.  [required]
* `--scaling-factor INTEGER`: The scaling factor for the decelerator.  [default: 10000]
* `--env-temperature INTEGER`: The temperature of the environment in K.  [default: 300]
* `--kappa FLOAT`: The thermal conductivity for the decelerator.  [default: 0.0025]
* `-H, --heat-neutral`: Whether the decelerator should be heat neutral.
* `-S`: Whether to enforce symmetry along the internal ring.
* `-C, --components PATH`: The path to the file containing a list of components.
* `-L, --limits PATH`: The path to the file containing a list of component limits.
* `-T, --timeout FLOAT`: The maximum time to spend designing the structure in seconds.
* `-O, --output PATH`: The path(s) to output the designs to.
* `-t, --transparent`: Whether to use transparent blocks in the schematic.
* `--help`: Show this message and exit.

#### `reiuji design qmd linear`

Designs a QMD linear accelerator.

**Usage**:

```console
$ reiuji design qmd linear [OPTIONS] LENGTH
```

**Arguments**:

* `LENGTH`: The length of the linear accelerator in blocks.  [required]

**Options**:

* `-e, --min-energy INTEGER`: The minimum energy of the output in KeV.  [required]
* `-E, --max-energy INTEGER`: The maximum energy of the output in KeV.  [required]
* `-F, --target-focus FLOAT`: The target focus of the output.  [required]
* `-q, --charge FLOAT`: The charge of the particles in the accelerator.  [required]
* `-s, --beam-strength INTEGER`: The strength of the beam in the accelerator in pu/t.  [required]
* `-f, --initial-focus FLOAT`: The focus of the beam entering the accelerator.  [required]
* `--scaling-factor INTEGER`: The scaling factor for the accelerator.  [default: 10000]
* `--env-temperature INTEGER`: The temperature of the environment in K.  [default: 300]
* `--kappa FLOAT`: The thermal conductivity for the accelerator.  [default: 0.0025]
* `-H, --heat-neutral`: Whether the accelerator should be heat neutral.
* `-X`: Whether to enforce symmetry along the horizontal axis.
* `-Y`: Whether to enforce symmetry along the vertical axis.
* `-C, --components PATH`: The path to the file containing a list of components.
* `-L, --limits PATH`: The path to the file containing a list of component limits.
* `-T, --timeout FLOAT`: The maximum time to spend designing the structure in seconds.
* `-O, --output PATH`: The path(s) to output the designs to.
* `-t, --transparent`: Whether to use transparent blocks in the schematic.
* `--help`: Show this message and exit.

#### `reiuji design qmd nucleosynthesis`

Designs a QMD nucleosynthesis chamber.

**Usage**:

```console
$ reiuji design qmd nucleosynthesis [OPTIONS]
```

**Options**:

* `-h, --recipe-heat INTEGER`: The heat of the recipe in H/t.  [required]
* `-X`: Whether to enforce symmetry along the X axis.
* `-Z`: Whether to enforce symmetry along the Z axis.
* `-C, --components PATH`: The path to the file containing a list of components.
* `-L, --limits PATH`: The path to the file containing a list of component limits.
* `-T, --timeout FLOAT`: The maximum time to spend designing the structure in seconds.
* `-O, --output PATH`: The path(s) to output the designs to.
* `-t, --transparent`: Whether to use transparent blocks in the schematic.
* `-f, --facing [x|z]`: The direction the structure should face.  [default: x]
* `--help`: Show this message and exit.

#### `reiuji design qmd synchrotron`

Designs a QMD synchrotron.

**Usage**:

```console
$ reiuji design qmd synchrotron [OPTIONS] SIDE_LENGTH
```

**Arguments**:

* `SIDE_LENGTH`: The side length of the synchrotron in blocks.  [required]

**Options**:

* `-e, --min-energy INTEGER`: The minimum energy of the output in MeV.  [required]
* `-E, --max-energy INTEGER`: The maximum energy of the output in MeV.  [required]
* `-F, --target-focus FLOAT`: The target focus of the output.  [required]
* `-q, --charge FLOAT`: The charge of the particles in the accelerator.  [required]
* `-m, --mass FLOAT`: The mass of the particles in the accelerator in MeV/c^2.  [required]
* `-s, --beam-strength INTEGER`: The strength of the beam in the accelerator in pu/t.  [required]
* `-f, --initial-focus FLOAT`: The focus of the beam entering the accelerator.  [required]
* `--scaling-factor INTEGER`: The scaling factor for the accelerator.  [default: 10000]
* `--env-temperature INTEGER`: The temperature of the environment in K.  [default: 300]
* `--kappa FLOAT`: The thermal conductivity for the accelerator.  [default: 0.0025]
* `-H, --heat-neutral`: Whether the accelerator should be heat neutral.
* `-S`: Whether to enforce symmetry along the internal ring.
* `-C, --components PATH`: The path to the file containing a list of components.
* `-L, --limits PATH`: The path to the file containing a list of component limits.
* `-T, --timeout FLOAT`: The maximum time to spend designing the structure in seconds.
* `-O, --output PATH`: The path(s) to output the designs to.
* `-t, --transparent`: Whether to use transparent blocks in the schematic.
* `--help`: Show this message and exit.

## `reiuji list`

List the components for a multiblock.

**Usage**:

```console
$ reiuji list [OPTIONS]
```

**Options**:

* `-c, --component-set [nco-turbine-rotor|nco-turbine-rotor-qmd|nco-turbine-dynamo|qmd-linear|qmd-synchrotron|qmd-nucleosynthesis]`: The set of components to list. Ignored if -C is set.
* `-C, --components PATH`: Path to the components file.
* `-O, --output PATH`: Path to the output file.
* `--help`: Show this message and exit.
