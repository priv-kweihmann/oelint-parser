import glob
import os
from collections import UserList
from typing import Iterable, List, Union
from urllib.parse import urlparse

from oelint_parser.cls_item import Inherit, Item, Unset, Variable
from oelint_parser.constants import CONSTANTS
from oelint_parser.parser import get_items
from oelint_parser.rpl_regex import RegexRpl


class Stash():
    """The Stash object is the central storage for extracting the bitbake information."""

    class StashList(UserList):
        """Extended list of Items."""

        def __init__(self, stash: 'Stash', items: Iterable[Item]) -> None:
            """StashList - Extended list of Items.

            Args:
                stash (Stash): Parent stash object
                items (Iterable): Iterable input
            """
            self._stash = stash
            super().__init__()
            self.data = items

        def __setitem__(self, index: int, item: Item) -> None:
            self.data[index] = item

        def __iadd__(self, __value: Iterable) -> List[Item]:
            return self.data.__iadd__(__value)

        def insert(self, index: int, item: Item) -> None:
            """Insert into list

            Args:
                index (int): index where to insert
                item (Item): object to insert
            """
            self.data.insert(index, item)

        def append(self, item: Union[Item, Iterable[Item]]) -> None:
            """Append to list

            Args:
                item (Union[Item, Iterable[Item]]): Item or Iterable of Items
            """
            if isinstance(item, (list, tuple)):
                for _item in item:
                    self.data.append(_item)
            else:
                self.data.append(item)

        def extend(self, other: 'Stash.StashList') -> None:
            """Extend list

            Args:
                other (Stash.StashList): Other stash other
            """
            if isinstance(other, type(Stash.StashList)):
                self.data.extend(other.data)

        def remove(self, item: Union[Item, Iterable[Item]]) -> None:
            """Remove from list

            Args:
                item (Item): Item(s) to remove
            """
            if isinstance(item, (list, tuple)):
                for _item in item:
                    self.data.remove(_item)
            else:
                self.data.remove(item)

        def reduce(self, filename: str = None,
                   classifier: Union[Iterable[str], str] = None,
                   attribute: Union[Iterable[str], str] = None,
                   attributeValue: Union[Iterable[str], str] = None,
                   nolink: bool = False) -> 'Stash.StashList':
            """Filters the list.

            NOTE: This is a destructive operation.
            If you want to have a copy returned use

            Stash.Reduce(<this object>,...) instead.

            Args:
                filename (str, optional): Full path to file. Defaults to None.
                classifier (Union[Iterable[str], str], optional): (iterable of) class specifier (e.g. Variable). Defaults to None.
                attribute (Union[Iterable[str], str], optional): (iterable of) class attribute name. Defaults to None.
                attributeValue (Union[Iterable[str], str], optional): (iterable of) value of the class attribute value. Defaults to None.
                nolink (bool, optional): Consider linked files. Defaults to False.

            Returns:
                Stash.StashList: self
            """
            self.data = self._stash.Reduce(self.data,
                                           filename=filename,
                                           classifier=classifier,
                                           attribute=attribute,
                                           attributeValue=attributeValue,
                                           nolink=nolink)
            return self

    def __init__(self, quiet: bool = False, new_style_override_syntax: bool = False) -> None:
        """Stash object

        Args:
            quiet (bool, optional): No progress printing. Defaults to False.
            new_style_override_syntax (bool, optional): Enforce new override syntax. Defaults to False.
        """
        self.__list = []
        self.__seen_files = set()
        self.__map = {}
        self.__quiet = quiet
        self.__new_style_override_syntax = new_style_override_syntax

    def AddFile(self, _file: str, lineOffset: int = 0, forcedLink: str = None) -> List[Item]:
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
        res = get_items(self,
                        _file,
                        lineOffset=lineOffset,
                        new_style_override_syntax=self.__new_style_override_syntax)
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

    def Append(self, item: Union[Item, Iterable[Item]]) -> None:
        """appends one or mote items to the stash

        Args:
            item (Item): Item(s) to append
        """
        if isinstance(item, (list, tuple, Stash.StashList)):
            for _item in item:
                self.__list.append(_item)
        else:
            self.__list.append(item)

    def Remove(self, item: Union[Item, Iterable[Item]]) -> None:
        """removes one or more items from the stash

        Args:
            item (Item): Item(s) to remove
        """
        if isinstance(item, (list, tuple, Stash.StashList)):
            for _item in item:
                self.__list.remove(_item)
        else:
            self.__list.remove(item)

    def AddDistroMachineFromLayer(self, path: str) -> None:
        """adds machine and distro configuration from the layer of the provided file

        Args:
            path (str): Path to file
        """
        _root = self.GetLayerRoot(path)
        if _root:
            for conf in glob.glob(os.path.join(_root, "conf", "distro", "*.conf")):
                _fn, _ = os.path.splitext(os.path.basename(conf))
                CONSTANTS.AddConstants({'replacements': {'distros': [_fn]}})
            for conf in glob.glob(os.path.join(_root, "conf", "machine", "*.conf")):
                _fn, _ = os.path.splitext(os.path.basename(conf))
                CONSTANTS.AddConstants({'replacements': {'machines': [_fn]}})

    def Finalize(self) -> None:
        """finalize the dependencies within the stash
        """
        # cross link all the files
        for k in self.__map.keys():
            for item in self.__map[k]:
                self.__map[k] += [x for x in self.__map[item] if x != k]
                self.__map[k] = list(set(self.__map[k]))
        for k, v in self.__map.items():
            for item in [x for x in self.__list if x.Origin == k]:
                for link in v:
                    item.AddLink(link)

    def GetRecipes(self) -> None:
        """Get bb files in stash

        Returns:
            list -- List of bb files in stash
        """
        return sorted({x.Origin for x in self.__list if x.Origin.endswith(".bb")})

    def GetLoneAppends(self) -> None:
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

    def __is_linked_to(self, item: Item, filename: str, nolink: bool = False) -> bool:
        return (filename in item.Links and not nolink) or filename == item.Origin

    def __get_items_by_file(self, items: Iterable[Item], filename: str, nolink: bool = False) -> List[Item]:
        if not filename:
            return items
        return [x for x in items if self.__is_linked_to(x, filename, nolink=nolink)]

    def __get_items_by_classifier(self, items: Iterable[Item], classifier: Iterable[str]) -> List[Item]:
        if not classifier:
            return items
        return [x for x in items if x.CLASSIFIER in classifier]

    def __get_items_by_attribute(self, items: Iterable[Item], attname: Iterable[str], attvalue: Iterable[str]) -> List[Item]:
        if not attname:
            return items

        def _filter(x: Item, attname: Iterable[str], attvalue: Iterable[str]) -> bool:
            attr_ = x.GetAttributes()
            res = False
            for name in attname:
                res |= name in attr_ and (not attvalue or any(x == attr_.get(name) for x in attvalue))
            return res

        return [x for x in items if _filter(x, attname, attvalue)]

    def GetLinksForFile(self, filename: str) -> List[str]:
        """Get file which this file is linked against

        Arguments:
            filename {str} -- full path to file

        Returns:
            list -- list of full paths the file is linked against
        """
        if not filename:
            return []
        return [x.Origin for x in self.__get_items_by_file(self.__list, filename) if x.Origin != filename]

    def Reduce(self,
               in_list: List[Item],
               filename: str = None,
               classifier: Union[Iterable[str], str] = None,
               attribute: Union[Iterable[str], str] = None,
               attributeValue: Union[Iterable[str], str] = None,
               nolink: bool = False) -> List[Item]:
        """Reduce a list by filtering

        Args:
            in_list (Stash.StashList): Input list.
            filename (str, optional): Full path to file. Defaults to None.
            classifier (Union[Iterable[str], str], optional): (iterable of) class specifier (e.g. Variable). Defaults to None.
            attribute (Union[Iterable[str], str], optional): (iterable of) class attribute name. Defaults to None.
            attributeValue (Union[Iterable[str], str], optional): (iterable of) value of the class attribute value. Defaults to None.
            nolink (bool, optional): Consider linked files. Defaults to False.

        Returns:
            List[Item]: Returns a list of items fitting the set filters
        """
        if not isinstance(classifier, (list, set, tuple)):
            classifier = [classifier] if classifier else []
        if not isinstance(attribute, (list, set, tuple)):
            attribute = [attribute] if attribute else []
        if not isinstance(attributeValue, (list, set, tuple)):
            attributeValue = [attributeValue] if attributeValue else []
        if filename:
            in_list = self.__get_items_by_file(in_list, filename, nolink=nolink)
        if classifier:
            in_list = self.__get_items_by_classifier(in_list, classifier)
        if attribute:
            in_list = self.__get_items_by_attribute(in_list, attribute, attributeValue)
        return sorted(set(in_list), key=lambda x: x.Line)

    def GetItemsFor(self,
                    filename: str = None,
                    classifier: Union[Iterable[str], str] = None,
                    attribute: Union[Iterable[str], str] = None,
                    attributeValue: Union[Iterable[str], str] = None,
                    nolink: bool = False) -> 'Stash.StashList':
        """Get items for filename

        Args:
            filename (str, optional): Full path to file. Defaults to None.
            classifier (Union[Iterable[str], str], optional): (iterable of) class specifier (e.g. Variable). Defaults to None.
            attribute (Union[Iterable[str], str], optional): (iterable of) class attribute name. Defaults to None.
            attributeValue (Union[Iterable[str], str], optional): (iterable of) value of the class attribute value. Defaults to None.
            nolink (bool, optional): Consider linked files. Defaults to False.

        Returns:
            Stash.StashList: Returns a list of items fitting the set filters
        """
        res = Stash.StashList(self, self.__list)
        res.reduce(filename=filename,
                   classifier=classifier,
                   attribute=attribute,
                   attributeValue=attributeValue,
                   nolink=nolink)
        return res

    def ExpandVar(self,
                  filename: str = None,
                  attribute: Union[Iterable[str], str] = None,
                  attributeValue: Union[Iterable[str], str] = None,
                  nolink: bool = False) -> dict:
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

        _res += self.GetItemsFor(filename=filename, classifier=Unset.CLASSIFIER)
        _exp = {
            "PN": self.GuessRecipeName(filename),
            "PV": self.GuessRecipeVersion(filename),
            "BPN": self.GuessBaseRecipeName(filename),
        }
        _exp = {**_exp, **CONSTANTS.SetsBase}
        for item in sorted(_res, key=lambda x: x.Line):
            if isinstance(item, Unset):
                if item.Flag:
                    continue
                if item.VarName in _exp:
                    del _exp[item.VarName]
                continue
            if item.Flag or not item.IsImmediateModify():
                continue
            varop = item.VarOp
            name = item.VarNameCompleteNoModifiers
            if name not in _exp.keys():
                _exp[name] = None
            if varop in [" = ", " := "]:
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
        # and now for a second run with special append
        for item in sorted(_res, key=lambda x: x.Line):
            if isinstance(item, Unset):
                continue
            if item.IsImmediateModify():
                continue
            varop = item.VarOp
            name = item.VarNameCompleteNoModifiers
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
            if isinstance(item, Unset):
                continue
            if item.IsImmediateModify():
                continue
            varop = item.VarOp
            name = item.VarNameCompleteNoModifiers
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
            _newkey = self.ExpandTerm(filename, k)
            if _newkey not in _finalexp:
                _finalexp[_newkey] = []
            _finalexp[_newkey] += Item.safe_linesplit(
                self.ExpandTerm(filename, v or ""))
        return _finalexp

    def GetFiles(self, _file: str, pattern: str) -> List[str]:
        """Get files matching SRC_URI entries

        Arguments:
            _file {str} -- Full path to filename
            pattern {str} -- glob pattern to apply

        Returns:
            list -- list of files matching pattern
        """
        res = set()
        src_uris = self.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                    attribute=Variable.ATTR_VAR, attributeValue="SRC_URI")
        files_paths = {
            "{dir}/*/{pattern}".format(dir=os.path.dirname(x.Origin), pattern=pattern) for x in src_uris}
        for item in src_uris:
            files_paths.update({"{dir}/*/{pattern}".format(dir=os.path.dirname(x.Origin), pattern=pattern)
                                for x in self.GetItemsFor(filename=item.Origin)})
        for item in files_paths:
            res.update(glob.glob(item))
        return sorted(res)

    def GetLayerRoot(self, name: str) -> str:
        """Find the path to the layer root of a file

        Arguments:
            name {str} -- filename

        Returns:
            str -- path to layer root or empty string
        """
        _curdir = os.path.dirname(name) if os.path.isfile(name) else name
        while os.path.isdir(_curdir):
            if _curdir == "/":
                break
            _curdir = os.path.dirname(_curdir)
            if os.path.exists(os.path.join(_curdir, "conf/layer.conf")):
                return _curdir
        return ""

    def FindLocalOrLayer(self, name: str, localdir: str) -> str:
        """Find file in local dir or in layer

        Arguments:
            name {str} -- filename
            localdir {str} -- path to local dir

        Returns:
            str -- path to found file or None
        """
        if os.path.exists(os.path.join(localdir, name)):
            return os.path.join(localdir, name)
        _curdir = localdir
        while os.path.isdir(_curdir):
            if _curdir == "/":
                break
            _curdir = os.path.dirname(_curdir)
            if os.path.exists(os.path.join(_curdir, "conf/layer.conf")):
                if os.path.exists(os.path.join(_curdir, name)):
                    return os.path.join(_curdir, name)
                else:
                    break
        return ""

    def _replace_with_known_mirrors(self, _in: dict) -> dict:
        """
        Replace the known mirror configuration items
        """
        for k, v in CONSTANTS.MirrorsKnown.items():
            _in = _in.replace(k, v)
        return _in

    def GetScrComponents(self, string: str) -> dict:
        """Return SRC_URI components

        Arguments:
            string {str} -- raw string

        Returns:
            dict -- scheme: protocol used, src: source URI, options: parsed options
        """
        _raw = self._replace_with_known_mirrors(string)
        _url = urlparse(self._replace_with_known_mirrors(string))
        _scheme = _url.scheme
        _tmp = _url.netloc
        if _url.path:
            _tmp += "/" + _url.path.lstrip("/")
        _path = _tmp.split(";")[0]
        _options = _raw.split(";")[1:] if ";" in _raw else []
        _parsed_opt = {x.split("=")[0]: x.split("=")[1]
                       for x in _options if "=" in x}
        return {"scheme": _scheme, "src": _path, "options": _parsed_opt}

    def SafeLineSplit(self, string: str) -> List[str]:
        """Split line in a safe manner

        Arguments:
            string {str} -- raw input

        Returns:
            list -- safely split input
        """
        return RegexRpl.split(r"\s|\t|\x1b", string)

    def GuessRecipeName(self, _file: str) -> str:
        """Get the recipe name from filename

        Arguments:
            _file {str} -- filename

        Returns:
            str -- recipe name
        """
        _name, _ = os.path.splitext(os.path.basename(_file))
        return _name.split("_")[0]

    def GuessBaseRecipeName(self, _file: str) -> str:
        """Get the base recipe name from filename (aka BPN)

        Arguments:
            _file {str} -- filename

        Returns:
            str -- recipe name
        """
        tmp_ = RegexRpl.sub(r"^(nativesdk-)*(.+)(-native)*(-cross)*", r"\2", self.GuessRecipeName(_file))
        tmp_ = RegexRpl.sub(r"^(.+)(-native)$", r"\1", tmp_)
        tmp_ = RegexRpl.sub(r"^(.+)(-cross)$", r"\1", tmp_)
        return tmp_

    def GuessRecipeVersion(self, _file: str) -> str:
        """Get recipe version from filename

        Arguments:
            _file {str} -- filename

        Returns:
            str -- recipe version
        """
        _name, _ = os.path.splitext(os.path.basename(_file))
        return _name.split("_")[-1]

    def ExpandTerm(self, _file: str, value: str, spare: List[str] = None, seen: List[str] = None) -> str:
        """Expand a variable (replacing all variables by known content)

        Arguments:
            _file {str} -- Full path to file
            value {str} -- Variable value to expand
            spare {list[str]} -- items to keep unexpanded (default: None)
            seen {list[str]} -- seen items (default: None)

        Returns:
            str -- expanded value
        """
        baseset = CONSTANTS.SetsBase
        pattern = r"\$\{(.+?)\}"
        seen = seen or {}
        spare = spare or []
        res = str(value)
        for m in RegexRpl.finditer(pattern, value):
            if m.group(1) in spare:
                continue
            _comp = [x for x in self.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                                 attribute=Variable.ATTR_VAR, attributeValue=m.group(1)) if not x.AppendOperation()]

            if any(_comp):
                if m.group(1) in seen.keys():
                    _rpl = seen[m.group(1)]
                else:
                    seen[m.group(1)] = ""
                    _rpl = self.ExpandTerm(_file, _comp[0].VarValueStripped, seen=seen)
                    seen[m.group(1)] = _rpl
                res = res.replace(m.group(0), _rpl)
            elif m.group(1) in baseset:
                if m.group(1) in seen.keys():
                    _rpl = seen[m.group(1)]
                elif m.group(1) in baseset:
                    seen[m.group(1)] = ""
                    _rpl = self.ExpandTerm(_file, baseset[m.group(1)], seen=seen)
                    seen[m.group(1)] = _rpl
                else:
                    _rpl = m.group(1)
                res = res.replace(m.group(0), _rpl)
            elif m.group(1) in ["PN"]:
                res = res.replace(m.group(0), self.GuessRecipeName(_file))
            elif m.group(1) in ["BPN"]:
                res = res.replace(m.group(0), self.GuessBaseRecipeName(_file))
            elif m.group(1) in ["PV"]:
                res = res.replace(m.group(0), self.GuessRecipeVersion(_file))
            elif not any(_comp):
                continue
        return res

    def GetValidPackageNames(self, _file: str, strippn: bool = False) -> List[str]:
        """Get known valid names for packages

        Arguments:
            _file {str} -- Full path to file
            strippn {bool} -- strip the package name (default: False)

        Returns:
            list -- list of valid package names
        """
        res = set()
        _comp = self.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                 attribute=Variable.ATTR_VAR, attributeValue="PACKAGES")
        _comp += self.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                  attribute=Variable.ATTR_VAR, attributeValue="PACKAGE_BEFORE_PN")
        for _pn in ['${PN}', self.GuessRecipeName(_file)]:
            res.add(_pn)
            res.add("{recipe}-ptest".format(recipe=_pn))
            res.update(["{recipe}-{pkg}".format(recipe=_pn, pkg=x)
                        for x in ["src", "dbg", "staticdev", "dev", "doc", "locale"]])
            for item in _comp:
                for pkg in [x for x in self.SafeLineSplit(self.ExpandTerm(_file, item.VarValueStripped, spare=["PN"])) if x]:
                    if not strippn:
                        _pkg = pkg.replace("${PN}", _pn)
                    else:
                        _pkg = pkg.replace("${PN}", "")
                    res.add(_pkg)
        return res

    def GetValidNamedResources(self, _file: str) -> List[str]:
        """Get list of valid SRCREV resource names

        Arguments:
            _file {str} -- Full path to file

        Returns:
            list -- list of valid SRCREV resource names
        """
        res = set()
        _comp = self.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                 attribute=Variable.ATTR_VAR, attributeValue="SRC_URI")
        _recipe_name = self.GuessRecipeName(_file)
        res.add(_recipe_name)
        for item in _comp:
            for name in [x for x in self.SafeLineSplit(item.VarValueStripped) if x]:
                _url = self.GetScrComponents(name)
                if "name" in _url["options"]:
                    res.add(_url["options"]["name"].replace("${PN}", _recipe_name))
        return res

    def IsImage(self, _file: str) -> bool:
        """returns if the file is likely an image recipe or not

        Args:
            _file {str} -- Full path to file

        Returns:
            bool -- True if _file is an image recipe
        """
        res = False

        _inherits = self.GetItemsFor(filename=_file, classifier=Inherit.CLASSIFIER)
        for item in _inherits:
            res |= any(True for x in item.get_items() if x in CONSTANTS.ImagesClasses)

        for _var in CONSTANTS.ImagesVariables:
            res |= any(self.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                        attribute=Variable.ATTR_VAR, attributeValue=_var))

        return res

    def IsPackageGroup(self, _file: str) -> bool:
        """returns if the file is likely a packagegroup recipe or not

        Args:
            _file {str} -- Full path to file

        Returns:
            bool -- True if _file is a packagegroup recipe
        """
        _inherits = self.GetItemsFor(filename=_file, classifier=Inherit.CLASSIFIER)
        return any(x for x in _inherits if "packagegroup" in x.get_items())
