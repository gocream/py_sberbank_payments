# -*- coding: utf-8 -*-

from unittest import TestCase
from unittest.mock import MagicMock
from unittest.mock import patch
import io
import json
import requests
import unittest




REGISTER_REQUEST = {
    "orderId": "70906e55-7114-41d6-8332-4609dc6590f4",
    "formUrl": "https://server/application_context/merchants/test/payment_ru.html?mdOrder=70906e55-7114-41d6-8332-4609dc6590f4"
}

def _test_request(url, params=None, **kwargs):
    response = requests.Response()

    if url == "https://3dsec.sberbank.ru/payment/rest/register.do":
        # register order
        response.raw = io.BytesIO(str.encode(json.dumps(REGISTER_REQUEST)))

    return response


class SberbankApiTestCase(TestCase):

    def setUp(self):
        from pysberbank import Sberbank
        self.api = Sberbank("test_username", "test_password")

    @patch('requests.post', side_effect=_test_request)
    def test_register_order(self, mock_requests):
        response = self.api.register("42000", "1000", "https://returnurl.example/")

        self.assertIsNotNone(response)
        self.assertEqual(response, REGISTER_REQUEST)


if __name__ == '__main__':
    unittest.main()
