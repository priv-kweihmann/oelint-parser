import os
import shutil
import tempfile
import textwrap


# flake8: noqa S101 - n.a. for test files
class TestBaseClass:

    def create_tempfile(self, _file, _input):
        self.__created_files = getattr(self, '__created_files', {})
        self._collected_tmpdirs = getattr(self, '_collect_tmpdirs', [])
        self._tmpdir = getattr(self, '_tmpdir', tempfile.mkdtemp())
        self._collected_tmpdirs.append(self._tmpdir)
        _path = os.path.join(self._tmpdir, _file)
        os.makedirs(os.path.dirname(_path), exist_ok=True)

        with open(_path, 'w') as o:
            _cnt = textwrap.dedent(_input).lstrip('\n')
            self.__created_files[_file] = _cnt
            o.write(_cnt)
        return _path

    def teardown_method(self):
        if getattr(self, '_collected_tmpdirs', None) is not None:
            for x in self._collected_tmpdirs:
                shutil.rmtree(x, ignore_errors=True)
