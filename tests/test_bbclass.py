from logging import log
import unittest
import os
import sys

class OelintBBClassTest(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "testlayer/recipes-foo/recipe-foo_1.0.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_stash(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        _stash = self.__stash.AddFile(OelintBBClassTest.RECIPE)
        self.assertTrue(_stash, msg="Stash has no items")

    def test_var_a(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, 
                                          attribute=Variable.ATTR_VAR, 
                                          attributeValue="FOO_A")
        self.assertTrue(_stash, msg="Stash has no items")

        _found = False
        for item in _stash:
            if item.Origin.endswith("foo.bbclass"):
                _found = True
                break

        self.assertTrue(_found, msg="No element of a layer bbclass was added")

    def test_non_layer_inherit(self):
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE)

        _stash = self.__stash.GetItemsFor()
        for item in _stash:
            self.assertFalse(item.Origin.endswith("foo-foreign.bbclass"), 
                             msg="A element of a non-layer bbclass was added")

    def test_export_functions(self):
        from oelint_parser.cls_item import FunctionExports
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=FunctionExports.CLASSIFIER)
        self.assertTrue(_stash, msg="Stash has no items")
        self.assertEqual(_stash[0].FuncNames, "do_install do_somenotexistingtask")
        self.assertEqual(_stash[0].get_items(), ["do_install", "do_somenotexistingtask"])
        self.assertEqual(_stash[0].get_items_unaliased(), ["foo-do_install", "foo-do_somenotexistingtask"])
        self.assertEqual(_stash[0].IsFromClass, True)

    def test_isfromclass(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, 
                                          attribute=Variable.ATTR_VAR, 
                                          attributeValue="B")
        self.assertTrue(_stash, msg="Stash has no items")
        self.assertEqual(_stash[0].IsFromClass, False)

if __name__ == "__main__": 
    unittest.main()