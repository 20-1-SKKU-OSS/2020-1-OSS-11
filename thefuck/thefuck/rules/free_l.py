from difflib import SequenceMatcher

def match(command):
    if SequenceMatcher(None, command.script_parts[0], "free").ratio() == 1:
        return 1
    else:
        return 0

def get_new_command(command):
    new_cmds = ["free"]
    return [' '.join([new_command] + ["-l"])
            for new_command in new_cmds] 
