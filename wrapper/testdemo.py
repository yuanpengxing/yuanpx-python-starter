# -*- coding: UTF-8 -*-
# author: yuanpx
import unittest

from wrapper.case_level import CaseLevel
from wrapper.decorator import caselevel
from wrapper.urls import URLMgr
from wrapper.httpwrapper import assertHttpGetResponseTextContains


class TestDemo(unittest.TestCase):
    @caselevel(CaseLevel.HIGH)
    @assertHttpGetResponseTextContains(URLMgr.baidu, 'baidu')
    def test_response(self):
        pass
