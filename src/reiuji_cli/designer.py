"""CLI for designer commands."""

from . import utils

import typing
import pathlib

import reiuji
import typer
import rich


designer_app = typer.Typer(help="Commands for invoking Reiuji's Designer.")

nco_designer = typer.Typer(help="Commands for designing NuclearCraft: Overhauled multiblocks.")
designer_app.add_typer(nco_designer, name="overhauled")


@nco_designer.command("turbine-rotor")
def design_nco_turbine_rotor(
    length: typing.Annotated[int, typer.Argument(help="The length of the rotor shaft in blocks.")],
    expansion: typing.Annotated[float, typer.Option("--expansion", "-e", help="The optimal expansion of the input fluid.", rich_help_panel="Fluid Options")],
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="The path to the file containing a list of components.", rich_help_panel="Component Options")] = None,
    limits_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--limits", "-L", help="The path to the file containing a list of component limits.", rich_help_panel="Component Options")] = None,
    is_qmd: typing.Annotated[bool, typer.Option("--qmd", help="Whether to include QMD-only components. Only has effect if -C is not specified.", rich_help_panel="Component Options")] = False,
    timeout: typing.Annotated[typing.Optional[float], typer.Option("--timeout", "-T", help="The maximum time to spend designing the structure in seconds.", rich_help_panel="Designer Options")] = None,
    output: typing.Annotated[list[pathlib.Path], typer.Option("--output", "-O", help="The path(s) to output the designs to.", rich_help_panel="Output Options")] = []
) -> None:
    """Designs a NuclearCraft: Overhauled turbine rotor sequence."""
    limits = utils.load_limits(limits_file)
    components = utils.load_component_list(components_file)
    if is_qmd and isinstance(components, type(None)):
        components = reiuji.components.defaults.OVERHAULED_TURBINE_ROTOR_COMPONENTS_QMD
    designer = reiuji.designer.overhauled.turbine_rotor.TurbineRotorDesigner(
        length=length,
        optimal_expansion=expansion,
        components=components,
        component_limits=limits
    )
    status, design = designer.design(timeout=timeout)
    utils.print_status(status)
    if not isinstance(design, type(None)):
        for comp in design:
            rich_short_name = utils.format_text_rich(comp.display.short_name, bold=comp.display.bold, italic=comp.display.italic, color=comp.display.color, bg_color=comp.display.bg_color)
            rich.print(rich_short_name, end=" ")
        print()
        for path in output:
            utils.write_design(design, path)


@nco_designer.command("turbine-dynamo")
def design_nco_turbine_dynamo(
    side_length: typing.Annotated[int, typer.Argument(help="The side length of the dynamo configuration in blocks.")],
    shaft_width: typing.Annotated[int, typer.Argument(help="The width of the rotor shaft in blocks.")] = 1,
    x_symmetry: typing.Annotated[bool, typer.Option("-X", help="Whether to enforce symmetry along the horizontal axis.", rich_help_panel="Symmetry Options")] = False,
    y_symmetry: typing.Annotated[bool, typer.Option("-Y", help="Whether to enforce symmetry along the vertical axis.", rich_help_panel="Symmetry Options")] = False,
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="The path to the file containing a list of components.", rich_help_panel="Component Options")] = None,
    limits_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--limits", "-L", help="The path to the file containing a list of component limits.", rich_help_panel="Component Options")] = None,
    timeout: typing.Annotated[typing.Optional[float], typer.Option("--timeout", "-T", help="The maximum time to spend designing the structure in seconds.", rich_help_panel="Designer Options")] = None,
    output: typing.Annotated[list[pathlib.Path], typer.Option("--output", "-O", help="The path(s) to output the designs to.", rich_help_panel="Output Options")] = []
) -> None:
    """Designs a NuclearCraft: Overhauled turbine dynamo configuration."""
    limits = utils.load_limits(limits_file)
    components = utils.load_component_list(components_file)
    designer = reiuji.designer.overhauled.turbine_dynamo.TurbineDynamoDesigner(
        side_length=side_length,
        shaft_width=shaft_width,
        x_symmetry=x_symmetry,
        y_symmetry=y_symmetry,
        components=components,
        component_limits=limits
    )
    status, design = designer.design(timeout=timeout)
    utils.print_status(status)
    if not isinstance(design, type(None)):
        for y in range(design.shape[0]):
            for x in range(design.shape[1]):
                rich_short_name = utils.format_text_rich(design[y, x].display.short_name, bold=design[y, x].display.bold, italic=design[y, x].display.italic, color=design[y, x].display.color, bg_color=design[y, x].display.bg_color)
                rich.print(rich_short_name, end=" ")
            print()
        for path in output:
            utils.write_design(design, path)


