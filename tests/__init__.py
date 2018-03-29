# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
import io
import json
import requests
import unittest

import pysberbank
from pysberbank import Sberbank



REGISTER_REQUEST = {
    "orderId": "70906e55-7114-41d6-8332-4609dc6590f4",
    "formUrl": "https://server/application_context/merchants/test/payment_ru.html?mdOrder=70906e55-7114-41d6-8332-4609dc6590f4"
}
REGISTER_ERRORS = {
    '0': {
        'errorCode': 0,
        'errorMessage': "Обработка запроса прошла без системных ошибок.",
    },

    '1000': {
        'errorCode': 1,
        'errorMessage': "Заказ с таким номером уже обработан.",
    },
    '1001': {
        'errorCode': 1,
        'errorMessage': "Неверный номер заказа.",
    },

    '3000': {
        'errorCode': 3,
        'errorMessage': "Неизвестная валюта.",
    },

    '4000': {
        'errorCode': 4,
        'errorMessage': "Номер заказа не может быть пуст.",
    },
    '4001': {
        'errorCode': 4,
        'errorMessage': "Имя продавца не может быть пустым.",
    },
    '4002': {
        'errorCode': 4,
        'errorMessage': "Отсутствует сумма.",
    },
    '4003': {
        'errorCode': 4,
        'errorMessage': "URL возврата не может быть пуст.",
    },
    '4004': {
        'errorCode': 4,
        'errorMessage': "Пароль не может быть пуст.",
    },

    '5000': {
        'errorCode': 5,
        'errorMessage': "Доступ запрещён.",
    },
    '5001': {
        'errorCode': 5,
        'errorMessage': "Пользователь должен сменить свой пароль.",
    },
    '5002': {
        'errorCode': 5,
        'errorMessage': "[jsonParams] неверен.",
    },

    '7000': {
        'errorCode': 7,
        'errorMessage': "Системная ошибка.",
    },

    '13000': {
        'errorCode': 13,
        'errorMessage': "Мерчант не имеет привилегии выполнять проверочные платежи.",
    },

    '14000': {
        'errorCode': 14,
        'errorMessage': "Features указаны некорректно.",
    },

    '42': REGISTER_REQUEST
}


def _test_request(url, params=None, **kwargs):
    response = requests.Response()

    if url == "https://3dsec.sberbank.ru/payment/rest/register.do":
        # register order
        data = kwargs['data']

        userName = data.get('userName', None)
        password = data.get('password', None)
        orderNumber = data.get('orderNumber', None)
        amount = data.get('amount', None)
        returnUrl = data.get('returnUrl', None)

        currency = data.get('currency', None)
        jsonParams = data.get('jsonParams', None)
        features = data.get('features', None)

        # if int(orderNumber) == 1:
        #     # 0, Обработка запроса прошла без системных ошибок.
        #     result = '0_all_good'

        # elif int(orderNumber) == 1001:
        #     # 1, Заказ с таким номером уже обработан.
        #     result = '1_orderNumber_exists'
        # elif int(orderNumber) == 1002:
        #     # 1, Неверный номер заказа.
        #     result = '1_orderNumber_incorrect'

        if orderNumber in REGISTER_ERRORS:
            result = orderNumber

        elif currency == "incorrect":
            # 3, Неизвестная валюта.
            result = '3001'

        elif not orderNumber:
            # 4, Номер заказа не может быть пуст.
            result = '4000'
        elif not userName:
            # 4, Имя продавца не может быть пустым.
            result = '4001'
        elif not amount:
            # 4, Отсутствует сумма.
            result = '4002'
        elif not returnUrl:
            # 4, URL возврата не может быть пуст.
            result = '4003'
        elif not password:
            # 4, Пароль не может быть пуст.
            result = '4004'

        elif password == "access_denied":
            # 5, Доступ запрещён.
            result = '5000'
        elif password == "must_change":
            # 5, Пользователь должен сменить свой пароль.
            result = '5001'
        elif jsonParams and jsonParams.get('code', None) == "incorrect":
            # 5, [jsonParams] неверен.
            result = '5002'

        elif int(orderNumber) == 500:
            # 7, Системная ошибка.
            result = '7000'

        elif int(orderNumber) == 300:
            # 13, Мерчант не имеет привилегии выполнять проверочные платежи.
            result = '13000'

        elif features and features != "AUTO_PAYMENT":
            # 14, Номер заказа не может быть пуст.
            result = '14000'

        else:
            result = '42'

        result = REGISTER_ERRORS[result]

    response.raw = io.BytesIO(str.encode(json.dumps(result)))
    return response


class SberbankApiTestCase(TestCase):

    def setUp(self):
        self.pathed_requests = patch('requests.post', side_effect=_test_request)
        self.mock_requests = self.pathed_requests.start()

    def tearDown(self):
        self.pathed_requests.stop()

    def test_register(self):
        api = Sberbank("test_username", "test_password")
        response = api.register("42000", "1000", "https://returnurl.example/")
        self.assertIsNotNone(response)
        self.assertEqual(response, REGISTER_REQUEST)

    def test_register_errors(self):
        api = Sberbank("test_username", "test_password")

        for k, v in REGISTER_ERRORS.items():
            with self.subTest(orderNumber=k):
                # self.assertIsNotNone(response)
                # self.assertEqual(response, v)
                # SberbankApiException
                # self.assertRaises()
                if k == '42':
                    continue

                with self.assertRaises(pysberbank.errors.SberbankApiException):
                    response = api.register(k, "1000", "https://returnurl.example/")


if __name__ == '__main__':
    unittest.main()
