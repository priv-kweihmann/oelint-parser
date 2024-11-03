import os
import sys
import unittest


class OelintIncludeBbFiles(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "testlayer/recipes-bar/test_2.bb")
    RECIPE_ALT = os.path.join(os.path.dirname(__file__), "testlayer/recipes-bar/test-alt_2.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_linking(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable

        self.__stash = Stash()
        self.__stash.AddFile(self.RECIPE)
        self.__stash.AddFile(self.RECIPE_ALT)
        self.__stash.Finalize()

        _stash = self.__stash.GetItemsFor(filename=self.RECIPE,
                                          classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="C")
        self.assertTrue(_stash, msg="Stash has items")
        values = sorted({y.VarValueStripped for y in _stash})
        self.assertEqual(values, ["1"])

        _stash = self.__stash.GetItemsFor(filename=self.RECIPE_ALT,
                                          classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="C")
        self.assertTrue(_stash, msg="Stash has items")
        values = sorted({y.VarValueStripped for y in _stash})
        self.assertEqual(values, ["1"])

    def test_include_filename(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Include

        self.__stash = Stash()
        self.__stash.AddFile(self.RECIPE)
        self.__stash.Finalize()

        _stash = self.__stash.GetItemsFor(filename=self.RECIPE,
                                          classifier=Include.CLASSIFIER)
        self.assertTrue(_stash, msg="Stash has items")
        values = sorted({y.FileIncluded for y in _stash})
        expected = [
            os.path.join(os.path.dirname(self.RECIPE), 'test.inc'),
            os.path.join(os.path.dirname(self.RECIPE), 'test2.inc'),
            os.path.join(os.path.dirname(self.RECIPE), 'test3.inc'),
        ]

        assert values == expected


if __name__ == "__main__":
    unittest.main()
