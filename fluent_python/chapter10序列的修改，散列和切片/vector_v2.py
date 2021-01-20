# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/19 23:49
# Description:

import math
import reprlib
from array import array


class Vector:
    type_code = 'd'

    def __init__(self, components):
        self._components = array(self.type_code, components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        return self._components[item]

    def __iter__(self):
        # 为了迭代，我们使用 self._components 构建一个迭代器
        return iter(self._components)

    def __repr__(self):
        # 使用 reprlib.repr() 函数获取 self._components 的有限长度表示形式（如 array('d', [0.0, 1.0, 2.0, 3.0, 4.0,...])）。
        components = reprlib.repr(self._components)
        # 把字符串插入 Vector 的构造方法调用之前，去掉前面的array('d' 和后面的 )。
        components = components[components.find('['):-1]
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        # 直接使用 self._components 构建 bytes 对象。
        return bytes([ord(self.type_code)]) + bytes(self._components)

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        # 不能使用 hypot(平方根) 方法了，因此我们先计算各分量的平方之和，然后再使用 sqrt 方法开平方。
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    @classmethod
    def frombytes(cls, b):
        type_code = chr(b[0])
        memv = memoryview(b[1:]).cast(type_code)
        # 因为直接传入序列（components），把 memoryview 传给构造方法，不用像前面那样使用 * 拆包。
        return cls(memv)


if __name__ == '__main__':
    v1 = Vector([3, 4, 5])
    print(len(v1))  # 3
    print(v1[0], v1[-1])  # 3.0 5.0
    v2 = Vector(range(7))
    print(v2[1:4])  # array('d', [1.0, 2.0, 3.0])
