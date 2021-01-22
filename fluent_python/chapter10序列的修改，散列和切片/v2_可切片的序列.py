# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/20 22:41
# Description:
import math
import reprlib
import numbers
import functools
import operator
import itertools
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
        return len(self) == len(other) and all(a == b for a, b in zip(self, other))

    def __hash__(self):
        # hashes = (hash(x) for x in self._components)
        hashes = map(hash, self._components)
        return functools.reduce(operator.xor, hashes)

    def __abs__(self):
        # 不能使用 hypot(平方根) 方法了，因此我们先计算各分量的平方之和，然后再使用 sqrt 方法开平方。
        return math.sqrt(sum(x * x for x in self))

    def __bool__(self):
        return bool(abs(self))

    def angle(self, n):
        """计算n纬球体中的某个角坐标"""
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n - 1])
        if (n == len(self) - 1) and self[-1] < 0:
            return math.pi * 2 - a
        else:
            return a

    def angles(self):
        """"""
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec=''):
        if format_spec.endswith('h'):  # h 这里为n维球坐标的标识
            format_spec = format_spec[:-1]
            # 使用 itertools.chain 函数生成生成器表达式，无缝迭代向量的模和各个角坐标。
            coords = itertools.chain([abs(self)], self.angles())
            out_fmt = '<{}>'  # 使用尖括号显示球面坐标
        else:
            coords = self
            out_fmt = '({})'  # 使用圆括号显示笛卡儿坐标
        components = (format(c, format_spec) for c in coords)
        return out_fmt.format(', '.join(components))

    @classmethod
    def frombytes(cls, b):
        type_code = chr(b[0])
        memv = memoryview(b[1:]).cast(type_code)
        # 因为直接传入序列（components），把 memoryview 传给构造方法，不用像前面那样使用 * 拆包。
        return cls(memv)


if __name__ == '__main__':
    # v = Vector([1, 2, 3, 4])
    # print(format(v))
    # print(format(v, 'h'))
    # (1.0, 2.0, 3.0, 4.0)
    # <5.477225575051661, 1.387192316515978, 1.1902899496825317, 0.9272952180016122>

    # v2 = Vector(range(5))
    # print(format(v2))
    # print(format(v2, '.2f'))
    # print(format(v2, '.3eh'))
    # print(format(v2, '.5fh'))
    # (0.0, 1.0, 2.0, 3.0, 4.0)
    # (0.00, 1.00, 2.00, 3.00, 4.00)
    # <5.477e+00, 1.571e+00, 1.387e+00, 1.190e+00, 9.273e-01>
    # <5.47723, 1.57080, 1.38719, 1.19029, 0.92730>

    print(hash(Vector([1, 3])))  # 2
    print(hash(Vector([3.1, 4.2])))  # 384307168202284039
    print(hash(Vector(range(6))))  # 1

