import unittest
import os
import sys


class OelintParserSyntaxIssuesTest(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "test-recipe-wrong-syntax_1.0.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_pythonblock(self):
        from oelint_parser.cls_item import PythonBlock
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserSyntaxIssuesTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=PythonBlock.CLASSIFIER)
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.FuncName, 'do-foo')

    def test_task(self):
        from oelint_parser.cls_item import Function
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserSyntaxIssuesTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Function.CLASSIFIER)
        self.assertTrue(_stash, msg='Stash has no items')

        for x in _stash:
            self.assertEqual(x.FuncName, 'do-bar')

    def test_addtask(self):
        from oelint_parser.cls_item import TaskAdd
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserSyntaxIssuesTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=TaskAdd.CLASSIFIER)
        self.assertTrue(_stash, msg='Stash has no items')

        for x in _stash:
            self.assertEqual(x.FuncName, 'do-bar')

    def test_deltask(self):
        from oelint_parser.cls_item import TaskDel
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserSyntaxIssuesTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=TaskDel.CLASSIFIER)
        self.assertTrue(_stash, msg='Stash has no items')

        for x in _stash:
            self.assertEqual(x.FuncName, 'do-bar')

    def test_urlparse(self):
        from oelint_parser.cls_item import TaskDel
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()

        res = self.__stash.GetScrComponents('http://foo.bar/baz.git;test1=1;test2=2')

        assert "scheme" in res
        assert "src" in res
        assert "options" in res

        assert "http" == res["scheme"]
        assert "foo.bar/baz.git" == res["src"]
        assert "test1" in res["options"]
        assert "test2" in res["options"]

        res = self.__stash.GetScrComponents("file://${@'.'.join(d.getVar('LINUX_VERSION').split('.')[0:2])};test1=1;test2=2")

        assert "scheme" in res
        assert "src" in res
        assert "options" in res

        assert not res["scheme"]
        assert not res["src"]
        assert "test1" not in res["options"]
        assert "test2" not in res["options"]
