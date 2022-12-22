import os
import sys
from conf import settings
from utils.filer import Filer
from utils.timer import Timer
from utils.printer import Printer
from editors.sewer import Sewer
from editors.ffbase import FFbase
class Filter(FFbase):

    def __init__(self): # 初始化方法
        self.sewer = Sewer()
        self.filer = Filer()
        self.timer = Timer()
        self.printer = Printer()

    def voverlay(self, input, overlay, start, duration):
        # init
        keypoint = start + duration
        func = sys._getframe().f_code.co_name
        work_path = self.ff_init(func)

        dirname = os.path.dirname(input)
        basename = os.path.basename(input)

        full_ahead_path = os.path.join(work_path, 'ahead_splice.mp4')
        ahead_splice = self.sewer.vsplit(input, full_ahead_path, 0, keypoint)
        full_back_path = os.path.join(work_path, 'back_splice.mp4')
        back_splice = self.sewer.vsplit(input, full_back_path, 
                                  keypoint, settings.MAX_TIMESTAMPS)

        # overlay
        ffinputs = {ahead_splice:None}
        overlay_data_path = os.path.join(work_path, 'overlay.mp4')
        ffoutputs = {overlay_data_path:None}

        overlay_data_path = self.ff_execute(ffinputs, ffoutputs, func, overlay_data_path)
        
        splice_list = []
        splice_list.append(overlay_data_path)
        splice_list.append(back_splice)

        # splice
        tmp_output_path = os.path.join(work_path, basename)
        result = self.sewer.vsplice(splice_list, tmp_output_path)
        
        # postprocess
        result = self.ff_post(input, work_path)

        return result

    def vblur(self, input, start, duration, x, y , w, h):
        result = None
        # init
        keypoint = start + duration
        func = sys._getframe().f_code.co_name
        work_path = self.ff_init(func)

        basename = os.path.basename(input)

        delogo_params = "delogo=x=" + str(x) + ':y=' + str(y) + ':w=' + str(w) + ':h=' + str(h) + ":show=0"
        time_params = ':enable=between(t\,' + str(start) + '\,' + str(keypoint) + ')'
        delogo_params += time_params
        
        # blur 
        ffinputs = {input:['-y']}
        # output_data_name = 'blur' + str(i) + '.mp4'
        output_data_path = os.path.join(work_path, basename)
        
        output_params = ['-vcodec', 'libx264', '-filter_complex', 
                            delogo_params, '-c:a', 'copy', '-f', 'mp4']
        ffoutputs = {output_data_path:output_params}

        result = self.ff_execute(ffinputs, ffoutputs, func, output_data_path)

        # postprocess
        result = self.ff_post(input, work_path)

        return result

if __name__ == "__main__":
    pass