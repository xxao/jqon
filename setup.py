# Created byMartin.cz
# Copyright (c) Martin Strohalm. All rights reserved.

from setuptools import setup, find_packages

# get description
with open("README.md", "r") as fh:
    long_description = fh.read()

# set classifiers
classifiers = [
    'Development Status :: 3 - Alpha',
    'Programming Language :: Python :: 3 :: Only',
    'Operating System :: OS Independent',
    'Topic :: Utilities']

# main setup
setup(
    name = 'jqon',
    version = "0.2.0",
    description = 'JSON expression language for querying Python objects.',
    long_description = long_description,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/xxao/jqon',
    author = 'Martin Strohalm',
    author_email = '',
    license = 'MIT',
    packages = find_packages(),
    package_data = {},
    classifiers = classifiers,
    install_requires = [],
    requires_python = ">=3.11",
    zip_safe = False)
