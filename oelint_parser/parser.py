import collections
import os
from typing import Iterable, List

import regex

from oelint_parser.cls_item import (
    AddPylib,
    Comment,
    Export,
    FlagAssignment,
    Function,
    FunctionExports,
    Include,
    Inherit,
    Item,
    PythonBlock,
    TaskAdd,
    TaskDel,
    Unset,
    Variable,
)
from oelint_parser.inlinerep import inlinerep
from oelint_parser.rpl_regex import RegexRpl

INLINE_BLOCK = "!!!inlineblock!!!"


def get_full_scope(_string: str, offset: int, _sstart: int, _send: int) -> str:
    """get full block of an inline statement

    Args:
        _string (str): input string
        offset (int): offset in string
        _sstart (int): block start index
        _send (int): block end index

    Returns:
        str: full block on inline statement
    """
    scopelevel = 0
    pos = 0
    for c in _string[offset:]:
        if c == _sstart:
            scopelevel += 1
        elif c == _send:
            scopelevel -= 1
        pos += 1
        if scopelevel < 0:
            break
    return _string[:pos + offset]


def prepare_lines_subparser(_iter: Iterable, lineOffset: int, num: int, line: int, raw_line: str = None) -> List[str]:
    """preprocess raw input

    Args:
        _iter (iterator): line interator object
        lineOffset (int): current line index
        num (int): internal line counter
        line (int): input string
        raw_line (string, optional): internal line representation. Defaults to None.

    Returns:
        list: list of preproccessed chunks
    """
    __func_start_regexp__ = r".*(((?P<py>python)|(?P<fr>fakeroot))\s*)*(?P<func>[\w\.\-\+\{\}\$]+)?\s*\(\s*\)\s*\{"
    res = []
    raw_line = raw_line or line
    if RegexRpl.search(r"\\\s*\n", raw_line):
        _, line = _iter.__next__()
        while RegexRpl.search(r"\\\s*\n", line):
            raw_line += line
            _, line = _iter.__next__()
        raw_line += line
    elif RegexRpl.match(__func_start_regexp__, raw_line):
        _, line = _iter.__next__()
        stopiter = False
        scope_level = 0
        while not stopiter:
            raw_line += line
            if "{" in line:
                scope_level += 1
            if "}" in line:
                scope_level -= 1
            try:
                _, line = _iter.__next__()
            except StopIteration:
                stopiter = True
            if line.strip() == "}" and not scope_level:
                stopiter = True
        if line.strip() == "}":
            raw_line += line
    elif raw_line.strip().startswith("def "):
        stopiter = False
        while not stopiter:
            try:
                _, line = _iter.__next__()
            except StopIteration:
                stopiter = True
            if RegexRpl.match("^[A-Za-z0-9#]+", line) or stopiter:
                if not stopiter:
                    res += prepare_lines_subparser(_iter,
                                                   lineOffset, num, line)
                break
            if line.startswith("def "):
                raw_line = line
                res += prepare_lines_subparser(_iter,
                                               lineOffset, num, line, raw_line=raw_line)
                break
            raw_line += line

    real_raw = raw_line
    while raw_line.find("${@") != -1:
        _inline_block = raw_line.find("${@")
        repl = get_full_scope(raw_line[_inline_block:], len("${@"), "{", "}")
        _repl = inlinerep(repl)
        if _repl is None:
            _repl = INLINE_BLOCK
        raw_line = raw_line.replace(repl, _repl)
    res.append({"line": num + 1 + lineOffset, "raw": raw_line,
                "realraw": real_raw,
                "cnt": raw_line.replace("\n", "").replace("\\", chr(0x1b))})
    return res


def prepare_lines(_file: str, lineOffset: int = 0) -> List[str]:
    """break raw file input into preprocessed chunks

    Args:
        _file (string): Full path to file
        lineOffset (int, optional): line offset counter. Defaults to 0.

    Returns:
        list: preprocessed list of chunks
    """
    try:
        prep_lines = []
        with open(_file) as i:
            _iter = enumerate(i.readlines())
            for num, line in _iter:
                prep_lines += prepare_lines_subparser(
                    _iter, lineOffset, num, line)
    except FileNotFoundError:
        pass
    return prep_lines


