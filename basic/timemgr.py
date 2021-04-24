# -*- coding: UTF-8 -*-
from datetime import datetime
from datetime import timedelta

import time
import unittest


class TimeMgr(unittest.TestCase):

    def test_time(self):
        print(time.localtime())

    # 可以理解为datetime基于time进行了封装，方便使用
    def test_datetime(self):
        print(datetime.now().timetuple())
        print(timedelta.days(1))
        pass
