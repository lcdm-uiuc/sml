---
layout: default
title: Parser
nav_order: 2
---

# Language/Parser
An SML command consists of a list of actions delimited by the (case insensitive) AND keyword
## Actions
An Action consists of the keyword for the action itself along with its options. For example
```
READ "data/auto.csv" (separator = "\s+", header = None)
```
In this case, the action consists of the READ keyword along with its options: filename, separator, header.

The SML parser currently supports the following actions:

#### [READ](https://github.com/UI-DataScience/sml/tree/master/sml/parser/actions/preprocessing)

#### [REPLACE](https://github.com/UI-DataScience/sml/tree/master/sml/parser/actions/preprocessing)

#### [SPLIT](https://github.com/UI-DataScience/sml/tree/master/sml/parser/actions/preprocessing)

#### [CLASSIFY](https://github.com/UI-DataScience/sml/tree/master/sml/parser/actions/algorithms)

#### [CLUSTER](https://github.com/UI-DataScience/sml/tree/master/sml/parser/actions/algorithms)

#### [REGRESS](https://github.com/UI-DataScience/sml/tree/master/sml/parser/actions/algorithms)
