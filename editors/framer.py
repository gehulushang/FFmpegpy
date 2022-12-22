
import os
import sys
from conf import settings
from utils.filer import Filer
from utils.timer import Timer
from utils.printer import Printer
from editors.sewer import Sewer
from editors.ffbase import FFbase

class Framer(FFbase):

    def __init__(self):
        self.sewer = Sewer()
        self.filer = Filer()
        self.timer = Timer()
        self.printer = Printer()

    def vintraframe(self, input, params=None):
        # init
        func = sys._getframe().f_code.co_name
        work_path = self.ff_init(func)
        basename = os.path.basename(input)

        # set intraframe
        ffinputs = {input:None}
        tmp_output_path = os.path.join(work_path, basename)
        ffoutputs = {tmp_output_path:['-strict', '-2', '-qscale', '0']}

        result = self.ff_execute(ffinputs, ffoutputs, func, tmp_output_path)

        # postprocess
        result = self.ff_post(input, work_path)
        return result

    def vctlframes(self, input, rate, params=None):
        func = sys._getframe().f_code.co_name
        work_path = self.ff_init(func)
        basename = os.path.basename(input)

        # set ctlframes
        ffinputs = {input:None}
        tmp_output_path = os.path.join(work_path, basename)
        ffoutputs = {tmp_output_path:None}

        result = self.ff_execute(ffinputs, ffoutputs, func, tmp_output_path)

        # postprocess
        result = self.ff_post(input, work_path)
        return result

    def vadjustframes(self, input, start, duration, rate):
        # init
        segment_dura = duration/settings.FRAMES_ADJUST_SPLIT_CNT
        func = sys._getframe().f_code.co_name
        work_path = self.ff_init(func)
        basename = os.path.basename(input)

        # split ahead and back
        dura = segment_dura * settings.FRAMES_ADJUST_SPLIT_CNT
        full_ahead_path = os.path.join(work_path, 'ahead_splice.mp4')
        ahead_splice = self.vsplit(input, full_ahead_path, 0, start)
        full_back_path = os.path.join(work_path, 'back_splice.mp4')
        back_splice = self.vsplit(input, full_back_path, 
                                  start + dura, settings.MAX_TIMESTAMPS)

        # adjust frames
        adjust_splice_list = []
        for i in range(settings.FRAMES_ADJUST_SPLIT_CNT):
            seg_rate = (1 - abs(i - 2) * 0.4) * rate
            seg_params = (start + i * segment_dura, segment_dura, seg_rate)
            seg_path = os.path.join(work_path, 'seg' + str(i) + '.mp4')
            segment = self.sewer.vsplit(input, seg_path, 
                                       start + i * segment_dura, segment_dura)
            self.vctlframes(segment, seg_rate)
            adjust_splice_list.append(segment)

        # splice
        tmp_output_path = os.path.join(work_path, 'tmp_' + basename)
        splice_result = self.sewer.vsplice(adjust_splice_list, tmp_output_path)

        splice_list = []
        splice_list.append(ahead_splice)
        splice_list.append(splice_result)
        splice_list.append(back_splice)
        output_path = os.path.join(work_path, basename)
        result = self.sewer.vsplice(splice_list, output_path)

        # postprocess
        result = self.ff_post(input, work_path)
        return result

if __name__ == "__main__":
    pass