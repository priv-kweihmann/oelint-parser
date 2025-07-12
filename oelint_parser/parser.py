import collections
import os
from typing import Iterable, List

import regex

from oelint_parser.cls_item import (
    AddFragements,
    AddPylib,
    Comment,
    Export,
    FlagAssignment,
    Function,
    FunctionExports,
    Include,
    IncludeAll,
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

__regex_var = regex.compile(
    r"^(?P<varname>([A-Z0-9a-z_.-]|\$|\{|\}|:)+?)(?P<varop>(\s|\t)*(\+|\?|\:|\.)*=(\+|\.)*(\s|\t)*)(?P<varval>.*)")
__regex_func = regex.compile(
    r"^((?P<py>python)\s*|(?P<fr>fakeroot\s*))*(?P<func>[\w\.\-\+\{\}:\$]+)?\s*\(\s*\)\s*\{(?P<funcbody>.*)\s*\}")
__regex_inherit = regex.compile(r"^(\s|\t)*(?P<statement>inherit(_defer)*)(\s+|\t+)(?P<inhname>.+)")
__regex_inherit_glob = regex.compile(r"^INHERIT(?P<varop>(\s|\t)*(\+|\?|\:|\.)*=(\+|\.)*(\s|\t)*)('|\")(?P<inhname>.*)('|\")")
__regex_export_wval = regex.compile(r"^\s*?export(\s+|\t+)(?P<name>.+)\s*=\s*\"(?P<value>.*)\"")
__regex_export_woval = regex.compile(r"^\s*?export(\s+|\t+)(?P<name>.+)\s*$")
__regex_comments = regex.compile(r"^(\s|\t)*#+\s*(?P<body>.*)")
__regex_python = regex.compile(r"^(\s*|\t*)def(\s+|\t+)(?P<funcname>[a-z0-9_\-]+)(\s*|\t*)\(.*\)\:")
__regex_include = regex.compile(r"^(\s*|\t*)(?P<statement>include|require)(\s+|\t+)(?P<incname>[A-za-z0-9\-\./\$\{\}]+)")
__regex_addtask = regex.compile(
    r"^(\s*|\t*)addtask\s+(?P<func>[\w\-]+)\s*((before\s*(?P<before>(([^#\n]*(?=after))|([^#\n]*))))|(after\s*(?P<after>(([^#\n]*(?=before))|([^#\n]*)))))*(?P<comment>#.*|.*?)")
__regex_deltask = regex.compile(r"^(\s*|\t*)deltask\s+(?P<func>[\w\-]+)\s*(?P<comment>#.*)*")
__regex_flagass = regex.compile(
    r"^(\s*|\t*)(?P<name>([A-Z0-9a-z_.-]|\$|\{|\}|:)+?)\[(?P<ident>(\w|-|\.|/|@|_)+)\](?P<varop>(\s|\t)*(\+|\?|\:|\.)*=(\+|\.)*(\s|\t)*)(?P<varval>.*)")
__regex_export_func = regex.compile(r"^EXPORT_FUNCTIONS\s+(?P<func>.*)")
__regex_addpylib = regex.compile(r"^(\s+|\t*)addpylib(\s+|\t+)(?P<path>\$\{LAYERDIR\}/.+)(\s+|\t+)(?P<namespace>.*)")
__regex_unset = regex.compile(r"^(\s+|\t+)*unset(\s+|\t+)+(?P<varname>.+?)(\[*(?P<flag>.+)\])*")
__regex_addfragments = regex.compile(r"addfragments\s+(?P<path>.+)\s+(?P<variable>.+)\s+(?P<flagged>.+)")
__regex_includeall = regex.compile(r"include_all\s+(?P<file>.+)")
__func_start_regexp__ = regex.compile(r".*(((?P<py>python)|(?P<fr>fakeroot))\s*)*(?P<func>[\w\.\-\+\{\}\$]+)?\s*\(\s*\)\s*\{")
__next_line_regex__ = regex.compile(r"\\\s*\n")
__valid_func_name_regex__ = regex.compile(r"^[A-Za-z0-9#]+")


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


def prepare_lines_subparser(_iter: Iterable, lineOffset: int, num: int, line: int, raw_line: str = None, negative: bool = False) -> tuple[dict, str]:
    """preprocess raw input

    Args:
        _iter (iterator): line interator object
        lineOffset (int): current line index
        num (int): internal line counter
        line (int): input string
        raw_line (string, optional): internal line representation. Defaults to None.
        negative (bool): Negative branch inline expansion. Defaults to False

    Returns:
        tuple[dict, str]: preproccessed chunk, buffer for next iteration
    """

    res = {}
    raw_line = raw_line or line

    def iterate(_iter: Iterable, buffer: str) -> tuple[str, str]:
        res = buffer
        next_ = ''
        if RegexRpl.search(__next_line_regex__, res):
            _, line = _iter.__next__()
            while RegexRpl.search(__next_line_regex__, line):
                res += line
                _, line = _iter.__next__()
            res += line
        elif RegexRpl.match(__func_start_regexp__, res):
            _, line = _iter.__next__()
            stopiter = False
            scope_level = 0
            while not stopiter:
                res += line
                if "{" in line:
                    scope_level += 1
                if "}" in line:
                    scope_level -= 1
                    if scope_level <= 0:
                        stopiter = True
                try:
                    _, line = _iter.__next__()
                except StopIteration:
                    stopiter = True
            if line.strip() == "}":
                res += line
        elif res.strip().startswith("def "):
            stopiter = False
            while not stopiter:
                try:
                    _, line = _iter.__next__()
                except StopIteration:
                    stopiter = True
                if stopiter:
                    break
                elif RegexRpl.match(__valid_func_name_regex__, line):
                    next_ = line
                    break
                if line.startswith("def "):
                    next_ = line
                    break
                res += line
        return (res, next_)

    raw_line, nextbuf = iterate(_iter, raw_line)

    real_raw = raw_line
    inline_blocks = []
    while "${@" in raw_line:
        _inline_block = raw_line.find("${@")
        repl = get_full_scope(raw_line[_inline_block:], 3, "{", "}")
        _repl = inlinerep(repl, negative)
        if _repl is None:
            _repl = INLINE_BLOCK
        raw_line = raw_line.replace(repl, _repl)
        inline_blocks.append((repl, _repl))
    res = {"line": num + 1 + lineOffset, "raw": raw_line,
           "realraw": real_raw,
           "inline_blocks": inline_blocks,
           "cnt": raw_line.replace("\n", "").replace("\\", chr(0x1b))}
    return (res, nextbuf)


def prepare_lines(_file: str, lineOffset: int = 0, negative: bool = False) -> List[str]:
    """break raw file input into preprocessed chunks

    Args:
        _file (string): Full path to file
        lineOffset (int, optional): line offset counter. Defaults to 0.
        negative (bool): Negative branch inline expansion. Defaults to False

    Returns:
        list: preprocessed list of chunks
    """
    try:
        prep_lines = []
        with open(_file) as i:
            _iter = enumerate(i.readlines())
            nextbuf = ''
            for num, line in _iter:
                line = nextbuf + line
                item, nextbuf = prepare_lines_subparser(_iter, lineOffset, num, line, negative=negative)
                prep_lines.append(item)
    except FileNotFoundError:
        pass
    return prep_lines


def get_items(stash: object,
              _file: str,
              lineOffset: int = 0,
              new_style_override_syntax: bool = False,
              negative: bool = False) -> List[Item]:
    """parses file

    Args:
        stash (oelint_parser.cls_stash.Stash): Stash object
        _file (string): Full path to file
        lineOffset (int, optional): line offset counter. Defaults to 0.
        new_style_override_syntax (bool, optional): default to new override syntax (default: False)
        negative (bool, optional): Negative branch inline expansion (default: False)

    Returns:
        list: List of oelint_parser.cls_item.* representations
    """
    res = []

    _order = collections.OrderedDict([
        ("comment", __regex_comments),
        ("func", __regex_func),
        ("inherit", __regex_inherit),
        ("inherit_glob", __regex_inherit_glob),
        ("export", __regex_export_wval),
        ("export_noval", __regex_export_woval),
        ("python", __regex_python),
        ("include", __regex_include),
        ("include_all", __regex_includeall),
        ("addtask", __regex_addtask),
        ("deltask", __regex_deltask),
        ("unset", __regex_unset),
        ("flagassign", __regex_flagass),
        ("exportfunc", __regex_export_func),
        ("addpylib", __regex_addpylib),
        ("addfragments", __regex_addfragments),
        ("vars", __regex_var),
    ])

    includeOffset = 0
    override_syntax_new = new_style_override_syntax

    if not os.path.isabs(_file):
        _file = os.path.abspath(_file)

    for line in prepare_lines(_file, lineOffset, negative=negative):
        good = False
        parameter = {
            'infileline': line['line'] - lineOffset,
            'inline_blocks': line['inline_blocks'],
            'line': line['line'] + includeOffset,
            'new_style_override_syntax': override_syntax_new,
            'origin': _file,
            'rawtext': line['raw'],
            'realraw': line['realraw'],
        }
        for k, v in _order.items():
            m = RegexRpl.match(v, line["cnt"], regex.regex.MULTILINE)
            if m:
                if k == "python":
                    parameter['name'] = m.group("funcname")
                    res.append(PythonBlock(**parameter))
                    good = True
                    break
                elif k == "exportfunc":
                    parameter['name'] = m.group("func")
                    res.append(FunctionExports(**parameter))
                    good = True
                    break
                elif k == "vars":
                    parameter['name'] = m.group("varname")
                    parameter['value'] = m.group("varval")
                    parameter['operator'] = m.group("varop")
                    res.append(Variable(**parameter))
                    good = True
                    break
                elif k == "func":
                    parameter['name'] = m.group("func")
                    parameter['body'] = m.group("funcbody")
                    parameter['python'] = m.group("py")
                    parameter['fakeroot'] = m.group("fr")
                    res.append(Function(**parameter))
                    good = True
                    break
                elif k == "unset":
                    parameter['name'] = m.group("varname")
                    parameter['flag'] = (m.groupdict().get("flag", "") or "").strip('[]')
                    res.append(Unset(**parameter))
                    good = True
                    break
                elif k == "comment":
                    res.append(Comment(**parameter))
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
                    parameter['statement'] = m.group("statement")
                    parameter['classes'] = m.group("inhname")
                    parameter['inherit_file_paths'] = _found_paths
                    res.append(Inherit(**parameter))
                    good = True
                    break
                elif k == "inherit_glob":
                    inhname = stash.ExpandTerm(_file, m.group("inhname"))
                    _found_paths = set()
                    for inh_item in [x for x in inhname.split(' ') if x]:
                        if not inh_item.endswith(".bbclass"):
                            inh_item += ".bbclass"
                        _path = None
                        for location in ["classes", "classes-global"]:
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
                    parameter['statement'] = 'INHERIT'
                    parameter['classes'] = m.group("inhname")
                    parameter['inherit_file_paths'] = _found_paths
                    res.append(Inherit(**parameter))
                    good = True
                    break
                elif k == "export":
                    parameter['name'] = m.group("name").strip()
                    parameter['value'] = m.group("value")
                    res.append(Export(**parameter))
                    good = True
                    break
                elif k == "export_noval":
                    parameter['name'] = m.group("name").strip()
                    parameter['value'] = ''
                    res.append(Export(**parameter))
                    good = True
                    break
                elif k == "flagassign":
                    parameter['name'] = m.group("name")
                    parameter['ident'] = m.group("ident")
                    parameter['value'] = m.group("varval")
                    parameter['varop'] = m.group("varop")
                    res.append(FlagAssignment(**parameter))
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
                    _comment = _g.get('comment', '')
                    parameter['name'] = m.group("func")
                    parameter['before'] = _b
                    parameter['after'] = _a
                    parameter['comment'] = _comment
                    res.append(TaskAdd(**parameter))
                    good = True
                    break
                elif k == "deltask":
                    parameter['name'] = m.group("func")
                    parameter['comment'] = m.groupdict().get('comment', '')
                    res.append(TaskDel(**parameter))
                    good = True
                    break
                elif k == "include":
                    _path = stash.FindLocalOrLayer(
                        stash.ExpandTerm(_file, m.group("incname")), os.path.dirname(_file))
                    if _path:
                        tmp = stash.AddFile(
                            _path, lineOffset=line["line"], forcedLink=_file)
                        if any(tmp):
                            includeOffset += max([x.InFileLine for x in tmp])
                    parameter['incname'] = m.group("incname")
                    parameter['fileincluded'] = _path or ''
                    parameter['statement'] = m.group("statement")
                    res.append(Include(**parameter))
                    good = True
                    break
                elif k == "include_all":
                    parameter['file'] = m.group('file')
                    res.append(IncludeAll(**parameter))
                    good = True
                    break
                elif k == "addpylib":
                    parameter['path'] = m.group("path")
                    parameter['namespace'] = m.group("namespace")
                    res.append(AddPylib(**parameter))
                    good = True
                    break
                elif k == "addfragments":
                    parameter['path'] = m.group("path")
                    parameter['variable'] = m.group("variable")
                    parameter['flagged'] = m.group("flagged")
                    res.append(AddFragements(**parameter))
                    good = True
                    break
        if not good:
            res.append(Item(**parameter))
        override_syntax_new |= res[-1].IsNewStyleOverrideSyntax

    return res
