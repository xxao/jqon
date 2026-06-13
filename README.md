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

### Path Query

- **path** - 

### Value Queries

- **value** - `{"value": VALUE}`
- **variable** - `{"var": [NAME, PATH]}`

### Functional Queries

- **bool** - `{"bool": null}` is equivalent to `bool(input_data)`
- **len** - `{"len": null}` is equivalent to `len(input_data)`
- **any** - `{"any": PATH}` is equivalent to `any(PATH(item) for item in input_data)`
- **all** - `{"all": PATH}` is equivalent to `all(PATH(item) for item in input_data)`
- **min** - `{"min": PATH}` is equivalent to `min(input_data, key=lambda x: PATH(x))`
- **max** - `{"max": PATH}` is equivalent to `max(input_data, key=lambda x: PATH(x))`
- **sum** - `{"sum": PATH}` is equivalent to `sum(PATH(item) for item in input_data)`
- **avg** - `{"avg": PATH}` is equivalent to `sum(PATH(item) for item in input_data) / len(input_data)`

### Logical Queries

- **AND** - `{"AND": [PATH, ...]}` is equivalent to `all(PATH(input_data), ...`
- **OR** - `{"OR": [PATH, ...]}` is equivalent to `any(PATH(input_data), ...`
- **NOT** -  `{"NOT": [PATH, ...]}` is equivalent to `not any(PATH(input_data), ...`

### Unary Queries

- **true** - `{"true": PATH}` is equivalent to `bool(PATH(input_data)) is True`
- **false** - `{"false": PATH}` is equivalent to `bool(PATH(input_data)) is False`
- **null** - `{"null": PATH}` is equivalent to `PATH(input_data) is None`
- **not_null** - `{"not_null": PATH}` is equivalent to `PATH(input_data) is not None`
- **empty** - `{"empty": PATH}` is equivalent to `PATH(input_data) in (None, "", [], (), {})`
- **not_empty** - `{"not_empty": PATH}}` is equivalent to `PATH(input_data) not in (None, "", [], (), {})`

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
- **select** - `{"select": PATH}` is equivalent to `[PATH(item) for item in input_data]`
- **many** - `{"many": PATH}` is equivalent to `[child for item in input_data for child in PATH(child)]`
- **where** - `{"where": PATH}` is equivalent to `[item for item in input_data if PATH(item)]`
- **distinct** - `{"distinct": PATH}`
- **single** - `{"single": PATH}`
- **first** - `{"first": PATH}` is equivalent to `next(item for item in input_data if PATH(item))`
- **last** - `{"last":  PATH}}` is equivalent to `next(item for item in reversed(input_data) if PATH(item))`
- **count** - `{"count": PATH}` is equivalent to `sum(1 for item in input_data if PATH(item)`


## Requirements

- [Python 3.11+](https://www.python.org)


## Disclaimer

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
