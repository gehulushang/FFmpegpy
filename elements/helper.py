
from conf import settings
from utils.printer import Printer


class Helper(object):

    def __init__(self): # 初始化方法
        self.printer = Printer()

    def all_func_list(self, cls):
        func_list = []
        for item in dir(cls):
            if callable(getattr(cls, item)):
                func_list.append(item)
        return func_list

    def inner_func_list(self, cls):
        func_list = []
        all_func_list = self.all_func_list(cls)

        for item in all_func_list:
            if item.endswith('__') and item.startswith('__'):
                func_list.append(item)
        return func_list

    def own_func_list(self, cls):
        func_list = []
        all_func_list = self.all_func_list(cls)

        for item in all_func_list:
            if item.endswith('__') and item.startswith('__'):
                continue
            if item.startswith('ff_'):
                continue

            func_list.append(item)

        return func_list

    def describe_func(self, func):
        pass
    
    def describe_class(self, cls):
 

        return []
    

