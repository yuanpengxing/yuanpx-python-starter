import requests
import time

import win32api


def getBeijinTime():
    try:
        return requests.get('http://time1909.beijing-time.org/time.asp', headers={'User-Agent': 'Mozilla/5.0'}).text
    except:
        return (-1)


def getSystemTime():
    year = ''
    month = ''
    mday = ''
    wday = ''
    hour = ''
    min = ''
    sec = ''
    for line in getBeijinTime().split('\n'):
        # print(line)
        if 'nyear=' in line:
            year = line[6:len(line) - 2]
        if 'nmonth' in line:
            month = line[7:len(line) - 2]
        if 'nday' in line:
            mday = line[5:len(line) - 2]
        if 'nwday' in line:
            wday = line[6:len(line) - 2]
        if 'nhrs' in line:
            hour = line[5:len(line) - 2]
        if 'nmin' in line:
            min = line[5:len(line) - 2]
        if 'nsec' in line:
            sec = line[5:len(line) - 1]
    return int(year), int(month), int(wday), int(mday), int(hour), int(min), int(sec)

year, month, wday, mday, hour, min, pre_sec = getSystemTime()

for i in range(2000):
    year, month, wday, mday, hour, min, now_sec = getSystemTime()
    if pre_sec == now_sec:
        continue
    else:
        win32api.SetSystemTime(year, month, wday, mday, hour-8, min, now_sec, 60)
        break

