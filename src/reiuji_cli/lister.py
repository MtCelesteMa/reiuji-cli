"""CLI for listing multiblock components."""

from . import utils

import enum
import typing
import pathlib

import reiuji
import typer
import rich
import rich.table


class ComponentSet(enum.StrEnum):
    """An enum for the different sets of components."""
    NCO_TURBINE_ROTOR = "nco-turbine-rotor"
    NCO_TURBINE_DYNAMO = "nco-turbine-dynamo"
    QMD_LINEAR = "qmd-linear"
    QMD_SYNCHROTRON = "qmd-synchrotron"
    QMD_NUCLEOSYNTHESIS = "qmd-nucleosynthesis"


def list_components(
        component_set: typing.Annotated[typing.Optional[ComponentSet], typer.Option("-c", "--component-set", help="The set of components to list. Ignored if -C is set.")] = None,
        components_file: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--components", "-C", help="Path to the components file.")] = None,
        output: typing.Annotated[typing.Optional[pathlib.Path], typer.Option("--output", "-O", help="Path to the output file.")] = None,
) -> None:
    """List the components for a multiblock."""
    if isinstance(component_set, type(None)) and isinstance(components_file, type(None)):
        rich.print("[red][bold]ERROR:[/bold] Either --component-set or --components must be set.[/red]")
        raise typer.Exit(code=1)
    if isinstance(components_file, pathlib.Path):
        components = utils.load_component_list(components_file)
    else:
        if component_set == ComponentSet.NCO_TURBINE_ROTOR:
            components = reiuji.designer.overhauled.turbine_rotor.models.DEFAULT_COMPONENTS
        elif component_set == ComponentSet.NCO_TURBINE_DYNAMO:
            components = reiuji.designer.overhauled.turbine_dynamo.models.DEFAULT_COMPONENTS
        elif component_set == ComponentSet.QMD_LINEAR:
            components = reiuji.designer.qmd.linear.models.DEFAULT_COMPONENTS
        elif component_set == ComponentSet.QMD_SYNCHROTRON:
            components = reiuji.designer.qmd.synchrotron.models.DEFAULT_COMPONENTS
        elif component_set == ComponentSet.QMD_NUCLEOSYNTHESIS:
            components = reiuji.designer.qmd.nucleosynthesis.models.DEFAULT_COMPONENTS
        else:
            rich.print("[red][bold]ERROR:[/bold] Invalid component set.[/red]")
            raise typer.Exit(code=1)
    table = rich.table.Table(title="Components")
    table.add_column("Full Name")
    table.add_column("Short Name")
    for comp in components:
        table.add_row(comp.full_name, comp.rich_short_name)
    rich.print(table)
    if isinstance(output, pathlib.Path):
        utils.write_component_list(components, output)
