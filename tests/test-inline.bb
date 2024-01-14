VAR_CONTAINS = "${@bb.utils.contains("TESTVAR", "one", "true", "false", d)}"
VAR_CONTAINS:aarch64 = "${@bb.utils.contains('TESTVAR', 'one', 'true', 'false', d)}"

VAR_CONTAINS_ANY = "${@bb.utils.contains_any("SOMEFLAG", "a", True, False, d)}"
VAR_CONTAINS_ANY:aarch64 = "${@bb.utils.contains_any('SOMEFLAG', 'a', True, False, d)}"

VAR_OE_CONDITIONAL = "${@oe.utils.conditional('X', 'a', 'true', 'b', d)}"
VAR_OE_CONDITIONAL:aarch64 = "${@oe.utils.conditional("X", "a", "true", "b", d)}"

VAR_OE_IFELSE = "${@oe.utils.ifelse(d.getVar("X") == "1", "true", "")}"
VAR_OE_IFELSE:aarch64 = "${@oe.utils.ifelse(d.getVar('X') == '1', 'true', '')}"

VAR_BB_FILTER = "${@bb.utils.filter("true", d.getVar("X"), d)}"
VAR_BB_FILTER:aarch64 = "${@bb.utils.filter('true', d.getVar('X'), d)}"
