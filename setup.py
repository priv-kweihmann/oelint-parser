import setuptools

import subprocess
_long_description = "See https://github.com/priv-kweihmann/oelint-parser for documentation"
_long_description_content_type = "text/plain"
try:
    _long_description = subprocess.check_output(
        ["pandoc", "--from", "markdown", "--to", "markdown", "README.md"]).decode("utf-8")
    _long_description_content_type = "text/markdown"
except (subprocess.CalledProcessError, FileNotFoundError):
    pass

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name="oelint_parser",
    version="1.3.2",
    author="Konrad Weihmann",
    author_email="kweihmann@outlook.com",
    description="Alternative parser for bitbake recipes",
    long_description=_long_description,
    long_description_content_type=_long_description_content_type,
    url="https://github.com/priv-kweihmann/oelint-parser",
    packages=setuptools.find_packages(),
    install_requires=requirements,
    extras_require={
        'dev': [
            'pydoc-markdown',
            'pytest'
        ]
    },
    package_data = {
        'oelint_parser': ['data/*'],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
    ],
)
