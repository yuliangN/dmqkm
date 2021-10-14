# coding=utf-8
import os


# 获取文件公共类
class GainFiles:

    # 获取一张图片地址
    def gain_images(self, image):
        base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        data_path = os.path.join(base_path, 'datas/image', image)
        files = {'imageFile1': ('1.jpg', open(data_path, 'rb'), "image/jpeg"),
                 'imageFile2': ('2.jpg', open(data_path, 'rb'), "image/jpeg"),
                 'imageFile3': ('3.jpg', open(data_path, 'rb'), "image/jpeg"),
                 }
        return files

    # 获取多张图片
    def gain_more_images(self):
        base_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        data_path1 = os.path.join(base_path, 'datas/image', '1.jpg')
        data_path2 = os.path.join(base_path, 'datas/image', '2.jpg')
        data_path3 = os.path.join(base_path, 'datas/image', '3.jpg')
        files = {'imageFile1': ('1.jpg', open(data_path1, 'rb'), "image/jpeg"),
                 'imageFile2': ('2.jpg', open(data_path2, 'rb'), "image/jpeg"),
                 'imageFile3': ('3.jpg', open(data_path3, 'rb'), "image/jpeg"),
                 }
        return files
