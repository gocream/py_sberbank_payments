# -*- coding: utf-8 -*-

import unittest

from .register import RegisterTestCase
from .reverse import ReverseTestCase
from .refund import RefundTestCase
from .order_status import OrderStatusTestCase



def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegisterTestCase('test_register'))
    suite.addTest(RegisterTestCase('test_register_errors'))
    suite.addTest(ReverseTestCase('test_reverse'))
    suite.addTest(ReverseTestCase('test_reverse_errors'))
    suite.addTest(RefundTestCase('test_refund'))
    suite.addTest(RefundTestCase('test_refund_errors'))
    suite.addTest(OrderStatusTestCase('test_order_status'))
    suite.addTest(OrderStatusTestCase('test_order_status_errors'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
