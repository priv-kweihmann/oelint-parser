import glob
import os

from oelint_parser.cls_item import Item
from oelint_parser.cls_item import Variable
from oelint_parser.constants import CONSTANTS
from oelint_parser.helper_files import expand_term
from oelint_parser.helper_files import get_layer_root
from oelint_parser.helper_files import guess_base_recipe_name
from oelint_parser.helper_files import guess_recipe_name
from oelint_parser.helper_files import guess_recipe_version
from oelint_parser.parser import get_items
from oelint_parser.rpl_regex import RegexRpl


class Stash():

    def __init__(self, quiet=False):
        """constructor
        """
        self.__list = []
        self.__seen_files = set()
        self.__map = {}
        self.__quiet = quiet

    def AddFile(self, _file, lineOffset=0, forcedLink=None):
        """Adds a file to the stash

        Arguments:
            _file {str} -- Full path to file

        Keyword Arguments:
            lineOffset {int} -- Line offset from the file that include this file (default: {0})
            forcedLink {[type]} -- Force link against a file (default: {None})

        Returns:
            list -- List of {oelint_parser.cls_item.Item}
        """
        _, _ext = os.path.splitext(_file)
        if _file in self.__seen_files and _ext not in [".inc"]:
            return []
        if not self.__quiet:
            print("Parsing {file}".format(file=_file))
        self.__seen_files.add(_file)
        res = get_items(self, _file, lineOffset=lineOffset)
        if forcedLink:
            for r in res:
                r.IncludedFrom = forcedLink
            if _file not in self.__map:
                self.__map[_file] = []
            self.__map[_file].append(forcedLink)
            if forcedLink not in self.__map:
                self.__map[forcedLink] = []
            self.__map[forcedLink].append(_file)
        # Match bbappends to bbs
        if _file.endswith(".bbappend"):
            bn_this = os.path.basename(_file).replace(
                ".bbappend", "").replace("%", ".*")
            for item in self.__list:
                if RegexRpl.match(bn_this, os.path.basename(item.Origin)):
                    if _file not in self.__map:
                        self.__map[_file] = []
                    self.__map[_file].append(item.Origin)
                    if item.Origin not in self.__map:
                        self.__map[item.Origin] = []
                    self.__map[item.Origin].append(_file)
                    # find maximum line number of the origin
                    _maxline = max(
                        x.Line for x in self.__list if x.Origin == item.Origin)
                    for r in res:
                        # pretend that we are adding the file to the end of the original
                        r.Line += _maxline
                    break
        self.AddDistroMachineFromLayer(_file)
        self.__list += res
        return res

    def Append(self, item):
        """appends one or mote items to the stash

        Args:
            item (Item): Item(s) to append
        """
        if isinstance(item, (list, tuple)):
            for _item in item:
                self.__list.append(_item)
        else:
            self.__list.append(item)

    def Remove(self, item):
        """removes one or more items from the stash

        Args:
            item (Item): Item(s) to remove
        """
        if isinstance(item, (list, tuple)):
            for _item in item:
                self.__list.remove(_item)
        else:
            self.__list.remove(item)

    def AddDistroMachineFromLayer(self, path):
        _root = get_layer_root(path)
        if _root:
            for conf in glob.glob(os.path.join(_root, "conf", "distro", "*.conf")):
                _fn, _ = os.path.splitext(os.path.basename(conf))
                CONSTANTS.AddConstants({'replacements': {'distros': [_fn]}})
            for conf in glob.glob(os.path.join(_root, "conf", "machine", "*.conf")):
                _fn, _ = os.path.splitext(os.path.basename(conf))
                CONSTANTS.AddConstants({'replacements': {'machines': [_fn]}})

    def Finalize(self):
        # cross link all the files
        for k in self.__map.keys():
            for item in self.__map[k]:
                self.__map[k] += [x for x in self.__map[item] if x != k]
                self.__map[k] = list(set(self.__map[k]))
        for k, v in self.__map.items():
            for item in [x for x in self.__list if x.Origin == k]:
                for link in v:
                    item.AddLink(link)

    def GetRecipes(self):
        """Get bb files in stash

        Returns:
            list -- List of bb files in stash
        """
        return sorted({x.Origin for x in self.__list if x.Origin.endswith(".bb")})

    def GetLoneAppends(self):
        """Get bbappend without a matching bb

        Returns:
            list -- list of bbappend without a matching bb
        """
        __linked_appends = []
        __appends = []
        for x in self.__list:
            if x.Origin.endswith(".bbappend"):
                __appends.append(x.Origin)
            elif x.Origin.endswith(".bb"):
                __linked_appends += x.Links
        return sorted({x for x in __appends if x not in __linked_appends})

    def __is_linked_to(self, item, filename, nolink=False):
        return (filename in item.Links and not nolink) or filename == item.Origin

    def __get_items_by_file(self, items, filename, nolink=False):
        if not filename:
            return items
        return [x for x in items if self.__is_linked_to(x, filename, nolink=nolink)]

    def __get_items_by_classifier(self, items, classifier):
        if not classifier:
            return items
        return [x for x in items if x.CLASSIFIER in classifier]

    def __get_items_by_attribute(self, items, attname, attvalue):
        if not attname:
            return items

        def _filter(x, attname, attvalue):
            attr_ = x.GetAttributes()
            res = False
            for name in attname:
                res |= name in attr_ and (not attvalue or any(x == attr_.get(name) for x in attvalue))
            return res

        return [x for x in items if _filter(x, attname, attvalue)]

    def GetLinksForFile(self, filename):
        """Get file which this file is linked against

        Arguments:
            filename {str} -- full path to file

        Returns:
            list -- list of full paths the file is linked against
        """
        if not filename:
            return []
        return [x.Origin for x in self.__get_items_by_file(self.__list, filename) if x.Origin != filename]

    def GetItemsFor(self, filename=None, classifier=None, attribute=None, attributeValue=None, nolink=False):
        """Get items for filename

        Keyword Arguments:
            filename {str} -- Full path to file (default: {None})
            classifier {str | iterable of str} -- (iterable of) class specifier (e.g. Variable) (default: {None})
            attribute {str | iterable of str} -- (iterable of) class attribute name (default: {None})
            attributeValue {str | iterable of str} -- (iterable of) value of the class attribute name (default: {None})
            nolink {bool} -- Consider linked files (default: {False})

        Returns:
            List[Item] -- Returns a list of items fitting the set filters
        """
        if not isinstance(classifier, (list, set, tuple)):
            classifier = [classifier] if classifier else []
        if not isinstance(attribute, (list, set, tuple)):
            attribute = [attribute] if attribute else []
        if not isinstance(attributeValue, (list, set, tuple)):
            attributeValue = [attributeValue] if attributeValue else []
        res = self.__list
        if filename:
            res = self.__get_items_by_file(res, filename, nolink=nolink)
        if classifier:
            res = self.__get_items_by_classifier(res, classifier)
        if attribute:
            res = self.__get_items_by_attribute(res, attribute, attributeValue)
        return sorted(set(res), key=lambda x: x.Line)

    def ExpandVar(self, filename=None, attribute=None, attributeValue=None, nolink=False):
        """Expand variable to dictionary

        Args:
            filename {str} -- Full path to file (default: {None})
            attribute {str} -- class attribute name (default: {None})
            attributeValue {str} -- value of the class attribute name (default: {None})
            nolink {bool} -- Consider linked files (default: {False})

        Returns:
            {dict}: expanded variables from call + base set of variables
        """
        _res = self.GetItemsFor(filename=filename,
                                classifier=Variable.CLASSIFIER,
                                attribute=attribute,
                                attributeValue=attributeValue,
                                nolink=nolink)
        _exp = {
            "PN": guess_recipe_name(filename),
            "PV": guess_recipe_version(filename),
            "BPN": guess_base_recipe_name(filename),
        }
        _exp = {**_exp, **CONSTANTS.SetsBase}
        for item in sorted(_res, key=lambda x: x.Line):
            varop = item.VarOp
            name = item.VarNameComplete
            if item.Flag:
                continue
            if name not in _exp.keys():
                _exp[name] = None
            if varop in [" = ", " := "]:
                if not item.IsAppend() and "remove" not in item.SubItems:
                    _exp[name] = item.VarValueStripped
            elif varop == " ?= " and _exp[name] is None:
                _exp[name] = item.VarValueStripped
            elif varop == " ??= " and _exp[name] is None:
                _exp[name] = item.VarValueStripped
            elif varop == " += ":
                if _exp[name] is None:
                    _exp[name] = ""
                _exp[name] += " " + item.VarValueStripped
            elif varop == " =+ ":
                if _exp[name] is None:
                    _exp[name] = ""
                _exp[name] = item.VarValueStripped + " " + _exp[name]
            elif varop in [" .= "]:
                if _exp[name] is None:
                    _exp[name] = ""
                _exp[name] += item.VarValueStripped
            elif varop in [" =. "]:
                if _exp[name] is None:
                    _exp[name] = ""
                _exp[name] = item.VarValueStripped + _exp[name]
        # and now for a second run with special
        for item in sorted(_res, key=lambda x: x.Line):
            varop = item.VarOp
            name = item.VarNameComplete
            if item.Flag:
                continue
            if name not in _exp.keys():
                _exp[name] = None
                if _exp[name] is None:
                    _exp[name] = ""
                _exp[name] += item.VarValueStripped
            elif "append" in item.SubItems:
                if _exp[name] is None:
                    _exp[name] = ""
                _exp[name] += item.VarValueStripped
            elif "prepend" in item.SubItems:
                if _exp[name] is None:
                    _exp[name] = ""
                _exp[name] = item.VarValueStripped + _exp[name]
        # and now for the run with remove
        for item in sorted(_res, key=lambda x: x.Line):
            varop = item.VarOp
            name = item.VarNameComplete
            if item.Flag:
                continue
            if name not in _exp.keys():
                _exp[name] = None
            if "remove" in item.SubItems:
                if _exp[name] is None:
                    _exp[name] = ""
                _exp[name] = _exp[name].replace(item.VarValueStripped, "")
        # final run and explode the settings
        _finalexp = {}
        for k, v in _exp.items():
            _newkey = expand_term(self, filename, k)
            if _newkey not in _finalexp:
                _finalexp[_newkey] = []
            _finalexp[_newkey] += Item.safe_linesplit(
                expand_term(self, filename, v or ""))
        return _finalexp
