# oelint-parser

![Build status](https://github.com/priv-kweihmann/oelint-parser/workflows/Python%20package/badge.svg)
[![PyPI version](https://badge.fury.io/py/oelint-parser.svg)](https://badge.fury.io/py/oelint-parser)
[![Python version](https://img.shields.io/pypi/pyversions/oelint-parser)](https://img.shields.io/pypi/pyversions/oelint-parser)
[![Downloads](https://img.shields.io/pypi/dm/oelint-parser)](https://img.shields.io/pypi/dm/oelint-parser)

alternative parser for bitbake recipes

## API documentation

Find the full API docs [here](docs/api-documentation.md)

## Examples

```python
from oelint_parser.cls_stash import Stash

# create an stash object
_stash = Stash()

# add any bitbake like file
_stash.AddFile("/some/file")

# Resolves proper cross file dependencies
_stash.Finalize()

# Use _stash.GetItemsFor() method to filter the stash
```

### Get variables from the files

To get variables from the stash object do

```python
from oelint_parser.cls_item import Variable

# get all variables of the name PV from all files
for x in _stash.GetItemsFor(attribute=Variable.ATTR_VAR, attributeValue="PV"):
    print(x)
```

this returns the raw object representation

### Expand raw variables

```python
from oelint_parser.cls_item import Variable
from oelint_parser.helper_files import expand_term

# get all variables of the name PV from all files
for x in _stash.GetItemsFor(attribute=Variable.ATTR_VAR, attributeValue="PV"):
    # raw unexpanded variable
    print(x.VarValue)
    # raw unexpanded variable without quotes
    print(x.VarValueStripped)
    # expanded variable
    print(expand_term(stash, "/some/file", x.VarValueStripped))
    # single items from a list
    print(x.get_items())
    # expanded single items from a list
    print([expand_term(stash, "/some/file", y) for y in x.get_items()])
```

## Working with constants

For this library a few basic sets of constant information, such as basic package definitions, known machines and functions are
needed.
Those can be easily modified, in case you have additional information to add/remove/modify.

The actual database is not accessible by the user, but a few methods in the `oelint_parse.constants.CONSTANT` class do exist.
Each of the method accepts a dictionary with the same key mapping as listed below (multilevel paths are displayed a JSON pointer)

| key                        | type | description                                           | getter for information                                     |
| -------------------------- | ---- | ----------------------------------------------------- | ---------------------------------------------------------- |
| functions/known            | list | known functions                                       | `oelint_parse.constants.CONSTANT.FunctionsKnown`           |
| functions/order            | list | preferred order of core functions                     | `oelint_parse.constants.CONSTANT.FunctionsOrder`           |
| images/known-classes       | list | bbclasses to be known to be used in images            | `oelint_parse.constants.CONSTANT.ImagesClasses`            |
| images/known-variables     | list | variables known to be used in images                  | `oelint_parse.constants.CONSTANT.ImagesVariables`          |
| replacements/machines      | list | known machine overrides                               | `oelint_parse.constants.CONSTANT.MachinesKnown`            |
| replacements/mirrors       | dict | known mirrors                                         | `oelint_parse.constants.CONSTANT.MirrorsKnown`             |
| variables/known            | list | known variables                                       | `oelint_parse.constants.CONSTANT.VariablesKnown`           |
| variables/mandatory        | list | variables mandatory to a recipe                       | `oelint_parse.constants.CONSTANT.VariablesMandatory`       |
| variables/order            | list | preferred order of variables                          | `oelint_parse.constants.CONSTANT.VariablesOrder`           |
| variables/protected        | list | variables not to be used in recipes                   | `oelint_parse.constants.CONSTANT.VariablesProtected`       |
| variables/protected-append | list | variables not to be used in bbappends                 | `oelint_parse.constants.CONSTANT.VariablesProtectedAppend` |
| variables/suggested        | list | suggested variable in a recipe                        | `oelint_parse.constants.CONSTANT.VariablesSuggested`       |
| sets/base                  | dict | base set of variables always used for value expansion | `oelint_parse.constants.CONSTANT.SetsBase`                 |

### Backward compatibility with rule/constant file

Originally offered support for **rule** or **constant** files is offered by the two new methods

* `oelint_parse.constants.CONSTANT.AddFromRuleFile`
* `oelint_parse.constants.CONSTANT.AddFromConstantFile`

**NOTE** these interfaces are considered *legacy* interfaces and will be removed at some point in the future
