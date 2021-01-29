# -*- encoding: utf-8 -*-
# @File    : demo2.py
# @Time    : 2021/1/26 13:54
# @Author  : gq
# @Email   : qianguo@zjft.com
# @Software: PyCharm
# @Desc    : 
"""
    现有字典 d= {'a':24,'g':52,'i':12,'k':33}请按value值进行排序?
"""

if __name__ == '__main__':
    d = {'a': 24, 'g': 52, 'i': 12, 'k': 33}
    sorted(d.items(), key=lambda x: x[1])
