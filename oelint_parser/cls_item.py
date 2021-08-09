import textwrap
import re
import os

from oelint_parser.constants import CONSTANTS


class Item():
    """Base class for all Stash items
    """
    ATTR_LINE = "Line"
    ATTR_RAW = "Raw"
    ATTR_ORIGIN = "Origin"
    CLASSIFIER = "Item"
    ATTR_SUB = "SubItem"

    def __init__(self, origin, line, infileline, rawtext, realraw):
        """constructor

        Arguments:
            origin {str} -- Full path of origin file
            line {int} -- Overall line counter
            infileline {int} -- Line number in file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
        """
        self.__Line = line
        self.__Raw = rawtext
        self.__Links = []
        self.__Origin = origin
        self.__InFileLine = infileline
        self.__IncludedFrom = []
        self.__RealRaw = realraw or rawtext

    @property
    def Line(self):
        """Overall line count

        Returns:
            int: overall line count of item
        """
        return self.__Line

    @Line.setter
    def Line(self, value):
        self.__Line = value

    @property
    def Raw(self):
        """Raw string (without inline code blocks)

        Returns:
            str: raw string of item
        """
        return self.__Raw

    @Raw.setter
    def Raw(self, value):
        self.__Raw = value

    @property
    def Links(self):
        """Linked files

        Returns:
            list: list of full path of linked files
        """
        return self.__Links

    @Links.setter
    def Links(self, value):
        self.__Links = value

    @property
    def Origin(self):
        """origin of item

        Returns:
            str: full path of origin file
        """
        return self.__Origin

    @property
    def InFileLine(self):
        """Line count in file

        Returns:
            int: [description]
        """
        return self.__InFileLine

    @property
    def IncludedFrom(self):
        """Files include this item

        Returns:
            list: list of files including this item
        """
        return self.__IncludedFrom

    @IncludedFrom.setter
    def IncludedFrom(self, value):
        self.__IncludedFrom = value

    @property
    def RealRaw(self):
        """Completely unprocessed raw text

        Returns:
            str: completely unprocessed raw text
        """
        return self.__RealRaw

    @RealRaw.setter
    def RealRaw(self, value):
        self.__RealRaw = value

    @property
    def IsFromClass(self):
        """Item comes from a bbclass

        Returns:
            bool: if item was set in a bbclass
        """
        return self.__Origin.endswith(".bbclass")

    @staticmethod
    def safe_linesplit(string):
        """Safely split an input line to chunks

        Args:
            string (str): raw input string

        Returns:
            list: list of chunks of original string
        """
        return Item(None, None, None, None, None)._safe_linesplit(string)

    def _safe_linesplit(self, string):
        return [x for x in re.split(r"\s|\t|\x1b", string) if x]

    def get_items(self):
        """Return single items

        Returns:
            list -- lines of raw input
        """
        return self._safe_linesplit(self.Raw)

    def extract_sub(self, name):
        """Extract modifiers

        Arguments:
            name {str} -- input string

        Returns:
            tuple -- clean variable name, modifiers, package specific modifiers
        """
        chunks = re.split(r"_|:", name)
        _suffix = []
        _var = []
        _pkgspec = []
        for i in chunks:
            tmp = ""
            if "-" in i:
                # just use the prefix in case a dash is found
                # that addresses things like FILES_${PN}-dev
                tmp = "-" + "-".join(i.split("-")[1:])
                i = i.split("-")[0]
            if re.match("^[a-z0-9{}$]+$", i):
                _suffix.append(i + tmp)
            else:
                _var.append(i + tmp)
        _var = [x for x in _var if x]
        _suffix = [x for x in _suffix if x]
        if not _var and _suffix:
            # special case for pkg-functions
            _var = _suffix
            _suffix = []
        return ("_".join(_var), "_".join(_suffix), _pkgspec)

    def extract_sub_func(self, name):
        """Extract modifiers for functions

        Arguments:
            name {str} -- input value

        Returns:
            tuple -- clean function name, modifiers
        """
        chunks = re.split(r"_|:", name)
        _marker = ["append", "prepend", "class-native",
                   "class-cross", "class-target", "remove"]
        _suffix = []
        _var = []
        for i in chunks:
            if i in _marker or "_".join(_var) in CONSTANTS.FunctionsKnown:
                _suffix = chunks[chunks.index(i):]
                break
            else:
                _var.append(i)
        _var = [x for x in _var if x]
        _suffix = [x for x in _suffix if x]
        return ("_".join(_var), "_".join(_suffix))

    def IsFromAppend(self):
        """Item originates from a bbappend

        Returns:
            bool -- True if coming from a bbappend
        """
        return self.Origin.endswith(".bbappend")

    def AddLink(self, _file):
        """Links files to each other in stash

        Arguments:
            _file {str} -- Full path of file to link against
        """
        self.Links.append(_file)
        self.Links = list(set(self.Links))

    def GetAttributes(self):
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

    def __repr__(self):
        return "{} -- {}\n".format(self.__class__.__name__, self.GetAttributes())


