"""Fixes gcc and g++ command mistake

Example:
g++ foo.c
-> gcc foo.cpp

"""
from thefuck.utils import for_app


@for_app('gpp')
def match(command):
    return command.script.endswith('.c')


def get_new_command(command):
    return 'gcc' + command.script[3:]
