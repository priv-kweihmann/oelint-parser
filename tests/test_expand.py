import os
import tempfile
import textwrap
import unittest


class OelintLinking(unittest.TestCase):

    def _create_tempfile(self, _input):
        self.__created_files = getattr(self, '__created_files', {})
        self._collected_tmpdirs = getattr(self, '_collect_tmpdirs', [])
        self._tmpdir = getattr(self, '_tmpdir', tempfile.mkdtemp())
        self._collected_tmpdirs.append(self._tmpdir)
        _file = 'testfile.bb'
        _path = os.path.join(self._tmpdir, _file)
        os.makedirs(os.path.dirname(_path), exist_ok=True)

        with open(_path, 'w') as o:
            _cnt = textwrap.dedent(_input).lstrip('\n')
            self.__created_files[_file] = _cnt
            o.write(_cnt)
            setattr(self, '__created_files', self.__created_files)
        return _path

    def test_expand_ref_other(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            B = "${@some.function(d, foo)}"
            A = "${B}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        _stash: list[Variable] = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                                          attribute=Variable.ATTR_VAR,
                                                          attributeValue="A")
        self.assertTrue(_stash, msg="Stash has no items")
        for item in _stash[0].get_items():
            self.assertEqual(self.__stash.ExpandTerm(_file, item), '${@some.function(d, foo)}/abc')

    def test_expand_inline_block(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            A = "${@some.function(d, foo)}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        _stash: list[Variable] = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                                          attribute=Variable.ATTR_VAR,
                                                          attributeValue="A")
        self.assertTrue(_stash, msg="Stash has no items")
        for item in _stash[0].get_items():
            self.assertEqual(self.__stash.ExpandTerm(_file, item, objref=_stash[0]), '${@some.function(d, foo)}/abc')

    def test_expand_multiple_inline_block(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            A = "${@some.function(d, foo)}/abc ${@some.function2(d, foo)}/def"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        _stash: list[Variable] = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                                          attribute=Variable.ATTR_VAR,
                                                          attributeValue="A")
        self.assertTrue(_stash, msg="Stash has no items")
        for item in _stash[0].get_items():
            self.assertEqual(self.__stash.ExpandTerm(
                _file, item, objref=_stash[0]), '${@some.function(d, foo)}/abc ${@some.function2(d, foo)}/def')

    def test_expand_nested_ref(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            B = "200"
            C = "${@some.function(d, foo)}/${B}"
            A = "${C}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        _stash: list[Variable] = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                                          attribute=Variable.ATTR_VAR,
                                                          attributeValue="A")
        self.assertTrue(_stash, msg="Stash has no items")
        for item in _stash[0].get_items():
            self.assertEqual(self.__stash.ExpandTerm(_file, item, objref=_stash[0]), '${@some.function(d, foo)}/200/abc')

    def test_expand_nested_python_ref(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            B = "200"
            C = "${@some.function(d, d.getVar('B'))}"
            A = "${C}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        _stash: list[Variable] = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                                          attribute=Variable.ATTR_VAR,
                                                          attributeValue="A")
        self.assertTrue(_stash, msg="Stash has no items")
        for item in _stash[0].get_items():
            self.assertEqual(self.__stash.ExpandTerm(_file, item, objref=_stash[0]), '${@some.function(d, 200)}/abc')

    def test_expand_file_ref(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            C = "${@some.function(d, d.getVar('FILE'))}"
            A = "${C}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        _stash: list[Variable] = self.__stash.GetItemsFor(classifier=Variable.CLASSIFIER,
                                                          attribute=Variable.ATTR_VAR,
                                                          attributeValue="A")
        self.assertTrue(_stash, msg="Stash has no items")
        for item in _stash[0].get_items():
            self.assertEqual(self.__stash.ExpandTerm(_file, item, objref=_stash[0]), f'${{@some.function(d, "{_file}")}}/abc')

    def test_expandvar_ref_other(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            B = "${@some.function(d, foo)}"
            A = "${B}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        res = self.__stash.ExpandVar(_file, attribute=Variable.ATTR_VAR, attributeValue='A')
        self.assertEqual(' '.join(res.get('A', '')), '${@some.function(d, foo)}/abc')

    def test_expandvar_inline_block(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            A = "${@some.function(d, foo)}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        res = self.__stash.ExpandVar(_file, attribute=Variable.ATTR_VAR, attributeValue='A')
        self.assertEqual(' '.join(res.get('A', '')), '${@some.function(d, foo)}/abc')

    def test_expandvar_multiple_inline_block(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            A = "${@some.function(d, foo)}/abc ${@some.function2(d, foo)}/def"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        res = self.__stash.ExpandVar(_file, attribute=Variable.ATTR_VAR, attributeValue='A')
        self.assertEqual(' '.join(res.get('A', '')), '${@some.function(d, foo)}/abc ${@some.function2(d, foo)}/def')

    def test_expandvar_nested_ref(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            B = "200"
            C = "${@some.function(d, foo)}/${B}"
            A = "${C}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        res = self.__stash.ExpandVar(_file, attribute=Variable.ATTR_VAR, attributeValue='A')
        self.assertEqual(' '.join(res.get('A', '')), '${@some.function(d, foo)}/200/abc')

    def test_expandvar_nested_python_ref(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            B = "200"
            C = "${@some.function(d, d.getVar('B'))}"
            A = "${C}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        res = self.__stash.ExpandVar(_file, attribute=Variable.ATTR_VAR, attributeValue='A')
        self.assertEqual(' '.join(res.get('A', '')), '${@some.function(d, 200)}/abc')

    def test_expandvar_file_ref(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Variable
        self.__stash = Stash()
        _file = self._create_tempfile(
            '''
            C = "${@some.function(d, d.getVar('FILE'))}"
            A = "${C}/abc"
            ''')
        self.__stash.AddFile(_file)
        self.__stash.Finalize()

        res = self.__stash.ExpandVar(_file, attribute=Variable.ATTR_VAR, attributeValue='A')
        self.assertEqual(' '.join(res.get('A', '')), f'${{@some.function(d, "{_file}")}}/abc')
