import os
from thefuck.utils import for_app


@for_app('cat', at_least=1)
def match(command):
    return (
        command.output.startswith('cat: ') and
        'No such file or directory' in command.output
    )


def get_new_command(command):
    return command.script.replace('cat', 'vim', 1)
    #return command.script.replace('head', 'ls', 1)
