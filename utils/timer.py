import os
import time
import datetime
from conf import settings

class Timer(object):

    def __init__(self):
        pass

    def strft_hms(self, seconds):
        return time.strftime('%H:%M:%S', time.gmtime(seconds))

    def current_ms(self):
        return round(time.time() * 1000)


if __name__ == "__main__":
    pass