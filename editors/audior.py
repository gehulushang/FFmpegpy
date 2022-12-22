
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

    def vaumix(self, input, audio, params=None):
        # init
        func = sys._getframe().f_code.co_name
        work_path = self.ff_init(func)
        basename = os.path.basename(input)
        
        # audio mix
        ffinputs = {input:None}
        tmp_output_path = os.path.join(work_path, basename)
        ffoutputs = {tmp_output_path:None}

        result = self.ff_execute(ffinputs, ffoutputs, func, tmp_output_path)

        # postprocess
        result = self.ff_post(input, work_path)

        return result

    def vauset(self, input, params=None):
        # init
        func = sys._getframe().f_code.co_name
        work_path = self.ff_init(func)
        basename = os.path.basename(input)
        
        # set audio
        ffinputs = {input:None}
        tmp_output_path = os.path.join(work_path, basename)
        ffoutputs = {tmp_output_path:None}

        result = self.ff_execute(ffinputs, ffoutputs, func, tmp_output_path)

        # postprocess
        result = self.ff_post(input, work_path)

        return result

if __name__ == "__main__":
    pass