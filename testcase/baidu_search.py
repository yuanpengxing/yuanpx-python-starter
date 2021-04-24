# -*- coding: UTF-8 -*-

import unittest
from time import sleep

from wrapper.case_level import CaseLevel
from wrapper.decorator import caselevel


class BaiduSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    # 标注该caselevel为HIGH， 如果CaseLevel.HIGH配置为True则该条case会被运行， 反之不被运行
    @caselevel(CaseLevel.HIGH)
    def test_demo1(self):
        print('test_demo1')
