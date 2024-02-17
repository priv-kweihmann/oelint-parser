SRC_URI = "http://example.com/foobar.tar.bz2;name=foo"
SRC_URI[foo.md5sum] = "5c274e52576976bd70565cd72505db41"

A:append = " X"

B:remove:qemuall = "X2"

do_example:prepend:qemux86-64:poky() {
    bbwarn "This is an example warning"
}

RDEPENDS:${PN}-test += "foo"

Y = "${P}"

SRCREV_foo = "abcd"
