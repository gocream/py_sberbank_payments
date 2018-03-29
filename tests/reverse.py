# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
import io
import json
import requests
import unittest

from pysberbank import Sberbank
import pysberbank



REVERSE_REQUEST = {
    'errorCode': "0",
    'errorMessage': "Успешно",
}
REVERSE_ERRORS = {
    '0': {
        'errorCode': "0",
        'errorMessage': "Обработка запроса прошла без системных ошибок.",
    },
    '5000': {
        'errorCode': "5",
        'errorMessage': "Доступ запрещён.",
    },
    '5001': {
        'errorCode': "5",
        'errorMessage': "Пользователь должен сменить свой пароль.",
    },
    '5002': {
        'errorCode': "5",
        'errorMessage': "[orderId] не задан.",
    },
    '6000': {
        'errorCode': "6",
        'errorMessage': "Неверный номер заказа.",
    },
    '7000': {
        'errorCode': "7",
        'errorMessage': "Недопустимая операция для текущего состояния заказа.",
    },
    '7001': {
        'errorCode': "7",
        'errorMessage': "Системная ошибка.",
    },
    '42': REVERSE_REQUEST
}


def _test_request(url, params=None, **kwargs):
    response = requests.Response()

    if url == "https://3dsec.sberbank.ru/payment/rest/reverse.do":
        # register order
        data = kwargs['data']

        userName = data.get('userName', None)
        password = data.get('password', None)
        orderId = data.get('orderId', None)

        if orderId in REVERSE_ERRORS:
            result = orderId
        else:
            result = '42'

        result = REVERSE_ERRORS[result]

    response.raw = io.BytesIO(str.encode(json.dumps(result)))
    return response


class ReverseTestCase(TestCase):

    def setUp(self):
        self.pathed_requests = patch('requests.post', side_effect=_test_request)
        self.mock_requests = self.pathed_requests.start()

    def tearDown(self):
        self.pathed_requests.stop()

    def test_register(self):
        api = Sberbank("test_username", "test_password")
        response = api.reverse("42000")
        self.assertIsNotNone(response)
        self.assertEqual(response, REVERSE_REQUEST)

    def test_register_errors(self):
        api = Sberbank("test_username", "test_password")

        for k, v in REVERSE_ERRORS.items():
            with self.subTest(orderNumber=k):
                if k in ['42', '0']:
                    continue

                with self.assertRaises(pysberbank.errors.SberbankApiException):
                    response = api.reverse(k)


if __name__ == '__main__':
    unittest.main()
