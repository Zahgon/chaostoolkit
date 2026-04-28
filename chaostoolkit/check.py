import logging

import requests
from chaoslib.types import Strategy

from chaostoolkit import __version__

__all__ = ["check_newer_version", "check_hypothesis_strategy_spelling"]

LATEST_RELEASE_URL = "https://releases.chaostoolkit.org/latest"
CHANGELOG_URL = "https://github.com/chaostoolkit/chaostoolkit/blob/master/CHANGELOG.md"  # nopep8
logger = logging.getLogger("chaostoolkit")


def check_newer_version(command: str):
    """
    Query for the latest release of the chaostoolkit to compare it
    with the current's version. If the former is higher then issue a warning
    inviting the user to upgrade its environment.
    """
    pass


def check_hypothesis_strategy_spelling(hypothesis_strategy: str) -> Strategy:
    """
    Checking for incorrectly spelt commands supported by
    previous versions of the cli
    """
    pass
