from logging import log
import unittest
import os
import sys


class OelintBBAppendsTest(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "testlayer/recipes-appends/test.bb")
    RECIPE_APPEND = os.path.join(os.path.dirname(__file__), "testlayer/recipes-appends/test.bbappend")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_recipe(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        self.__stash.AddFile(OelintBBAppendsTest.RECIPE)
        self.__stash.Finalize()
        self.assertEqual(len(self.__stash.GetLoneAppends()), 0, msg="No lone appends")
        self.assertEqual(len(self.__stash.GetRecipes()), 1, msg="One recipe")

    def test_bbappend(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        self.__stash.AddFile(OelintBBAppendsTest.RECIPE_APPEND)
        self.__stash.Finalize()
        self.assertEqual(len(self.__stash.GetLoneAppends()), 1, msg="One lone appends")
        self.assertEqual(len(self.__stash.GetRecipes()), 0, msg="No recipe")

    def test_bbappend_and_recipe(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        self.__stash.AddFile(OelintBBAppendsTest.RECIPE)
        self.__stash.AddFile(OelintBBAppendsTest.RECIPE_APPEND)
        self.__stash.Finalize()
        self.assertEqual(len(self.__stash.GetLoneAppends()), 0, msg="No lone appends")
        self.assertEqual(len(self.__stash.GetRecipes()), 1, msg="One recipe")


if __name__ == "__main__":
    unittest.main()
