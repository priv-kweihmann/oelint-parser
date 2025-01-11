import unittest
import os
import sys


class OelintParserTest(unittest.TestCase):

    RECIPE = os.path.join(os.path.dirname(__file__), "test-recipe_1.0.bb")
    RECIPE_LAYER = os.path.join(os.path.dirname(__file__), "testlayer/recipes-foo/recipe-foo_1.0.bb")

    def setUp(self):
        sys.path.insert(0, os.path.abspath(os.path.dirname(__file__) + "/../"))

    def test_stash(self):
        from oelint_parser.cls_stash import Stash
        self.__stash = Stash()
        _stash = self.__stash.AddFile(OelintParserTest.RECIPE)
        self.assertTrue(_stash, msg="Stash has no items")

    def test_var(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="LICENSE")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarValue, '"BSD-2-Clause"')
            self.assertEqual(x.VarValueStripped, 'BSD-2-Clause')
            self.assertEqual(x.VarName, 'LICENSE')
            self.assertEqual(x.VarNameComplete, 'LICENSE')
            self.assertEqual(x.Raw, 'LICENSE = "BSD-2-Clause"\n')
            self.assertEqual(x.RawVarName, 'LICENSE')
            self.assertEqual(x.get_items(), ["BSD-2-Clause"])
            self.assertEqual(x.SubItem, "")
            self.assertEqual(x.SubItems, [])
            self.assertEqual(x.VarOp, " = ")
            self.assertEqual(x.GetClassOverride(), "")

    def test_some_var_with_periods(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="SOME.VAR.WITH.PERIODS")
        self.assertTrue(_stash, msg="Stash has no items for SOME.VAR.WITH.PERIODS")

        for x in _stash:
            self.assertEqual(x.VarValue, '"foo"')
            self.assertEqual(x.VarValueStripped, 'foo')
            self.assertEqual(x.VarName, 'SOME.VAR.WITH.PERIODS')
            self.assertEqual(x.VarNameComplete, 'SOME.VAR.WITH.PERIODS')
            self.assertEqual(x.Raw, 'SOME.VAR.WITH.PERIODS = "foo"\n')
            self.assertEqual(x.RawVarName, 'SOME.VAR.WITH.PERIODS')
            self.assertEqual(x.get_items(), ["foo"])
            self.assertEqual(x.SubItem, "")
            self.assertEqual(x.SubItems, [])
            self.assertEqual(x.VarOp, " = ")
            self.assertEqual(x.GetClassOverride(), "")

    def test_var_rdepends(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="RDEPENDS")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarValue, '"foo"')
            self.assertEqual(x.VarValueStripped, 'foo')
            self.assertEqual(x.VarName, 'RDEPENDS')
            self.assertEqual(x.VarNameComplete, 'RDEPENDS_${PN}-test')
            self.assertEqual(x.RawVarName, 'RDEPENDS')
            self.assertEqual(x.get_items(), ["foo"])
            self.assertEqual(x.SubItems, ["${PN}-test"])
            self.assertEqual(x.VarOp, " += ")
            self.assertEqual(x.OverrideDelimiter, "_")

    def test_include(self):
        from oelint_parser.cls_item import Include
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Include.CLASSIFIER)

        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.Raw, "require another_file.inc\n")
            self.assertEqual(x.IncName, "another_file.inc")
            self.assertEqual(x.Statement, "require")

    def test_export(self):
        from oelint_parser.cls_item import Export
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Export.CLASSIFIER)

        self.assertTrue(_stash, msg="Stash has no items")

        _withval = [x for x in _stash if x.Value]
        _woval = [x for x in _stash if not x.Value]
        self.assertTrue(_withval, msg="One item with value exists")
        self.assertTrue(_woval, msg="One item without value exists")

        self.assertEqual(_withval[0].Name, "lib")
        self.assertEqual(_withval[0].Value, "${bindir}/foo")

        self.assertEqual(_woval[0].Name, "PYTHON_ABI")
        self.assertEqual(_woval[0].Value, "")

        self.assertTrue(not any(x.Name in ['something', 'SOMETHING']) for x in _withval)
        self.assertTrue(not any(x.Name in ['something', 'SOMETHING']) for x in _woval)

    def test_FlagAssignment(self):
        from oelint_parser.cls_item import FlagAssignment
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=FlagAssignment.CLASSIFIER,
                                          attribute=FlagAssignment.ATTR_NAME,
                                          attributeValue="do_configure")

        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.Raw, 'do_configure[noexec] = "1"\n')
            self.assertEqual(x.VarName, "do_configure")
            self.assertEqual(x.Value, '"1"')
            self.assertEqual(x.Flag, "noexec")

    def test_pythonblock(self):
        from oelint_parser.cls_item import PythonBlock
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=PythonBlock.CLASSIFIER)

        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.FuncName, "example_function")

    def test_taskadd(self):
        from oelint_parser.cls_item import TaskAdd
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=TaskAdd.CLASSIFIER)

        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.FuncName, "do_example")
            self.assertEqual(x.After, ["do_foo"])
            self.assertEqual(x.Before, ["do_bar"])
            self.assertEqual(x.Comment, "# comment")

    def test_taskdel(self):
        from oelint_parser.cls_item import TaskDel
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=TaskDel.CLASSIFIER)

        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertIn(x.FuncName, ["do_baz", "do_baz2"])
            if x.FuncName == "do_baz":
                self.assertEqual(x.Comment, "# comment")
            elif x.FuncName == "do_baz2":
                self.assertEqual(x.Comment, "")

    def test_function(self):
        from oelint_parser.cls_item import Function
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Function.CLASSIFIER)

        self.assertTrue(_stash, msg="Stash has no items")
        self.assertTrue(any([x for x in _stash if "append" in x.SubItems]))
        self.assertTrue(any([x for x in _stash if "append" not in x.SubItems]))

        x = [x for x in _stash if "append" not in x.SubItems][0]
        self.assertEqual(x.IsPython, False)
        self.assertEqual(x.IsFakeroot, False)
        self.assertEqual(x.FuncName, "do_example")
        self.assertEqual(x.FuncNameComplete, "do_example")
        self.assertIn('bbwarn "This is an example warning"', x.FuncBody)
        self.assertEqual(x.IsAppend(), False)
        self.assertEqual(x.FuncBodyStripped, 'bbwarn "This is an example warning"')
        self.assertEqual(x.GetDistroEntry(), "")
        self.assertEqual(x.GetMachineEntry(), "")

        x = [x for x in _stash if "append" in x.SubItems][0]
        self.assertEqual(x.IsPython, True)
        self.assertEqual(x.IsFakeroot, True)
        self.assertEqual(x.FuncName, "do_something")
        self.assertIn('bb.warn("This is another example warning")', x.FuncBody)
        self.assertEqual(x.IsAppend(), True)
        self.assertEqual(x.FuncBodyStripped, 'bb.warn("This is another example warning")')
        self.assertEqual(x.GetDistroEntry(), "")
        self.assertEqual(x.GetMachineEntry(), "")
        self.assertEqual(x.OverrideDelimiter, "_")

    def test_anon_function(self):
        from oelint_parser.cls_item import Function
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Function.CLASSIFIER)
        self.assertTrue(_stash, msg="Stash has no items")

        _filteredStash = [x for x in _stash if x.FuncName in ["", "__anonymous"]]
        self.assertEqual(len(_filteredStash), 3)

        for item in _filteredStash:
            self.assertEqual(item.IsPython, True)
            self.assertIn(item.FuncName, ["", "__anonymous"])

    def test_varflag(self):
        from oelint_parser.cls_item import FlagAssignment
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=FlagAssignment.CLASSIFIER,
                                          attribute=FlagAssignment.ATTR_NAME,
                                          attributeValue="PACKAGECONFIG")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarName, "PACKAGECONFIG")
            self.assertEqual(x.Flag, "abc")

    def test_multiline(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="SOMELIST")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarName, "SOMELIST")
            self.assertEqual(x.get_items(), ["a", "b", "c"])

    def test_expand(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="SOMEOTHERVAR")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarName, "SOMEOTHERVAR")
            self.assertEqual(self.__stash.ExpandTerm(OelintParserTest.RECIPE,
                                                     x.VarValueStripped), "source/SOMEMORE")
            self.assertNotEqual(x.VarValueStripped, "source/SOMEMORE")

    def test_expand_var(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        res = self.__stash.ExpandVar(OelintParserTest.RECIPE, attribute=Variable.ATTR_VAR, attributeValue='RDEPENDS')

        self.assertIn('RDEPENDS_test-recipe-test', res)

    def test_inlinecodeblock(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="INLINECODEBLOCK")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarName, "INLINECODEBLOCK")
            self.assertEqual(x.VarValueStripped, "systemd-systemctl-native")
            self.assertNotEqual(x.Raw, x.RealRaw)

    def test_lineattributerw(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER)
        self.assertTrue(_stash, msg="Stash has no items")
        try:
            _stash[0].Line = 10000
        except Exception as e:
            self.fail("Setting Line attribute shouldn't raise an exception")

    def test_multiline_no_ml(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="UPSTREAM_CHECK_REGEX")
        self.assertTrue(_stash, msg="Stash has no items")
        self.assertFalse(_stash[0].IsMultiLine(), msg="UPSTREAM_CHECK_REGEX is no multiline")

    def test_multiline_ml(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="SOMELIST")
        self.assertTrue(_stash, msg="Stash has no items")
        self.assertTrue(_stash[0].IsMultiLine(), msg="SOMELIST is a multiline")

    def test_class_target(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="TARGETVAR")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarValueStripped, 'foo')
            self.assertEqual(x.VarName, 'TARGETVAR')
            self.assertEqual(x.GetClassOverride(), 'class-target')

    def test_class_cross(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="CROSSVAR")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarValueStripped, 'foo')
            self.assertEqual(x.VarName, 'CROSSVAR')
            self.assertEqual(x.GetClassOverride(), 'class-cross')

    def test_class_native(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="NATIVEVAR")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarValueStripped, 'foo')
            self.assertEqual(x.VarName, 'NATIVEVAR')
            self.assertEqual(x.GetClassOverride(), 'class-native')

    def test_class_nativesdk(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="SDKVAR")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarValueStripped, 'foo')
            self.assertEqual(x.VarName, 'SDKVAR')
            self.assertEqual(x.GetClassOverride(), 'class-nativesdk')

    def test_distro_from_layer(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.constants import CONSTANTS

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE_LAYER)

        assert 'anotherdistro' in CONSTANTS.DistrosKnown
        assert 'mydistro' in CONSTANTS.DistrosKnown

    def test_machine_from_layer(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.constants import CONSTANTS

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE_LAYER)

        assert 'another-machine' in CONSTANTS.MachinesKnown
        assert 'abc' in CONSTANTS.MachinesKnown

    def test_remove_from_stash(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Export
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Export.CLASSIFIER)

        assert len(_stash) == 2

        print(_stash)

        self.__stash.Remove(_stash)

        _stash = self.__stash.GetItemsFor(classifier=Export.CLASSIFIER)

        assert not any(_stash)

    def test_list_reduce(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Export
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Export.CLASSIFIER)

        assert len(_stash) == 2

        _stash = _stash.reduce(attribute=Export.ATTR_NAME, attributeValue='PYTHON_ABI')

        assert len(_stash) == 1

        _stash = _stash.reduce(attribute=Export.ATTR_NAME, attributeValue='NOT_EXISTING_VALUE')

        assert not any(_stash)

        _stash = self.__stash.GetItemsFor(classifier=Export.CLASSIFIER).reduce(
            attribute=Export.ATTR_NAME, attributeValue='PYTHON_ABI')

        assert len(_stash) == 1

    def test_append_to_stash(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Comment
        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Comment.CLASSIFIER)

        assert len(_stash) == 2

        new_comment = Comment('foo', 1, 1, '# abc', '# def', [])
        self.__stash.Append(new_comment)

        _stash = self.__stash.GetItemsFor(classifier=Comment.CLASSIFIER)

        assert len(_stash) == 3

    def test_inherit(self):
        from oelint_parser.cls_item import Inherit
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Inherit.CLASSIFIER)
        self.assertTrue(_stash, msg="Stash has no items")
        self.assertEqual(len(_stash), 4, msg="Only 4 items are found")
        for x in _stash:
            self.assertIn(x.Class, ['someclass', '${CLASS_TO_INHERIT}', 'foo bar'])

        self.assertTrue(any('inherit_defer' in x.Statement for x in _stash), msg='inherit_defer found')
        self.assertTrue(any('inherit' in x.Statement for x in _stash), msg='inherit found')
        self.assertTrue(any('INHERIT' in x.Statement for x in _stash), msg='INHERIT found')

    def test_multi_filter(self):
        from oelint_parser.cls_item import Variable, Function
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=[Variable.CLASSIFIER, Function.CLASSIFIER])
        self.assertTrue(_stash, msg="Stash has items")
        self.assertTrue(all(isinstance(x, (Function, Variable)) for x in _stash))

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR, attributeValue=['SOMEVAR', 'LICENSE'])
        self.assertTrue(_stash, msg="Stash has items")
        self.assertTrue(all(x.VarName in ['SOMEVAR', 'LICENSE']) for x in _stash)
        self.assertEqual(len(_stash), 3)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=(Variable.ATTR_VAR, Variable.ATTR_VARVALSTRIPPED),
                                          attributeValue='destination')
        self.assertTrue(_stash, msg="Stash has items")
        self.assertTrue(all(x.VarName in ['SOMEVAR', 'YETANOTHERVAR']) for x in _stash)
        self.assertEqual(len(_stash), 2)

    def test_unset(self):
        from oelint_parser.cls_item import Unset
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Unset.CLASSIFIER,
                                          attribute=Unset.ATTR_VARNAME,
                                          attributeValue="Z")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarName, "Z")
            self.assertEqual(x.Flag, "")

        _stash = self.__stash.GetItemsFor(classifier=Unset.CLASSIFIER,
                                          attribute=Unset.ATTR_VARNAME,
                                          attributeValue="A")
        self.assertTrue(_stash, msg="Stash has no items")
        for x in _stash:
            self.assertEqual(x.VarName, "A")
            self.assertEqual(x.Flag, "my-flag")

    def test_varvaluestripped_non_volatile(self):
        from oelint_parser.cls_item import Variable
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                          attribute=Variable.ATTR_VAR,
                                          attributeValue="LICENSE")
        self.assertTrue(_stash, msg="Stash has no items")

        first = _stash[0].VarValueStripped
        # now change
        _stash[0].VarValue = 'abc'

        self.assertNotEqual(_stash[0].VarValueStripped, first)

    def test_function_stripped_non_volatile(self):
        from oelint_parser.cls_item import Function
        from oelint_parser.cls_stash import Stash

        self.__stash = Stash()
        self.__stash.AddFile(OelintParserTest.RECIPE)

        _stash = self.__stash.GetItemsFor(classifier=Function.CLASSIFIER)

        self.assertTrue(_stash, msg="Stash has no items")

        first = _stash[0].FuncBodyStripped
        # now change
        _stash[0].FuncBody = 'abc'

        self.assertNotEqual(_stash[0].FuncBodyStripped, first)


if __name__ == "__main__":
    unittest.main()
