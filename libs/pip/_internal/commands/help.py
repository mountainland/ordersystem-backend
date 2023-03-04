from optparse import Values
from typing import List

from libs.pip import Command
from libs.pip import SUCCESS
from libs.pip import CommandError


class HelpCommand(Command):
    """Show help for commands"""

    usage = """
      %prog <command>"""
    ignore_require_venv = True

    def run(self, options: Values, args: List[str]) -> int:
        from libs.pip import (
            commands_dict,
            create_command,
            get_similar_commands,
        )

        try:
            # 'pip help' with no args is handled by pip.__init__.parseopt()
            cmd_name = args[0]  # the command we need help for
        except IndexError:
            return SUCCESS

        if cmd_name not in commands_dict:
            guess = get_similar_commands(cmd_name)

            msg = [f'unknown command "{cmd_name}"']
            if guess:
                msg.append(f'maybe you meant "{guess}"')

            raise CommandError(" - ".join(msg))

        command = create_command(cmd_name)
        command.parser.print_help()

        return SUCCESS
