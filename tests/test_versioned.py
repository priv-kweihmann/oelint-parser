import unittest
import os
import sys


class OelintVersionedVarTest(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "test-versioned.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_versioned(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintVersionedVarTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="DEPENDS")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.get_items(versioned=True), ["a", "b", "c"])

    def test_unversioned(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintVersionedVarTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="SOMEVALUE")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertNotEqual(x.get_items(versioned=False), ["a", "b", "c"])
            self.assertNotEqual(x.get_items(), ["a", "b", "c"])
            for y in ["a", "b", "c"]:
                self.assertIn(y, x.get_items())


if __name__ == "__main__":
    unittest.main()
