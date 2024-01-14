import unittest
import os
import sys

class OelintParserInlineReplacements(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "test-inline.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_bb_utils_contains(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserInlineReplacements.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, attribute=Variable.ATTR_VAR, attributeValue="VAR_CONTAINS")

        self.assertEqual(len(_stash), 2, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.VarValue, '"true"')
            self.assertEqual(item.VarValueStripped, 'true')

    def test_bb_utils_contains_any(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserInlineReplacements.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, attribute=Variable.ATTR_VAR, attributeValue="VAR_CONTAINS_ANY")

        self.assertEqual(len(_stash), 2, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.VarValue, '"True"')
            self.assertEqual(item.VarValueStripped, 'True')

    def test_oe_utils_conditional(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserInlineReplacements.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, attribute=Variable.ATTR_VAR, attributeValue="VAR_OE_CONDITIONAL")

        self.assertEqual(len(_stash), 2, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.VarValue, '"true"')
            self.assertEqual(item.VarValueStripped, 'true')

    def test_oe_utils_ifelse(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserInlineReplacements.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, attribute=Variable.ATTR_VAR, attributeValue="VAR_OE_IFELSE")

        self.assertEqual(len(_stash), 2, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.VarValue, '"true"')
            self.assertEqual(item.VarValueStripped, 'true')

    def test_bb_utils_filter(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserInlineReplacements.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, attribute=Variable.ATTR_VAR, attributeValue="VAR_BB_FILTER")

        self.assertEqual(len(_stash), 2, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.VarValue, '"true"')
            self.assertEqual(item.VarValueStripped, 'true')

    def test_oe_any_distro_feature(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserInlineReplacements.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER, attribute=Variable.ATTR_VAR, attributeValue="VAR_ANY_DISTRO_FEATURE")

        self.assertEqual(len(_stash), 2, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.VarValue, '"true"')
            self.assertEqual(item.VarValueStripped, 'true')