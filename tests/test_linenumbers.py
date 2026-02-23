import pytest  # noqa: I900

from .utils import TestBaseClass

class TestOelintLineNumbers(TestBaseClass):

    FILE_CONTENTS = [
                        (
                        '''
                        ''', 0),
                        (
                        '''
                        A = "1"
                        ''', 1),
                        (
                        '''
                        FOO = "1"

                        BAR = "abc"
                        ''', 3),
                    ]

    @pytest.mark.parametrize('bbappend', FILE_CONTENTS)
    @pytest.mark.parametrize('recipe', FILE_CONTENTS)
    def test_max_line(self, recipe, bbappend):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Item

        self.__stash = Stash()
        recipe_path = self.create_tempfile("myrecipe_3.1.bb", recipe[0])
        self.__stash.AddFile(recipe_path)
        bbappend_path = self.create_tempfile("myrecipe_3.1.bbappend", bbappend[0])
        self.__stash.AddFile(bbappend_path)
        self.__stash.Finalize()

        recipe_items = self.__stash.GetItemsFor(
            attribute=Item.ATTR_ORIGIN,
            attributeValue=recipe_path,
            nolink=True,
        )
        expected = recipe[1]
        assert max((i.Line for i in recipe_items), default=0) == expected, \
                f"Last item in the recipe is on line {expected}"

        bbappend_items = self.__stash.GetItemsFor(
            attribute=Item.ATTR_ORIGIN,
            attributeValue=bbappend_path,
        )
        expected = recipe[1] + bbappend[1] if bbappend[1] else 0
        assert max((i.Line for i in bbappend_items), default=0) == expected, \
                f"Last item in the bbappend is on line {expected}"

    def test_unrelated_recipe(self):
        from oelint_parser.cls_stash import Stash
        from oelint_parser.cls_item import Item

        self.__stash = Stash()
        recipe_path = self.create_tempfile(
            "myrecipe_3.1.bb",
            '''
            A = "21"
            Z = "foo"
            ''')
        self.__stash.AddFile(recipe_path)
        bbappend_path = self.create_tempfile(
            "myrecipe_%.bbappend",
            '''
            FOO = "abc"
            BAR = "xyz"
            BAZ = "123"
            ''')
        self.__stash.AddFile(bbappend_path)
        other_recipe_path = self.create_tempfile(
            "otherrecipe_2.4.bb",
            '''
            M = "42"
            P = "bar"
            Q = "alpha"
            S = "${WORKDIR}/git"
            ''')
        self.__stash.AddFile(other_recipe_path)
        self.__stash.Finalize()

        recipe_items = self.__stash.GetItemsFor(
            attribute=Item.ATTR_ORIGIN,
            attributeValue=recipe_path,
            nolink=True,
        )
        expected = 2
        assert max((i.Line for i in recipe_items), default=0) == expected, \
                f"Last item in the recipe is on line {expected}"

        bbappend_items = self.__stash.GetItemsFor(
            attribute=Item.ATTR_ORIGIN,
            attributeValue=bbappend_path,
        )
        expected = 5
        assert max((i.Line for i in bbappend_items), default=0) == expected, \
                f"Last item in the bbappend is on line {expected}"

        other_recipe_items = self.__stash.GetItemsFor(
            attribute=Item.ATTR_ORIGIN,
            attributeValue=other_recipe_path,
        )
        expected = 4
        assert max((i.Line for i in other_recipe_items), default=0) == expected, \
                f"Last item in the other recipe is on line {expected}"
