# -*- encoding: utf-8 -*-
# @File    : demo2.py
# @Time    : 2021/1/26 10:31
# @Author  : gq
# @Email   : qianguo@zjft.com
# @Software: PyCharm
# @Desc    : 
"""
    补充缺失的代码
"""
import os

# def print_directory_contents(path):
#     """
#         这个函数接收文件夹的名称作为输入参数
#         返回该文件夹中文件的路径以及其包含文件夹中文件的路径
#     """
#     child_path = os.path.join(path)  # 获取子目录
#     if os.path.isdir(child_path):  # 如果子目录是文件夹，则递归向下查找
#         print_directory_contents(child_path)
#     else:  # 否则付汇文件名称
#         print(child_path)

"""
    设计实现遍历目录与子目录，抓取.pyc文件
"""


def get_files(dir, suffix):
    res = []
    for root, dirs, files in os.walk(dir):
        for file_name in files:
            name, suf = os.path.splitext(file_name)
            if suf == suffix:
                res.append(os.path.join(root, file_name))
    print(res)


if __name__ == '__main__':
    get_files('./', '.py')
