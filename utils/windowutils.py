import time

import win32gui
import win32ui
import win32con
import win32api


def capture_whole_screen(filename):
    hwndDC = win32gui.GetWindowDC(0)  # 0表示当前活跃的窗口
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[0][2][2]
    h = MoniterDev[0][2][3]
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    # 第4个参数(0, 0)表示截取从左上角(0, 0)开始，截取长宽为(w, h)的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


def capture_specify_area(filename, loc1, loc2):
    hwndDC = win32gui.GetWindowDC(0)  # 0表示当前活跃的窗口
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()
    saveBitMap = win32ui.CreateBitmap()
    # MoniterDev = win32api.EnumDisplayMonitors(None, None)
    # w = MoniterDev[0][2][2]
    # h = MoniterDev[0][2][3]
    w = loc2[0] - loc1[0]
    h = loc2[1] - loc1[1]
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    saveDC.SelectObject(saveBitMap)
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (loc1[0], loc1[1]), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, filename)


def mouse_click(x, y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)


def mouse_slice(x1, y1, x2, y2):
    win32api.SetCursorPos([x1, y1])  # 鼠标移动到
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)  # 左键按下
    time.sleep(0.5)
    dx = x2 - x1
    dy = y2 - y1
    time.sleep(0.5)
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, dx, dy)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def mouse_wheel():
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -1000)  # 滚动网页
