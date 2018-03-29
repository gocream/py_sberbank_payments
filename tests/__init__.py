# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
import io
import json
import requests
import unittest

from pysberbank import Sberbank



REGISTER_REQUEST = {
    "orderId": "70906e55-7114-41d6-8332-4609dc6590f4",
    "formUrl": "https://server/application_context/merchants/test/payment_ru.html?mdOrder=70906e55-7114-41d6-8332-4609dc6590f4"
}
REGISTER_ERRORS = {
    '0_all_good': {
        'errorCode': 0,
        'errorMessage': "Обработка запроса прошла без системных ошибок.",
    },

    '1_orderNumber_exists': {
        'errorCode': 1,
        'errorMessage': "Заказ с таким номером уже обработан.",
    },
    '1_orderNumber_incorrect': {
        'errorCode': 1,
        'errorMessage': "Неверный номер заказа.",
    },

    '3_currency_incorrect': {
        'errorCode': 3,
        'errorMessage': "Неизвестная валюта.",
    },

    '4_userName_Blank': {
        'errorCode': 4,
        'errorMessage': "Имя продавца не может быть пустым.",
    },
    '4_password_Blank': {
        'errorCode': 4,
        'errorMessage': "Пароль не может быть пуст.",
    },
    '4_orderNumber_Blank': {
        'errorCode': 4,
        'errorMessage': "Номер заказа не может быть пуст.",
    },
    '4_amount_Blank': {
        'errorCode': 4,
        'errorMessage': "Отсутствует сумма.",
    },
    '4_returnUrl_Blank': {
        'errorCode': 4,
        'errorMessage': "URL возврата не может быть пуст.",
    },

    '5_password_access_denied': {
        'errorCode': 5,
        'errorMessage': "Доступ запрещён.",
    },
    '5_password_must_change': {
        'errorCode': 5,
        'errorMessage': "Пользователь должен сменить свой пароль.",
    },
    '5_jsonParams_incorrect': {
        'errorCode': 5,
        'errorMessage': "[jsonParams] неверен.",
    },

    '7_error_500': {
        'errorCode': 7,
        'errorMessage': "Системная ошибка.",
    },

    '13_merch_cant_checkpay': {
        'errorCode': 13,
        'errorMessage': "Мерчант не имеет привилегии выполнять проверочные платежи.",
    },

    '14_features_incorrect': {
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

        if int(orderNumber) == 1:
            # 0, Обработка запроса прошла без системных ошибок.
            result = '0_all_good'

        elif int(orderNumber) == 1001:
            # 1, Заказ с таким номером уже обработан.
            result = '1_orderNumber_exists'
        elif int(orderNumber) == 1002:
            # 1, Неверный номер заказа.
            result = '1_orderNumber_incorrect'

        elif currency == "incorrect":
            # 3, Неизвестная валюта.
            result = '3_currency_incorrect'

        elif not userName:
            # 4, Имя продавца не может быть пустым.
            result = '4_userName_Blank'
        elif not password:
            # 4, Пароль не может быть пуст.
            result = '4_password_Blank'
        elif not amount:
            # 4, Отсутствует сумма.
            result = '4_amount_Blank'
        elif not returnUrl:
            # 4, URL возврата не может быть пуст.
            result = '4_returnUrl_Blank'
        elif not orderNumber:
            # 4, Номер заказа не может быть пуст.
            result = '4_orderNumber_Blank'

        elif password == "access_denied":
            # 5, Доступ запрещён.
            result = '5_password_access_denied'
        elif password == "must_change":
            # 5, Пользователь должен сменить свой пароль.
            result = '5_password_must_change'
        elif jsonParams and jsonParams.get('code', None) == "incorrect":
            # 5, [jsonParams] неверен.
            result = '5_jsonParams_incorrect'

        elif int(orderNumber) == 500:
            # 7, Системная ошибка.
            result = '7_error_500'

        elif int(orderNumber) == 300:
            # 13, Мерчант не имеет привилегии выполнять проверочные платежи.
            result = '13_merch_cant_checkpay'

        elif features and features != "AUTO_PAYMENT":
            # 14, Номер заказа не может быть пуст.
            result = '14_features_incorrect'

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
        response = api.register("1", "1000", "https://returnurl.example/")
        self.assertIsNotNone(response)
        self.assertEqual(response, REGISTER_ERRORS['0_all_good'])


if __name__ == '__main__':
    unittest.main()
