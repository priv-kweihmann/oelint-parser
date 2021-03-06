LICENSE = "BSD-2-Clause"
SOMEOTHERVAR = "${SOMEVAR}/SOMEMORE"
SOMEVAR = "source"
SOMELIST += "a \
             b \
             c \ 
            "
PACKAGECONFIG[abc] = "foo,bar,baz"

INLINECODEBLOCK = "${@bb.utils.contains('DISTRO_FEATURES', 'systemd', 'systemd-systemctl-native', '', d)}"
UPSTREAM_CHECK_REGEX = "(?P<pver>12\.\d+\.\d+)"

# Just a comment
# across multiple lines

do_example() {
    bbwarn "This is an example warning"
}

fakeroot python do_something_append() {
    bb.warn("This is another example warning")
}

def example_function():
    pass

addtask do_example after do_foo before do_bar

require another_file.inc

inherit someclass

do_configure[noexec] = "1"

export lib = "${bindir}/foo"
export PYTHON_ABI
