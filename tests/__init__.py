# -*- coding: utf-8 -*-

import unittest

from .register import RegisterTestCase
from .reverse import ReverseTestCase
from .refund import RefundTestCase



def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegisterTestCase('test_register'))
    suite.addTest(RegisterTestCase('test_register_errors'))
    suite.addTest(ReverseTestCase('test_reverse'))
    suite.addTest(ReverseTestCase('test_reverse_errors'))
    suite.addTest(RefundTestCase('test_refund'))
    suite.addTest(RefundTestCase('test_refund_errors'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