qmd_designer = typer.Typer(help="Commands for designing QMD multiblocks.")
designer_app.add_typer(qmd_designer, name="qmd")


@qmd_designer.command("linear")
def design_qmd_linear(
    length: typing.Annotated[int, typer.Argument(help="The length of the linear accelerator in blocks.")],
    minimum_energy: typing.Annotated[int, typer.Option("--min-energy", "-e", help="The minimum energy of the output in KeV.", rich_help_panel="Target Options")],
    maximum_energy: typing.Annotated[int, typer.Option("--max-energy", "-E", help="The maximum energy of the output in KeV.", rich_help_panel="Target Options")],
    target_focus: typing.Annotated[float, typer.Option("--target-focus", "-F", help="The target focus of the output.", rich_help_panel="Target Options")],
    charge: typing.Annotated[float, typer.Option("--charge", "-q", help="The charge of the particles in the accelerator.", rich_help_panel="Particle Options")],
    beam_strength: typing.Annotated[int, typer.Option("--beam-strength", "-s", help="The strength of the beam in the accelerator in pu/t.", rich_help_panel="Particle Options")],
    initial_focus: typing.Annotated[float, typer.Option("--initial-focus", "-f", help="The focus of the beam entering the accelerator.", rich_help_panel="Particle Options")],
    scaling_factor: typing.Annotated[int, typer.Option("--scaling-factor", help="The scaling factor for the accelerator.", rich_help_panel="Particle Options")] = 10000,
    env_temperature: typing.Annotated[int, typer.Option("--env-temperature", help="The temperature of the environment in K.", rich_help_panel="Heating Options")] = 300,
    kappa: typing.Annotated[float, typer.Option("--kappa", help="The thermal conductivity for the accelerator.", rich_help_panel="Heating Options")] = 0.0025,
    heat_neutral: typing.Annotated[bool, typer.Option("--heat-neutral", "-H", help="Whether the accelerator should be heat neutral.", rich_help_panel="Heating Options")] = False,
    x_symmetry: typing.Annotated[bool, typer.Option("-X", help="Whether to enforce symmetry along the horizontal axis.", rich_help_panel="Symmetry Options")] = False,
    y_symmetry: typing.Annotated[bool, typer.Option("-Y", help="Whether to enforce symmetry along the vertical axis.", rich_help_panel="Symmetry Options")] = False,
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="The path to the file containing a list of components.", rich_help_panel="Component Options")] = None,
    limits_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--limits", "-L", help="The path to the file containing a list of component limits.", rich_help_panel="Component Options")] = None,
    timeout: typing.Annotated[typing.Optional[float], typer.Option("--timeout", "-T", help="The maximum time to spend designing the structure in seconds.", rich_help_panel="Designer Options")] = None,
    output: typing.Annotated[list[pathlib.Path], typer.Option("--output", "-O", help="The path(s) to output the designs to.", rich_help_panel="Output Options")] = [],
    transparent: typing.Annotated[bool, typer.Option("--transparent", "-t", help="Whether to use transparent blocks in the schematic.", rich_help_panel="Output Options")] = False,
) -> None:
    """Designs a QMD linear accelerator."""
    limits = utils.load_limits(limits_file)
    components = utils.load_component_list(components_file)
    designer = reiuji.designer.qmd.linear.LinearAcceleratorDesigner(
        length=length,
        minimum_energy=minimum_energy,
        maximum_energy=maximum_energy,
        target_focus=target_focus,
        charge=charge,
        beam_strength=beam_strength,
        initial_focus=initial_focus,
        scaling_factor=scaling_factor,
        env_temperature=env_temperature,
        kappa=kappa,
        heat_neutral=heat_neutral,
        z_symmetry=x_symmetry,
        y_symmetry=y_symmetry,
        components=components,
        component_limits=limits
    )
    status, design = designer.design(timeout=timeout)
    utils.print_status(status)
    if not isinstance(design, type(None)):
        for x in range(design.shape[0]):
            for y in range(design.shape[2]):
                for z in range(design.shape[1]):
                    rich_short_name = utils.format_text_rich(design[x, z, y].display.short_name, bold=design[x, z, y].display.bold, italic=design[x, z, y].display.italic, color=design[x, z, y].display.color, bg_color=design[x, z, y].display.bg_color)
                    rich.print(rich_short_name, end=" ")
                print()
            print()
        for path in output:
            utils.write_design(design, path, schematic_type="accelerator", transparent=transparent)


