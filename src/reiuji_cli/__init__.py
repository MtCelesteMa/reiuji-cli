"""A command line interface for Reiuji."""

from . import designer

import typer


app = typer.Typer(name="reiuji")
app.add_typer(designer.designer_app, name="design")
