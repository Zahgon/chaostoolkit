import os

import click

from chaoslib import __version__ as chaoslib_version
from chaoslib.info import list_extensions
from chaostoolkit import __version__


@click.command()
@click.argument(
    "target",
    type=click.Choice(["core", "settings", "extensions"]),
    metavar="TARGET",
)
@click.pass_context
def info(ctx: click.Context, target: str):
    """Display information about the Chaos Toolkit environment.

    Available targets are:

    * core: display the information about your version of the Chaos Toolkit

    * extensions: display the list of installed extensions and plugins

    * settings: display your current full settings
    """
    pass
