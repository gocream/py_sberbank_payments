# -*- coding: utf-8 -*-

import logging




class SberbankException(Exception):
    pass

class SberbankRequestException(SberbankException):
    pass

class SberbankRequestCodeException(SberbankException):
    def __init__(self, request, code, message):
        self.request = request
        self.code = code
        self.message = message

        super().__init__(f'Error {self.code}: {self.message}')
