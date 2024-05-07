"""A command line interface for Reiuji."""

from . import lister
from . import designer
from . import converter

import typer


app = typer.Typer(name="reiuji")
app.command("list")(lister.list_components)
app.add_typer(designer.designer_app, name="design")
app.add_typer(converter.converter_app, name="convert")
