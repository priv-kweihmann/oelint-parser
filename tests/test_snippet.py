import pytest  # noqa: I900

from .utils import TestBaseClass


class TestOelintSnippets(TestBaseClass):

    @pytest.mark.parametrize('input_',
                             [
                                 'VAR = "1"',
                                 '''
                                 python do_foo() {
                                    :
                                 }
                                 ''',
                                 '''
                                 fakeroot do_foo() {
                                    :
                                 }
                                 ''',
                                 '''
                                 python fakeroot do_foo() {
                                    :
                                 }
                                 ''',
                                 '''
                                 do_foo() {
                                    :
                                 }
                                 ''',
                                 'inherit foo',
                                 'inherit_defer foo',
                                 'INHERIT += "foo"',
                                 'export foo = 1',
                                 'export foo',
                                 '# foo',
                                 '## foo',
                                 '''
                                 def foo(d):
                                     pass
                                 ''',
                                 'include foo.inc',
                                 'require foo.inc',
                                 'addtask foo before bar',
                                 'addtask foo after bar',
                                 'addtask foo',
                                 'addtask foo before bar after baz',
                                 'addtask foo after baz before bar',
                                 'deltask foo',
                                 'foo[bar] = "baz"',
                                 'EXPORT_FUNCTIONS foo',
                                 'addpylib foo bar',
                                 'unset foo',
                                 'unset foo[bar]'
                             ],
                             )
    def test_item_classification(self, input_):
        from oelint_parser.cls_stash import Stash

        path = self.create_tempfile('test-snippet.bb', input_)

        self.__stash = Stash()
        self.__stash.AddFile(path)

        _stash = self.__stash.GetItemsFor()
        assert len(_stash.data) == 1

    def test_handler_after_def_blocks(self):
        # 'python ...() {}' event handlers following one or more 'def' helper
        # blocks must still parse as a single Function with the complete body,
        # not be merged with the preceding 'addhandler' line and have the body
        # spill out as loose Items.
        from oelint_parser.cls_item import Function, Item, PythonBlock
        from oelint_parser.cls_stash import Stash

        path = self.create_tempfile(
            'test-handler.bb',
            '''
            def _helper_a(d):
                return d.getVar('A')

            def _helper_b(d):
                return d.getVar('B')

            addhandler myclass_eventhandler
            python myclass_eventhandler() {
                if bb.event.getName(e) == "ConfigParsed":
                    _helper_a(e.data)
            }
            ''',
        )

        self.__stash = Stash()
        self.__stash.AddFile(path)

        _funcs = self.__stash.GetItemsFor(classifier=Function.CLASSIFIER)
        assert len(_funcs) == 1
        assert _funcs[0].FuncName == 'myclass_eventhandler'
        assert _funcs[0].IsPython
        # the whole body, up to the closing brace, belongs to the handler
        assert 'bb.event.getName' in _funcs[0].RealRaw
        assert _funcs[0].RealRaw.rstrip().endswith('}')

        # both helpers stay recognised as Python blocks
        assert len(self.__stash.GetItemsFor(classifier=PythonBlock.CLASSIFIER)) == 2

        # the handler body must not leak out as loose base Items
        _loose = [x for x in self.__stash.GetItemsFor()
                  if type(x) is Item and 'python' in x.RealRaw]
        assert not _loose
