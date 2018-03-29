# -*- coding: utf-8 -*-

import unittest

from .register_test import RegisterTestCase



def suite():
    suite = unittest.TestSuite()
    suite.addTest(RegisterTestCase('test_register'))
    suite.addTest(RegisterTestCase('test_register_errors'))
    return suite

if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
