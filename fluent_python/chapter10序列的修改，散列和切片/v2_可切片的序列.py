# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/20 22:41
# Description:
import math
import reprlib
import numbers
from array import array


class Vector:
    type_code = 'd'
    shortcut_names = 'xyzt'

    def __init__(self, components):
        self._components = array(self.type_code, components)

    def __len__(self):
        return len(self._components)

    def __getitem__(self, item):
        cls = type(self)
        if isinstance(item, slice):
            return cls(self._components[item])
        elif isinstance(item, numbers.Integral):
            return self._components[item]
        else:
            msg = "{cls.__name__} indices must be integers"
            raise TypeError(msg.format(cls=cls))

    def __setattr__(self, key, value):
        cls = type(self)
        if len(key) == 1:
            if key in cls.shortcut_names:
                error = 'readonly attribute {attr_name!r}'
            elif key.islower():
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else:
                error = ''

            if error:
                msg = error.format(cls_name=cls.__name__, attr_name=key)
                raise AttributeError(msg)
        super().__setattr__(key, value)  # 默认情况：在超类上调用 __setattr__ 方法，提供标准行为。

    def __getattr__(self, item):
        """检查所查找的属性是不是 xyzt 中的某个字母，如果是，那么返回对应的分量"""
        cls = type(self)

        if len(item) == 1:
            index = cls.shortcut_names.find(item)
            if 0 <= index <= len(self._components):
                return self._components[index]
        msg = '{.__name!r} object has no attribute {!r}'
        raise AttributeError(msg.format(cls, item))

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
    v = Vector(range(5))
    print(repr(v))  # Vector([0.0, 1.0, 2.0, 3.0, 4.0])
    print(v.x)  # 0.0

    try:
        v.x = 10
    except AttributeError as e:
        print(e)  # readonly attribute 'x'

    try:
        v.c = 1
    except AttributeError as e:
        print(e)  # can't set attributes 'a' to 'z' in 'Vector'
