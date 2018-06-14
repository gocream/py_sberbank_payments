# -*- coding: utf-8 -*-


__VERSION__ = (
    (0, 1, 4),
    # ('a', 1),
    # ('dev', 1)
)

try:
    from verlib import NormalizedVersion
    version = str(NormalizedVersion.from_parts(*__VERSION__))
except ImportError:
    version = '.'.join([str(j) for i in __VERSION__ for j in i])

try:
    from .http import SberbankPaymentApi as Sberbank
except ModuleNotFoundError:
    pass
