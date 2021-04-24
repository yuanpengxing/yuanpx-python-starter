# -*- coding: UTF-8 -*-
from libs.driver_data_source import DriverDataSource


class DriverMgr:
    @classmethod
    def screenshot(cls, filename):
        DriverDataSource.get_driver().save_screenshot(filename)