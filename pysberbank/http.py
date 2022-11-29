# -*- coding: utf-8 -*-

from requests import RequestException
import json
import logging
import requests

from .errors import SberbankApiException
from .errors import SberbankException
from .errors import SberbankRequestException


logger = logging.getLogger("pysberbank")


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
                 language=DEFAULT_LANGUAGE, currency=DEFAULT_CURREBCY,
                 ensure_ascii=True):
        """
            username - username at sberbank api
            password - password at sberbank api
            url - api url address
            api_type - api type (soap | rest) only rest ready
            language - default language (ISO 639-1)
            currency - default currency (ISO 4217)

            @TODO:
             * remove `url` parameter in favor of a boolean `production` parameter
             * move `ensure_ascii` parameter to `_make_data` method parameter and pass it from class methods
        """

        if (not (bool(username) and bool(password))) == (token is None):
            raise SberbankException(
                "Auth params require. "
                "Setup username/password pair or token, not both"
            )

        self.username = username
        self.password = password
        self.token = token

        self.url = url
        self.api_type = api_type
        self.language = language
        self.currency = currency

        self.ensure_ascii = ensure_ascii

    def _make_data(self, params, remove_null=True):
        """
        add username/password pair or token to request params

        remove_null: if True - remove all None elements from params
        """

        if remove_null:
            data = dict(filter(lambda x: x[1], params.items()))
        else:
            data = params.copy()

        if self.token:
            data['token'] = self.token
        else:
            data.update({
                'userName': self.username,
                'password': self.password,
            })

        # we need to encode lists and dicts in json
        for k, v in data.items():
            if not isinstance(v, (list, dict)):
                continue
            data[k] = json.dumps(data[k], ensure_ascii=self.ensure_ascii)

        return data

    def _make_request(
        self,
        url,
        api_type,
        method_name,
        params=None,
        remove_null=True,
        **kwargs,
    ):
        # resource
        if api_type == 'rest':
            method = f'{method_name}.do'
        else:
            method = method_name
        url = url.format(api_type=api_type, method=method)

        # pyload
        if params is None:
            params = {}
        data = self._make_data(params, remove_null=remove_null)

        logger.debug(f"Make request to {url} with data {data} and params {kwargs}.")
        try:
            response = requests.post(url, data=data, **kwargs)
            logger.debug(f"Response to {url} request is {response.content}.")

            if api_type == 'rest':
                result = response.content.json()

                if result.get('errorCode', '0') != '0':
                    raise SberbankApiException(result['errorCode'],
                                               result['errorMessage'])
            else:
                result = response.content

        except RequestException as e:
            # wrap Requests exception in our for filtration purposes
            raise SberbankRequestException(
                request=e.request,
                response=e.response
            ) from e

        return result

    def register(
        self,
        orderNumber,
        amount,
        returnUrl,
        currency=None,
        failUrl=None,
        description=None,
        language=None,
        pageView=None,
        clientId=None,
        merchantLogin=None,
        sonParams=None,
        order_bundle=None,
        tax_system=None,
        sessionTimeoutSecs=None,
        expirationDate=None,
        bindingId=None,
        features=None,
        url=None,
        api_type=None,
        **kwargs,
    ):
        """
        Register cart

        `Request doc`_
        `Request Cart doc`_

        Attributes:
            orderBundle: корзина для чека
            taxSystem: система налогообложения

        .. _Request doc:
           https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:register

        .. _Request Cart doc:
           https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:register_cart
        """

        params = {
            'orderNumber': orderNumber,
            'amount': amount,
            'currency': currency or self.currency,
            'returnUrl': returnUrl,
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
            'orderBundle': order_bundle,
            'taxSystem': tax_system,
        }
        result = self._make_request(url or self.url, api_type or self.api_type,
                                    'register', params, **kwargs)
        return result

    def reverse(self, orderId, language=None, url=None, api_type=None, **kwargs):
        """
        Reverse payment

        Функция отмены доступна в течение ограниченного времени после оплаты,
        точные сроки необходимо уточнять в «Сбербанке».

        `Request doc`_

        Attributes:
            orderId: Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.

        .. _Request doc:
           https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:reverse
        """

        params = {
            'orderId': orderId,
            'language': language or self.language,
        }
        result = self._make_request(url or self.url, api_type or self.api_type,
                                    'reverse', params, **kwargs)
        return result

    def refund(self, orderId, refundAmount, language=None, url=None, api_type=None, **kwargs):
        """
        Refund

        `Request doc`_

        Attributes
            orderId: Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
            refundAmount: Сумма возврата в валюте заказа. Может быть меньше или
                равна остатку в заказе.
            language: Не указан в документации, но вероятно по аналогии с
                остальными методами он всё же там должен быть... Вероятно...
                Нужно поправить если ругаться будет

        .. _Request doc:
           https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:refund
        """

        params = {
            'orderId': orderId,
            'amount': refundAmount,
            'language': language or self.language,
        }
        result = self._make_request(url or self.url, api_type or self.api_type,
                                    'refund', params, **kwargs)
        return result

    def order_status(self, orderId, language=None, url=None, api_type=None, **kwargs):
        """
        Order status

        `Request doc`_

        Attributes
            orderId: Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
            language: Не указан в документации, но вероятно по аналогии с
                остальными методами он всё же там должен быть... Вероятно...
                Нужно поправить если ругаться будет

        .. _Request doc:
           https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:getorderstatus
        """

        params = {
            'orderId': orderId,
            'language': language or self.language,
        }
        result = self._make_request(url or self.url, api_type or self.api_type,
                                    'getOrderStatus', params, **kwargs)
        return result

    def order_status_extended(
        self,
        orderId=None,
        orderNumber=None,
        anguage=None,
        url=None,
        api_type=None,
        **kwargs,
    ):
        """
        Order status extended

        В запросе должен присутствовать либо _orderId_, либо _orderNumber_.
        Если в запросе присутствуют оба параметра, то приоритетным считается
        _orderId_.

        `Request doc`_

        Attributes
            orderId: Номер заказа в платёжном шлюзе. Уникален в пределах шлюза.
            orderNumber: Номер (идентификатор) заказа в системе магазина,
            уникален для каждого магазина в пределах системы - до 30 символов.
            language: Не указан в документации, но вероятно по аналогии с
                остальными методами он всё же там должен быть... Вероятно...
                Нужно поправить если ругаться будет

        .. _Request doc:
           https://securepayments.sberbank.ru/wiki/doku.php/integration:api:rest:requests:getorderstatusextended
        """

        if (orderId is None) and (orderNumber is None):
            raise SberbankException(
                "none of the orderId and "
                "orderNumber parameters is specified"
            )

        params = {
            'orderId': orderId,
            'orderNumber': orderNumber,
            'language': language or self.language,
        }
        result = self._make_request(url or self.url, api_type or self.api_type,
                                    'getOrderStatusExtended', params, **kwargs)
        return result
