import sys
from optparse import Values
from typing import List

from libs.pip import cmdoptions
from libs.pip import Command
from libs.pip import SUCCESS
from libs.pip import freeze
from libs.pip import stdlib_pkgs

DEV_PKGS = {"pip", "setuptools", "distribute", "wheel"}


class FreezeCommand(Command):
    """
    Output installed packages in requirements format.

    packages are listed in a case-insensitive sorted order.
    """

    usage = """
      %prog [options]"""
    log_streams = ("ext://sys.stderr", "ext://sys.stderr")

    def add_options(self) -> None:
        self.cmd_opts.add_option(
            "-r",
            "--requirement",
            dest="requirements",
            action="append",
            default=[],
            metavar="file",
            help=(
                "Use the order in the given requirements file and its "
                "comments when generating output. This option can be "
                "used multiple times."
            ),
        )
        self.cmd_opts.add_option(
            "-l",
            "--local",
            dest="local",
            action="store_true",
            default=False,
            help=(
                "If in a virtualenv that has global access, do not output "
                "globally-installed packages."
            ),
        )
        self.cmd_opts.add_option(
            "--user",
            dest="user",
            action="store_true",
            default=False,
            help="Only output packages installed in user-site.",
        )
        self.cmd_opts.add_option(cmdoptions.list_path())
        self.cmd_opts.add_option(
            "--all",
            dest="freeze_all",
            action="store_true",
            help=(
                "Do not skip these packages in the output:"
                " {}".format(", ".join(DEV_PKGS))
            ),
        )
        self.cmd_opts.add_option(
            "--exclude-editable",
            dest="exclude_editable",
            action="store_true",
            help="Exclude editable package from output.",
        )
        self.cmd_opts.add_option(cmdoptions.list_exclude())

        self.parser.insert_option_group(0, self.cmd_opts)

    def run(self, options: Values, args: List[str]) -> int:
        skip = set(stdlib_pkgs)
        if not options.freeze_all:
            skip.update(DEV_PKGS)

        if options.excludes:
            skip.update(options.excludes)

        cmdoptions.check_list_path_option(options)

        for line in freeze(
            requirement=options.requirements,
            local_only=options.local,
            user_only=options.user,
            paths=options.path,
            isolated=options.isolated_mode,
            skip=skip,
            exclude_editable=options.exclude_editable,
        ):
            sys.stdout.write(line + "\n")
        return SUCCESS