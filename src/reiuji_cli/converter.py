"""CLI for converting JSON blueprints to .schematic files."""

from . import utils

import typing
import pathlib

import reiuji
import typer
import rich
import rich.table


converter_app = typer.Typer(help="Commands for converting JSON blueprints to .schematic files.")

nco_converter = typer.Typer(help="Commands for converting NuclearCraft: Overhauled blueprints.")
converter_app.add_typer(nco_converter, name="overhauled")


@nco_converter.command("turbine")
def convert_nco_turbine_blueprint(
    rotor_file: typing.Annotated[pathlib.Path, typer.Argument(help="Path to the rotor JSON blueprint file.")],
    dynamo_file: typing.Annotated[pathlib.Path, typer.Argument(help="Path to the dynamo JSON blueprint file.")],
    shaft_width: typing.Annotated[int, typer.Option("--shaft-width", "-w", help="The width of the rotor shaft in blocks.", rich_help_panel="Structure Options")],
    output: typing.Annotated[pathlib.Path, typer.Option("--output", "-O", help="Path to the output .schematic file.", rich_help_panel="Output Options")],
    transparent: typing.Annotated[bool, typer.Option("--transparent", "-t", help="Whether the turbine should have transparent casing.", rich_help_panel="Output Options")] = False,
    facing: typing.Annotated[utils.Facing, typer.Option("--facing", "-f", help="The facing of the rotor.", rich_help_panel="Output Options")] = utils.Facing.X
) -> None:
    """Convert a NuclearCraft: Overhauled turbine blueprint to a .schematic file."""
    with rotor_file.open("r") as file:
        rotor_bp = reiuji.io.serialization.SerializableMultiSequence.model_validate_json(file.read()).to_multi_sequence()
    with dynamo_file.open("r") as file:
        dynamo_bp = reiuji.io.serialization.SerializableMultiSequence.model_validate_json(file.read()).to_multi_sequence()
    if output.suffix == ".schematic":
        reiuji.io.schematics.turbine.TurbineSchematicWriter(dynamo_bp, rotor_bp, shaft_width, transparent=transparent, facing=facing.value).write(output)
    else:
        rich.print(f"[red][bold]ERROR:[/bold] Unsupported file format: {output.suffix}[/red]")


qmd_converter = typer.Typer(help="Commands for converting QMD blueprints.")
converter_app.add_typer(qmd_converter, name="qmd")


@qmd_converter.command("accelerator")
def convert_qmd_accelerator_blueprint(
    blueprint_file: typing.Annotated[pathlib.Path, typer.Argument(help="Path to the accelerator JSON blueprint file.")],
    output: typing.Annotated[pathlib.Path, typer.Option("--output", "-O", help="Path to the output .schematic file.", rich_help_panel="Output Options")],
    transparent: typing.Annotated[bool, typer.Option("--transparent", "-t", help="Whether the accelerator should have transparent casing.", rich_help_panel="Output Options")] = False
) -> None:
    """Convert a QMD accelerator blueprint to a .schematic file."""
    with blueprint_file.open("r") as file:
        blueprint = reiuji.io.serialization.SerializableMultiSequence.model_validate_json(file.read()).to_multi_sequence()
    if output.suffix == ".schematic":
        reiuji.io.schematics.accelerator.AcceleratorSchematicWriter(blueprint, transparent=transparent).write(output)
    else:
        rich.print(f"[red][bold]ERROR:[/bold] Unsupported file format: {output.suffix}[/red]")


@qmd_converter.command("nucleosynthesis")
def convert_qmd_nucleosynthesis_blueprint(
    blueprint_file: typing.Annotated[pathlib.Path, typer.Argument(help="Path to the nucleosynthesis JSON blueprint file.")],
    output: typing.Annotated[pathlib.Path, typer.Option("--output", "-O", help="Path to the output .schematic file.", rich_help_panel="Output Options")],
    transparent: typing.Annotated[bool, typer.Option("--transparent", "-t", help="Whether the nucleosynthesis chamber should have transparent casing.", rich_help_panel="Output Options")] = False,
    facing: typing.Annotated[utils.Facing, typer.Option("--facing", "-f", help="The facing of the nucleosynthesis chamber.", rich_help_panel="Output Options")] = utils.Facing.X
) -> None:
    """Convert a QMD nucleosynthesis reactor blueprint to a .schematic file."""
    with blueprint_file.open("r") as file:
        blueprint = reiuji.io.serialization.SerializableMultiSequence.model_validate_json(file.read()).to_multi_sequence()
    if output.suffix == ".schematic":
        reiuji.io.schematics.nucleosynthesis.NucleosynthesisSchematicWriter(blueprint, transparent=transparent, facing=facing.value).write(output)
    else:
        rich.print(f"[red][bold]ERROR:[/bold] Unsupported file format: {output.suffix}[/red]")
