"""Utility functions for the Reiuji CLI."""

import enum
import pathlib
import json

import rich
import rich.markup
import pydantic
import reiuji
from ortools.sat.python import cp_model
from ortools.sat import cp_model_pb2


class Facing(enum.StrEnum):
    X = "x"
    Z = "z"


def load_limits(path: pathlib.Path | None) -> dict[str, tuple[int, int]]:
    if isinstance(path, pathlib.Path):
        with path.open("r") as file:
            return json.load(file)
    return {}


def load_component_list(path: pathlib.Path | None) -> list[reiuji.components.types.Component] | None:
    if isinstance(path, pathlib.Path):
        with path.open("r") as file:
            return pydantic.TypeAdapter(list[reiuji.components.types.Component]).validate_json(file.read())
    return None


def write_component_list(components: list[reiuji.components.types.Component], path: pathlib.Path) -> None:
    if path.suffix == ".json":
        with path.open("w") as file:
            file.write(pydantic.TypeAdapter(list[reiuji.components.types.Component]).dump_json(components, indent=4).decode("utf-8"))
    else:
        rich.print(f"[yellow][bold]WARNING:[/bold] Unsupported file format: {path.suffix}[/yellow]")


def format_text_rich(text: str, *, bold: bool = False, italic: bool = False, color: tuple[int, int, int] | None = None, bg_color: tuple[int, int, int] | None = None) -> str:
    tags = []
    if bold:
        tags.append("bold")
    if italic:
        tags.append("italic")
    if not isinstance(color, type(None)):
        tags.append(f"rgb({color[0]},{color[1]},{color[2]})")
    if not isinstance(bg_color, type(None)):
        tags.append(f"on rgb({bg_color[0]},{bg_color[1]},{bg_color[2]})")
    if len(tags) == 0:
        return rich.markup.escape(text)
    return f"[{" ".join(tags)}]{rich.markup.escape(text)}[/{" ".join(tags)}]"


def print_status(status: cp_model_pb2.CpSolverStatus) -> None:
    if status == cp_model.OPTIMAL:
        rich.print("[green][bold]STATUS:[/bold] Optimal solution found[/green]")
    elif status == cp_model.FEASIBLE:
        rich.print("[green][bold]STATUS:[/bold] Solution found[/green]")
    elif status == cp_model.UNKNOWN:
        rich.print("[red][bold]STATUS:[/bold] No solution found[/red]")
    elif status == cp_model.INFEASIBLE:
        rich.print("[red][bold]STATUS:[/bold] No solution exists[/red]")
    else:
        rich.print("[red][bold]STATUS:[/bold] Error[/red]")


def write_design(
        design: reiuji.core.multi_sequence.MultiSequence[reiuji.components.types.Component],
        path: pathlib.Path,
        *,
        schematic_type: str | None = None,
        **kwargs
    ) -> None:
    if path.suffix == ".json":
        with path.open("w") as file:
            file.write(reiuji.io.serialization.SerializableMultiSequence.from_multi_sequence(design).model_dump_json(indent=4))
    elif path.suffix == ".schematic":
        if schematic_type == "accelerator":
            reiuji.io.schematics.accelerator.AcceleratorSchematicWriter(design, **kwargs).write(path)
        elif schematic_type == "nucleosynthesis":
            reiuji.io.schematics.nucleosynthesis.NucleosynthesisSchematicWriter(design, **kwargs).write(path)
        else:
            rich.print("[yellow][bold]WARNING:[/bold] Schematic output is not supported for this designer.[/yellow]")
    else:
        rich.print(f"[yellow][bold]WARNING:[/bold] Unsupported file format: {path.suffix}[/yellow]")
