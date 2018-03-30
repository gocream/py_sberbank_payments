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
    "expiration": "201512",
    "cardholderName": "tr tr",
    "depositAmount": 789789,
    "currency": "643",
    "approvalCode": "123456",
    "authCode": 2,
    "clientId": "666",
    "bindingId": "07a90a5d-cc60-4d1b-a9e6-ffd15974a74f",
    "ErrorCode": "0",
    "ErrorMessage": "Успешно",
    "OrderStatus": 2,
    "OrderNumber": "23asdafaf",
    "Pan": "411111**1111",
    "Amount": 789789
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
    '42': REQUEST
}


def _test_request(url, params=None, **kwargs):
    response = requests.Response()

    if url == "https://3dsec.sberbank.ru/payment/rest/getOrderStatus.do":
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


class OrderStatusTestCase(TestCase):

    def setUp(self):
        self.pathed_requests = patch('requests.post', side_effect=_test_request)
        self.mock_requests = self.pathed_requests.start()

    def tearDown(self):
        self.pathed_requests.stop()

    def test_order_status(self):
        api = Sberbank("test_username", "test_password")
        response = api.order_status(
            orderId = 'b8d70aa7-bfb3-4f94-b7bb-aec7273e1fce',
            language = 'ru',
        )
        self.assertIsNotNone(response)
        self.assertEqual(response, REQUEST)

    def test_order_status_errors(self):
        api = Sberbank("test_username", "test_password")

        for k, v in ERRORS.items():
            with self.subTest(orderNumber=k):
                if k in ['42', '0']:
                    continue

                with self.assertRaises(pysberbank.errors.SberbankApiException):
                    response = api.order_status(k)


if __name__ == '__main__':
    unittest.main()
