import unittest
import os
import sys


class OelintParserImageTest(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_constant_interfaces(self):
        from oelint_parser.constants import Constants

        _const = Constants()
        assert _const.VariablesKnown == {}
        assert _const.FunctionsKnown == []
        assert (any(_const.FunctionsOrder))
        assert (any(_const.DistrosKnown))
        assert _const.MachinesKnown == []
        assert (any(_const.MirrorsKnown))
        assert (any(_const.SetsBase))

    def test_singleton_classes(self):
        from oelint_parser.constants import CONSTANTS, Constants

        assert (isinstance(CONSTANTS, Constants))

    def test_remove(self):
        from oelint_parser.constants import Constants

        _remkeys = {
            "functions": {
                "order": ["do_fetch"]
            }
        }

        _const = Constants()
        assert ("do_fetch" in _const.FunctionsOrder)
        _const.RemoveConstants(_remkeys)
        assert ("do_fetch" not in _const.FunctionsOrder)
        assert (len(_const.FunctionsOrder) > 1)

    def test_add(self):
        from oelint_parser.constants import Constants

        _addkeys = {
            "functions": {
                "order": ["do_foo"]
            }
        }
        _const = Constants()
        assert ("do_foo" not in _const.FunctionsOrder)
        _const.AddConstants(_addkeys)
        assert ("do_foo" in _const.FunctionsOrder)
        assert (len(_const.FunctionsOrder) > 1)

    def test_override(self):
        from oelint_parser.constants import Constants

        _keys = {
            "functions": {
                "order": ["do_foo"]
            }
        }
        _const = Constants()
        assert (len(_const.FunctionsOrder) > 1)
        _const.OverrideConstants(_keys)
        assert (["do_foo"] == list(_const.FunctionsOrder))

    def test_add_custom(self):
        from oelint_parser.constants import Constants

        _addkeys = {
            "custom": {
                "mykey": ["1"]
            }
        }
        _const = Constants()
        _const.AddConstants(_addkeys)
        assert ("1" in _const.GetByPath('custom/mykey'))
        assert (len(_const.FunctionsOrder) > 1)


if __name__ == "__main__":
    unittest.main()
