# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/7 22:09
# Description:

from array import array
import math
from loguru import logger


class Vector2d:
    type_code = 'd'

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return bytes(ord(self.type_code)) + bytes(array(self.type_code, self))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, oc):
        typecode = chr(oc[0])
        print(typecode)
        memv = memoryview(oc[1:]).cast(typecode)
        return cls(*memv)


if __name__ == '__main__':
    v1 = Vector2d(3, 4)
    # print(v1)
    # # (3.0, 4.0)
    # print(v1.x, v1.y)
    # # 3.0 4.0
    #
    # x, y = v1
    # print(x, y)
    # # 3.0 4.0
    #
    # v1_clone = eval(repr(v1))
    # print(v1_clone)
    # # (3.0, 4.0)
    # print(repr(v1) == 'Vector2d(3.0, 4.0)')
    # # True
    # print(v1 == v1_clone)
    # True

    octets = "abc".encode('utf-8')
    # print(octets)
    # b'\x00\x00\x00\x00\x00\x00\x00\...
    Vector2d.frombytes(octets)

    # print(abs(v1))
    # # 5.0
    # print(bool(v1), bool(Vector2d(0, 0)))
    # True, False