class Variable(Item):
    """Stash item for variables
    """
    ATTR_VAR = "VarName"
    ATTR_VARVAL = "VarValue"
    ATTR_VARRAW = "RawVarName"
    ATTR_VARVALSTRIPPED = "VarValueStripped"
    CLASSIFIER = "Variable"
    VAR_VALID_OPERATOR = [" = ", " += ",
                          " ?= ", " ??= ", " := ", " .= ", " =+ ", " =. "]

    def __init__(self, origin, line, infileline, rawtext, name, value, operator, flag, realraw):
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
            flag {str} -- Optional variable flag
        """
        super().__init__(origin, line, infileline, rawtext, realraw)
        if "inherit" != name:
            self.__VarName, self.__SubItem, self.__PkgSpec = self.extract_sub(
                name)
            self.__SubItem += " ".join(self.PkgSpec)
        else:
            self.__VarName = name
            self.__SubItem = ""
            self.__PkgSpec = []
        self.__SubItems = [x for x in self.SubItem.split(
            "_") + self.PkgSpec if x]
        self.__VarValue = value
        self.__VarOp = operator
        self.__Flag = flag or ""
        self.__RawVarName = "{}[{}]".format(
            self.VarName, self.Flag) if self.Flag else self.VarName
        self.__VarValueStripped = self.VarValue.strip().lstrip('"').rstrip('"')

    @property
    def VarName(self):
        """Variable name

        Returns:
            str: name of variable
        """
        return self.__VarName

    @property
    def SubItem(self):
        """Variable modifiers

        Returns:
            str: variable modifiers like packages, machines, appends, prepends
        """
        return self.__SubItem

    @property
    def SubItems(self):
        """Variable modifiers list

        Returns:
            list: variable modifiers list like packages, machines, appends, prepends
        """
        return self.__SubItems

    @property
    def PkgSpec(self):
        """Variable modifiers

        Returns:
            str: variable modifiers like packages, machines, appends, prepends
        """
        return self.__PkgSpec

    @property
    def VarValue(self):
        """variable value

        Returns:
            str: unstripped variable value
        """
        return self.__VarValue

    @VarValue.setter
    def VarValue(self, value):
        self.__VarValue = value

    @property
    def VarOp(self):
        """Variable operation

        Returns:
            str: operation did on the variable
        """
        return self.__VarOp

    @property
    def Flag(self):
        """Variable flag like PACKAGECONFIG[xyz]

        Returns:
            str: variable sub flags
        """
        return self.__Flag

    @property
    def RawVarName(self):
        """Variable name and flags combined

        Returns:
            str: raw representation of the variable name
        """
        return self.__RawVarName

    @property
    def VarValueStripped(self):
        """Stripped variable value

        Returns:
            str: stripped version of variable value
        """
        return self.__VarValueStripped

    def IsAppend(self):
        """Check if operation is an append

        Returns:
            bool -- True is variable is appended
        """
        return self.VarOp in [" += ", " =+ ", " =. ", " .= "] or "append" in self.SubItems or "prepend" in self.SubItems

    def AppendOperation(self):
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

    def get_items(self, override="", versioned=False):
        """Get items of variable value

        Arguments:
            override {str} -- String to take instead of VarValue
            versioned {bool} -- items can be versioned (versions will be stripped in this case)

        Returns:
            list -- clean list of items in variable value
        """
        _x = override.strip('"') or self.VarValue.strip('"')
        if versioned:
            _x = re.sub(r"\s*\(.*?\)", "", _x)
        return self._safe_linesplit(_x)

    def IsMultiLine(self):
        """Check if variable has a multiline assignment

        Returns:
            bool -- True if multiline
        """
        return "\\x1b" in self.Raw or "\\\n" in self.Raw

    def GetMachineEntry(self):
        """Get machine specific entries in variable

        Returns:
            str -- machine specific modifier of variable or ""
        """
        for x in self.SubItems:
            if x not in ["append", "prepend", "class-native", "class-nativesdk", "class-cross", "class-target", "remove", "machine"] + self.PkgSpec:
                return x
        return ""

    def GetClassOverride(self):
        """Get class specific entries in variable

        Returns:
            str -- class specific modifier of variable or ""
        """
        for x in self.SubItems:
            if x in ["class-native", "class-nativesdk", "class-cross", "class-target"]:
                return x
        return ""


class Comment(Item):
    CLASSIFIER = "Comment"

    def __init__(self, origin, line, infileline, rawtext, realraw):
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
        """
        super().__init__(origin, line, infileline, rawtext, realraw)

    def get_items(self):
        """Get single lines of block

        Returns:
            list -- single lines of comment block
        """
        return self.Raw.split("\n")


