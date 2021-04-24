# -*- coding: UTF-8 -*-
import unittest

from testcase.baidu_search import BaiduSearch


class Entry:
    """
    创建suite，最终被main.py引入使用
    """
    def run_suite(self):
        suite = unittest.TestSuite()
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(BaiduSearch))
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(BaiduSearch))
        runner = unittest.TextTestRunner()
        runner.run(suite)
