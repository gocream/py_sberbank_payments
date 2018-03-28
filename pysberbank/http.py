# -*- coding: utf-8 -*-

import logging
import requests

from .errors import SberbankException
from .errors import SberbankRequestException

logger = logging.getLogger("pysberbank")



# def request_decorator(fn):
#     def wrapper(cls, url=None, api_type=None, *args, **kwargs):
#         method_name, params = fn(cls, *args, **kwargs)
#         return cls._make_request(url, api_type, method_name, params)
#     return wrapper


def remove_null_elements(d):
    for k, v in



DEFAULT_URL = "https://3dsec.sberbank.ru/payment/{api_type}/{method}"
DEFAULT_API_TYPE = "rest"
DEFAULT_LANGUAGE = "ru"
DEFAULT_CURREBCY = 643

class SberbankPaymentApi:
    """
        sberbank payment api
    """

    def __init__(self, username=None, password=None, token=None,
                 url=DEFAULT_URL, api_type=DEFAULT_API_TYPE,
                 language=DEFAULT_LANGUAGE, currency=DEFAULT_CURREBCY):
        """
            username - username at sberbank api
            password - password at sberbank api
            url - api url address
            api_type - api type (soap | rest) only rest ready
            language - default language (ISO 639-1)
            currency - default currency (ISO 4217)
        """

        if (not (bool(username) and bool(password))) != (token is None):
            raise SberbankException("Auth params require. Setup username/password pair or token, not booth")

        self.username = username
        self.password = password
        self.token = token

        self.url = url
        self.api_type = api_type
        self.language = language
        self.currency = currency

    def _make_data(self, params, remove_null=True):
        """
        add username/password pair or token to request params

        remove_null: if True - remove all None elements from params
        """

        if remove_null:
            data = dict(filter(lambda x:x[1], params.items()))
        else:
            data = params.copy()

        if self.token:
            data['token'] = self.token
        else:
            data.update({
                'userName': self.username,
                'password': self.password,
            })

        return data

    def _make_request(self, url, api_type, method_name, params=dict(),
                      remove_null=True):
        if api_type == 'rest':
            method = f'{method_name}.do'
        else:
            method = method_name

        data = self._make_data(params)
        response = requests.post(url.format(api_type=api_type, method=method),
                                 data=data, remove_null=remove_null)

        result = response.content
        if api_type == 'rest':
            result = response.json()
        return result

    def register(self, orderNumber, amount, returnUrl, currency=None,
                 failUrl=None, description=None, language=None, pageView=None,
                 clientId=None, merchantLogin=None, jsonParams=None,
                 sessionTimeoutSecs=None, expirationDate=None, bindingId=None,
                 features=None, extra_params=dict(), url=None, api_type=None):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:register
        """

        params = {
            'orderNumber': orderNumber,
            'amount': amount,
            'returnUrl': returnUrl,
            'currency': currency or self.currency,
            'failUrl': failUrl,
            'description': description,
            'language': language or self.language,
            'pageView': pageView,
            'clientId': clientId,
            'merchantLogin': merchantLogin,
            'jsonParams': jsonParams,
            'sessionTimeoutSecs': sessionTimeoutSecs,
            'expirationDate': expirationDate,
            'bindingId': bindingId,
            'features': features,
        }
        result = self._make_request(url or self.url, api_type or self.api_type, 'register', params)
        return result

    def reverse(self, orderId, extra_params=dict(), url=None, api_type=None):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:reverse

        orderId - Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
        """

        params = extra_params.copy()
        params.update({
            'orderId': orderId,
        })
        result = self._make_request(url or self.url, api_type or self.api_type, 'reverse', params)
        return result

    def refund(self, orderId, refundAmount, extra_params=dict(), url=None, api_type=None):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:refund

        orderId - Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
        refundAmount - Сумма возврата в валюте заказа. Может быть меньше или
            равна остатку в заказе.
        """

        params = extra_params.copy()
        params.update({
            'orderId': orderId,
            'refundAmount': refundAmount,
        })
        result = self._make_request(url or self.url, api_type or self.api_type, 'refund', params)
        return result

    def order_status(self, orderId, extra_params=dict(), url=None, api_type=None):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:getorderstatus

        orderId - Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
        """

        params = extra_params.copy()
        params.update({
            'orderId': orderId,
        })
        result = self._make_request(url or self.url, api_type or self.api_type, 'getOrderStatus', params)
        return result

    def order_full_status(self, orderId=None, orderNumber=None,
                          extra_params=dict(), url=None, api_type=None):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:getorderstatusextended

        orderId - Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
        orderNumber - Номер (идентификатор) заказа в системе магазина,
            уникален для каждого магазина в пределах системы - до 30 символов.

        В запросе должен присутствовать либо orderId, либо orderNumber. Если в
        запросе присутствуют оба параметра, то приоритетным считается orderId.
        """

        if (orderId is None) and (orderNumber is None):
            raise SberbankApiRequestException("none of the orderId and \
                orderNumber parameters is specified")

        params = extra_params.copy()
        params.update({
            'orderId': orderId,
            'orderNumber': orderNumber,
        })
        result = self._make_request(url or self.url, api_type or self.api_type, 'getOrderStatusExtended', params)
        return result
