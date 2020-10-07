LICENSE = "BSD-2-Clause"
SOMEOTHERVAR = "${SOMEVAR}/SOMEMORE"
SOMEVAR = "source"
SOMELIST += "a \
             b \
             c \ 
            "
PACKAGECONFIG[abc] = "foo,bar,baz"

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