@qmd_designer.command("synchrotron")
def design_qmd_synchrotron(
    side_length: typing.Annotated[int, typer.Argument(help="The side length of the synchrotron in blocks.")],
    minimum_energy: typing.Annotated[int, typer.Option("--min-energy", "-e", help="The minimum energy of the output in MeV.", rich_help_panel="Target Options")],
    maximum_energy: typing.Annotated[int, typer.Option("--max-energy", "-E", help="The maximum energy of the output in MeV.", rich_help_panel="Target Options")],
    target_focus: typing.Annotated[float, typer.Option("--target-focus", "-F", help="The target focus of the output.", rich_help_panel="Target Options")],
    charge: typing.Annotated[float, typer.Option("--charge", "-q", help="The charge of the particles in the accelerator.", rich_help_panel="Particle Options")],
    mass: typing.Annotated[float, typer.Option("--mass", "-m", help="The mass of the particles in the accelerator in MeV/c^2.", rich_help_panel="Particle Options")],
    beam_strength: typing.Annotated[int, typer.Option("--beam-strength", "-s", help="The strength of the beam in the accelerator in pu/t.", rich_help_panel="Particle Options")],
    initial_focus: typing.Annotated[float, typer.Option("--initial-focus", "-f", help="The focus of the beam entering the accelerator.", rich_help_panel="Particle Options")],
    scaling_factor: typing.Annotated[int, typer.Option("--scaling-factor", help="The scaling factor for the accelerator.", rich_help_panel="Particle Options")] = 10000,
    env_temperature: typing.Annotated[int, typer.Option("--env-temperature", help="The temperature of the environment in K.", rich_help_panel="Heating Options")] = 300,
    kappa: typing.Annotated[float, typer.Option("--kappa", help="The thermal conductivity for the accelerator.", rich_help_panel="Heating Options")] = 0.0025,
    heat_neutral: typing.Annotated[bool, typer.Option("--heat-neutral", "-H", help="Whether the accelerator should be heat neutral.", rich_help_panel="Heating Options")] = False,
    internal_symmetry: typing.Annotated[bool, typer.Option("-S", help="Whether to enforce symmetry along the internal ring.", rich_help_panel="Symmetry Options")] = False,
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="The path to the file containing a list of components.", rich_help_panel="Component Options")] = None,
    limits_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--limits", "-L", help="The path to the file containing a list of component limits.", rich_help_panel="Component Options")] = None,
    timeout: typing.Annotated[typing.Optional[float], typer.Option("--timeout", "-T", help="The maximum time to spend designing the structure in seconds.", rich_help_panel="Designer Options")] = None,
    output: typing.Annotated[list[pathlib.Path], typer.Option("--output", "-O", help="The path(s) to output the designs to.", rich_help_panel="Output Options")] = [],
    transparent: typing.Annotated[bool, typer.Option("--transparent", "-t", help="Whether to use transparent blocks in the schematic.", rich_help_panel="Output Options")] = False,
) -> None:
    """Designs a QMD synchrotron."""
    limits = utils.load_limits(limits_file)
    components = utils.load_component_list(components_file)
    designer = reiuji.designer.qmd.synchrotron.SynchrotronDesigner(
        side_length=side_length,
        minimum_energy=minimum_energy,
        maximum_energy=maximum_energy,
        target_focus=target_focus,
        charge=charge,
        mass=mass,
        beam_strength=beam_strength,
        initial_focus=initial_focus,
        scaling_factor=scaling_factor,
        env_temperature=env_temperature,
        kappa=kappa,
        heat_neutral=heat_neutral,
        internal_symmetry=internal_symmetry,
        components=components,
        component_limits=limits
    )
    status, design = designer.design(timeout=timeout)
    utils.print_status(status)
    if not isinstance(design, type(None)):
        for y in range(design.shape[2]):
            for x in range(design.shape[0]):
                for z in range(design.shape[1]):
                    rich_short_name = utils.format_text_rich(design[x, z, y].display.short_name, bold=design[x, z, y].display.bold, italic=design[x, z, y].display.italic, color=design[x, z, y].display.color, bg_color=design[x, z, y].display.bg_color)
                    rich.print(rich_short_name, end=" ")
                print()
            print()
        for path in output:
            utils.write_design(design, path, schematic_type="accelerator", transparent=transparent)


