from pathlib import Path

import setuptools

this_directory = Path(__file__).parent
long_description = (this_directory / 'README.md').read_text()

requirements = []
with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setuptools.setup(
    name='oelint_parser',
    version='8.2.1',
    author='Konrad Weihmann',
    author_email='kweihmann@outlook.com',
    description='Alternative parser for bitbake recipes',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/priv-kweihmann/oelint-parser',
    packages=setuptools.find_packages(),
    install_requires=requirements,
    package_data={
        'oelint_parser': ['data/*'],
    },
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Programming Language :: Python :: 3',
    ],
    python_requires='>=3.9',
)
