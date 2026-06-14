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

- **attr** - `{"attr": NAME}` is equivalent to `getattr(input_data, NAME)`
- **item** - `{"item": KEY}` is equivalent to `input_data[KEY]`

### Expression Query

- **expr** - 

### Value Queries

- **value** - `{"value": VALUE}`
- **variable** - `{"var": [NAME, EXPR]}`

### Functional Queries

- **bool** - `{"bool": null}` is equivalent to `bool(input_data)`
- **len** - `{"len": null}` is equivalent to `len(input_data)`
- **min** - `{"min": KEY}` is equivalent to `min(input_data, key=KEY)`
- **max** - `{"max": KEY}` is equivalent to `max(input_data, key=KEY)`

### Logical Queries

- **AND** - `{"AND": [EXPR, ...]}` is equivalent to `all(EXPR(input_data), ...)`
- **OR** - `{"OR": [EXPR, ...]}` is equivalent to `any(EXPR(input_data), ...)`
- **NOT** -  `{"NOT": [EXPR, ...]}` is equivalent to `not any(EXPR(input_data), ...)`

### Unary Queries

- **true** - `{"true": EXPR}` is equivalent to `bool(EXPR(input_data)) is True`
- **false** - `{"false": EXPR}` is equivalent to `bool(EXPR(input_data)) is False`
- **null** - `{"null": EXPR}` is equivalent to `EXPR(input_data) is None`
- **not_null** - `{"not_null": EXPR}` is equivalent to `EXPR(input_data) is not None`
- **empty** - `{"empty": EXPR}` is equivalent to `EXPR(input_data) in (None, "", [], (), {})`
- **not_empty** - `{"not_empty": EXPR}}` is equivalent to `EXPR(input_data) not in (None, "", [], (), {})`

### Binary Queries

- **==** - `{"==": [LEFT, RIGHT]}` is equivalent to `LEFT == RIGHT`
- **!=** - `{"!=": [LEFT, RIGHT]}` is equivalent to `LEFT != RIGHT`
- **>** - `{">": [LEFT, RIGHT]}` is equivalent to `LEFT > RIGHT`
- **<** - `{"<": [LEFT, RIGHT]}` is equivalent to `LEFT < RIGHT`
- **>=** - `{">=": [LEFT, RIGHT]}` is equivalent to `LEFT >= RIGHT`
- **<=** - `{"<=": [LEFT, RIGHT]}` is equivalent to `LEFT <= RIGHT`
- **in** - `{"in": [LEFT, RIGHT]}` is equivalent to `LEFT in RIGHT`
- **not_in** - `{"not_in": [LEFT, RIGHT]}` is equivalent to `LEFT not in RIGHT`
- **contains** - `{"contains": [LEFT, RIGHT]}` is equivalent to `RIGHT in LEFT`

### Enumerable Queries

- **take** - `{"take": COUNT}` is equivalent to `input_data[:COUNT]`
- **skip** - `{"skip": COUNT}` is equivalent to `input_data[COUNT:]`
- **slice** - `{"slice": [START:STOP:END]}` is equivalent to `input_data[START:STOP:END]`
- **any** - `{"any": EXPR}` is equivalent to `any(EXPR(item) for item in input_data)`
- **all** - `{"all": EXPR}` is equivalent to `all(EXPR(item) for item in input_data)`
- **select** - `{"select": EXPR}` is equivalent to `[EXPR(item) for item in input_data]`
- **many** - `{"many": EXPR}` is equivalent to `[child for item in input_data for child in EXPR(child)]`
- **where** - `{"where": EXPR}` is equivalent to `[item for item in input_data if EXPR(item)]`
- **distinct** - `{"distinct": EXPR}`
- **single** - `{"single": EXPR}`
- **first** - `{"first": EXPR}` is equivalent to `next(item for item in input_data if EXPR(item))`
- **last** - `{"last":  EXPR}}` is equivalent to `next(item for item in reversed(input_data) if EXPR(item))`
- **count** - `{"count": EXPR}` is equivalent to `sum(1 for item in input_data if EXPR(item)`
- **sum** - `{"sum": EXPR}` is equivalent to `sum(EXPR(item) for item in input_data)`
- **avg** - `{"avg": EXPR}` is equivalent to `sum(EXPR(item) for item in input_data) / len(input_data)`


## Requirements

- [Python 3.11+](https://www.python.org)


## Disclaimer

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
