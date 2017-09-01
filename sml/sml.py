import sys
from .parser.parser import smlparser
from .connector.connector import handle

def execute(command, verbose=False):
	"""
	Used to parse and execute a SMLL command supplied by the user.
	This function is meant to exported for use in other modules.
	"""
	myparser = smlparser()
	result = myparser.parseString(command)
	return handle(result, verbose)



def repl(verbose=False):
	"""
	Used to create a read-evaluate-print-loop sequence for the SMLL langauge.
	This function will continually parse and execute user input from command
	line until the word exit is typed.
	"""
	print("Initializing Parser...")
	myparser = smlparser()

	print("SML Parser is ready for use")

	while True:
		command = input(">")
		if command.lower() == "exit":
			print("Exiting SML")
			break
		else:
			result = myparser.parseString(command)
			handle(result, verbose)

if __name__ == "__main__":
	repl()
