from ...util.grammar import *
from ...util._constants import decimal
from pyparsing import oneOf, Literal, Word, Optional, Combine, alphas, MatchFirst, delimitedList

def define_plot():
	'''
	Defition of PLOT Keyword
	:returns pyparsing object
	'''

	#  Keyword for PLOT
	plot_keyword = oneOf(["plot", "PLOT"]).setResultsName("plot")

	plot_model_type = (Literal("modelType") + Literal("=")).suppress()
	plot_model_value = Quote + Word(alphas + ' ') + Quote
	_plot_model_values = openBracket + delimitedList(plot_model_value, delim=',', combine=True) + closeBracket
	plot_model_values = MatchFirst([plot_model_value, _plot_model_values]).setResultsName('plot_model_type')

	plot_type = (Literal("plotTypes") + Literal("=")).suppress()
	plot_type_value = Quote + Word(alphas + ' ') + Quote
	_plot_type_values = openBracket + delimitedList(plot_type_value, delim=',', combine=True) + closeBracket
	plot_type_values = MatchFirst([plot_type_value, _plot_type_values]).setResultsName('plot_type_values')

	plot = plot_keyword + openParen + plot_model_type + plot_model_values + ocomma + plot_type + plot_type_values + closeParen 

	return plot
