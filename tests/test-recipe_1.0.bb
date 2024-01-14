LICENSE = "BSD-2-Clause"
SOMEOTHERVAR = "${SOMEVAR}/SOMEMORE"
SOMEVAR = "source"
SOMEVAR_class-target = "destination"
YETANOTHERVAR = "destination"
SOME.VAR.WITH.PERIODS = "foo"
SOMELIST += "a \
             b \
             c \ 
            "
PACKAGECONFIG[abc] = "foo,bar,baz"

INLINECODEBLOCK = "${@bb.utils.contains('DISTRO_FEATURES', 'systemd', 'systemd-systemctl-native', '', d)}"
UPSTREAM_CHECK_REGEX = "(?P<pver>12\.\d+\.\d+)"
TARGETVAR_class-target = "foo"
NATIVEVAR_class-native = "foo"
CROSSVAR_class-cross = "foo"
SDKVAR_class-nativesdk = "foo"

# Just a comment
# across multiple lines

do_example() {
    bbwarn "This is an example warning"
}

fakeroot python do_something_append() {
    bb.warn("This is another example warning")
}

python() {
    bb.info("Hi my name is function, and I have a problem...")
}

python () {
    bb.info("Hi my name is function, and I have a problem...")
}

python __anonymous() {
    bb.info("Hi my name is function, and I have a problem...")
}

def example_function():
    pass

addtask do_example after do_foo before do_bar

require another_file.inc

inherit someclass

inherit_defer someclass

CLASS_TO_INHERIT = "someclass"

inherit ${CLASS_TO_INHERIT}

A[doc] = "This string is not an inherit statement."

do_configure[noexec] = "1"

export lib = "${bindir}/foo"
export PYTHON_ABI

do_foo() {
    export SOMETHING=1
}

python do_bar() {
    export = 'something'
    if export == "PSEUDO_DISABLED":
        print('bar')
}

RDEPENDS_${PN}-test += "foo"
