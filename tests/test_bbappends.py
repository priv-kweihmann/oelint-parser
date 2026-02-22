from logging import log
import unittest
import os
import sys


class OelintBBAppendsTest(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "testlayer/recipes-appends/test.bb")
    RECIPE_INC = os.path.join(os.path.dirname(__file__), "testlayer/recipes-appends/test.inc")
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

    def test_bbappend_and_recipe_reversed_order(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        self.__stash.AddFile(OelintBBAppendsTest.RECIPE_APPEND)
        self.__stash.AddFile(OelintBBAppendsTest.RECIPE)
        self.__stash.Finalize()
        self.assertEqual(len(self.__stash.GetLoneAppends()), 0, msg="No lone appends")
        self.assertEqual(len(self.__stash.GetRecipes()), 1, msg="One recipe")

    def test_bbappend_doesnt_append_inc(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        self.__stash.AddFile(OelintBBAppendsTest.RECIPE_APPEND)
        self.__stash.Finalize()

        # Python's name mangling forces us to mangle the attribute name ourselves
        stash_map = self.__stash._Stash__map

        inc_linked_to_bbappend = OelintBBAppendsTest.RECIPE_INC in stash_map.get(OelintBBAppendsTest.RECIPE_APPEND, {})
        self.assertTrue(inc_linked_to_bbappend, msg="include file is linked to the bbappend")

        bbappend_linked_to_inc = OelintBBAppendsTest.RECIPE_APPEND in stash_map.get(OelintBBAppendsTest.RECIPE_INC, {})
        self.assertFalse(bbappend_linked_to_inc, msg="bbappend is not linked to the include file")


if __name__ == "__main__":
    unittest.main()
