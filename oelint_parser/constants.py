import os
import sys
import json

DEFAULT_DB = os.path.join(os.path.dirname(__file__), 'data', 'const-default.json')

class Constants():
    """Interface for constants
    """

    LEGACY_MAPPING = {
        'known_machines': 'replacements/machines',
        'known_mirrors': 'replacements/mirrors',
        'known_vars': 'variables/known',
        'mandatory_vars': 'variables/mandatory',
        'protected_append_vars': 'variables/protected-append',
        'protected_vars': 'variables/protected',
        'suggested_vars': 'variables/suggested',
    }

    def __init__(self):
        self.__db = self.__load_db(DEFAULT_DB)
    
    def __load_db(self, path):
        try:
            with open(path) as _in:
                return json.load(_in)
        except (FileNotFoundError, OSError, json.JSONDecodeError) as e:
            sys.stderr.write('Cannot load constant database\n')
            return {}

    def __get_from_path(self, path):     
        paths = path.rstrip('/').split('/')
        data = self.__db
        for index, value in enumerate(paths):
            data = data.get(value, {})
        return data
    
    def AddConstants(self, _dict):
        """Add constants to the existing

        Args:
            dict (dict): constant dictionary to add
        """
        def dict_merge(a, b):
            for k, v in b.items():
                if isinstance(b[k], dict):
                    dict_merge(a[k], b[k])
                elif k not in a:
                    a[k] = v
                else:
                    a[k] += v
            return a
        self.__db = dict_merge(self.__db, _dict)

    def RemoveConstants(self, _dict):
        """Remove constants from the existing

        Args:
            dict (dict): constant dictionary to remove
        """
        def dict_merge(a, b):
            for k, v in b.items():
                if isinstance(b[k], dict):
                    dict_merge(a[k], b[k])
                elif k not in a:
                    pass
                else:
                    a[k] = [x for x in a[k] if x not in v]
            return a
        self.__db = dict_merge(self.__db, _dict)

    def OverrideConstants(self, _dict):
        """Override constants in the existing db

        Args:
            dict (dict]): constant dictionary with override values
        """
        def dict_merge(a, b):
            for k, v in b.items():
                if isinstance(b[k], dict):
                    dict_merge(a[k], b[k])
                else:
                    a[k] = v
            return a
        self.__db = dict_merge(self.__db, _dict)

    def AddFromRuleFile(self, dict):
        """Legacy interface to support rule files

        Args:
            dict (dict): rule file dictionary
        """
        def dict_nested_set(d, path, value):
            crumb = path[0]
            if len(path) == 1:
                d[crumb] = value
            else:
                if not crumb in d:
                    d[crumb] = {}
                dict_nested_set(d[crumb], path[1:], value)
        _translated = {}
        for n, r in Constants.LEGACY_MAPPING.items():
            if n in dict:
                dict_nested_set(_translated, r.split('/'), dict[n])
        self.AddConstants(_translated)

    def AddFromConstantFile(self, dict):
        """Legacy interface to support constant files

        Args:
            dict (dict): constant file dictionary
        """
        self.AddFromRuleFile(dict)

    @property
    def FunctionsKnown(self):
        """Return known functions

        Returns:
            list: list of known functions
        """
        return self.__get_from_path('functions/known')

    @property
    def FunctionsOrder(self):
        """Return function order

        Returns:
            list: List of functions to order in their designated order
        """
        return self.__get_from_path('functions/order')

    @property
    def VariablesMandatory(self):
        """Return mandatory variables

        Returns:
            list: List of mandatory variables
        """
        return self.__get_from_path('variables/mandatory')

    @property
    def VariablesSuggested(self):
        """Return suggested variables

        Returns:
            list: List of suggested variables
        """
        return self.__get_from_path('variables/suggested')

    @property
    def MirrorsKnown(self):
        """Return known mirrors and their replacements

        Returns:
            dict: Dict of known mirrors and their replacements
        """
        return self.__get_from_path('replacements/mirrors')

    @property
    def VariablesProtected(self):
        """Return protected variables

        Returns:
            list: List of protected variables
        """
        return self.__get_from_path('variables/protected')

    @property
    def VariablesProtectedAppend(self):
        """Return protected variables in bbappend files

        Returns:
            list: List of protected variables in bbappend files
        """
        return self.__get_from_path('variables/protected-append')

    @property
    def VariablesOrder(self):
        """Variable order

        Returns:
            list: List of variables to order in their designated order
        """
        return self.__get_from_path('variables/order')

    @property
    def VariablesKnown(self):
        """Known variables

        Returns:
            list: List of known variables
        """
        return self.__get_from_path('variables/known')

    @property
    def MachinesKnown(self):
        """Known machines

        Returns:
            list: List of known machines
        """
        return self.__get_from_path('replacements/machines')

    @property
    def MachinesKnown(self):
        """Known machines

        Returns:
            list: List of known machines
        """
        return self.__get_from_path('replacements/machines')

    @property
    def ImagesClasses(self):
        """Classes that are used in images

        Returns:
            list: Classes that are used in images
        """
        return self.__get_from_path('images/known-classes')

    @property
    def ImagesVariables(self):
        """Variables that are used in images

        Returns:
            list: Variables that are used in images
        """
        return self.__get_from_path('images/known-variables')

    @property
    def SetsBase(self):
        """Base variable set

        Returns:
            dict: dictionary with base variable set
        """
        return self.__get_from_path('sets/base')

CONSTANTS = getattr(sys.modules[__name__], 'CONSTANTS', Constants())

