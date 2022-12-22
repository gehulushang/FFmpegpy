
import os
import sys
from conf import settings
from utils.filer import Filer
from utils.timer import Timer
from utils.printer import Printer
from editors.sewer import Sewer
from editors.ffbase import FFbase

class Audior(FFbase):

    def __init__(self):
        self.filer = Filer()
        self.timer = Timer()
        self.printer = Printer()

    def vsubtitles(self, input, subtitles, start, dura, x=-1, y=-1, params=None):
        # init
        func = sys._getframe().f_code.co_name
        


        # return result
        
    def vsubtitleVFX(self):
        pass

if __name__ == "__main__":
    pass