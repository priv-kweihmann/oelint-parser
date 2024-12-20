import unittest
import os
import sys


class OelintParserConf(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "test-conf.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_addpylib(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import AddPylib
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserConf.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=AddPylib.CLASSIFIER)

        print(_stash)

        self.assertEqual(len(_stash), 1, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.Path, '${LAYERDIR}/path/to/somewhere')
            self.assertEqual(item.Namespace, 'foo')

    def test_addfragments(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import AddFragements
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserConf.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=AddFragements.CLASSIFIER)

        print(_stash)

        self.assertEqual(len(_stash), 1, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.Path, 'when/I/grow/up/I/going/to/be/a/full/path')
            self.assertEqual(item.Variable, 'FOO')
            self.assertEqual(item.Flagged, 'BAR')

    def test_includeall(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import IncludeAll
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserConf.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=IncludeAll.CLASSIFIER)

        print(_stash)

        self.assertEqual(len(_stash), 1, msg="Stash has items")

        for item in _stash:
            self.assertEqual(item.File, 'I/wish/I/was/implemented/as/a/well/known/bitbake/handler.conf')
