import os
import shutil
from conf import settings

class Filer(object):

    def __init__(self):
        pass

    def rm_staff(self, staff_path):
        if os.path.exists(staff_path):
            if os.path.isfile(staff_path):
                os.remove(staff_path)
            elif os.path.isdir(staff_path):
                shutil.rmtree(staff_path)

    def cp_staff(self, staff_path, dest):
        if not os.path.exists(dest) or os.path.isfile(dest):
            os.mkdir(dest)

        basename = os.path.basename(staff_path)
        full_dest_path = os.path.join(dest, basename)
        self.rm_staff(full_dest_path)

        if os.path.isfile(staff_path):
            shutil.copy(staff_path, dest)
        elif os.path.isdir(staff_path):
            shutil.copytree(staff_path, dest)   

    def mk_dir(self, root, name):
        dir_path = os.path.join(root, name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)
        elif os.path.isfile(dir_path):
            os.remove(dir_path)
            os.mkdir(dir_path)

    def cp_staffs(self, staffs, dest):
        for item in staffs:
            self.cp_staff(item, dest)

    def rm_staffs(self, staffs):
        for item in staffs:
            self.rm_staff(item)

    def mv_staff(self, staff, dest):
        self.cp_staff(staff, dest)
        self.rm_staff(staff)

    def mv_staffs(self, staffs, dest):
        for staff in staffs:
            self.mv_staff(staff, dest)

    def touch_file(self, file_path, content):
        with open(file_path,'w') as file_obj:
            file_obj.write(content)

if __name__ == "__main__":
    pass