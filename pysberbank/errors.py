# -*- coding: utf-8 -*-

import logging




class SberbankException(Exception):
    pass

class SberbankApiException(SberbankException):
    pass

class SberbankRequestException(SberbankException):
    def __init__(self, code, message):
        self.code = code
        self.message = message

        super().__init__(f'Error {self.code}: {self.message}')