@qmd_designer.command("decelerator")
def design_qmd_decelerator(
    side_length: typing.Annotated[int, typer.Argument(help="The side length of the decelerator in blocks.")],
    minimum_energy: typing.Annotated[int, typer.Option("--min-energy", "-e", help="The minimum energy of the input in MeV.", rich_help_panel="Target Options")],
    maximum_energy: typing.Annotated[int, typer.Option("--max-energy", "-E", help="The maximum energy of the input in MeV.", rich_help_panel="Target Options")],
    target_focus: typing.Annotated[float, typer.Option("--target-focus", "-F", help="The target focus of the output.", rich_help_panel="Target Options")],
    charge: typing.Annotated[float, typer.Option("--charge", "-q", help="The charge of the particles in the decelerator.", rich_help_panel="Particle Options")],
    mass: typing.Annotated[float, typer.Option("--mass", "-m", help="The mass of the particles in the decelerator in MeV/c^2.", rich_help_panel="Particle Options")],
    beam_strength: typing.Annotated[int, typer.Option("--beam-strength", "-s", help="The strength of the beam in the decelerator in pu/t.", rich_help_panel="Particle Options")],
    initial_focus: typing.Annotated[float, typer.Option("--initial-focus", "-f", help="The focus of the beam entering the decelerator.", rich_help_panel="Particle Options")],
    scaling_factor: typing.Annotated[int, typer.Option("--scaling-factor", help="The scaling factor for the decelerator.", rich_help_panel="Particle Options")] = 10000,
    env_temperature: typing.Annotated[int, typer.Option("--env-temperature", help="The temperature of the environment in K.", rich_help_panel="Heating Options")] = 300,
    kappa: typing.Annotated[float, typer.Option("--kappa", help="The thermal conductivity for the decelerator.", rich_help_panel="Heating Options")] = 0.0025,
    heat_neutral: typing.Annotated[bool, typer.Option("--heat-neutral", "-H", help="Whether the decelerator should be heat neutral.", rich_help_panel="Heating Options")] = False,
    internal_symmetry: typing.Annotated[bool, typer.Option("-S", help="Whether to enforce symmetry along the internal ring.", rich_help_panel="Symmetry Options")] = False,
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="The path to the file containing a list of components.", rich_help_panel="Component Options")] = None,
    limits_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--limits", "-L", help="The path to the file containing a list of component limits.", rich_help_panel="Component Options")] = None,
    timeout: typing.Annotated[typing.Optional[float], typer.Option("--timeout", "-T", help="The maximum time to spend designing the structure in seconds.", rich_help_panel="Designer Options")] = None,
    output: typing.Annotated[list[pathlib.Path], typer.Option("--output", "-O", help="The path(s) to output the designs to.", rich_help_panel="Output Options")] = [],
    transparent: typing.Annotated[bool, typer.Option("--transparent", "-t", help="Whether to use transparent blocks in the schematic.", rich_help_panel="Output Options")] = False,
) -> None:
    """Designs a QMD decelerator."""
    limits = utils.load_limits(limits_file)
    components = utils.load_component_list(components_file)
    designer = reiuji.designer.qmd.decelerator.DeceleratorDesigner(
        side_length=side_length,
        minimum_energy=minimum_energy,
        maximum_energy=maximum_energy,
        target_focus=target_focus,
        charge=charge,
        mass=mass,
        beam_strength=beam_strength,
        initial_focus=initial_focus,
        scaling_factor=scaling_factor,
        env_temperature=env_temperature,
        kappa=kappa,
        heat_neutral=heat_neutral,
        internal_symmetry=internal_symmetry,
        components=components,
        component_limits=limits
    )
    status, design = designer.design(timeout=timeout)
    utils.print_status(status)
    if not isinstance(design, type(None)):
        for y in range(design.shape[2]):
            for x in range(design.shape[0]):
                for z in range(design.shape[1]):
                    rich_short_name = utils.format_text_rich(design[x, z, y].display.short_name, bold=design[x, z, y].display.bold, italic=design[x, z, y].display.italic, color=design[x, z, y].display.color, bg_color=design[x, z, y].display.bg_color)
                    rich.print(rich_short_name, end=" ")
                print()
            print()
        for path in output:
            utils.write_design(design, path, schematic_type="accelerator", transparent=transparent)


