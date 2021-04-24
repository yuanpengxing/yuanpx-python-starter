# -*- coding: UTF-8 -*-

from PyQt5.QtWidgets import QApplication
import sys
import time
import os


def screenshots(savepath):
    app = QApplication(sys.argv)
    screen = QApplication.primaryScreen()
    img = screen.grabWindow(QApplication.desktop().winId())
    img.save(savepath)


def take():
    savename = time.strftime("%Y%m%d%H%M%S", time.localtime()) + '.png'
    saveparent = 'd:/screenshot/'
    if not os.path.isdir(saveparent):
        os.makedirs(saveparent)
    savepath = saveparent + savename
    screenshots(savepath)