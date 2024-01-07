import unittest
import os
import sys

class OelintParserImageTest(unittest.TestCase):

    RECIPE_IMAGE = os.path.join(os.path.dirname(__file__), "test-image.bb")
    RECIPE = os.path.join(os.path.dirname(__file__), "test-recipe_1.0")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_stash(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        _stash = self.__stash.AddFile(OelintParserImageTest.RECIPE_IMAGE)
        self.assertTrue(_stash, msg="Stash has no items")

    def test_isimage(self):
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserImageTest.RECIPE_IMAGE)

        self.assertTrue(self.__stash.IsImage(OelintParserImageTest.RECIPE_IMAGE), msg="Recipe is parsed as image")
    
    def test_notisimage(self):
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserImageTest.RECIPE)

        self.assertFalse(self.__stash.IsImage(OelintParserImageTest.RECIPE), msg="Recipe is NOT parsed as image")


if __name__ == "__main__": 
    unittest.main()