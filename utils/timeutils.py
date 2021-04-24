import time


def timer_millseconds(timestr):
    parser = time.strptime(timestr, "%Y-%m-%d %H:%M:%S")
    specifystamp = int(time.mktime(parser) * 1000)
    while True:
        currentstamp = int(time.time() * 1000)
        if currentstamp < specifystamp:
            if currentstamp < (specifystamp - 1000):
                time.sleep(1)
            else:
                time.sleep(0.002)
        else:
            break


timer_millseconds("2020-12-12 14:07:00")
