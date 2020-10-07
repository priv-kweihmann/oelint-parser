# oelint-parser

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
