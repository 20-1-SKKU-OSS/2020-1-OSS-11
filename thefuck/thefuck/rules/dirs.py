from difflib import SequenceMatcher

def match(command):
    if SequenceMatcher(None, command.script_parts[0], "dirs").ratio() > 0.6:
        return 1
    else:
        return 0

def get_new_command(command):
    return "dirs"
