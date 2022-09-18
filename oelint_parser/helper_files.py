import glob
import os
import re
from urllib.parse import urlparse

from oelint_parser.cls_item import Variable
from oelint_parser.constants import CONSTANTS
from oelint_parser.rpl_regex import RegexRpl


def get_files(stash, _file, pattern):
    """Get files matching SRC_URI entries

    Arguments:
        stash {oelint_parser.cls_stash.Stash} -- current stash
        _file {str} -- Full path to filename
        pattern {str} -- glob pattern to apply

    Returns:
        list -- list of files matching pattern
    """
    res = set()
    src_uris = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                 attribute=Variable.ATTR_VAR, attributeValue="SRC_URI")
    files_paths = {
        "{dir}/*/{pattern}".format(dir=os.path.dirname(x.Origin), pattern=pattern) for x in src_uris}
    for item in src_uris:
        files_paths.update({"{dir}/*/{pattern}".format(dir=os.path.dirname(x.Origin), pattern=pattern)
                           for x in stash.GetItemsFor(filename=item.Origin)})
    for item in files_paths:
        res.update(glob.glob(item))
    return sorted(res)


def get_layer_root(name):
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


def find_local_or_in_layer(name, localdir):
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
    return None


def _replace_with_known_mirrors(_in):
    """
    Replace the known mirror configuration items
    """
    for k, v in CONSTANTS.MirrorsKnown.items():
        _in = _in.replace(k, v)
    return _in


def get_scr_components(string):
    """Return SRC_URI components

    Arguments:
        string {str} -- raw string

    Returns:
        dict -- scheme: protocol used, src: source URI, options: parsed options
    """
    _raw = _replace_with_known_mirrors(string)
    _url = urlparse(_replace_with_known_mirrors(string))
    _scheme = _url.scheme
    _tmp = _url.netloc
    if _url.path:
        _tmp += "/" + _url.path.lstrip("/")
    _path = _tmp.split(";")[0]
    _options = _raw.split(";")[1:] if ";" in _raw else []
    _parsed_opt = {x.split("=")[0]: x.split("=")[1]
                   for x in _options if "=" in x}
    return {"scheme": _scheme, "src": _path, "options": _parsed_opt}


def safe_linesplit(string):
    """Split line in a safe manner

    Arguments:
        string {str} -- raw input

    Returns:
        list -- safely split input
    """
    return RegexRpl.split(r"\s|\t|\x1b", string)


def guess_recipe_name(_file):
    """Get the recipe name from filename

    Arguments:
        _file {str} -- filename

    Returns:
        str -- recipe name
    """
    _name, _ = os.path.splitext(os.path.basename(_file))
    return _name.split("_")[0]


def guess_base_recipe_name(_file):
    """Get the base recipe name from filename (aka BPN)

    Arguments:
        _file {str} -- filename

    Returns:
        str -- recipe name
    """
    tmp_ = re.sub(r"^(nativesdk-)*(.+)(-native)*(-cross)*", r"\2", guess_recipe_name(_file))
    tmp_ = re.sub(r"^(.+)(-native)$", r"\1", tmp_)
    tmp_ = re.sub(r"^(.+)(-cross)$", r"\1", tmp_)
    return tmp_


def guess_recipe_version(_file):
    """Get recipe version from filename

    Arguments:
        _file {str} -- filename

    Returns:
        str -- recipe version
    """
    _name, _ = os.path.splitext(os.path.basename(_file))
    return _name.split("_")[-1]


