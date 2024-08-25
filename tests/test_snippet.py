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
