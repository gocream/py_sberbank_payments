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



REQUEST = {
    'errorCode': "0",
    'errorMessage': "Успешно",
}
ERRORS = {
    "0": {
        "errorCode": "0",
        "errorMessage": "Обработка запроса прошла без системных ошибок.",
    },
    "5000": {
        "errorCode": "5",
        "errorMessage": "Доступ запрещён.",
    },
    "5001": {
        "errorCode": "5",
        "errorMessage": "Пользователь должен сменить свой пароль.",
    },
    "5002": {
        "errorCode": "5",
        "errorMessage": "[orderId] не задан.",
    },
    "5003": {
        "errorCode": "5",
        "errorMessage": "Неверная сумма.",
    },
    "6000": {
        "errorCode": "6",
        "errorMessage": "Неверный номер заказа.",
    },
    "7000": {
        "errorCode": "7",
        "errorMessage": "Платёж должен быть в корректном состоянии.",
    },
    "7001": {
        "errorCode": "7",
        "errorMessage": "Сумма возврата превышает сумму списания.",
    },
    "7002": {
        "errorCode": "7",
        "errorMessage": "Системная ошибка.",
    },
    '42': REQUEST
}


def _test_request(url, params=None, **kwargs):
    response = requests.Response()

    if url == "https://3dsec.sberbank.ru/payment/rest/refund.do":
        data = kwargs['data']

        userName = data.get('userName', None)
        password = data.get('password', None)
        orderId = data.get('orderId', None)

        if orderId in ERRORS:
            result = orderId
        else:
            result = '42'

        result = ERRORS[result]

    response.raw = io.BytesIO(str.encode(json.dumps(result)))
    return response


class RefundTestCase(TestCase):

    def setUp(self):
        self.pathed_requests = patch('requests.post', side_effect=_test_request)
        self.mock_requests = self.pathed_requests.start()

    def tearDown(self):
        self.pathed_requests.stop()

    def test_register(self):
        api = Sberbank("test_username", "test_password")
        response = api.refund(
            orderId = "4302d369-a5e8-4432-a5e5-42acfab52c86",
            refundAmount = 20000,
            language = "ru",
        )
        self.assertIsNotNone(response)
        self.assertEqual(response, REQUEST)

    def test_register_errors(self):
        api = Sberbank("test_username", "test_password")

        for k, v in ERRORS.items():
            with self.subTest(orderNumber=k):
                if k in ['42', '0']:
                    continue

                with self.assertRaises(pysberbank.errors.SberbankApiException):
                    response = api.refund(k, 20000)


if __name__ == '__main__':
    unittest.main()
