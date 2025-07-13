do_install() {
    install -d ${D}${datadir}/my-example

    # A Comment
    cp -r ${S}/* ${D}${datadir}/my-example/
}

do_something() {
    a
    b
    c
    d
}

python do_something_2() {
    a = 1
    b = 2
    c = 3
    d = 5
}

fakeroot do_something_3() {
    a
    b
    c
    d
}
