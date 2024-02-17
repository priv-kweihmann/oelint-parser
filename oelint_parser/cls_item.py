import os
import textwrap
from typing import List, Set, Tuple

from deprecated import deprecated

from oelint_parser.constants import CONSTANTS
from oelint_parser.rpl_regex import RegexRpl


class Item():
    """Base class for all Stash items
    """
    ATTR_LINE = "Line"
    ATTR_RAW = "Raw"
    ATTR_ORIGIN = "Origin"
    CLASSIFIER = "Item"
    ATTR_SUB = "SubItem"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path of origin file
            line {int} -- Overall line counter
            infileline {int} -- Line number in file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        self.__Line = line
        self.__Raw = rawtext
        self.__Links = []
        self.__Origin = origin
        self.__InFileLine = infileline
        self.__IncludedFrom = []
        self.__RealRaw = realraw or rawtext
        self.__OverrideDelimiter = ':' if new_style_override_syntax else '_'

    @property
    def Line(self) -> int:
        """Overall line count

        Returns:
            int: overall line count of item
        """
        return self.__Line

    @Line.setter
    def Line(self, value: int) -> None:
        self.__Line = value

    @property
    def Raw(self) -> str:
        """Raw string (without inline code blocks)

        Returns:
            str: raw string of item
        """
        return self.__Raw

    @Raw.setter
    def Raw(self, value: str) -> None:
        self.__Raw = value

    @property
    def Links(self) -> List[str]:
        """Linked files

        Returns:
            list: list of full path of linked files
        """
        return self.__Links

    @Links.setter
    def Links(self, value: List[str]) -> None:
        self.__Links = value

    @property
    def Origin(self) -> str:
        """origin of item

        Returns:
            str: full path of origin file
        """
        return self.__Origin

    @property
    def InFileLine(self) -> int:
        """Line count in file

        Returns:
            int: [description]
        """
        return self.__InFileLine

    @property
    def IncludedFrom(self) -> List[str]:
        """Files include this item

        Returns:
            list: list of files including this item
        """
        return self.__IncludedFrom

    @IncludedFrom.setter
    def IncludedFrom(self, value: List[str]) -> None:
        self.__IncludedFrom = value

    @property
    def RealRaw(self) -> str:
        """Completely unprocessed raw text

        Returns:
            str: completely unprocessed raw text
        """
        return self.__RealRaw

    @RealRaw.setter
    def RealRaw(self, value: str) -> None:
        self.__RealRaw = value

    @property
    def IsFromClass(self) -> bool:
        """Item comes from a bbclass

        Returns:
            bool: if item was set in a bbclass
        """
        return self.__Origin.endswith(".bbclass")

    @property
    def OverrideDelimiter(self) -> str:
        """Override delimiter

        Returns:
            str: Override delimiter
        """
        return self.__OverrideDelimiter

    @property
    def IsNewStyleOverrideSyntax(self) -> bool:
        """New style override syntax detected

        Returns:
            bool: True if new style has been detected
        """
        return self.__OverrideDelimiter == ':'

    @staticmethod
    def safe_linesplit(string: str) -> List[str]:
        """Safely split an input line to chunks

        Args:
            string (str): raw input string

        Returns:
            list: list of chunks of original string
        """
        return Item(None, None, None, None, None)._safe_linesplit(string)

    def _safe_linesplit(self, string: str) -> List[str]:
        return [x for x in RegexRpl.split(r"\s|\t|\x1b", string) if x]

    def get_items(self) -> List[str]:
        """Return single items

        Returns:
            list -- lines of raw input
        """
        return self._safe_linesplit(self.Raw)

    def extract_sub(self, name: str) -> Tuple[List[str], List[str]]:
        """Extract modifiers

        Arguments:
            name {str} -- input string

        Returns:
            tuple -- clean variable name, modifiers, package specific modifiers
        """
        if ":" in name:
            self.__OverrideDelimiter = ":"
        if any(name.startswith(x) for x in ['SRCREV_']):
            self.__OverrideDelimiter = "_"
        chunks = name.split(self.__OverrideDelimiter)
        _suffix = []
        _var = [chunks[0]]
        for i in chunks[1:]:
            tmp = ""
            if "-" in i:
                # just use the prefix in case a dash is found
                # that addresses things like FILES_${PN}-dev
                tmp = "-" + "-".join(i.split("-")[1:])
                i = i.split("-")[0]
            if RegexRpl.match("[a-z0-9{}$]+", i) and _var[0] != "pkg":  # noqa: P103
                _suffix.append(i + tmp)
            elif i in ["${PN}"]:
                _suffix.append(i + tmp)
            else:
                _var.append(i + tmp)
        _var = [x for x in _var if x]
        _suffix = [x for x in _suffix if x]
        return (self.__OverrideDelimiter.join(_var), self.__OverrideDelimiter.join(_suffix))

    def extract_sub_func(self, name: str) -> Tuple[List[str], List[str]]:
        """Extract modifiers for functions

        Arguments:
            name {str} -- input value

        Returns:
            tuple -- clean function name, modifiers
        """
        if ":" in name:
            self.__OverrideDelimiter = ":"
        chunks = name.split(self.__OverrideDelimiter)
        if name in ['__anonymous']:
            return (name, '')
        _marker = ["append", "prepend", "class-native",
                   "class-cross", "class-target", "remove"]
        _suffix = []
        _var = [chunks[0]]
        for i in chunks[1:]:
            if i in _marker or self.__OverrideDelimiter.join(_var) in CONSTANTS.FunctionsKnown:
                _suffix = chunks[chunks.index(i):]
                break
            else:
                _var.append(i)
        _var = [x for x in _var if x]
        _suffix = [x for x in _suffix if x]
        return (self.__OverrideDelimiter.join(_var), self.__OverrideDelimiter.join(_suffix))

    def IsFromAppend(self) -> bool:
        """Item originates from a bbappend

        Returns:
            bool -- True if coming from a bbappend
        """
        return self.Origin.endswith(".bbappend")

    def AddLink(self, _file: str) -> None:
        """Links files to each other in stash

        Arguments:
            _file {str} -- Full path of file to link against
        """
        self.Links.append(_file)
        self.Links = list(set(self.Links))

    def GetAttributes(self) -> dict:
        """Get all public attributes of this class

        Returns:
            dict -- all public attributes and their values
        """
        T = type(self)
        res = {}
        for _ in dir(self):
            try:
                attr = getattr(T, _)
            except AttributeError:
                continue  # Skip dunder attributes, i.e. private attributes
            else:
                if isinstance(attr, property):
                    res[_] = getattr(self, _)

        return res

    def __repr__(self) -> str:
        return "{name} -- {attr}\n".format(name=self.__class__.__name__, attr=self.GetAttributes())


