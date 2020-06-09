from difflib import SequenceMatcher

def match(command):
	if SequenceMatcher(None, command.script_parts[0], "nvm").ratio() > 0.6:
		return 1
	else:
	    return 0

def get_new_command(command):
	new_cmds = ["nvm"]
	nextcommand = []
	for e in command.script_parts[2:]:
		if e.replace('.', '', 2).isdigit():
		    nextcommand.append(e)
		else:
		    nextcommand = ["node"]
		    break	
	return [' '.join([new_command] + ["install"] + nextcommand) for new_command in new_cmds] 
