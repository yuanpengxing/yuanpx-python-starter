# -*- coding: UTF-8 -*-
from threading import current_thread

from selenium import webdriver

from conf.driverconf import BasicDriverSetting

"""
Chrome Options常用设置以下：
    禁止图片和视频的加载
    添加扩展：像正常使用浏览器一样的功能
"""


class ChromeInit:
    @classmethod
    def init(cls):
        options = webdriver.ChromeOptions()
        options.add_argument('--disable-infobars')  # 禁用浏览器正在被自动化程序控制的提示
        options.add_argument('--start-maximized')

        # 针对禁止加载图片的操作
        # prefs = {"profile.managed_default_content_settings.images": 2}
        # options.add_experimental_option("prefs", prefs)
        # options.add_argument('--disable-infobars')  # 禁止策略化
        # options.add_argument('--no-sandbox')
        # options.add_argument('--incognito')  # 隐身模式（无痕模式）
        # options.add_argument('--disable-javascript')
        # options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
        # options.add_argument('--proxy-server=http://ip:port')  # 尽量选择静态IP，提升稳定性
        # options.add_argument('--headless')  # 浏览器不提供可视化页面. linux下必须

        current_thread_name = current_thread().name
        if current_thread_name == 'chrome':
            return webdriver.Chrome(BasicDriverSetting.CHROME_PATH, chrome_options=options)
        elif current_thread_name == 'firefox':
            return webdriver.Chrome(BasicDriverSetting.FIREFOX_PATH, chrome_options=options)
        elif current_thread_name == 'ie':
            return webdriver.Chrome(BasicDriverSetting.IE_PATH, chrome_options=options)
        elif current_thread_name == 'edge':
            return webdriver.Chrome(BasicDriverSetting.EDGE_PATH, chrome_options=options)
        elif current_thread_name == 'opera':
            return webdriver.Chrome(BasicDriverSetting.OPERA_PATH, chrome_options=options)
        elif current_thread_name == 'phantomjs':
            return webdriver.Chrome(BasicDriverSetting.PHANTOMJS_PATH, chrome_options=options)
        elif current_thread_name == 'android':
            return webdriver.Chrome(BasicDriverSetting.ANDROID_PATH, chrome_options=options)
        else:
            return webdriver.Chrome("D:/chromedriver.exe", chrome_options=options)


if __name__ == '__main__':
    ChromeInit.init()
