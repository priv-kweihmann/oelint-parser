from oelint_parser.rpl_regex import RegexRpl


def bb_utils_contains(_in: str) -> str:
    """bb.utils.contains emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(
        r"(.*)bb\.utils\.contains\(.*?,\s*.*?,\s*(.*?),\s*.*?,\s*.\)", _in)
    if m:
        return m.group(1) + m.group(2).strip("\"'")
    return None


def bb_utils_contains_any(_in: str) -> str:
    """bb.utils.contains_any emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(
        r"(.*)bb\.utils\.contains_any\(.*?,\s*.*?,\s*(.*?),\s*.*?,\s*.\)", _in)
    if m:
        return m.group(1) + m.group(2).strip("\"'")
    return None


def oe_utils_conditional(_in: str) -> str:
    """oe.utils.conditional emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(
        r"(.*)oe\.utils\.conditional\(.*?,\s*.*?,\s*(.*?),\s*.*?,\s*.\)", _in)
    if m:
        return m.group(1) + m.group(2).strip("\"'")
    return None


def oe_utils_ifelse(_in: str) -> str:
    """oe.utils.ifelse emulation

    Args:
        _in (str): Input string

    Returns:
        str: True argument of the conditional or None if not applicable
    """
    m = RegexRpl.match(r"(.*)oe\.utils\.ifelse\(.*?,\s*(.*?),\s*.*?\)", _in)
    if m:
        return m.group(1) + m.group(2).strip("\"'")
    return None


def inlinerep(_in: str) -> str:
    """Replaces inline code expressions

    Args:
        _in (str): Input string

    Returns:
        str: Expanded string or None, if not applicable
    """
    _clean_in = _in.lstrip("${@").rstrip("}")
    for x in [bb_utils_contains(_clean_in),
              bb_utils_contains_any(_clean_in),
              oe_utils_conditional(_clean_in),
              oe_utils_ifelse(_clean_in)]:
        if x:
            return x
    return None