def expand_term(stash, _file, value, spare=None, seen=None):
    """Expand a variable (replacing all variables by known content)

    Arguments:
        stash {oelint_parser.cls_stash.Stash} -- current stash
        _file {str} -- Full path to file
        value {str} -- Variable value to expand

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
        _comp = [x for x in stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                              attribute=Variable.ATTR_VAR, attributeValue=m.group(1)) if not x.AppendOperation()]

        if any(_comp):
            if m.group(1) in seen.keys():
                _rpl = seen[m.group(1)]
            else:
                seen[m.group(1)] = ""
                _rpl = expand_term(
                    stash, _file, _comp[0].VarValueStripped, seen=seen)
                seen[m.group(1)] = _rpl
            res = res.replace(m.group(0), _rpl)
        elif m.group(1) in baseset:
            if m.group(1) in seen.keys():
                _rpl = seen[m.group(1)]
            elif m.group(1) in baseset:
                seen[m.group(1)] = ""
                _rpl = expand_term(
                    stash, _file, baseset[m.group(1)], seen=seen)
                seen[m.group(1)] = _rpl
            else:
                _rpl = m.group(1)
            res = res.replace(m.group(0), _rpl)
        elif m.group(1) in ["PN"]:
            res = res.replace(m.group(0), guess_recipe_name(_file))
        elif m.group(1) in ["BPN"]:
            res = res.replace(m.group(0), guess_base_recipe_name(_file))
        elif m.group(1) in ["PV"]:
            res = res.replace(m.group(0), guess_recipe_version(_file))
        elif not any(_comp):
            continue
    return res


def get_valid_package_names(stash, _file, strippn=False):
    """Get known valid names for packages

    Arguments:
        stash {oelint_parser.cls_stash.Stash} -- current stash
        _file {str} -- Full path to file

    Returns:
        list -- list of valid package names
    """
    res = set()
    _comp = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                              attribute=Variable.ATTR_VAR, attributeValue="PACKAGES")
    _comp += stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                               attribute=Variable.ATTR_VAR, attributeValue="PACKAGE_BEFORE_PN")
    _recipe_name = guess_recipe_name(_file)
    res.add(_recipe_name)
    res.add("{recipe}-ptest".format(recipe=_recipe_name))
    res.update(["{recipe}-{pkg}".format(recipe=_recipe_name, pkg=x)
               for x in ["src", "dbg", "staticdev", "dev", "doc", "locale"]])
    for item in _comp:
        for pkg in [x for x in safe_linesplit(expand_term(stash, _file, item.VarValueStripped, spare=["PN"])) if x]:
            if not strippn:
                _pkg = pkg.replace("${PN}", _recipe_name)
            else:
                _pkg = pkg.replace("${PN}", "")
            res.add(_pkg)
    return res


def get_valid_named_resources(stash, _file):
    """Get list of valid SRCREV resource names

    Arguments:
        stash {oelint_parser.cls_stash.Stash} -- current stash
        _file {str} -- Full path to file

    Returns:
        list -- list of valid SRCREV resource names
    """
    res = set()
    _comp = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                              attribute=Variable.ATTR_VAR, attributeValue="SRC_URI")
    _recipe_name = guess_recipe_name(_file)
    res.add(_recipe_name)
    for item in _comp:
        for name in [x for x in safe_linesplit(item.VarValueStripped) if x]:
            _url = get_scr_components(name)
            if "name" in _url["options"]:
                res.add(_url["options"]["name"].replace("${PN}", _recipe_name))
    return res


def is_image(stash, _file):
    """returns if the file is likely an image recipe or not

    Args:
        stash {oelint_parser.cls_stash.Stash} -- current stash
        _file {str} -- Full path to file

    Returns:
        bool -- True if _file is an image recipe
    """
    res = False

    _inherits = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                  attribute=Variable.ATTR_VAR, attributeValue="inherit")
    res |= any(
        x for x in _inherits if x.VarValueStripped in CONSTANTS.ImagesClasses)

    for _var in CONSTANTS.ImagesVariables:
        res |= any(stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                     attribute=Variable.ATTR_VAR, attributeValue=_var))

    return res


def is_packagegroup(stash, _file):
    """returns if the file is likely a packagegroup recipe or not

    Args:
        stash {oelint_parser.cls_stash.Stash} -- current stash
        _file {str} -- Full path to file

    Returns:
        bool -- True if _file is a packagegroup recipe
    """
    _inherits = stash.GetItemsFor(filename=_file, classifier=Variable.CLASSIFIER,
                                  attribute=Variable.ATTR_VAR, attributeValue="inherit")
    return any(x for x in _inherits if x.VarValueStripped in ["packagegroup"])
