from logging import log
import unittest
import os
import sys

class OelintParserTestNew(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "test-recipe-new_1.0.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_stash(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        _stash = self.__stash.AddFile(OelintParserTestNew.RECIPE)
        self.assertTrue(_stash, msg="Stash has no items")

    def test_var_a(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.helper_files import expand_term
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTestNew.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, 
                                          attribute=Variable.ATTR_VAR, 
                                          attributeValue="A")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarValue, '" X"')
            self.assertEqual(x.VarValueStripped, ' X')
            self.assertEqual(x.VarName, 'A')
            self.assertEqual(x.RawVarName, 'A')
            self.assertEqual(x.get_items(), ["X"])
            self.assertEqual(x.SubItems, ["append"])
            self.assertEqual(x.VarOp, " = ")

    def test_var_b(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.helper_files import expand_term
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTestNew.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, 
                                          attribute=Variable.ATTR_VAR, 
                                          attributeValue="B")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarValue, '"X2"')
            self.assertEqual(x.VarValueStripped, 'X2')
            self.assertEqual(x.VarName, 'B')
            self.assertEqual(x.RawVarName, 'B')
            self.assertEqual(x.get_items(), ["X2"])
            self.assertEqual(x.SubItems, ["remove", "qemuall"])
            self.assertEqual(x.VarOp, " = ")

    def test_function(self):
        from oelint_parser.cls_item import Function
        from oelint_parser.helper_files import expand_term
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTestNew.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Function.CLASSIFIER)

        self.assertTrue(_stash, msg="Stash has no items")
        self.assertEqual(_stash[0].IsPython, False)
        self.assertEqual(_stash[0].IsFakeroot, False)
        self.assertEqual(_stash[0].FuncName, "do_example")
        self.assertIn('bbwarn "This is an example warning"', _stash[0].FuncBody)
        self.assertIn("prepend", _stash[0].SubItems)
        self.assertEqual(_stash[0].IsAppend(), True)
        self.assertEqual(_stash[0].FuncBodyStripped, 'bbwarn "This is an example warning"')
        self.assertEqual(_stash[0].GetMachineEntry(), "qemux86-64")

if __name__ == "__main__": 
    unittest.main()