class Include(Item):
    CLASSIFIER = "Include"
    ATTR_INCNAME = "IncName"
    ATTR_STATEMENT = "Statement"

    def __init__(self, origin, line, infileline, rawtext, incname, statement, realraw):
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            incname {str} -- raw name of the include file
            statement {str} -- either include or require
        """
        super().__init__(origin, line, infileline, rawtext, realraw)
        self.__IncName = incname
        self.__Statement = statement

    @property
    def IncName(self):
        """Include name

        Returns:
            str: name of the file to include/require
        """
        return self.__IncName

    @property
    def Statement(self):
        """statement either include or require

        Returns:
            str: include or require
        """
        return self.__Statement

    def get_items(self):
        """Get items

        Returns:
            list -- include name, include statement
        """
        return [self.IncName, self.Statement]


class Export(Item):
    CLASSIFIER = "Exclude"
    ATTR_INCNAME = "Name"
    ATTR_STATEMENT = "Value"

    def __init__(self, origin, line, infileline, rawtext, name, value, realraw):
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- variable name of the export
            value {str} -- (optional) value of the export
        """
        super().__init__(origin, line, infileline, rawtext, realraw)
        self.__Name = name
        self.__Value = value

    @property
    def Name(self):
        """Name of the exported var

        Returns:
            str: name of the exported var
        """
        return self.__Name

    @property
    def Value(self):
        """value of the export

        Returns:
            str: optional value of the export
        """
        return self.__Value

    def get_items(self):
        """Get items

        Returns:
            list -- include name, include statement
        """
        return [self.Name, self.Value]


class Function(Item):
    ATTR_FUNCNAME = "FuncName"
    ATTR_FUNCBODY = "FuncBody"
    CLASSIFIER = "Function"

    def __init__(self, origin, line, infileline, rawtext, name, body, realraw, python=False, fakeroot=False):
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
        """
        super().__init__(origin, line, infileline, rawtext, realraw)
        self.__IsPython = python is not None
        self.__IsFakeroot = fakeroot is not None
        name = name or ""
        self.__FuncName, self.__SubItem = self.extract_sub_func(name.strip())
        self.__SubItems = self.SubItem.split("_")
        self.__FuncBody = body
        self.__FuncBodyStripped = body.replace(
            "{", "").replace("}", "").replace("\n", "").strip()
        self.__FuncBodyRaw = textwrap.dedent(
            rawtext[rawtext.find("{") + 1:].rstrip().rstrip("}"))

    @property
    def IsPython(self):
        """Is python function

        Returns:
            bool: is a python function
        """
        return self.__IsPython

    @property
    def IsFakeroot(self):
        """Is fakeroot function

        Returns:
            bool: is a python function
        """
        return self.__IsFakeroot

    @property
    def FuncName(self):
        """Function name

        Returns:
            str: name of function
        """
        return self.__FuncName

    @property
    def SubItem(self):
        """Function modifiers

        Returns:
            str: function modifiers like packages, machines, appends, prepends
        """
        return self.__SubItem

    @property
    def SubItems(self):
        """Function modifiers list

        Returns:
            list: function modifiers list like packages, machines, appends, prepends
        """
        return self.__SubItems

    @property
    def FuncBody(self):
        """Function body

        Returns:
            str: function body text
        """
        return self.__FuncBody

    @property
    def FuncBodyStripped(self):
        """Stripped function body

        Returns:
            str: stripped function body text
        """
        return self.__FuncBodyStripped

    @property
    def FuncBodyRaw(self):
        """Raw function body (including brackets)

        Returns:
            str: raw function body text
        """
        return self.__FuncBodyRaw

    def GetMachineEntry(self):
        """Get machine specific modifiers

        Returns:
            str -- machine specific modifier or ""
        """
        for x in self.SubItems:
            if x not in ["append", "prepend", "class-native", "class-cross", "class-target", "remove", "machine"]:
                return x
        return ""

    def IsAppend(self):
        """Return if function appends another function

        Returns:
            bool -- True is append or prepend operation
        """
        return any([x in ["append", "prepend"] for x in self.SubItems])

    def get_items(self):
        """Get items of function body

        Returns:
            list -- single lines of function body
        """
        return self.FuncBodyRaw.split("\n")


class PythonBlock(Item):
    ATTR_FUNCNAME = "FuncName"
    CLASSIFIER = "PythonBlock"

    def __init__(self, origin, line, infileline, rawtext, name, realraw):
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- Function name
        """
        super().__init__(origin, line, infileline, rawtext, realraw)
        self.__FuncName = name

    @property
    def FuncName(self):
        """Function name

        Returns:
            str: name of function
        """
        return self.__FuncName

    def get_items(self):
        """Get lines of function body

        Returns:
            list -- lines of function body
        """
        return self.Raw.split("\n")


