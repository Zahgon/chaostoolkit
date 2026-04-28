import json
import logging
import os
from typing import List

import click
import yaml
from chaoslib.discovery.discover import portable_type_name_to_python_type
from chaoslib.notification import (
    InitFlowEvent,
    notify,
)
from chaoslib.types import Activity, Experiment
from chaoslib.settings import load_settings

from chaostoolkit import encoder


logger = logging.getLogger("chaostoolkit")


@click.command()
@click.option(
    "--discovery-path",
    default="./discovery.json",
    help="Path to the discovery outcome.",
    show_default=True,
    type=click.Path(exists=False),
)
@click.option(
    "--experiment-path",
    default="./experiment.json",
    type=click.Path(exists=False),
    help="Path where to save the experiment (.yaml or .json)",
    show_default=True,
)
@click.pass_context
def init(
    ctx: click.Context,
    discovery_path: str = "./discovery.json",  # noqa: C901
    experiment_path: str = "./experiment.json",
) -> Experiment:
    """Initialize a new experiment from discovered capabilities."""
    pass


###############################################################################
# Private functions
###############################################################################
def is_yaml(experiment_path: str) -> bool:
    pass


def add_activities(
    activities: List[Activity],
    pool: List[Activity],  # noqa: C901
    with_tolerance: bool = False,
):
    """
    Add activities to the given pool.
    """
    pass
