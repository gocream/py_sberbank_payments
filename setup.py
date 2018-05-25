#!/usr/bin/env python
# -*- coding: utf-8 -*-

import codecs
import os

from setuptools import find_packages
from setuptools import setup


long_description = '\n'.join([
    open(os.path.join(os.path.dirname(__file__), 'README.md')).read(),
])

reqs_path = 'requirements.txt'
with codecs.open(os.path.join(os.path.dirname(__file__), reqs_path)) as reqs_file:
    requirements = reqs_file.read().split('\n')

print(requirements)

setup(
    author = 'Gocream',
    author_email = 'dmitry.dobrynin@gocream.ru',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Operating System :: OS Independent',
        'Natural Language :: Russian',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    description = 'python wrapper for sberbank api',
    include_package_data = True,
    install_requires = requirements,
    license = 'GNU GPL v3',
    long_description = long_description,
    name = 'pysberbank',
    packages = find_packages(),
    platforms = 'All',
    url = 'https://gitlab.com/gocream/pysberbank.git',
    version = __import__('pysberbank').version,
    zip_safe = False,
)
