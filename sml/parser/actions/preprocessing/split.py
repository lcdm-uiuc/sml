from ...util.grammar import *
from ...util._constants import decimal, word_to_word_list
from pyparsing import oneOf, Literal, Word, Optional, Combine, delimitedList, MatchFirst

def define_split():
	'''
	Definition of SPLIT Keyword
	:returns pyparsing object
	'''
	#define so that there can be multiple verisions of Split
	splitKeyword = oneOf(["Split", "SPLIT"]).setResultsName("split")
	splitOptions = _define_split_options()

	#Creating Optional Split phrases
	split = splitKeyword + splitOptions

	return split
def _define_split_options():
	#train
	trainPhrase = (CaselessLiteral("train") + Literal("=")).suppress()
	trainS = decimal.setResultsName("train_split")
	training = trainPhrase + trainS

	#test
	testPhrase = (CaselessLiteral("test") + Literal("=")).suppress()
	testS = decimal.setResultsName("test_split")
	testing = testPhrase + testS


	#val
	valPhrase = (CaselessLiteral("validation") + Literal("=")).suppress()
	valS = decimal.setResultsName("validation_split")
	val = valPhrase + valS

	#persist
	persistPhrase = (CaselessLiteral("persist") + Literal("=")).suppress()
	persist_names = word_to_word_list.setResultsName("persist_names_split")
	persist = Optional(persistPhrase + openBracket + persist_names + closeBracket)



	option = MatchFirst([training, testing,val,persist])
	splitOptions = openParen + delimitedList(option, delim=',') + closeParen

	return splitOptions
