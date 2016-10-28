# Key Components
## [Parser](https://github.com/UI-DataScience/sml/tree/master/sml/parser)
The parser takes in an SML command and interprets the main actions the command is doing into a python dictionary. This dictionary is passed into the connector
## [Connector](https://github.com/UI-DataScience/sml/tree/master/sml/connector)
The connector takes the dictionary of parsed actions and performs the actions via language drivers

## Language Drivers ([Python](https://github.com/UI-DataScience/sml/tree/master/sml/python))
The language drivers do the heavy lifting of the actual machine learning algorithms/actions.
