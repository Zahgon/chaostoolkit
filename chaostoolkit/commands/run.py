import json
import logging
from typing import Any, Dict, List, Optional

import click
from chaoslib import __version__ as chaoslib_version
from chaoslib import convert_vars, merge_vars
from chaoslib.control import load_global_controls
from chaoslib.exceptions import ChaosException, InvalidSource
from chaoslib.experiment import ensure_experiment_is_valid, run_experiment
from chaoslib.loader import load_experiment
from chaoslib.notification import (
    RunFlowEvent,
    notify,
)
from chaoslib.settings import (
    load_settings,
)
from chaoslib.types import (
    Dry,
    Journal,
    Schedule,
)

from chaostoolkit import encoder
from chaostoolkit.check import (
    check_hypothesis_strategy_spelling,
)

DEFAULT_ROLLBACK_STRATEGY = "default"
DEFAULT_HYPOTHESIS_STRATEGY = "default"
logger = logging.getLogger("chaostoolkit")


def validate_vars(
    ctx: click.Context, param: click.Option, value: List[str]
) -> Dict[str, Any]:
    """
    Process all `--var key=value` and return a dictionary of them with the
    value converted to the appropriate type.
    """
    pass


@click.command()
@click.option(
    "--journal-path",
    default="./journal.json",
    help="Path where to save the journal from the execution.",
)
@click.option(
    "--dry",
    type=click.Choice(["probes", "actions", "activities", "pause"]),
    show_default=False,
    help="Run the experiment without executing the chosen strategy.",
)
@click.option(
    "--no-validation",
    is_flag=True,
    help="Do not validate the experiment before running.",
)
@click.option(
    "--no-verify-tls", is_flag=True, help="Do not verify TLS certificate."
)
@click.option(
    "--rollback-strategy",
    show_default=False,
    help="Rollback runtime strategy. Default is to never play them "
    "on interruption or failed hypothesis.",
    type=click.Choice(["default", "always", "never", "deviated"]),
)
@click.option(
    "--var",
    multiple=True,
    callback=validate_vars,
    help="Specify substitution values for configuration only. Can "
    "be provided multiple times. The pattern must be "
    "key=value or key:type=value. In that latter case, the "
    "value will be casted as the specified type. Supported "
    "types are: int, float, bytes. No type specified means "
    "a utf-8 decoded string.",
)
@click.option(
    "--var-file",
    multiple=True,
    type=click.Path(exists=True),
    help="Specify files that contain configuration and secret "
    "substitution values. Either as a json/yaml payload where "
    "each key has a value mapping to a configuration entry. "
    "Or a .env file defining environment variables. "
    "Can be provided multiple times.",
)
@click.option(
    "--control-file",
    multiple=True,
    type=click.Path(exists=True),
    help="Specify files that can contain controls definitions "
    "that will be loaded as global controls at startup. So before "
    "the experiment was even loaded.",
)
@click.option(
    "--hypothesis-strategy",
    type=click.Choice(
        [
            "default",
            "before-method-only",
            "after-method-only",
            "during-method-only",
            "continuously",
            "continously",
        ],
        case_sensitive=True,
    ),
    help="Strategy to execute the hypothesis during the run.",
)
@click.option(
    "--hypothesis-frequency",
    default=1.0,
    type=float,
    help="Pace at which running the hypothesis. "
    "Only applies when strategy is either: "
    "during-method-only or continuously",
)
@click.option(
    "--fail-fast",
    is_flag=True,
    default=False,
    help="When running in the during-method-only or continuous "
    "strategies, indicate the hypothesis can fail the "
    "experiment as soon as it deviates once. Otherwise, keeps "
    "running until the end of the experiment.",
)
@click.argument("source")
@click.pass_context
def run(
    ctx: click.Context,
    source: str,
    journal_path: str = "./journal.json",
    dry: Optional[str] = None,
    no_validation: bool = False,
    no_exit: bool = False,
    no_verify_tls: bool = False,
    rollback_strategy: str = None,
    var: Dict[str, Any] = None,
    var_file: List[str] = None,
    control_file: List[str] = None,
    hypothesis_strategy: Optional[str] = None,
    hypothesis_frequency: float = 1.0,
    fail_fast: bool = False,
) -> Journal:
    """Run the experiment loaded from SOURCE, either a local file or a
    HTTP resource. SOURCE can be formatted as JSON or YAML."""
    pass
