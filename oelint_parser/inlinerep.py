import regex

from oelint_parser.rpl_regex import RegexRpl

__bb_utils_filter_regex__ = regex.compile(r'(.*)bb\.utils\.filter\(\s*(?P<trueval>.*?),.*?,.*?\)')
__bb_utils_contains_regex__ = regex.compile(
    r"(.*)bb\.utils\.contains\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*(?P<falseval>.*?),\s*.\)")
__bb_utils_contains_any_regex__ = regex.compile(
    r"(.*)bb\.utils\.contains_any\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*(?P<falseval>.*?),\s*.\)")
__oe_utils_conditional_regex__ = regex.compile(
    r"(.*)oe\.utils\.conditional\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*(?P<falseval>.*?),\s*.*?\)")
__oe_utils_ifelse_regex__ = regex.compile(r"(.*)oe\.utils\.ifelse\(.*?,\s*(?P<trueval>.*?),\s*(?P<falseval>.*?)\)")
__oe_utils_any_distro_features_regex__ = regex.compile(
    r"(.*)oe\.utils\.any_distro_features\(.*?,\s*(?P<feature>.*?)(,\s*(?P<trueval>.*?)(,\s*(?P<falseval>.*?))*)*\)")
__oe_utils_all_distro_features_regex__ = regex.compile(
    r"(.*)oe\.utils\.all_distro_features\(.*?,\s*(?P<feature>.*?)(,\s*(?P<trueval>.*?)(,\s*(?P<falseval>.*?))*)*\)")
__oe_utils_vartrue_regex__ = regex.compile(r"(.*)oe\.utils\.vartrue\(.*?,\s*(?P<trueval>.*?),\s*(?P<falseval>.*?),.*?\)")
__oe_utils_less_or_equal_regex__ = regex.compile(
    r"(.*)oe\.utils\.less_or_equal\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*(?P<falseval>.*?),.*?\)")
__oe_utils_version_less_or_equal_regex__ = regex.compile(
    r"(.*)oe\.utils\.version_less_or_equal\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*(?P<falseval>.*?),.*?\)")
__oe_utils_both_contain_regex__ = regex.compile(r"(.*)oe\.utils\.both_contain\(.*?,\s*.*?,\s*(?P<trueval>.*?),.*?\)")


def bb_utils_filter(_in: str, negative_clause: bool = False) -> str:
    """bb.utils.filter emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'bb.utils.filter' not in _in:
        return None
    m = RegexRpl.match(__bb_utils_filter_regex__, _in)
    if m:
        if negative_clause:
            return ''
        return m.group('trueval').strip("\"'")
    return None


def bb_utils_contains(_in: str, negative_clause: bool = False) -> str:
    """bb.utils.contains emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'bb.utils.contains' not in _in:
        return None
    m = RegexRpl.match(__bb_utils_contains_regex__, _in)
    if m:
        if negative_clause:
            return m.group('falseval').strip("\"'")
        return m.group('trueval').strip("\"'")
    return None


def bb_utils_contains_any(_in: str, negative_clause: bool = False) -> str:
    """bb.utils.contains_any emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'bb.utils.contains_any' not in _in:
        return None
    m = RegexRpl.match(__bb_utils_contains_any_regex__, _in)
    if m:
        if negative_clause:
            return m.group('falseval').strip("\"'")
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_conditional(_in: str, negative_clause: bool = False) -> str:
    """oe.utils.conditional emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'oe.utils.conditional' not in _in:
        return None
    m = RegexRpl.match(__oe_utils_conditional_regex__, _in)
    if m:
        if negative_clause:
            return m.group('falseval').strip("\"'")
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_ifelse(_in: str, negative_clause: bool = False) -> str:
    """oe.utils.ifelse emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'oe.utils.ifelse' not in _in:
        return None
    m = RegexRpl.match(__oe_utils_ifelse_regex__, _in)
    if m:
        if negative_clause:
            return m.group('falseval').strip("\"'")
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_any_distro_features(_in: str, negative_clause: bool = False) -> str:
    """oe.utils.any_distro_features emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'oe.utils.any_distro_features' not in _in:
        return None
    m = RegexRpl.match(__oe_utils_any_distro_features_regex__, _in)
    if m:
        trueval = '1' if not m.groupdict().get('trueval', '') else m.group('trueval')
        falseval = '' if not m.groupdict().get('falseval', '') else m.group('falseval')
        if negative_clause:
            return falseval.strip("\"'")
        return trueval.strip("\"'")
    return None


def oe_utils_all_distro_features(_in: str, negative_clause: bool = False) -> str:
    """oe.utils.all_distro_features emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'oe.utils.all_distro_features' not in _in:
        return None
    m = RegexRpl.match(__oe_utils_all_distro_features_regex__, _in)
    if m:
        trueval = '1' if not m.groupdict().get('trueval', '') else m.group('trueval')
        falseval = '' if not m.groupdict().get('falseval', '') else m.group('falseval')
        if negative_clause:
            return falseval.strip("\"'")
        return trueval.strip("\"'")
    return None


def oe_utils_vartrue(_in: str, negative_clause: bool = False) -> str:
    """oe.utils.vartrue emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'oe.utils.vartrue' not in _in:
        return None
    m = RegexRpl.match(__oe_utils_vartrue_regex__, _in)
    if m:
        if negative_clause:
            return m.group('falseval').strip("\"'")
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_less_or_equal(_in: str, negative_clause: bool = False) -> str:
    """oe.utils.less_or_equal emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'oe.utils.less_or_equal' not in _in:
        return None
    m = RegexRpl.match(__oe_utils_less_or_equal_regex__, _in)
    if m:
        if negative_clause:
            return m.group('falseval').strip("\"'")
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_version_less_or_equal(_in: str, negative_clause: bool = False) -> str:
    """oe.utils.version_less_or_equal emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'oe.utils.version_less_or_equal' not in _in:
        return None
    m = RegexRpl.match(__oe_utils_version_less_or_equal_regex__, _in)
    if m:
        if negative_clause:
            return m.group('falseval').strip("\"'")
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_both_contain(_in: str, negative_clause: bool = False) -> str:
    """oe.utils.both_contain emulation

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    if 'oe.utils.both_contain' not in _in:
        return None
    m = RegexRpl.match(__oe_utils_both_contain_regex__, _in)
    if m:
        if negative_clause:
            return ''
        return m.group('trueval').strip("\"'")
    return None


def inlinerep(_in: str, negative_clause: bool = False) -> str:
    """Replaces inline code expressions

    Args:
        _in (str): Input string
        negative_clause (bool): return negative branch

    Returns:
        str: Expanded string or None, if not applicable
    """
    _clean_in = _in.lstrip("${@").rstrip("}")
    for x in [
        bb_utils_contains(_clean_in, negative_clause),
        bb_utils_contains_any(_clean_in, negative_clause),
        bb_utils_filter(_clean_in, negative_clause),
        oe_utils_all_distro_features(_clean_in, negative_clause),
        oe_utils_any_distro_features(_clean_in, negative_clause),
        oe_utils_both_contain(_clean_in, negative_clause),
        oe_utils_conditional(_clean_in, negative_clause),
        oe_utils_ifelse(_clean_in, negative_clause),
        oe_utils_less_or_equal(_clean_in, negative_clause),
        oe_utils_vartrue(_clean_in, negative_clause),
        oe_utils_version_less_or_equal(_clean_in, negative_clause),
    ]:
        if x is not None:
            return x
    return None
