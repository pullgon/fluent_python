# -*- encoding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2021/1/26 9:39
# @Author  : gq
# @Email   : qianguo@zjft.com
# @Software: PyCharm
# @Desc    :
import weakref
import objgraph


class A:
    pass


class B:
    pass


def bye():
    print("bye bye!")


if __name__ == '__main__':
    a = A()
    b = B()
    print(objgraph.count('A'))
    ender = weakref.finalize(a, bye)
    print(ender.alive)
    a.name = b
    b.dsa = a
    del a
    del b
    print(objgraph.count('A'))

