import pytest  # noqa: I900

from .utils import TestBaseClass

class TestOelintPackagesDynamic(TestBaseClass):
    def test_packages_dynamic(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Item

        self.__stash = Stash()
        recipe_path = self.create_tempfile(
            "myrecipe_3.1.bb",
            '''
            PACKAGES_DYNAMIC = "^${PN}-lib.* ^foo-"
            RDEPENDS:${PN}-libfoo += "baz"
            RSUGGESTS:myrecipe-libbar += "baz"
            FILES:foo-bar += "baz"
            ''')
        self.__stash.AddFile(recipe_path)
        self.__stash.Finalize()

        assert self.__stash.IsDynamicPackage(recipe_path, "${PN}-libfoo")
        assert self.__stash.IsDynamicPackage(recipe_path, "myrecipe-libfoo")
        assert self.__stash.IsDynamicPackage(recipe_path, "foo-bar")
        assert not self.__stash.IsDynamicPackage(recipe_path, "myrecipe")
