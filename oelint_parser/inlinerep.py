from oelint_parser.rpl_regex import RegexRpl


def bb_utils_filter(_in: str) -> str:
    """bb.utils.filter emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r'(.*)bb\.utils\.filter\(\s*(?P<trueval>.*?),.*?,.*?\)', _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def bb_utils_contains(_in: str) -> str:
    """bb.utils.contains emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(
        r"(.*)bb\.utils\.contains\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*.*?,\s*.\)", _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def bb_utils_contains_any(_in: str) -> str:
    """bb.utils.contains_any emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(
        r"(.*)bb\.utils\.contains_any\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*.*?,\s*.\)", _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_conditional(_in: str) -> str:
    """oe.utils.conditional emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(
        r"(.*)oe\.utils\.conditional\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*.*?,\s*.*?\)", _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_ifelse(_in: str) -> str:
    """oe.utils.ifelse emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r"(.*)oe\.utils\.ifelse\(.*?,\s*(?P<trueval>.*?),\s*.*?\)", _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_any_distro_features(_in: str) -> str:
    """oe.utils.any_distro_features emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r"(.*)oe\.utils\.any_distro_features\(.*?,\s*.*?(,\s*(?P<trueval>.*?))*\)", _in)
    if m:
        if 'trueval' not in m.groups():
            return 'True'
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_all_distro_features(_in: str) -> str:
    """oe.utils.all_distro_features emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r"(.*)oe\.utils\.all_distro_features\(.*?,\s*.*?(,\s*(?P<trueval>.*?))*\)", _in)
    if m:
        if 'trueval' not in m.groups():
            return 'True'
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_vartrue(_in: str) -> str:
    """oe.utils.vartrue emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r"(.*)oe\.utils\.vartrue\(.*?,\s*(?P<trueval>.*?),\s*.*?,.*?\)", _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_less_or_equal(_in: str) -> str:
    """oe.utils.less_or_equal emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r"(.*)oe\.utils\.less_or_equal\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*.*?,.*?\)", _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_version_less_or_equal(_in: str) -> str:
    """oe.utils.version_less_or_equal emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r"(.*)oe\.utils\.version_less_or_equal\(.*?,\s*.*?,\s*(?P<trueval>.*?),\s*.*?,.*?\)", _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def oe_utils_both_contain(_in: str) -> str:
    """oe.utils.both_contain emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r"(.*)oe\.utils\.both_contain\(.*?,\s*.*?,\s*(?P<trueval>.*?),.*?\)", _in)
    if m:
        return m.group('trueval').strip("\"'")
    return None


def inlinerep(_in: str) -> str:
    """Replaces inline code expressions

    Args:
        _in (str): Input string

    Returns:
        str: Expanded string or None, if not applicable
    """
    _clean_in = _in.lstrip("${@").rstrip("}")
    for x in [
        bb_utils_contains(_clean_in),
        bb_utils_contains_any(_clean_in),
        bb_utils_filter(_clean_in),
        oe_utils_all_distro_features(_clean_in),
        oe_utils_any_distro_features(_clean_in),
        oe_utils_both_contain(_clean_in),
        oe_utils_conditional(_clean_in),
        oe_utils_ifelse(_clean_in),
        oe_utils_less_or_equal(_clean_in),
        oe_utils_vartrue(_clean_in),
        oe_utils_version_less_or_equal(_clean_in),
    ]:
        if x:
            return x
    return None
