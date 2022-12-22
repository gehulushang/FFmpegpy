import os
import ffmpy
from conf import settings
from utils.timer import Timer
from utils.filer import Filer
from utils.printer import Printer

class FFbase(object):

    def __init__(self): # 初始化方法
        self.printer = Printer()
        self.filer = Filer()
        self.timer = Timer()

    def ff_obj(self, ffinputs, ffoutputs):
        outputs_params = ffoutputs.values()
        keys = ffoutputs.keys()
        for key in keys:
            outputs_params = ffoutputs[key]
            outputs_params.append('-loglevel')
            outputs_params.append('quiet')
            ffoutputs[key] = outputs_params

        ffobj = ffmpy.FFmpeg(inputs=ffinputs, outputs=ffoutputs)
        return ffobj
    
    def ff_execute(self, ffinputs, ffoutputs, func, output=None):
        ffobj = self.ff_obj(ffinputs,ffoutputs)
        self.printer.hint('ffmpeg cmd: ')
        self.printer.info(ffobj.cmd)
        ffobj.run()
        result = None
        if output == None:
            return result
        
        if os.path.exists(output):
            self.printer.hint(func + ' output:')
            self.printer.info(output)
            result = output
        else:
            self.printer.err(str(ffobj.cmd) + ' run with error')

        return result

    def ff_init_dir(self, func):
        dir_name = func + '_' + str(self.timer.current_ms())

        root_path = os.path.join(os.getcwd(), settings.OUTPUTS_DIR)
        self.filer.mk_dir(root_path, str(dir_name))
        work_path = os.path.join(root_path, str(dir_name))

        return work_path

    def ff_session(self, func):
        self.printer.session(func, {})

    def ff_init(self, func):
        self.printer.session(func, {})
        work_path = self.ff_init_dir(func)
        return work_path

    def ff_post(self, input, work_path):
        dirname = os.path.dirname(input)
        basename = os.path.basename(input)

        tmp_output_path = os.path.join(work_path, basename)
        self.filer.rm_staff(input) 
        self.filer.cp_staff(tmp_output_path, dirname)
        result = os.path.join(dirname, basename)
        self.filer.rm_staff(work_path)

        return result