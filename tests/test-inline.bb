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

VAR_ANY_DISTRO_FEATURE = "${@oe.utils.any_distro_features(d, "foo bar", "True")}"
VAR_ANY_DISTRO_FEATURE:aarch64 = "${@oe.utils.any_distro_features(d, 'foo bar', 'True')}"
VAR_ANY_DISTRO_FEATURE:armv7a = "${@oe.utils.any_distro_features(d, "foo bar")}"
VAR_ANY_DISTRO_FEATURE:armv4 = "${@oe.utils.any_distro_features(d, 'foo bar')}"

VAR_ALL_DISTRO_FEATURE = "${@oe.utils.all_distro_features(d, "foo bar", "True")}"
VAR_ALL_DISTRO_FEATURE:aarch64 = "${@oe.utils.all_distro_features(d, 'foo bar', 'True')}"
VAR_ALL_DISTRO_FEATURE:armv7a = "${@oe.utils.all_distro_features(d, "foo bar")}"
VAR_ALL_DISTRO_FEATURE:armv4 = "${@oe.utils.all_distro_features(d, 'foo bar')}"

VAR_VARTRUE = "${@oe.utils.vartrue("X", "true", "", d)}"
VAR_VARTRUE:aarch64 = "${@oe.utils.vartrue('X', 'true', '', d)}"

VAR_OE_LESS_OR_EQUAL = "${@oe.utils.less_or_equal("X", "1", "true", "", d)}"
VAR_OE_LESS_OR_EQUAL:aarch64 = "${@oe.utils.less_or_equal('X', '1', 'true', '', d)}"
