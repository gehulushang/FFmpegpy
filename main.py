from editors.sewer import Sewer
from editors.filter import Filter
from editors.ffbase import FFbase
from elements.helper import Helper

if __name__ == "__main__":
    src_path = '/home/zjf/video/FFmpy//output2.mp4'
    obj = Sewer()
    # obj.vsplit(src_path, './output.mp4', 13, 1155)
    
    
    inputs = ['/home/zjf/video/FFmpy/output/splits/output0.mp4',
              '/home/zjf/video/FFmpy/output/splits/output1.mp4',
              '/home/zjf/video/FFmpy/output/splits/output2.mp4',
              '/home/zjf/video/FFmpy/output/splits/output3.mp4',
              
              '/home/zjf/video/FFmpy/output/splits/output4.mp4',
              '/home/zjf/video/FFmpy/output/splits/output5.mp4',
              '/home/zjf/video/FFmpy/output/splits/output6.mp4',
              '/home/zjf/video/FFmpy/output/splits/output7.mp4',
              
              '/home/zjf/video/FFmpy/output/splits/output8.mp4',
              '/home/zjf/video/FFmpy/output/splits/output9.mp4',
              '/home/zjf/video/FFmpy/output/splits/output10.mp4',
              '/home/zjf/video/FFmpy/output/splits/output11.mp4',
              ]
    
    # obj.vsplice(inputs, 'joinoutput.mp4')

    # obj.vdrawframes('', 0, 0)

    # base_obj = FFbase()

    # base_obj.ff_init('test')

    # helper = Helper()
    # infos = helper.own_func_list(obj)

    # print(infos)
    
    flt = Filter()
    
    flt.vblur(src_path, 116, 32, 20, 10, 330, 380)