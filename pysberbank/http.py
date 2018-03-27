# -*- coding: utf-8 -*-

import logging
import requests

from .errors import SberbankException
from .errors import SberbankRequestException

logger = logging.getLogger("pysberbank")




DEFAULT_URL = "https://3dsec.sberbank.ru/payment/{api_type}/{method}"
DEFAULT_API_TYPE = "rest"

class SberbankPaymentApi:
    """
        sberbank payment api
    """

    def __init__(self, user=None, password=None, url=DEFAULT_URL,
                 api_type=DEFAULT_API_TYPE, language="ru", currency=643):
        self.user = user
        self.password = password
        self.url = url
        self.api_type = api_type
        self.language = language
        self.currency = currency

    def _make_data(self, params):
        data = {
            'userName': self.user,
            'password': self.password,
            'language': self.language,
        }
        data.update(params)
        return data

    def _make_request(self, api_type, method_name, data):
        method = method_name
        if api_type == 'rest':
            method = f'{method_name}.do'

        response = requests.post(url.format(api_type=api_type, method=method),
                                 data=data)

        result = response.content
        if api_type == 'rest':
            result = response.json()
        return result

    def register(self, orderNumber, amount, returnUrl, currency=None,
                 extra_params=dict()):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:register

        orderNumber - Номер (идентификатор) заказа в системе магазина, уникален
            для каждого магазина в пределах системы - до 30 символов.

        amount - Сумма платежа в минимальных единицах валюты (копейки, центы и
            т. п.).

        returnUrl - Адрес, на который требуется перенаправить пользователя в
            случае успешной оплаты. Адрес должен быть указан полностью, включая
            используемый протокол (например, https://test.ru вместо test.ru).
            В противном случае пользователь будет перенаправлен по адресу
            следующего вида: http://<адрес_платёжного_шлюза>/<адрес_продавца>.

        currency - Код валюты платежа ISO 4217. Если не указан, считается
            равным коду валюты по умолчанию.
        """

        params = extra_params.copy()
        params.update({
            'orderNumber': orderNumber,
            'amount': amount,
            'returnUrl': returnUrl,
            'currency': currency or self.currency,
        })
        result = self._make_request(self.url, self.api_type, 'register',
                               self._make_data(params))
        return result

    def reverse(self, orderId, extra_params=dict()):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:reverse

        orderId - Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
        """

        params = extra_params.copy()
        params.update({
            'orderId': orderId,
        })
        result = self._make_request(self.url, self.api_type, 'reverse',
                               self._make_data(params))
        return result

    def refund(self, orderId, refundAmount, extra_params=dict()):
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
        result = self._make_request(self.url, self.api_type, 'refund',
                               self._make_data(params))
        return result

    def order_status(self, orderId, extra_params=dict()):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:getorderstatus

        orderId - Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
        """

        params = extra_params.copy()
        params.update({
            'orderId': orderId,
        })
        result = self._make_request(self.url, self.api_type, 'getOrderStatus', self._make_data(params))
        return result

    def order_full_status(self, orderId=None, orderNumber=None,
                          extra_params=dict()):
        """
        https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:getorderstatusextended

        orderId - Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
        orderNumber - Номер (идентификатор) заказа в системе магазина,
            уникален для каждого магазина в пределах системы - до 30 символов.

        В запросе должен присутствовать либо orderId, либо orderNumber. Если в
        запросе присутствуют оба параметра, то приоритетным считается orderId.
        """

        if (orderId is None) and (orderNumber is None):
            raise SberbankRequestException("none of the orderId and \
                orderNumber parameters is specified")

        params = extra_params.copy()
        params.update({
            'orderId': orderId,
            'orderNumber': orderNumber,
        })
        result = self._make_request(self.url, self.api_type, 'getOrderStatusExtended', self._make_data(params))
        return result
