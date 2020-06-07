from difflib import SequenceMatcher

def match(command):
    if SequenceMatcher(None, command.script_parts[0], "dirs").ratio() == 1:
        return 0
    if SequenceMatcher(None, command.script_parts[0], "dirs").ratio() > 0.6:
        return 1
    else:
        return 0

def get_new_command(command):
    new_cmds = ["dirs"]
    return [' '.join([new_command] + command.script_parts[1:])
            for new_command in new_cmds]
