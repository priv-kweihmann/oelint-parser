import sys

from oelint_parser.constants import CONSTANTS, Constants

__warning_shown = False

if not __warning_shown:
    sys.stderr.write('{} is deprecated. Please use "from oelint_parser.constants import CONSTANTS" instead\n'.format(__name__))
    __warning_shown = True


def set_constantfile(obj):
    """set constants

    Args:
        obj (dict): dictionary with constants
    """
    CONSTANTS.AddFromConstantFile(obj)


def set_rulefile(obj):
    """set rules

    Args:
        obj (dict): dictionary with rule definitions
    """
    CONSTANTS.AddFromRuleFile(obj)


def get_mandatory_vars():
    """get mandatory variables

    Returns:
        list: list of mandatory variable names
    """
    return CONSTANTS.VariablesMandatory


def get_suggested_vars():
    """get suggested variables

    Returns:
        list: list of suggested variable names
    """
    return CONSTANTS.VariablesSuggested


def get_known_mirrors():
    """get known mirror replacements

    Returns:
        dict: dictionary of known mirror replacements
    """
    return CONSTANTS.MirrorsKnown


def get_protected_vars():
    """get protected variables

    Returns:
        list: list of protected variables
    """
    return CONSTANTS.VariablesProtected


def get_protected_append_vars():
    """get protected variables in bbappends

    Returns:
        list: list of protected variables
    """
    return CONSTANTS.VariablesProtectedAppend


VAR_ORDER = CONSTANTS.VariablesOrder

def get_known_vars():
    """get list of known variables

    Returns:
        list: list of known variable names
    """
    return CONSTANTS.VariablesKnown

def get_known_machines():
    """get known machines

    Returns:
        list: list of known machine names
    """
    return CONSTANTS.MachinesKnown


def get_image_classes():
    """get known classes used exclusively in an image

    Returns:
        list: list of known class names
    """
    return CONSTANTS.ImagesClasses


def get_image_variables():
    """get known variables used exclusively in an image

    Returns:
        list: list of known variable names
    """
    return CONSTANTS.ImagesVariables


def get_base_varset():
    """get variable baseset
    Set includes basic package definitions

    Returns:
        dict: base variable set
    """
    return CONSTANTS.SetsBase
