from typing import List, Union

from regex import Match, Scanner, regex


class RegexRpl():
    """Safe regex replacements
    """

    @staticmethod
    def search(pattern: str, string: str, flags: int = 0, timeout: int = 5, default: object = None, **kwargs) -> Union[Match, None]:
        """replacement for re.search

        Args:
            pattern (str): regex pattern
            string (str): input string
            flags (int, optional): flags modifying expression behaviour
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to None.

        Returns:
            Match: Match object or None
        """
        try:
            return regex.search(pattern, string, flags=flags, timeout=timeout, **kwargs)
        except TimeoutError:
            return default

    @staticmethod
    def split(pattern: str, string: str, maxsplit: int = 0, flags: int = 0, timeout: int = 5, default: object = None, **kwargs) -> List[str]:
        """replacement for re.split

        Args:
            pattern (str): regex pattern
            string (str): input string
            maxsplit (int, optional): if nonzero, at most `maxsplit` splits occur
            flags (int, optional): flags modifying expression behaviour
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to None.

        Returns:
            list: list object or None
        """
        try:
            return regex.split(pattern, string, maxsplit=maxsplit, flags=flags, timeout=timeout, **kwargs)
        except TimeoutError:
            return default or []

    @staticmethod
    def match(pattern: str, string: str, flags: int = 0, timeout: int = 5, default: object = None, **kwargs) -> Union[Match, None]:
        """replacement for re.match

        Args:
            pattern (str): regex pattern
            string (str): input string
            flags (int, optional): flags modifying expression behaviour
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to None.

        Returns:
            Match: Match object or None
        """
        try:
            return regex.match(pattern, string, timeout=timeout, **kwargs)
        except TimeoutError:
            return default

    @staticmethod
    def sub(pattern: str, repl: str, string: str, count: int = 0, flags: int = 0, timeout: int = 5, default: str = '', **kwargs) -> str:
        """replacement for re.sub

        Args:
            pattern (str): regex pattern
            repl (str): replacement string
            string (str): input string
            count (int, optional): if nonzero, at most `count` occurrences are replaced
            flags (int, optional): flags modifying expression behaviour
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to ''.

        Returns:
            str: string
        """
        try:
            return regex.sub(pattern, repl, string, count=count, flags=flags, timeout=timeout, **kwargs)
        except TimeoutError:
            return default

    @staticmethod
    def finditer(pattern: str, string: str, flags: int = 0, timeout: int = 5, default: object = None, **kwargs) -> Scanner:
        """replacement for re.finditer

        Args:
            pattern (str): regex pattern
            string (str): input string
            flags (int, optional): flags modifying expression behaviour
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to None.

        Returns:
            Scanner: Scanner object or None
        """
        try:
            return regex.finditer(pattern, string, flags=flags, timeout=timeout, **kwargs)
        except TimeoutError:
            return default
