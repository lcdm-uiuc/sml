"""
Performs logic to handle the load keyword from ML-SQL language
"""
from .modelIO import load_model
from ...utils.filepath import is_sml_file
from os.path import isfile

def handle_load(filename):
	#Check if the file exists
	if is_sml_file(filename):
		print("Loading model from: '" + filename + "'")
		model = load_model(filename)
		return model
	else:
		print("Filename: '" + filename + "' does not have a .mlsql extension")
		return None
