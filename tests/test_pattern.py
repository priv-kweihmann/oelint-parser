import os
import pytest
import json
import logging


@pytest.mark.parametrize('file',
                         [
                             'pattern_var.bb',
                         ],
                         )
def test_pattern(file):
    from oelint_parser.cls_stash import Stash

    _filepath = os.path.join(os.path.dirname(__file__), "pattern", file)
    _expectpath = os.path.join(os.path.dirname(__file__), "pattern", f'{file}.expect')

    __stash = Stash()
    __stash.AddFile(_filepath)
    __stash.Finalize()

    with open(_expectpath) as i:
        _expect = json.load(i)

    for index, item in enumerate(__stash.GetItemsFor()):
        itemval = item.GetAttributes()
        for k, v in _expect[index].items():
            print(f'Checking {index}: {k} - {v}')
            assert k in itemval
            assert itemval[k] == v
