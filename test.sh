#! /bin/sh
python3 -c "from oelint_parser import *" || echo "Test failed" && exit 1
