# -*- coding: utf-8 -*-

import logging




class SberbankApiException(Exception):
    pass

class SberbankApiRequestException(SberbankApiException):
    pass

# class SberRequestException(SberbankApiException):
#     def __init__(self, request, code, desc):
#         self.request = request
#         self.code = code
#         self.desc = desc
#         super(SberRequestError, self).__init__('{0.request} error {0.code}: {0.desc}'.format(self))
