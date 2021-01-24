# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/19 23:48
# Description:
import operator
import functools


class A:
    def __init__(self, x, y):
        self.__x = x
        self._y = y


if __name__ == '__main__':
    a = A(1, 2)


