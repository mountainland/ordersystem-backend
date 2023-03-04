import logging
from optparse import Values
from typing import List

from libs.pip import Command
from libs.pip import ERROR, SUCCESS
from libs.pip import (
    check_package_set,
    create_package_set_from_installed,
)
from libs.pip import write_output

logger = logging.getLogger(__name__)


class CheckCommand(Command):
    """Verify installed packages have compatible dependencies."""

    usage = """
      %prog [options]"""

    def run(self, options: Values, args: List[str]) -> int:

        package_set, parsing_probs = create_package_set_from_installed()
        missing, conflicting = check_package_set(package_set)

        for project_name in missing:
            version = package_set[project_name].version
            for dependency in missing[project_name]:
                write_output(
                    "%s %s requires %s, which is not installed.",
                    project_name,
                    version,
                    dependency[0],
                )

        for project_name in conflicting:
            version = package_set[project_name].version
            for dep_name, dep_version, req in conflicting[project_name]:
                write_output(
                    "%s %s has requirement %s, but you have %s %s.",
                    project_name,
                    version,
                    req,
                    dep_name,
                    dep_version,
                )

        if missing or conflicting or parsing_probs:
            return ERROR
        else:
            write_output("No broken requirements found.")
            return SUCCESS