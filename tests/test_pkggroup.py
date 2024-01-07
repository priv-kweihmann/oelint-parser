import unittest
import os
import sys

class OelintParserPkgGroupTest(unittest.TestCase):

    RECIPE_PKGGROUP = os.path.join(os.path.dirname(__file__), "test-pkggroup.bb")
    RECIPE = os.path.join(os.path.dirname(__file__), "test-recipe_1.0")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_stash(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        _stash = self.__stash.AddFile(OelintParserPkgGroupTest.RECIPE_PKGGROUP)
        self.assertTrue(_stash, msg="Stash has no items")

    def test_ispkggroup(self):
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserPkgGroupTest.RECIPE_PKGGROUP)

        self.assertTrue(self.__stash.IsPackageGroup(OelintParserPkgGroupTest.RECIPE_PKGGROUP), msg="Recipe is parsed as pkggroup")
    
    def test_notispkggroup(self):
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserPkgGroupTest.RECIPE)

        self.assertFalse(self.__stash.IsPackageGroup(OelintParserPkgGroupTest.RECIPE), msg="Recipe is NOT parsed as pkgroup")


if __name__ == "__main__": 
    unittest.main()