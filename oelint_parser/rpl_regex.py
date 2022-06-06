from regex import regex


class RegexRpl():
    """Safe regex replacements
    """

    @staticmethod
    def search(pattern, string, timeout=5, default=None, *args, **kwargs):
        """replacement for re.search

        Args:
            pattern (str): regex pattern
            string (str): input string
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to None.

        Returns:
            Match: Match object or None
        """
        try:
            return regex.search(pattern, string, timeout=timeout, *args, **kwargs)
        except TimeoutError:
            return default

    @staticmethod
    def split(pattern, string, timeout=5, default=None, *args, **kwargs):
        """replacement for re.split

        Args:
            pattern (str): regex pattern
            string (str): input string
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to None.

        Returns:
            list: list object or None
        """
        try:
            return regex.split(pattern, string, timeout=timeout, *args, **kwargs)
        except TimeoutError:
            return default

    @staticmethod
    def match(pattern, string, timeout=5, default=None, *args, **kwargs):
        """replacement for re.match

        Args:
            pattern (str): regex pattern
            string (str): input string
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to None.

        Returns:
            Match: Match object or None
        """
        try:
            return regex.match(pattern, string, timeout=timeout, *args, **kwargs)
        except TimeoutError:
            return default

    @staticmethod
    def sub(pattern, repl, string, timeout=5, default='', *args, **kwargs):
        """replacement for re.sub

        Args:
            pattern (str): regex pattern
            repl (str): replacement string
            string (str): input string
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to ''.

        Returns:
            str: string
        """
        try:
            return regex.sub(pattern, repl, string, timeout=timeout, *args, **kwargs)
        except TimeoutError:
            return default

    @staticmethod
    def finditer(pattern, string, timeout=5, default=None, *args, **kwargs):
        """replacement for re.finditer

        Args:
            pattern (str): regex pattern
            string (str): input string
            timeout (int, optional): Timeout for operation. On timeout `default` will be returned. Defaults to 5.
            default (_type_, optional): Default to return on timeout. Defaults to None.

        Returns:
            Scanner: Scanner object or None
        """
        try:
            return regex.finditer(pattern, string, timeout=timeout, *args, **kwargs)
        except TimeoutError:
            return default
