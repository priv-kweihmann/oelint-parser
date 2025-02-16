import json
import os
import sys
from typing import Dict, List, Union

DEFAULT_DB = os.path.join(os.path.dirname(
    __file__), 'data', 'const-default.json')


class Constants():
    """Interface for constants"""

    def __init__(self) -> None:
        self.__db = self.__load_db(DEFAULT_DB)

    def __load_db(self, path: str) -> dict:
        try:
            with open(path) as _in:
                return json.load(_in)
        except (OSError, json.JSONDecodeError):
            sys.stderr.write('Cannot load constant database\n')
            return {}

    def GetByPath(self, path: str) -> Union[Dict, List]:
        """Get constant from path

        Args:
            path (str): / joined path in the constant structure

        Returns:
            Union[Dict, List]: Item in structure or empty dictionary
        """
        paths = path.rstrip('/').split('/')
        data = self.__db
        for _, value in enumerate(paths):
            data = data.get(value, {})
        return data

    def AddConstants(self, _dict: dict) -> None:
        """Add constants to the existing

        Args:
            dict (dict): constant dictionary to add
        """
        def dict_merge(a: dict, b: dict) -> dict:
            for k, v in b.items():
                if k not in a:
                    a[k] = v
                elif isinstance(b[k], dict):
                    dict_merge(a[k], b[k])
                else:
                    a[k] += v
            return a
        self.__db = dict_merge(self.__db, _dict)

    def RemoveConstants(self, _dict: dict) -> None:
        """Remove constants from the existing

        Args:
            dict (dict): constant dictionary to remove
        """
        def dict_merge(a: dict, b: dict) -> dict:
            for k, v in b.items():
                if k not in a:
                    pass
                elif isinstance(b[k], dict):
                    dict_merge(a[k], b[k])
                else:
                    a[k] = [x for x in a[k] if x not in v]
            return a
        self.__db = dict_merge(self.__db, _dict)

    def OverrideConstants(self, _dict: dict) -> None:
        """Override constants in the existing db

        Args:
            dict (dict]): constant dictionary with override values
        """
        def dict_merge(a: dict, b: dict) -> dict:
            for k, v in b.items():
                if k not in a:
                    a[k] = v
                elif isinstance(b[k], dict):
                    dict_merge(a[k], b[k])
                else:
                    a[k] = v
            return a
        self.__db = dict_merge(self.__db, _dict)

    @property
    def FunctionsKnown(self) -> List[str]:
        """Return known functions

        Returns:
            list: list of known functions
        """
        return self.GetByPath('functions/known')

    @property
    def FunctionsOrder(self) -> List[str]:
        """Return function order

        Returns:
            list: List of functions to order in their designated order
        """
        return self.GetByPath('functions/order')

    @property
    def MirrorsKnown(self) -> Dict[str, str]:
        """Return known mirrors and their replacements

        Returns:
            dict: Dict of known mirrors and their replacements
        """
        return self.GetByPath('replacements/mirrors')

    @property
    def VariablesKnown(self) -> List[str]:
        """Known variables

        Returns:
            list: List of known variables
        """
        return self.GetByPath('variables/known')

    @property
    def DistrosKnown(self) -> List[str]:
        """Known distros

        Returns:
            list: List of known distros
        """
        return self.GetByPath('replacements/distros')

    @property
    def MachinesKnown(self) -> List[str]:
        """Known machines

        Returns:
            list: List of known machines
        """
        return self.GetByPath('replacements/machines')

    @property
    def ImagesClasses(self) -> List[str]:
        """Classes that are used in images

        Returns:
            list: Classes that are used in images
        """
        return self.GetByPath('images/known-classes')

    @property
    def ImagesVariables(self) -> List[str]:
        """Variables that are used in images

        Returns:
            list: Variables that are used in images
        """
        return self.GetByPath('images/known-variables')

    @property
    def SetsBase(self) -> Dict[str, str]:
        """Base variable set

        Returns:
            dict: dictionary with base variable set
        """
        return self.GetByPath('sets/base')


CONSTANTS = getattr(sys.modules[__name__], 'CONSTANTS', Constants())
