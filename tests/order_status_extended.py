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
    "errorCode": "0",
    "errorMessage": "Успешно",
    "orderNumber": "0784sse49d0s134567890",
    "orderStatus": 6,
    "actionCode": -2007,
    "actionCodeDescription": "Время сессии истекло",
    "amount": 33000,
    "currency": "643",
    "date": 1383819429914,
    "orderDescription": " ",
    "merchantOrderParams": [{
        "name": "email",
        "value": "yap"
    }],
    "attributes": [{
        "name": "mdOrder",
        "value": "b9054496-c65a-4975-9418-1051d101f1b9"
    }],
    "cardAuthInfo": {
        "expiration": "201912",
        "cardholderName": "Ivan",
        "secureAuthInfo": {
            "eci": 6,
            "threeDSInfo": {
                "xid": "MDAwMDAwMDEzODM4MTk0MzAzMjM="
            }
        },
        "pan": "411111**1111"
    },
    "terminalId": "333333"
}

ERRORS = {
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
        'errorMessage': "Незарегистрированный orderId.",
    },
    '7000': {
        'errorCode': "7",
        'errorMessage': "Системная ошибка.",
    },
    '42': REQUEST
}


def _test_request(url, params=None, **kwargs):
    response = requests.Response()

    if url == "https://3dsec.sberbank.ru/payment/rest/getOrderStatusExtended.do":
        # register order
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


class OrderStatusExtendedTestCase(TestCase):

    def setUp(self):
        self.pathed_requests = patch('requests.post', side_effect=_test_request)
        self.mock_requests = self.pathed_requests.start()

    def tearDown(self):
        self.pathed_requests.stop()

    def test_order_status_extended(self):
        api = Sberbank("test_username", "test_password")
        response = api.order_status_extended(
            orderId = "b9054496-c65a-4975-9418-1051d101f1b9",
            language = "ru",
        )
        self.assertIsNotNone(response)
        self.assertEqual(response, REQUEST)

    def test_order_status_extended_errors(self):
        api = Sberbank("test_username", "test_password")

        for k, v in ERRORS.items():
            with self.subTest(orderNumber=k):
                if k in ['42', '0']:
                    continue

                with self.assertRaises(pysberbank.errors.SberbankApiException):
                    response = api.order_status_extended(k)


if __name__ == '__main__':
    unittest.main()
