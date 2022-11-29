# -*- coding: utf-8 -*-
"""
See PEP 386 (https://www.python.org/dev/peps/pep-0386/)

Release logic:
 1. Remove ".devX" from __version__ (below)
 2. git add treebeard/__init__.py
 3. git commit -m 'Bump to <version>'
 4. git tag <version>
 5. git push
 6. assure that all tests pass on https://travis-ci.org/django-treebeard/django-treebeard/builds/
 7. git push --tags
 8. pip install --upgrade pip wheel twine
 9. python setup.py clean --all
 9. python setup.py sdist bdist_wheel
10. twine upload dist/*
11. bump the version, append ".dev0" to __version__
12. git add treebeard/__init__.py
13. git commit -m 'Start with <version>'
14. git push
"""


def get_version(raw_version):
    # https://www.python.org/dev/peps/pep-0386/#the-new-versioning-algorithm

    version = ""
    for subversion in raw_version:

        if subversion[0] in ['a', 'b', 'c', 'rc']:
            # [{a|b|c|rc}N[.N]+]
            version += f'{subversion[0]}{subversion[1]}'
            if len(subversion) == 3:
                version += f'.{subversion[2]}'

        elif subversion[0] in ['post', 'dev']:
            # [.postN][.devN]
            version += f'.{subversion[0]}{subversion[1]}'

        else:
            # N.N[.N]
            version = '.'.join([str(i) for i in subversion])
    return version


version = __version__ = get_version((
    (0, 1, 7),
    # ('a', 1),
    # ('dev', 1)
))


try:
    from .http import SberbankPaymentApi as Sberbank
except ModuleNotFoundError:
    # ignore import error for setup script
    # deprecated import
    pass
