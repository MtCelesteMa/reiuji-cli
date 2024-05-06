"""A command line interface for Reiuji."""

from . import lister
from . import designer

import typer


app = typer.Typer(name="reiuji")
app.add_typer(lister.lister_app, name="list")
app.add_typer(designer.designer_app, name="design")
