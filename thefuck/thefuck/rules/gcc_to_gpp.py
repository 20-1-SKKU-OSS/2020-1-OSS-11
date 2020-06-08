"""Fixes gcc and g++ command mistake

Example:
gcc foo.cpp
-> g++ foo.cpp

"""
from thefuck.utils import for_app


@for_app('gcc')
def match(command):
    return command.script.endswith('.cpp')


def get_new_command(command):
    return 'g++' + command.script[3:]
