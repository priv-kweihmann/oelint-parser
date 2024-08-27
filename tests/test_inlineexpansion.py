from typing import List
import pytest  # noqa: I900

from .utils import TestBaseClass


class TestOelintInlineexpansion(TestBaseClass):

    @pytest.mark.parametrize('input_',
                             [
                                 ('VAR = "1"', False, 'VAR = "1"'),
                                 ('VAR = "1"', True, 'VAR = "1"'),
                                 ('${@bb.utils.filter(\'TUNE_FEATURES\', \'spe\', d)}', False, 'TUNE_FEATURES'),
                                 ('${@bb.utils.filter(\'TUNE_FEATURES\', \'spe\', d)}', True, ''),
                                 ('${@bb.utils.contains(\'BUILDHISTORY_FEATURES\', \'image\', \'1\', \'0\', d)}', False, '1'),
                                 ('${@bb.utils.contains(\'BUILDHISTORY_FEATURES\', \'image\', \'1\', \'0\', d)}', True, '0'),
                                 ('${@bb.utils.contains_any(\'TUNE_FEATURES\', \'fpu-hard fpu-hard-extended\', \'fpu-hard\', \'fpu-soft\', d)}', False, 'fpu-hard'),
                                 ('${@bb.utils.contains_any(\'TUNE_FEATURES\', \'fpu-hard fpu-hard-extended\', \'fpu-hard\', \'fpu-soft\', d)}', True, 'fpu-soft'),
                                 ('${@oe.utils.conditional(\'SITEINFO_ENDIANNESS\', \'le\', \'-l\', \'-b\', d)}', False, '-l'),
                                 ('${@oe.utils.conditional(\'SITEINFO_ENDIANNESS\', \'le\', \'-l\', \'-b\', d)}', True, '-b'),
                                 ('${@oe.utils.ifelse(d.getVar(\'PACKAGE_ARCH_EXPANDED\') == \'all\', \'allarch\', \'noarch\')}', False, 'allarch'),
                                 ('${@oe.utils.ifelse(d.getVar(\'PACKAGE_ARCH_EXPANDED\') == \'all\', \'allarch\', \'noarch\')}', True, 'noarch'),
                                 ('${@ oe.utils.any_distro_features(d, "foo bar")}', False, '1'),
                                 ('${@ oe.utils.any_distro_features(d, "foo bar")}', True, ''),
                                 ('${@ oe.utils.any_distro_features(d, "foo bar", "foo-or-bar.inc")}', False, 'foo-or-bar.inc'),
                                 ('${@ oe.utils.any_distro_features(d, "foo bar", "foo-or-bar.inc")}', True, ''),
                                 ('${@ oe.utils.any_distro_features(d, "foo bar", "foo-or-bar.inc", "baz")}', False, 'foo-or-bar.inc'),
                                 ('${@ oe.utils.any_distro_features(d, "foo bar", "foo-or-bar.inc", "baz")}', True, 'baz'),
                                 ('${@ oe.utils.all_distro_features(d, "foo bar")}', True, ''),
                                 ('${@ oe.utils.all_distro_features(d, "foo bar", "foo-or-bar.inc")}', False, 'foo-or-bar.inc'),
                                 ('${@ oe.utils.all_distro_features(d, "foo bar", "foo-or-bar.inc")}', True, ''),
                                 ('${@ oe.utils.all_distro_features(d, "foo bar", "foo-or-bar.inc", "baz")}', False, 'foo-or-bar.inc'),
                                 ('${@ oe.utils.all_distro_features(d, "foo bar", "foo-or-bar.inc", "baz")}', True, 'baz'),
                                 ('${@oe.utils.vartrue(\'DEBUG_BUILD\', \'1\', \'0\', d)}', False, '1'),
                                 ('${@oe.utils.vartrue(\'DEBUG_BUILD\', \'1\', \'0\', d)}', True, '0'),
                                 ('${@oe.utils.less_or_equal(\'DEBUG_BUILD\', \'2\', \'1\', \'0\', d)}', False, '1'),
                                 ('${@oe.utils.less_or_equal(\'DEBUG_BUILD\', \'2\', \'1\', \'0\', d)}', True, '0'),
                                 ('${@oe.utils.version_less_or_equal(\'DEBUG_BUILD\', \'2\', \'1\', \'0\', d)}', False, '1'),
                                 ('${@oe.utils.version_less_or_equal(\'DEBUG_BUILD\', \'2\', \'1\', \'0\', d)}', True, '0'),
                                 ('${@oe.utils.both_contain(\'VAR_1\', \'VAR_2\', \'1\', d)}', False, '1'),
                                 ('${@oe.utils.both_contain(\'VAR_1\', \'VAR_2\', \'1\', d)}', True, ''),
                             ],
                             )
    def test_inline_expansion(self, input_):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Item

        _cnt, neg, _res = input_

        path = self.create_tempfile('test-snippet.bb', _cnt)

        self.__stash = Stash(negative_inline=neg)
        self.__stash.AddFile(path)

        _stash: List[Item] = self.__stash.GetItemsFor()
        assert len(_stash.data) == 1
        assert _stash[0].Raw == _res