class Variable(Item):
    """Items representing variables in bitbake."""
    ATTR_VAR = "VarName"
    ATTR_VARVAL = "VarValue"
    ATTR_VARRAW = "RawVarName"
    ATTR_VARVALSTRIPPED = "VarValueStripped"
    CLASSIFIER = "Variable"
    VAR_VALID_OPERATOR = [" = ", " += ",
                          " ?= ", " ??= ", " := ", " .= ", " =+ ", " =. "]

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 value: str,
                 operator: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- Variable name
            value {str} -- Variable value
            operator {str} -- Operation performed to the variable

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__VarName, self.__SubItem = self.extract_sub(name)
        self.__SubItems = [x for x in self.SubItem.split(
            self.OverrideDelimiter) if x]
        self.__VarValue = value
        self.__VarOp = operator
        self.__RawVarName = self.VarName
        self.__VarValueStripped = self.VarValue.strip().lstrip('"').rstrip('"')

    @property
    def VarName(self) -> str:
        """Variable name

        Returns:
            str: name of variable
        """
        return self.__VarName

    @property
    def SubItem(self) -> str:
        """Variable modifiers

        Returns:
            str: variable modifiers like packages, machines, appends, prepends
        """
        return self.__SubItem

    @property
    def SubItems(self) -> List[str]:
        """Variable modifiers list

        Returns:
            list: variable modifiers list like packages, machines, appends, prepends
        """
        return self.__SubItems

    @property
    def VarValue(self) -> str:
        """variable value

        Returns:
            str: unstripped variable value
        """
        return self.__VarValue

    @VarValue.setter
    def VarValue(self, value: str) -> None:
        self.__VarValue = value

    @property
    @deprecated(version='3.0.0', reason='Flag values are now part of FlagAssignment class')
    def Flag(self) -> str:
        """Flag value (deprecated)

        Use FlagAssignment class instead.

        Returns:
            str: Empty string.
        """
        return ''

    @property
    def VarOp(self) -> str:
        """Variable operation

        Returns:
            str: operation did on the variable
        """
        return self.__VarOp

    @property
    def VarNameComplete(self) -> str:
        """Complete variable name included overrides and flags

        Returns:
            str: complete variable name
        """
        return self.OverrideDelimiter.join([self.VarName] + self.SubItems)

    @property
    def VarNameCompleteNoModifiers(self) -> str:
        """Complete variable name included overrides but without modifiers like append, prepend and remove

        Returns:
            str: complete variable name
        """
        return self.OverrideDelimiter.join([self.VarName] + [x for x in self.SubItems if x not in ['prepend', 'append', 'remove']])

    @property
    def RawVarName(self) -> str:
        """Variable name and flags combined

        Returns:
            str: raw representation of the variable name
        """
        return self.__RawVarName

    @property
    def VarValueStripped(self) -> str:
        """Stripped variable value

        Returns:
            str: stripped version of variable value
        """
        return self.__VarValueStripped

    def IsAppend(self) -> bool:
        """Check if operation is an append

        Returns:
            bool -- True is variable is appended
        """
        return self.VarOp in [" += ", " =+ ", " =. ", " .= "] or "append" in self.SubItems or "prepend" in self.SubItems

    def AppendOperation(self) -> List[str]:
        """Get variable modifiers

        Returns:
            list -- list could contain any combination of 'append', ' += ', 'prepend' and 'remove'
        """
        res = []
        if self.VarOp in [" += ", " .= ", " =+ ", " =. "]:
            res.append(self.VarOp)
        if "append" in self.SubItems:
            res.append("append")
        if "prepend" in self.SubItems:
            res.append("prepend")
        if "remove" in self.SubItems:
            res.append("remove")
        return res

    def get_items(self, override: str = "", versioned: bool = False) -> List[str]:
        """Get items of variable value

        Arguments:
            override {str} -- String to take instead of VarValue
            versioned {bool} -- items can be versioned (versions will be stripped in this case)

        Returns:
            list -- clean list of items in variable value
        """
        _x = override.strip('"') or self.VarValue.strip('"')
        if versioned:
            _x = RegexRpl.sub(r"\s*\(.*?\)", "", _x)
        return self._safe_linesplit(_x)

    def IsMultiLine(self) -> bool:
        """Check if variable has a multiline assignment

        Returns:
            bool -- True if multiline
        """
        return "\\x1b" in self.Raw or "\\\n" in self.Raw

    def GetDistroEntry(self) -> str:
        """Get distro specific entries in variable

        Returns:
            str -- distro specific modifier of variable or ""
        """
        _x = [x for x in self.SubItems if x in CONSTANTS.DistrosKnown]
        return _x[0] if _x else ""

    def GetMachineEntry(self) -> str:
        """Get machine specific entries in variable

        Returns:
            str -- machine specific modifier of variable or ""
        """
        for x in self.SubItems:
            if x not in ["append", "prepend", "class-native", "class-nativesdk", "class-cross", "class-target", "remove", "machine"]:
                return x
        return ""

    def GetClassOverride(self) -> str:
        """Get class specific entries in variable

        Returns:
            str -- class specific modifier of variable or ""
        """
        for x in self.SubItems:
            if x in ["class-native", "class-nativesdk", "class-cross", "class-target"]:
                return x
        return ""

    def IsImmediateModify(self) -> bool:
        """Variable operation is done immediately

        Returns:
            bool: true if it isn't a prepend/append or remove operation
        """
        return not any(x in ['prepend', 'append', 'remove'] for x in self.SubItems)