class TaskAssignment(Item):
    ATTR_FUNCNAME = "FuncName"
    ATTR_VAR = "VarName"
    ATTR_VARVAL = "VarValue"
    CLASSIFIER = "TaskAssignment"

    def __init__(self, origin, line, infileline, rawtext, name, ident, value, realraw):
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
        """
        super().__init__(origin, line, infileline, rawtext, realraw)
        self.__FuncName = name
        self.__VarName = ident
        self.__VarValue = value

    @property
    def FuncName(self):
        """Function name

        Returns:
            str: name of function
        """
        return self.__FuncName

    @property
    def VarValue(self):
        """Task flag value

        Returns:
            str: Task flag value
        """
        return self.__VarValue

    @property
    def VarName(self):
        """Task flag name

        Returns:
            str: name of task flag
        """
        return self.__VarName

    def get_items(self):
        """Get items

        Returns:
            list -- function name, flag, modification value
        """
        return [self.FuncName, self.VarName, self.VarValue]

class FunctionExports(Item):
    ATTR_FUNCNAME = "FuncName"
    CLASSIFIER = "FunctionExports"

    def __init__(self, origin, line, infileline, rawtext, name, realraw):
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            rawtext {str} -- Raw input string (except inline code blocks)
            realraw {str} -- Unprocessed input
            name {str} -- name of function to be exported
        """
        super().__init__(origin, line, infileline, rawtext, realraw)
        self.__FuncNames = name

    @property
    def FuncNames(self):
        """Function name

        Returns:
            str: names of exported functions
        """
        return self.__FuncNames

    def get_items(self):
        """Get items

        Returns:
            list -- function names
        """
        return [x for x in self.__FuncNames.split(" ") if x]

    def get_items_unaliased(self):
        """Get items with their bbclass scope names

        Returns:
            list -- function names in the scope of a bbclass (foo becomes classname-foo in this case)
        """
        _name, _ = os.path.splitext(os.path.basename(self.Origin))
        return ["{}-{}".format(_name, x) for x in self.get_items()]

class TaskAdd(Item):
    ATTR_FUNCNAME = "FuncName"
    ATTR_BEFORE = "Before"
    ATTR_AFTER = "After"
    CLASSIFIER = "TaskAdd"

    def __init__(self, origin, line, infileline, rawtext, name, realraw, before="", after=""):
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
        """
        super().__init__(origin, line, infileline, rawtext, realraw)
        self.__FuncName = name
        self.__Before = [x for x in (before or "").split(" ") if x]
        self.__After = [x for x in (after or "").split(" ") if x]

    @property
    def FuncName(self):
        """Function name

        Returns:
            str: name of function
        """
        return self.__FuncName

    @property
    def Before(self):
        """Tasks executed before

        Returns:
            list: tasks to be executed before
        """
        return self.__Before

    @property
    def After(self):
        """Tasks executed after

        Returns:
            list: tasks to be executed after
        """
        return self.__After

    def get_items(self):
        """get items

        Returns:
            list -- function name, all before statements, all after statements
        """
        return [self.FuncName] + self.Before + self.After


class MissingFile(Item):
    ATTR_FILENAME = "Filename"
    ATTR_STATEMENT = "Statement"
    CLASSIFIER = "MissingFile"

    def __init__(self, origin, line, infileline, filename, statement):
        """constructor

        Arguments:
            origin {str} -- Full path to file of origin
            line {int} -- Overall line counter
            infileline {int} -- Line counter in the particular file
            filename {str} -- filename of the file that can't be found
            statement {str} -- either include or require
        """
        super().__init__(origin, line, infileline, "", "")
        self.__Filename = filename
        self.__Statement = statement

    @property
    def Filename(self):
        """Filename of the file missing

        Returns:
            str: filename that can't be resolved
        """
        return self.__Filename

    @property
    def Statement(self):
        """statement either include or require

        Returns:
            str: include or require
        """
        return self.__Statement

    def get_items(self):
        return [self.Filename, self.Statement]