@qmd_designer.command("nucleosynthesis")
def design_qmd_nucleosynthesis(
    recipe_heat: typing.Annotated[int, typer.Option("--recipe-heat", "-h", help="The heat of the recipe in H/t.", rich_help_panel="Recipe Options")],
    x_symmetry: typing.Annotated[bool, typer.Option("-X", help="Whether to enforce symmetry along the X axis.", rich_help_panel="Symmetry Options")] = False,
    z_symmetry: typing.Annotated[bool, typer.Option("-Z", help="Whether to enforce symmetry along the Z axis.", rich_help_panel="Symmetry Options")] = False,
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="The path to the file containing a list of components.", rich_help_panel="Component Options")] = None,
    limits_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--limits", "-L", help="The path to the file containing a list of component limits.", rich_help_panel="Component Options")] = None,
    timeout: typing.Annotated[typing.Optional[float], typer.Option("--timeout", "-T", help="The maximum time to spend designing the structure in seconds.", rich_help_panel="Designer Options")] = None,
    output: typing.Annotated[list[pathlib.Path], typer.Option("--output", "-O", help="The path(s) to output the designs to.", rich_help_panel="Output Options")] = [],
    transparent: typing.Annotated[bool, typer.Option("--transparent", "-t", help="Whether to use transparent blocks in the schematic.", rich_help_panel="Output Options")] = False,
    facing: typing.Annotated[utils.Facing, typer.Option("--facing", "-f", help="The direction the structure should face.", rich_help_panel="Output Options")] = utils.Facing.X
) -> None:
    """Designs a QMD nucleosynthesis chamber."""
    limits = utils.load_limits(limits_file)
    components = utils.load_component_list(components_file)
    designer = reiuji.designer.qmd.nucleosynthesis.NucleosynthesisDesigner(
        recipe_heat=recipe_heat,
        x_symmetry=x_symmetry,
        z_symmetry=z_symmetry,
        components=components,
        component_limits=limits
    )
    status, design = designer.design(timeout=timeout)
    utils.print_status(status)
    if not isinstance(design, type(None)):
        for y in range(design.shape[2]):
            for x in range(design.shape[0]):
                for z in range(design.shape[1]):
                    rich_short_name = utils.format_text_rich(design[x, z, y].display.short_name, bold=design[x, z, y].display.bold, italic=design[x, z, y].display.italic, color=design[x, z, y].display.color, bg_color=design[x, z, y].display.bg_color)
                    rich.print(rich_short_name, end=" ")
                print()
            print()
        for path in output:
            utils.write_design(design, path, schematic_type="nucleosynthesis", transparent=transparent, facing=facing.value)
