import os
import tempfile
import textwrap
import unittest


class OelintLayerPath(unittest.TestCase):

    def _make_layer(self, name):
        # a minimal layer root is a directory that holds conf/layer.conf
        _root = os.path.join(tempfile.mkdtemp(), name)
        os.makedirs(os.path.join(_root, 'conf'), exist_ok=True)
        with open(os.path.join(_root, 'conf', 'layer.conf'), 'w') as o:
            o.write('# test layer\n')
        return _root

    def _write(self, _root, relpath, content=''):
        _path = os.path.join(_root, relpath)
        os.makedirs(os.path.dirname(_path), exist_ok=True)
        with open(_path, 'w') as o:
            o.write(textwrap.dedent(content).lstrip('\n'))
        return _path

    def test_default_has_no_layer_paths(self):
        from oelint_parser.cls_stash import Stash
        _stash = Stash()
        self.assertEqual(_stash.LayerPaths, [])

    def test_layer_paths_are_absolute(self):
        from oelint_parser.cls_stash import Stash
        _stash = Stash(layer_paths=['some/relative/path'])
        self.assertTrue(all(os.path.isabs(x) for x in _stash.LayerPaths))

    def test_find_falls_back_to_layer_path(self):
        # the file lives only in a sister layer, so only a layer_path resolves it
        from oelint_parser.cls_stash import Stash

        _recipe_layer = self._make_layer('meta-consumer')
        _sister_layer = self._make_layer('meta-provider')
        _recipe_dir = os.path.join(_recipe_layer, 'recipes-foo', 'foo')
        os.makedirs(_recipe_dir, exist_ok=True)
        self._write(_sister_layer, 'recipes-foo/foo/foo-common.inc', 'PV = "1.0"\n')

        _stash = Stash(layer_paths=[_sister_layer])
        _found = _stash.FindLocalOrLayer('recipes-foo/foo/foo-common.inc', _recipe_dir)
        self.assertTrue(_found)
        self.assertTrue(os.path.exists(_found))

    def test_find_without_layer_path_misses_sister_layer(self):
        # same setup without layer_paths: the file stays unresolved (opt-in)
        from oelint_parser.cls_stash import Stash

        _recipe_layer = self._make_layer('meta-consumer')
        _sister_layer = self._make_layer('meta-provider')
        _recipe_dir = os.path.join(_recipe_layer, 'recipes-foo', 'foo')
        os.makedirs(_recipe_dir, exist_ok=True)
        self._write(_sister_layer, 'recipes-foo/foo/foo-common.inc', 'PV = "1.0"\n')

        _stash = Stash()
        _found = _stash.FindLocalOrLayer('recipes-foo/foo/foo-common.inc', _recipe_dir)
        self.assertFalse(_found)

    def test_local_dir_still_wins(self):
        # a file present in the recipe dir resolves there even with layer paths
        from oelint_parser.cls_stash import Stash

        _recipe_layer = self._make_layer('meta-consumer')
        _sister_layer = self._make_layer('meta-provider')
        _recipe_dir = os.path.join(_recipe_layer, 'recipes-foo', 'foo')
        os.makedirs(_recipe_dir, exist_ok=True)
        _local = self._write(_recipe_layer, 'recipes-foo/foo/local.inc', '')

        _stash = Stash(layer_paths=[_sister_layer])
        _found = _stash.FindLocalOrLayer('local.inc', _recipe_dir)
        self.assertEqual(_found, _local)


if __name__ == '__main__':
    unittest.main()
