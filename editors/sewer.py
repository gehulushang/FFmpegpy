import os
import sys
from conf import settings
from utils.filer import Filer
from utils.timer import Timer
from utils.printer import Printer
from editors.ffbase import FFbase

class Sewer(FFbase):

    def __init__(self):
        self.filer = Filer()
        self.timer = Timer()
        self.printer = Printer()

    def vsplit(self, input, output, startpoint, duration, params=None):
        self.filer.rm_staff(output)
        func = sys._getframe().f_code.co_name
        start = self.timer.strft_hms(startpoint)
        ffinputs = {input:['-ss', start]}

        dura = self.timer.strft_hms(duration)
        
        output_params = ['-t', dura,
                          '-vcodec', 'copy',
                          '-acodec', 'copy',]
        
        ffoutputs = {output:output_params}
        result = self.ff_execute(ffinputs, ffoutputs, func, output)

        return result

    def vsplice(self, inputs, output):
        self.filer.rm_staff(output)
        func = sys._getframe().f_code.co_name
        work_path = self.ff_init(func)
        
        self.filer.cp_staffs(inputs, work_path)

        # splice
        content = ''
        splits_path = os.path.join(work_path, 'splits.txt')
        for item in inputs:
            basename = os.path.basename(item)
            content += "file " + "'" + str(basename) + "'\n"
            
        self.filer.touch_file(splits_path, content)

        ffinputs = {splits_path:['-f', 'concat']}
        
        output_params = ['-c', 'copy']
        ffoutputs = {output:output_params}
            
        result = self.ff_execute(ffinputs, ffoutputs, 'vsplice', output)

        # postprocess
        self.filer.rm_staff(work_path)

        return result

    def vinsertdraw(self, func, input, patch_list, keypoint):
        work_path = self.ff_init(func)

        dirname = os.path.dirname(input)
        basename = os.path.basename(input)

        full_ahead_path = os.path.join(work_path, 'ahead_splice.mp4')
        ahead_splice = self.vsplit(input, full_ahead_path, 0, keypoint)
        full_back_path = os.path.join(work_path, 'back_splice.mp4')
        back_splice = self.vsplit(input, full_back_path, 
                                  keypoint, settings.MAX_TIMESTAMPS)
        splice_list = []
        splice_list.append(ahead_splice)

        for item in patch_list:
            splice_list.append(item)
        splice_list.append(back_splice)
        tmp_output_path = os.path.join(work_path, basename)
        result = self.vsplice(splice_list, tmp_output_path)

        self.result = self.ff_post(input, work_path)

        return result

    def vinsert(self, input, patch, insertpoint):
        patch_list = [patch]
        func = sys._getframe().f_code.co_name
        result = self.vinsertdraw(func, input, patch_list, insertpoint)
        return result

    def vdrawframes(self, input, start, duration):
        patch_list = []
        keypoint = start + duration
        func = sys._getframe().f_code.co_name
        result = self.vinsertdraw(func, input, patch_list, keypoint)
        return result

if __name__ == "__main__":
    obj = Sewer('')
    obj.vsplit(0, 0, 'output.mp4')