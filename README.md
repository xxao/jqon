#  JqON

The *jqon* package was developed to provide a simple way to define queries in JSON format, which can later be run
in Python. It can be utilized in testing automations, where expected output of a system can be submitted a 
predefined set of tests.


## Installation

This package is fully implemented in Python. No additional compiler is necessary. After downloading the source
code just run the following command from the main package folder:

`$ python setup.py install`

or simply by using pip

`$ pip install jqson`


## Available Queries

### Getter Queries

- **attr** - `{"attr": NAME}`
- **item** - `{"item": KEY}`

### Path Query

- **path** - 

### Value Queries

- **value** - `{"value": VALUE}`
- **variable** - `{"var": [NAME, PATH]}`

### Functional Queries

- **bool** - `{"bool": PATH}`
- **len** - `{"len": PATH}`
- **any** - `{"any": PATH}`
- **all** - `{"all": PATH}`
- **min** - `{"min": PATH}`
- **max** - `{"max": PATH}`
- **sum** - `{"sum": PATH}`
- **avg** - `{"avg": PATH}`

### Logical Queries

- **AND** - `{"AND": [PATH, ...]}`
- **OR** - `{"OR": [PATH, ...]}`
- **NOT** -  `{"NOT": [PATH, ...]}`

### Unary Queries

- **true** - `{"true": PATH}`
- **false** - `{"false": PATH}`
- **null** - `{"null": PATH}`
- **not_null** - `{"not_null": PATH}`
- **empty** - `{"empty": PATH}`
- **not_empty** - `{"not_empty": PATH}}`

### Binary Queries

- **==** - `{"==": [LEFT, RIGHT]}`
- **!=** - `{"!=": [LEFT, RIGHT]}`
- **>** - `{">": [LEFT, RIGHT]}`
- **<** - `{"<": [LEFT, RIGHT]}`
- **>=** - `{">=": [LEFT, RIGHT]}`
- **<=** - `{"<=": [LEFT, RIGHT]}`
- **in** - `{"in": [LEFT, RIGHT]}`
- **not_in** - `{"not_in": [LEFT, RIGHT]}`
- **contains** - `{"contains": [LEFT, RIGHT]}`

### Enumerable Queries

- **take** - `{"take": COUNT}`
- **skip** - `{"skip": COUNT}`
- **slice** - `{"slice": [START:STOP:END]}`
- **select** - `{"select": PATH}`
- **many** - `{"many": PATH}`
- **where** - `{"where": PATH}`
- **distinct** - `{"distinct": PATH}`
- **single** - `{"single": PATH}`
- **first** - `{"first": PATH}`
- **last** - `{"last":  PATH}}`
- **count** - `{"count": PATH}`


## Requirements

- [Python 3.11+](https://www.python.org)


## Disclaimer

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
