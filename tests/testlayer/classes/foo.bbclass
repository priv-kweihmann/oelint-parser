FOO_A = "1"

foo-do_install() {
    bbwarn "A class task"
}

EXPORT_FUNCTIONS do_install do_somenotexistingtask
