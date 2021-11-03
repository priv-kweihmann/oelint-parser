A:append = " X"

B:remove:qemuall = "X2"

do_example:prepend:qemux86-64:poky() {
    bbwarn "This is an example warning"
}

RDEPENDS:${PN}-test += "foo"
