from .grammar import *
from pyparsing import *

#Define list of column numbers in brackets or single column number
column = Word(numbers + ' ')

_columns = delimitedList(column, delim = ',', combine = True)
_list_columns = openBracket + _columns + closeBracket
choice_columns = MatchFirst([column,_list_columns])

#Define a numerical values
decimal = Regex(r'\d*\.?\d*')

#Define a list of column numbers and types
# [{<index>: <numerical, object>}, ]
index_and_type = Combine(Word(numbers + ' ') + ':' + Word(alphas + ' '))
index_and_type_list = delimitedList(index_and_type, combine=True)

word_to_word = Combine(Word(alphas + ' ') + ':' + Word(letters + '.' + ' '))
word_to_word_list = delimitedList(word_to_word, combine=True)


listOptions = ['predictors', 'dtypes']
