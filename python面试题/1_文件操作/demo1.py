# -*- encoding: utf-8 -*-
# @File    : demo1.py
# @Time    : 2021/1/26 9:41
# @Author  : gq
# @Email   : qianguo@zjft.com
# @Software: PyCharm
# @Desc    : 
"""
    有一个jsonline格式的文件file.txt大小约为10K
"""


# def get_lines():
#     """dsa"""
#     with open('file.txt', 'rb') as f:
#         return f.readlines()


# if __name__ == '__main__':
    # for e in get_lines():
        # process(e)  # 处理每一行数据

"""
    现在要处理一个大小为10G的文件，但是内存只有4G，
    如果在只修改get_lines 函数而其他代码保持不变的情况下，应该如何实现？需要考虑的问题都有那些？
"""

"""
    普通实现
"""
def get_lines():
    """使用yield生成器函数，截断文件读取，每次读取一个值，"""
    with open('xxx.txt','rb') as f:
        for i in f:
            yield i  # yield 可以看做返回


"""
    要考虑的问题有：内存只有4G无法一次性读入10G文件，需要分批读入分批读入数据要记录每次读入数据的位置。
    分批每次读取数据的大小，太小会在读取操作花费过多时间。
"""
