#!/bin/sh -e
python3 setup.py build
python3 setup.py sdist
pytest