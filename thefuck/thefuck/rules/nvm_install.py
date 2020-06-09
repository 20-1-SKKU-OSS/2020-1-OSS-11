from difflib import SequenceMatcher

def match(command):
	if SequenceMatcher(None, command.script_parts[0], "nvm").ratio() > 0.6:
		return 1
	else:
	    return 0

def get_new_command(command):
	new_cmds = ["nvm"]
	return [' '.join(new_command + ["install"]) for new_command in new_cmds] 