class Comment(Item):
    """Items representing comments in bitbake."""
    CLASSIFIER = "Comment"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)

    def get_items(self) -> List[str]:
        """Get single lines of block

        Returns:
            list -- single lines of comment block
        """
        return self.Raw.split("\n")


class Include(Item):
    """Items that representing include/require statements."""

    CLASSIFIER = "Include"
    ATTR_INCNAME = "IncName"
    ATTR_STATEMENT = "Statement"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 incname: str,
                 statement: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            incname {str} -- raw name of the include file
            statement {str} -- either include or require

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__IncName = incname
        self.__Statement = statement

    @property
    def IncName(self) -> str:
        """Include name

        Returns:
            str: name of the file to include/require
        """
        return self.__IncName

    @property
    def Statement(self) -> str:
        """statement either include or require

        Returns:
            str: include or require
        """
        return self.__Statement

    def get_items(self) -> Tuple[str, str]:
        """Get items

        Returns:
            list -- include name, include statement
        """
        return [self.IncName, self.Statement]


class Export(Item):
    """Items representing export statements in bitbake."""

    CLASSIFIER = "Export"
    ATTR_NAME = "Name"
    ATTR_STATEMENT = "Value"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 value: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- variable name of the export
            value {str} -- (optional) value of the export

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__Name = name
        self.__Value = value

    @property
    def Name(self) -> str:
        """Name of the exported var

        Returns:
            str: name of the exported var
        """
        return self.__Name

    @property
    def Value(self) -> str:
        """value of the export

        Returns:
            str: optional value of the export
        """
        return self.__Value

    def get_items(self) -> Tuple[str, str]:
        """Get items

        Returns:
            list -- include name, include statement
        """
        return [self.Name, self.Value]


