# --*-- coding:utf-8 -*-
import cv2
import numpy as np
from PIL import Image,ImageDraw,ImageFont


def process(img_array, i, j):
    
    # for k in range(i-1, i+2):
    #     for v in range(j-1, j+2):
    #         if img_array[k,v][3] == 0:
    #             print('asddas')
    if img_array[i,j][3] != 255:
        img_array[i,j][0] = 255
        img_array[i,j][1] = 255
        img_array[i,j][2] = 255
        img_array[i,j][3] = 255
    
    

def get_img():
 
    image = Image.new(mode='RGBA', size=(400, 100))
    draw_table = ImageDraw.Draw(im=image)
    draw_table.text(xy=(0, 0), text='朱剑锋喜欢潘钰华', fill='#000000', font=ImageFont.truetype('/home/zjf/video/FFmpy/fonts/msyh.ttf', 80))
    
    # image.show()  # 直接显示图片
    # image.save('manyue.png', 'PNG')  # 保存在当前路径下，格式为PNG
    # image.close()
    
    img_array = np.array(image)
    shape = img_array.shape    #将图像转为矩阵
    print(shape)
    # print(img_array.shape)       #图像大小
    for i in range(0, shape[0]):        #行总数
        for j in range(0, shape[1]):    #列总数
            if img_array[i,j][3] != 0:
                process(img_array, i, j)
                
            # value = img_array[i, j]    #数组中的元素
            # if value >= 10:
            #     value = 0
            #     img_array[i,j] = value
    img2 = Image.fromarray(np.uint8(img_array))
    img2.save('manyue.png', 'PNG')
    image.close()
 
def draw_box_string(img, box, string):
    """
    img: read by cv;
    box:[xmin, ymin, xmax, ymax];
    string: what you want to draw in img;
    return: img
    """
    x,y,x1,y1 = box
    # cv2.rectangle(img, (x,y), (x1, y1), (0,0,255), 2)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img)
    draw = ImageDraw.Draw(img)
    # simhei.ttf 是字体，你如果没有字体，需要下载
    font = ImageFont.truetype("/home/zjf/video/FFmpy/fonts/msyh.ttf", 40, encoding="utf-8")
    draw.text((x, y-20), string, (160, 160, 160), font=font)
    img = cv2.cvtColor(np.array(img), cv2.COLOR_RGB2BGR)
    return img
 
 
if __name__ == "__main__":
    # img_path = "/home/zjf/video/FFmpy/jiantou.jpg"
    # img = cv2.imread(img_path)
    # box = [200, 800, 499, 263]
    # string = "飞机"
    # img = draw_box_string(img, box, string)
    # cv2.imwrite("airplane.jpg", img)
    
    get_img()