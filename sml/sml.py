import sys
from .parser.parser import smlparser
from .connector.connector import handle

def execute(command, verbose=False, web=False):
	"""
	Used to parse and execute a SMLL command supplied by the user.
	This function is meant to exported for use in other modules.
	"""
	myparser = smlparser()
	result = myparser.parseString(command)

	query_result = handle(result, verbose, web)  # Returning results of query for apps that call this

	# KI: Not sure if we should just create a new module or dir for stuff that connects to this function, but web app stuff is below.

	if web:  # If web app is calling this function
		import random
		import string
		def gen_key(): # Used to generate key
			return ''.join(random.SystemRandom().choice(string.ascii_letters + string.digits) for _ in range(512))


		if query_result['metric_summary'] is not None:  # If we generated some plots

			from hashlib import sha512
			filenames = {}
			static_filenames = {}

			for i, img in enumerate(query_result['metric_summary']):
				img_name = sha512(gen_key().encode('utf-8')).hexdigest() # Create 1 time hashes for the name of each image
				filenames[i]  = './static/data/imgs/' + img_name + '.png'  # Relative path to file
				static_filenames[i] = '"/static/data/imgs/' + img_name + '.png"'  # Following static file for python flask
				img.savefig(filenames[i])
			query_result['metric_summary'] = static_filenames # Delete and Replace the matplotlib object with the path to the image
	return query_result


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
