# -*- coding: utf-8 -*-
from requests import RequestException


class BaseSberbankException(Exception):
    pass


class SberbankException(BaseSberbankException):
    """
    General exception

    Thrown _before_ any request is made - configuration or pre checks error
    """


class SberbankApiException(SberbankException):
    """
    Sberbank API errors

    Exception contains `code` and `message`
    """

    def __init__(self, code, message):
        self.code = code
        self.message = message

        super().__init__(f'Error {self.code}: {self.message}')


class SberbankRequestException(BaseSberbankException, RequestException):
    """
    Wrapper around `RequestException` so we can catch them separatly
    """
