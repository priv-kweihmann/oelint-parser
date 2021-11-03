import unittest
import os
import sys

class OelintParserImageTest(unittest.TestCase):

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_constant_interfaces(self):
        from oelint_parser.constants import Constants

        _const = Constants()
        assert (any(_const.VariablesKnown))
        assert (any(_const.VariablesMandatory))
        assert (any(_const.VariablesOrder))
        assert (any(_const.VariablesProtected))
        assert (any(_const.VariablesProtectedAppend))
        assert (any(_const.VariablesSuggested))
        assert (any(_const.FunctionsKnown))
        assert (any(_const.FunctionsOrder))
        assert (any(_const.DistrosKnown))
        assert (any(_const.MachinesKnown))
        assert (any(_const.MirrorsKnown))
        assert (any(_const.SetsBase))

    def test_singleton_classes(self):
        from oelint_parser.constants import CONSTANTS, Constants

        assert(isinstance(CONSTANTS, Constants))

    def test_rulefile(self):
        from oelint_parser.constants import Constants

        _constants = {
            "known_machines": [
                "libcrypto"
            ],
            "known_distros": [
                "libcrypto"
            ],
            "known_vars": [
                "EXTRA_DEPENDS",
                "EXTRA_RDEPENDS",
                "GEMPREFIX",
                "GEM_BUILT_FILE",
                "GEM_DIR",
                "GEM_DISABLE_STRICT_VER",
                "GEM_FILE",
                "GEM_FILENAME",
                "GEM_HOME",
                "GEM_INSTALL_FLAGS",
                "GEM_NAME",
                "GEM_PATH",
                "GEM_SPEC_CACHE",
                "GEM_SPEC_FILE",
                "GEM_SPEC_FILENAME",
                "GEM_SRC",
                "GEM_VERSION",
                "RUBY_SITEDIR"
            ],
            "oelint.foo.bar": "info"
        }

        _const = Constants()
        _const.AddFromRuleFile(_constants)

        assert ("GEM_FILE" in _const.VariablesKnown)
        assert ("libcrypto" in _const.DistrosKnown)
        assert ("libcrypto" in _const.MachinesKnown)

    def test_constantfile(self):
        from oelint_parser.constants import Constants

        _constants = {
            "known_machines": [
                "libcrypto"
            ],
            "known_distros": [
                "libcrypto"
            ],
            "known_vars": [
                "EXTRA_DEPENDS",
                "EXTRA_RDEPENDS",
                "GEMPREFIX",
                "GEM_BUILT_FILE",
                "GEM_DIR",
                "GEM_DISABLE_STRICT_VER",
                "GEM_FILE",
                "GEM_FILENAME",
                "GEM_HOME",
                "GEM_INSTALL_FLAGS",
                "GEM_NAME",
                "GEM_PATH",
                "GEM_SPEC_CACHE",
                "GEM_SPEC_FILE",
                "GEM_SPEC_FILENAME",
                "GEM_SRC",
                "GEM_VERSION",
                "RUBY_SITEDIR"
            ]
        }

        _const = Constants()
        _const.AddFromConstantFile(_constants)

        assert ("EXTRA_DEPENDS" in _const.VariablesKnown)
        assert ("libcrypto" in _const.DistrosKnown)
        assert ("libcrypto" in _const.MachinesKnown)

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

if __name__ == "__main__": 
    unittest.main()
