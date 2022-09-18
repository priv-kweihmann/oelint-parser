import sys

from oelint_parser.constants import CONSTANTS

__warning_shown = False

if not __warning_shown:
    sys.stderr.write(
        '{name} is deprecated. Please use "from oelint_parser.constants import CONSTANTS" instead\n'.format(name=__name__))
    __warning_shown = True

FUNC_ORDER = CONSTANTS.FunctionsOrder

KNOWN_FUNCS = CONSTANTS.FunctionsKnown