def get_items(stash: object,
              _file: str,
              lineOffset: int = 0,
              new_style_override_syntax: bool = False) -> List[Item]:
    """parses file

    Args:
        stash (oelint_parser.cls_stash.Stash): Stash object
        _file (string): Full path to file
        lineOffset (int, optional): line offset counter. Defaults to 0.
        new_style_override_syntax (bool, optional): default to new override syntax (default: False)

    Returns:
        list: List of oelint_parser.cls_item.* representations
    """
    res = []
    __regex_var = r"^(?P<varname>([A-Z0-9a-z_.-]|\$|\{|\}|:)+?)(?P<varop>(\s|\t)*(\+|\?|\:|\.)*=(\+|\.)*(\s|\t)*)(?P<varval>.*)"
    __regex_func = r"^((?P<py>python)\s*|(?P<fr>fakeroot\s*))*(?P<func>[\w\.\-\+\{\}:\$]+)?\s*\(\s*\)\s*\{(?P<funcbody>.*)\s*\}"
    __regex_inherit = r"^(\s|\t)*(?P<statement>inherit(_defer)*)(\s+|\t+)(?P<inhname>.+)"
    __regex_export_wval = r"^\s*?export(\s+|\t+)(?P<name>.+)\s*=\s*\"(?P<value>.*)\""
    __regex_export_woval = r"^\s*?export(\s+|\t+)(?P<name>.+)\s*$"
    __regex_comments = r"^(\s|\t)*#+\s*(?P<body>.*)"
    __regex_python = r"^(\s*|\t*)def(\s+|\t+)(?P<funcname>[a-z0-9_\-]+)(\s*|\t*)\(.*\)\:"
    __regex_include = r"^(\s*|\t*)(?P<statement>include|require)(\s+|\t+)(?P<incname>[A-za-z0-9\-\./\$\{\}]+)"
    __regex_addtask = r"^(\s*|\t*)addtask\s+(?P<func>[\w\-]+)\s*((before\s*(?P<before>((.*(?=after))|(.*))))|(after\s*(?P<after>((.*(?=before))|(.*)))))*"
    __regex_deltask = r"^(\s*|\t*)deltask\s+(?P<func>[\w\-]+)"
    __regex_flagass = r"^(\s*|\t*)(?P<name>([A-Z0-9a-z_.-]|\$|\{|\}|:)+?)\[(?P<ident>(\w|-|\.)+)\](?P<varop>(\s|\t)*(\+|\?|\:|\.)*=(\+|\.)*(\s|\t)*)(?P<varval>.*)"
    __regex_export_func = r"^EXPORT_FUNCTIONS\s+(?P<func>.*)"
    __regex_addpylib = r"^(\s+|\t*)addpylib(\s+|\t+)(?P<path>\$\{LAYERDIR\}/.+)(\s+|\t+)(?P<namespace>.*)"
    __regex_unset = r"^(\s+|\t+)*unset(\s+|\t+)+(?P<varname>.+?)(\[*(?P<flag>.+)\])*"

    _order = collections.OrderedDict([
        ("comment", __regex_comments),
        ("func", __regex_func),
        ("inherit", __regex_inherit),
        ("export", __regex_export_wval),
        ("export_noval", __regex_export_woval),
        ("python", __regex_python),
        ("include", __regex_include),
        ("addtask", __regex_addtask),
        ("deltask", __regex_deltask),
        ("unset", __regex_unset),
        ("flagassign", __regex_flagass),
        ("exportfunc", __regex_export_func),
        ("addpylib", __regex_addpylib),
        ("vars", __regex_var),
    ])

    includeOffset = 0
    override_syntax_new = new_style_override_syntax

    if not os.path.isabs(_file):
        _file = os.path.abspath(_file)

    for line in prepare_lines(_file, lineOffset):
        good = False
        for k, v in _order.items():
            m = RegexRpl.match(v, line["cnt"], regex.regex.MULTILINE)
            if m:
                if k == "python":
                    res.append(
                        PythonBlock(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("funcname"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "exportfunc":
                    res.append(
                        FunctionExports(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("func"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "vars":
                    res.append(
                        Variable(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("varname"),
                            m.group("varval"),
                            m.group("varop"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "func":
                    res.append(
                        Function(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("func"),
                            m.group("funcbody"),
                            line["realraw"],
                            m.group("py"),
                            m.group("fr"),
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "unset":
                    res.append(
                        Unset(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("varname"),
                            line["realraw"],
                            flag=(m.groupdict().get("flag", "") or "").strip('[]'),
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "comment":
                    res.append(
                        Comment(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "inherit":
                    inhname = stash.ExpandTerm(_file, m.group("inhname"))
                    _found_paths = set()
                    for inh_item in [x for x in inhname.split(' ') if x]:
                        if not inh_item.endswith(".bbclass"):
                            inh_item += ".bbclass"
                        _path = None
                        for location in ["classes", "classes-recipe", "classes-global"]:
                            _path = stash.FindLocalOrLayer(
                                os.path.join(location, inh_item),
                                os.path.dirname(_file))
                            if _path:
                                break
                        if _path:
                            _found_paths.add(_path)
                            tmp = stash.AddFile(
                                _path, lineOffset=line["line"], forcedLink=_file)
                            if any(tmp):
                                includeOffset += max([x.InFileLine for x in tmp])
                    res.append(
                        Inherit(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("statement"),
                            m.group("inhname"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                            inherit_file_paths=_found_paths,
                        ))
                    good = True
                    break
                elif k == "export":
                    res.append(
                        Export(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("name").strip(),
                            m.group("value"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "export_noval":
                    res.append(
                        Export(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("name").strip(),
                            "",
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "flagassign":
                    res.append(
                        FlagAssignment(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("name"),
                            m.group("ident"),
                            m.group("varval"),
                            m.group("varop"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "addtask":
                    # treat the following as variables
                    if any(m.group("func").startswith(x) for x in ['pkg_preinst', 'pkg_postinst', 'pkg_prerm', 'pkg_postrm']):
                        continue
                    _g = m.groupdict()
                    if "before" in _g.keys():
                        _b = _g["before"]
                    else:
                        _b = ""
                    if "after" in _g.keys():
                        _a = _g["after"]
                    else:
                        _a = ""
                    res.append(
                        TaskAdd(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("func"),
                            line["realraw"],
                            _b,
                            _a,
                            new_style_override_syntax=override_syntax_new,
                        ))
                    break
                elif k == "deltask":
                    res.append(
                        TaskDel(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("func"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    break
                elif k == "include":
                    _path = stash.FindLocalOrLayer(
                        stash.ExpandTerm(_file, m.group("incname")), os.path.dirname(_file))
                    if _path:
                        tmp = stash.AddFile(
                            _path, lineOffset=line["line"], forcedLink=_file)
                        if any(tmp):
                            includeOffset += max([x.InFileLine for x in tmp])
                    res.append(
                        Include(
                            _file,
                            line["line"],
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("incname"),
                            m.group("statement"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
                elif k == "addpylib":
                    res.append(
                        AddPylib(
                            _file,
                            line["line"] + includeOffset,
                            line["line"] - lineOffset,
                            line["raw"],
                            m.group("path"),
                            m.group("namespace"),
                            line["realraw"],
                            new_style_override_syntax=override_syntax_new,
                        ))
                    good = True
                    break
        if not good:
            res.append(
                Item(
                    _file,
                    line["line"],
                    line["line"] - lineOffset,
                    line["raw"],
                    line["realraw"],
                    new_style_override_syntax=override_syntax_new,
                ))
        override_syntax_new |= res[-1].IsNewStyleOverrideSyntax

    return res
