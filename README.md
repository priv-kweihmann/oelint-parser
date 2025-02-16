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
    print([_stash.ExpandTerm("/some/file", y, objref=x) for y in x.get_items()])
```

### Filtering

You can filter by multiple items

```python
from oelint_parser.cls_item import Variable

# get all variables of the name PV or BPV from all files
for x in _stash.GetItemsFor(attribute=Variable.ATTR_VAR, attributeValue=["PV", "BPV"]):
    # variable name
    print(x.VarName)
    # raw unexpanded variable
    print(x.VarValue)
    # raw unexpanded variable without quotes
    print(x.VarValueStripped)
```

and you can reduce the list after the initial filtering even more

```python
from oelint_parser.cls_item import Variable

# get all variables of the name PV or BPV from all files if the value is '1.0'
for x in _stash.GetItemsFor(attribute=Variable.ATTR_VAR, attributeValue=["PV", "BPV"]).reduce(
                                attribute=Variable.ATTR_VARVAL, attributeValue=["1.0"]):
    # variable name
    print(x.VarName)
    # raw unexpanded variable -> "1.0"
    print(x.VarValue)
    # raw unexpanded variable without quotes -> 1.0
    print(x.VarValueStripped)
```

but if you need copies from a wider list to smaller lists use

```python
from oelint_parser.cls_item import Variable

_all = _stash.GetItemsFor(attribute=Variable.ATTR_VAR, attributeValue=["PV", "BPV"])
_pv = _stash.Reduce(_all, attribute=Variable.ATTR_VAR, attributeValue="PV")
_bpv = _stash.Reduce(_all, attribute=Variable.ATTR_VAR, attributeValue="BPV")

for x in _pv:
    # variable name
    print(x.VarName)
    # raw unexpanded variable -> "1.0"
    print(x.VarValue)
    # raw unexpanded variable without quotes -> 1.0
    print(x.VarValueStripped)
```

### Expanding a Variable

To get the effective value of a Variable after parsing you can use

```python
from oelint_parser.cls_item import Variable

result_set = _stash.ExpandVar(attribute=Variable.ATTR_VAR, attributeValue=["PV"]):
print(result_set.get('PV'))
```

### Inline branch expansion

By default the parser will expand parsable and known inline blocks (``${@oe.utils.something(...)}``) to the branch
value that would match if the programmed condition is ``true``.

You can invert this selection by setting ``negative_inline`` to ``True`` in the ``Stash`` object.

E.g.

with ``some/file`` being

```text
VAR_1 = "${@bb.utils.contains('BUILDHISTORY_FEATURES', 'image', 'foo', 'bar', d)}"
```

and

```python
from oelint_parser.cls_stash import Stash

# create an stash object
_stash = Stash()

# add any bitbake like file
_stash.AddFile("/some/file")

# Resolves proper cross file dependencies
_stash.Finalize()
```

the ``VAR_1``'s  ``VarValue`` value would be ``foo``.

With

```python
from oelint_parser.cls_stash import Stash

# create an stash object
_stash = Stash(negative_inline=True)

# add any bitbake like file
_stash.AddFile("/some/file")

# Resolves proper cross file dependencies
_stash.Finalize()
```

the ``VAR_1``'s ``VarValue`` value would be ``bar``.

## Working with constants

For this library a few basic sets of constant information, such as basic package definitions, known machines and functions are
needed.
Those can be easily modified, in case you have additional information to add/remove/modify.

The actual database is not directly accessible by the user, but a few methods in the `oelint_parse.constants.CONSTANT` class do exist.
Each of the method accepts a dictionary with the same key mapping as listed below (multilevel paths are displayed a JSON pointer)

| key                        | type | description                                           | getter for information                                     |
| -------------------------- | ---- | ----------------------------------------------------- | ---------------------------------------------------------- |
| functions/known            | list | known functions                                       | `oelint_parse.constants.CONSTANT.FunctionsKnown`           |
| functions/order            | list | preferred order of core functions                     | `oelint_parse.constants.CONSTANT.FunctionsOrder`           |
| images/known-classes       | list | bbclasses to be known to be used in images            | `oelint_parse.constants.CONSTANT.ImagesClasses`            |
| images/known-variables     | list | variables known to be used in images                  | `oelint_parse.constants.CONSTANT.ImagesVariables`          |
| replacements/distros       | list | known distro overrides                                | `oelint_parse.constants.CONSTANT.DistrosKnown`             |
| replacements/machines      | list | known machine overrides                               | `oelint_parse.constants.CONSTANT.MachinesKnown`            |
| replacements/mirrors       | dict | known mirrors                                         | `oelint_parse.constants.CONSTANT.MirrorsKnown`             |
| variables/known            | list | known variables                                       | `oelint_parse.constants.CONSTANT.VariablesKnown`           |
| sets/base                  | dict | base set of variables always used for value expansion | `oelint_parse.constants.CONSTANT.SetsBase`                 |

For additional constants

```python
from oelint_parser.constants import CONSTANTS

CONSTANTS.GetByPath('/-joined path')
```

will offer access

## Contributing

Before any contribution please run the following

```shell
python3 -m venv --clear .env
. .env/bin/activate
pip install -r requirements.txt -r requirements-dev.txt
flake8 oelint_parser/ tests/
pytest
./gendoc.sh
```
