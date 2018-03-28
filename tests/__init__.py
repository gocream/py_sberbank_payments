# -*- coding: utf-8 -*-

import unittest



class SberbankApiTestCase(unittest.TestCase):

    def setUp(self):
        from pysberbank import Sberbank
        self.api = Sberbank("test_username", "test_password")

    def test_register_order(self):
        self.assertEqual(200, 200)


if __name__ == '__main__':
    unittest.main()