class Function(Item):
    """Items representing task definitions in bitbake."""

    ATTR_FUNCNAME = "FuncName"
    ATTR_FUNCBODY = "FuncBody"
    CLASSIFIER = "Function"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 body: str,
                 realraw: str,
                 python: bool = False,
                 fakeroot: bool = False,
                 new_style_override_syntax: bool = False) -> None:
        """[summary]

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- Raw function name
            body {str} -- Function body

        Keyword Arguments:
            python {bool} -- python function according to parser (default: {False})
            fakeroot {bool} -- uses fakeroot (default: {False})
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__IsPython = python is not None
        self.__IsFakeroot = fakeroot is not None
        name = name or ""
        self.__FuncName, self.__SubItem = self.extract_sub_func(name.strip())
        self.__SubItems = [x for x in self.SubItem.split(
            self.OverrideDelimiter) if x]
        self.__FuncBody = body
        self.__FuncBodyStripped = body.replace(
            "{", "").replace("}", "").replace("\n", "").strip()
        self.__FuncBodyRaw = textwrap.dedent(
            rawtext[rawtext.find("{") + 1:].rstrip().rstrip("}"))

    @property
    def IsPython(self) -> bool:
        """Is python function

        Returns:
            bool: is a python function
        """
        return self.__IsPython

    @property
    def IsFakeroot(self) -> bool:
        """Is fakeroot function

        Returns:
            bool: is a python function
        """
        return self.__IsFakeroot

    @property
    def FuncName(self) -> str:
        """Function name

        Returns:
            str: name of function
        """
        return self.__FuncName

    @property
    def FuncNameComplete(self) -> str:
        """Complete function name (including overrides)

        Returns:
            str: complete name of function
        """
        return self.OverrideDelimiter.join([self.__FuncName] + self.__SubItems)

    @property
    def SubItem(self) -> str:
        """Function modifiers

        Returns:
            str: function modifiers like packages, machines, appends, prepends
        """
        return self.__SubItem

    @property
    def SubItems(self) -> List[str]:
        """Function modifiers list

        Returns:
            list: function modifiers list like packages, machines, appends, prepends
        """
        return self.__SubItems

    @property
    def FuncBody(self) -> str:
        """Function body

        Returns:
            str: function body text
        """
        return self.__FuncBody

    @property
    def FuncBodyStripped(self) -> str:
        """Stripped function body

        Returns:
            str: stripped function body text
        """
        return self.__FuncBodyStripped

    @property
    def FuncBodyRaw(self) -> str:
        """Raw function body (including brackets)

        Returns:
            str: raw function body text
        """
        return self.__FuncBodyRaw

    def GetDistroEntry(self) -> str:
        """Get distro specific modifiers

        Returns:
            str -- distro specific modifier or ""
        """
        _x = [x for x in self.SubItems if x in CONSTANTS.DistrosKnown]
        return _x[0] if _x else ""

    def GetMachineEntry(self) -> str:
        """Get machine specific modifiers

        Returns:
            str -- machine specific modifier or ""
        """
        for x in self.SubItems:
            if x not in ["append", "prepend", "class-native", "class-cross", "class-target", "remove", "machine"]:
                return x
        return ""

    def IsAppend(self) -> bool:
        """Return if function appends another function

        Returns:
            bool -- True is append or prepend operation
        """
        return any(x in ["append", "prepend"] for x in self.SubItems)

    def get_items(self) -> List[str]:
        """Get items of function body

        Returns:
            list -- single lines of function body
        """
        return self.FuncBodyRaw.split("\n")


class PythonBlock(Item):
    """Items representing python functions in bitbake."""

    ATTR_FUNCNAME = "FuncName"
    CLASSIFIER = "PythonBlock"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- Function name

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__FuncName = name

    @property
    def FuncName(self) -> str:
        """Function name

        Returns:
            str: name of function
        """
        return self.__FuncName

    def get_items(self) -> List[str]:
        """Get lines of function body

        Returns:
            list -- lines of function body
        """
        return self.Raw.split("\n")


class FlagAssignment(Item):
    """Items representing flag assignments in bitbake."""

    ATTR_NAME = "VarName"
    ATTR_FLAG = "Flag"
    ATTR_VARVAL = "Value"
    ATTR_VARVAL_STRIPPED = "ValueStripped"
    ATTR_VAROP = "VarOp"
    CLASSIFIER = "FlagAssignment"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 ident: str,
                 value: str,
                 varop: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- name of task to be modified
            ident {str} -- task flag
            value {str} -- value of modification
            varop {str} -- variable operation

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__name = name
        self.__flag = ident
        self.__value = value
        self.__varop = varop

    @property
    def VarName(self) -> str:
        """Variable name

        Returns:
            str: name of variable
        """
        return self.__name

    @property
    def Flag(self) -> str:
        """Flag name

        Returns:
            str: Flag name
        """
        return self.__flag

    @property
    def VarOp(self) -> str:
        """Modifier operation

        Returns:
            str: used modifier in operation
        """
        return self.__varop

    @property
    def Value(self) -> str:
        """Value

        Returns:
            str: value set
        """
        return self.__value

    @property
    def ValueStripped(self) -> str:
        """Value stripped of the quotes

        Returns:
            str: value set
        """
        return self.__value.strip('"')

    def get_items(self) -> Tuple[str, str, str, str]:
        """Get items

        Returns:
            list -- variable name, flag, variable operation, modification value
        """
        return [self.VarName, self.Flag, self.VarOp, self.ValueStripped]


class FunctionExports(Item):
    """Items representing EXPORT_FUNCTIONS in bitbake."""

    ATTR_FUNCNAME = "FuncName"
    CLASSIFIER = "FunctionExports"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- name of function to be exported

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__FuncNames = name

    @property
    def FuncNames(self) -> str:
        """Function name

        Returns:
            str: names of exported functions
        """
        return self.__FuncNames

    def get_items(self) -> List[str]:
        """Get items

        Returns:
            list -- function names
        """
        return [x for x in self.__FuncNames.split(" ") if x]

    def get_items_unaliased(self) -> List[str]:
        """Get items with their bbclass scope names

        Returns:
            list -- function names in the scope of a bbclass (foo becomes classname-foo in this case)
        """
        _name, _ = os.path.splitext(os.path.basename(self.Origin))
        return ["{name}-{item}".format(name=_name, item=x) for x in self.get_items()]


class TaskAdd(Item):
    """Items representing addtask statements in bitbake."""

    ATTR_FUNCNAME = "FuncName"
    ATTR_BEFORE = "Before"
    ATTR_AFTER = "After"
    CLASSIFIER = "TaskAdd"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 realraw: str,
                 before: str = "",
                 after: str = "",
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- name of task to be executed

        Keyword Arguments:
            before {str} -- before statement (default: {""})
            after {str} -- after statement (default: {""})
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__FuncName = name
        self.__Before = [x for x in (before or "").split(" ") if x]
        self.__After = [x for x in (after or "").split(" ") if x]

    @property
    def FuncName(self) -> str:
        """Function name

        Returns:
            str: name of function
        """
        return self.__FuncName

    @property
    def Before(self) -> List[str]:
        """Tasks executed before

        Returns:
            list: tasks to be executed before
        """
        return self.__Before

    @property
    def After(self) -> List[str]:
        """Tasks executed after

        Returns:
            list: tasks to be executed after
        """
        return self.__After

    def get_items(self) -> List[str]:
        """get items

        Returns:
            list -- function name, all before statements, all after statements
        """
        return [self.FuncName] + self.Before + self.After


class TaskDel(Item):
    """Items representing deltask statements in bitbake."""

    ATTR_FUNCNAME = "FuncName"
    CLASSIFIER = "TaskDel"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- name of task to be executed

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__FuncName = name

    @property
    def FuncName(self) -> str:
        """Function name

        Returns:
            str: name of function
        """
        return self.__FuncName

    def get_items(self) -> List[str]:
        """get items

        Returns:
            list -- function name
        """
        return [self.FuncName]


class MissingFile(Item):
    """Items representing missing files found while parsing."""

    ATTR_FILENAME = "Filename"
    ATTR_STATEMENT = "Statement"
    CLASSIFIER = "MissingFile"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 filename: str,
                 statement: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            filename {str} -- filename of the file that can't be found
            statement {str} -- either include or require

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, "", "", new_style_override_syntax)
        self.__Filename = filename
        self.__Statement = statement

    @property
    def Filename(self) -> str:
        """Filename of the file missing

        Returns:
            str: filename that can't be resolved
        """
        return self.__Filename

    @property
    def Statement(self) -> str:
        """statement either include or require

        Returns:
            str: include or require
        """
        return self.__Statement

    def get_items(self) -> Tuple[str, str]:
        return [self.Filename, self.Statement]


@deprecated(version='3.0.0', reason='TaskAssignment is now part of FlagAssignment class')
class TaskAssignment(Item):
    """Deprecated. Use FlagAssignment class instead."""

    ATTR_FUNCNAME = "FuncName"
    ATTR_VAR = "VarName"
    ATTR_VARVAL = "VarValue"
    CLASSIFIER = "TaskAssignment"

    def __init__(self, *args, **kwargs):
        pass

    @property
    def FuncName(self) -> str:
        """Deprecated.

        Use FlagAssignment class instead

        Returns:
            str: Empty string
        """
        return ''

    @property
    def VarValue(self) -> str:
        """Deprecated.

        Use FlagAssignment class instead

        Returns:
            str: Empty string
        """
        return ''

    @property
    def VarName(self) -> str:
        """Deprecated.

        Use FlagAssignment class instead

        Returns:
            str: Empty string
        """
        return ''

    def get_items(self) -> List:
        """Deprecated.

        Use FlagAssignment class instead

        Returns:
            list: Empty list
        """
        return []


class AddPylib(Item):
    """Items representing addpylib statements in bitbake."""

    CLASSIFIER = "AddPylib"
    ATTR_PATH = "Path"
    ATTR_NAMESPACE = "Namespace"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 path: str,
                 namespace: str,
                 realraw: str,
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            path {str} -- path to the namespace
            namespace {str} -- namespace name

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__Path = path
        self.__Namespace = namespace

    @property
    def Path(self) -> str:
        """Path of the library addition

        Returns:
            str: path of the library addition
        """
        return self.__Path

    @property
    def Namespace(self) -> str:
        """Namespace of the addition

        Returns:
            str: Namespace of the addition
        """
        return self.__Namespace

    def get_items(self) -> Tuple[str, str]:
        """Get items

        Returns:
            list -- library path, library namespace
        """
        return [self.Path, self.Namespace]


class Inherit(Item):
    """Items that representing inherit(_defer) statements."""

    CLASSIFIER = "Inherit"
    ATTR_STATEMENT = "Statement"
    ATTR_CLASS = "Class"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 statement: str,
                 classes: str,
                 realraw: str,
                 new_style_override_syntax: bool = False,
                 inherit_file_paths: Set[str] = None,
                 ) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            class {str} -- class code to inherit
            statement {str} -- inherit statement

        Keyword Arguments:
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
            inherit_file_paths {Set[str]} -- Paths of the identified inherited classes
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__Class = classes
        self.__Statement = statement
        self.__FilePaths = inherit_file_paths or {}

    @property
    def Class(self) -> str:
        """Class(es) to inherit

        Returns:
            str: slass(es) to inherit
        """
        return self.__Class

    @property
    def Statement(self) -> str:
        """inherit statement

        Returns:
            str: inherit or inherit_defer
        """
        return self.__Statement

    @property
    def FilePaths(self) -> Set[str]:
        """File paths to identified bbclasses

        As some classes might not be resolvable in the current context
        the order doesn't necessarily reflect the order of the
        inherit statements

        Returns:
            Set[str]: File paths to identified bbclasses
        """
        return self.__FilePaths

    def get_items(self) -> List[str]:
        """Get items

        Returns:
            list -- parsed Class items
        """
        return self.safe_linesplit(self.__Class)


class Unset(Item):
    """Items representing unset statements in bitbake."""

    ATTR_VARNAME = "VarName"
    ATTR_FLAG = "Flag"
    CLASSIFIER = "Unset"

    def __init__(self,
                 origin: str,
                 line: int,
                 infileline: int,
                 rawtext: str,
                 name: str,
                 realraw: str,
                 flag: str = "",
                 new_style_override_syntax: bool = False) -> None:
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- name of variable to be unset

        Keyword Arguments:
            flag {str} -- Flag to unset
            new_style_override_syntax {bool} -- Use ':' a override delimiter (default: {False})
        """
        super().__init__(origin, line, infileline, rawtext, realraw, new_style_override_syntax)
        self.__VarName = name
        self.__Flag = flag

    @property
    def VarName(self) -> str:
        """Variable name

        Returns:
            str: name of the variable
        """
        return self.__VarName

    @property
    def Flag(self) -> str:
        """Variable flag

        Returns:
            str: name of the variable flag
        """
        return self.__Flag

    def get_items(self) -> List[str]:
        """get items

        Returns:
            list -- variable name, variable flag
        """
        return [self.VarName, self.Flag]
