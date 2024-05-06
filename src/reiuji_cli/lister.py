"""CLI for listing components."""

from . import utils

import typing
import pathlib

import reiuji
import typer
import rich
import rich.table


lister_app = typer.Typer(help="Commands for listing multiblock components.")

nco_lister = typer.Typer(help="Commands for listing NuclearCraft: Overhauled components.")
lister_app.add_typer(nco_lister, name="overhauled")


@nco_lister.command("turbine-rotor")
def list_nco_turbine_rotor_components(
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="Path to the components file.")] = None,
    output: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--output", "-O", help="Path to the output file.")] = None,
) -> None:
    components = utils.load_component_list(components_file)
    if isinstance(components, type(None)):
        components = reiuji.designer.overhauled.turbine_rotor.models.DEFAULT_COMPONENTS
    table = rich.table.Table(title="NuclearCraft: Overhauled Turbine Rotor Components")
    table.add_column("Full Name")
    table.add_column("Short Name")
    for comp in components:
        table.add_row(comp.full_name, comp.rich_short_name)
    rich.print(table)
    if isinstance(output, pathlib.Path):
        utils.write_component_list(components, output)


@nco_lister.command("turbine-dynamo")
def list_nco_turbine_dynamo_components(
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="Path to the components file.")] = None,
    output: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--output", "-O", help="Path to the output file.")] = None,
) -> None:
    components = utils.load_component_list(components_file)
    if isinstance(components, type(None)):
        components = reiuji.designer.overhauled.turbine_dynamo.models.DEFAULT_COMPONENTS
    table = rich.table.Table(title="NuclearCraft: Overhauled Turbine Dynamo Components")
    table.add_column("Full Name")
    table.add_column("Short Name")
    for comp in components:
        table.add_row(comp.full_name, comp.rich_short_name)
    rich.print(table)
    if isinstance(output, pathlib.Path):
        utils.write_component_list(components, output)


qmd_list = typer.Typer(help="Commands for listing QMD components.")
lister_app.add_typer(qmd_list, name="qmd")


@qmd_list.command("linear")
def list_qmd_linear_components(
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="Path to the components file.")] = None,
    output: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--output", "-O", help="Path to the output file.")] = None,
) -> None:
    components = utils.load_component_list(components_file)
    if isinstance(components, type(None)):
        components = reiuji.designer.qmd.linear.models.DEFAULT_COMPONENTS
    table = rich.table.Table(title="QMD Linear Accelerator Components")
    table.add_column("Full Name")
    table.add_column("Short Name")
    for comp in components:
        table.add_row(comp.full_name, comp.rich_short_name)
    rich.print(table)
    if isinstance(output, pathlib.Path):
        utils.write_component_list(components, output)


@qmd_list.command("synchrotron")
def list_qmd_synchrotron_components(
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="Path to the components file.")] = None,
    output: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--output", "-O", help="Path to the output file.")] = None,
) -> None:
    components = utils.load_component_list(components_file)
    if isinstance(components, type(None)):
        components = reiuji.designer.qmd.synchrotron.models.DEFAULT_COMPONENTS
    table = rich.table.Table(title="QMD Synchrotron Components")
    table.add_column("Full Name")
    table.add_column("Short Name")
    for comp in components:
        table.add_row(comp.full_name, comp.rich_short_name)
    rich.print(table)
    if isinstance(output, pathlib.Path):
        utils.write_component_list(components, output)


@qmd_list.command("nucleosynthesis")
def list_qmd_nucleosynthesis_components(
    components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="Path to the components file.")] = None,
    output: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--output", "-O", help="Path to the output file.")] = None,
) -> None:
    components = utils.load_component_list(components_file)
    if isinstance(components, type(None)):
        components = reiuji.designer.qmd.nucleosynthesis.models.DEFAULT_COMPONENTS
    table = rich.table.Table(title="QMD Nucleosynthesis Components")
    table.add_column("Full Name")
    table.add_column("Short Name")
    for comp in components:
        table.add_row(comp.full_name, comp.rich_short_name)
    rich.print(table)
    if isinstance(output, pathlib.Path):
        utils.write_component_list(components, output)
