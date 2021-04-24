# author: yuanpx
import os
from os import path


# 递归获取目录下所有文件绝对路径，方式一(推荐)
def get_filenames(dirpath, filenames):  # 传入存储的list，用来存储所有文件绝对路径
    for (pathname, dirs, files) in os.walk(dirpath):
        if files:  # 文件,则添加进列表
            for f in files:
                filenames.append(path.join(pathname, f))
        if dirs:  # 目录,递归获取
            for dir in dirs:
                get_filenames(path.join(pathname, dir), filenames)


# 递归获取目录下所有文件绝对路径，方式二
def listdir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):
            listdir(file_path, list_name)
        else:
            list_name.append(file_path)
