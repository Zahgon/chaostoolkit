import logging

import click

from chaoslib.exceptions import ChaosException, InvalidSource
from chaoslib.experiment import ensure_experiment_is_valid
from chaoslib.loader import load_experiment
from chaoslib.notification import (
    ValidateFlowEvent,
    notify,
)
from chaoslib.types import Experiment
from chaoslib.settings import load_settings

logger = logging.getLogger("chaostoolkit")


@click.command()
@click.option(
    "--no-verify-tls", is_flag=True, help="Do not verify TLS certificate."
)
@click.argument("source")
@click.pass_context
def validate(
    ctx: click.Context, source: str, no_verify_tls: bool = False
) -> Experiment:
    """Validate the experiment at SOURCE."""
    pass
