from logging import log
import unittest
import os
import sys


class OelintBBClassTest(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "testlayer/recipes-foo/recipe-foo_1.0.bb")
    RECIPE_MULTILINEINHERIT = os.path.join(os.path.dirname(__file__), "testlayer/recipes-foo/recipe-foo_2.0.bb")
    RECIPE_WITHPATHS = os.path.join(os.path.dirname(__file__), "testlayer/recipes-foo/recipe-foo_3.0.bb")
    RECIPE_WITHPATHS_NRES = os.path.join(os.path.dirname(__file__), "testlayer/recipes-foo/recipe-foo_3.1.bb")
    RECIPE_GLOBAL = os.path.join(os.path.dirname(__file__), "testlayer/recipes-foo/recipe-bar_1.0.bb")
    RECIPE_RECIPE = os.path.join(os.path.dirname(__file__), "testlayer/recipes-foo/recipe-baz_1.0.bb")

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

    def test_var_a_global(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE_GLOBAL)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="FOO_A")
        self.assertTrue(_stash, msg="Stash has no items")

        _found = False
        for item in _stash:
            if item.Origin.endswith("global-foo.bbclass"):
                _found = True
                break

        self.assertTrue(_found, msg="No element of a layer bbclass was added")

    def test_var_a_recipe(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE_RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="FOO_A")
        self.assertTrue(_stash, msg="Stash has no items")

        _found = False
        for item in _stash:
            if item.Origin.endswith("recipe-foo.bbclass"):
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

    def test_multiitem_inherit(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE_MULTILINEINHERIT)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue=["A", "B"])
        self.assertEqual(len(_stash), 2, msg="Stash has items")

    def test_inherit_filepaths(self):
        from oelint_parser.cls_item import Inherit
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE_WITHPATHS)

        _stash = self.__stash.GetItemsFor(classifier=Inherit.CLASSIFIER)

        self.assertEqual(len(_stash), 1, msg="Stash has items")

        inh_item: Inherit = _stash[0]

        self.assertIn(os.path.join(os.path.dirname(__file__), "testlayer/classes/foo.bbclass"), inh_item.FilePaths)
        self.assertIn(os.path.join(os.path.dirname(__file__), "testlayer/classes-recipe/recipe-foo.bbclass"), inh_item.FilePaths)

    def test_inherit_filepaths_non_resolve(self):
        from oelint_parser.cls_item import Inherit
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintBBClassTest.RECIPE_WITHPATHS_NRES)

        _stash = self.__stash.GetItemsFor(classifier=Inherit.CLASSIFIER)

        self.assertEqual(len(_stash), 1, msg="Stash has items")

        inh_item: Inherit = _stash[0]

        self.assertEqual(len(inh_item.FilePaths), 0)


if __name__ == "__main__":
    unittest.main()
