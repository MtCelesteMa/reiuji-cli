"""Utility functions for the Reiuji CLI."""

import enum
import pathlib
import json

import rich
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


def load_component_list(path: pathlib.Path | None) -> list[reiuji.core.components.Component] | None:
    if isinstance(path, pathlib.Path):
        with path.open("r") as file:
            component_list = json.load(file)
            return list(reiuji.io.serialization.SerializableMultiSequence(shape=(len(component_list),), seq=component_list).to_multi_sequence().seq)
    return None


def write_component_list(components: list[reiuji.core.components.Component], path: pathlib.Path) -> None:
    if path.suffix == ".json":
        with path.open("w") as file:
            ser = reiuji.io.serialization.SerializableMultiSequence.from_multi_sequence(reiuji.core.multi_sequence.MultiSequence(shape=(len(components),), seq=components))
            json.dump(ser.model_dump()["seq"], file, indent=4)
    else:
        rich.print(f"[yellow][bold]WARNING:[/bold] Unsupported file format: {path.suffix}[/yellow]")


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
        design: reiuji.core.multi_sequence.MultiSequence[reiuji.core.components.Component],
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
