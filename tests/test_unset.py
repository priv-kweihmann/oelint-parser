import unittest
import os
import sys


class OelintParserUnset(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "test-unset.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_expand_with_unset(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserUnset.RECIPE)

        res = self.__stash.ExpandVar(OelintParserUnset.RECIPE, attribute=Variable.ATTR_VAR, attributeValue='A')
        
        self.assertEqual(['3', '2'], res.get('A'))
