# -*- encoding: utf-8 -*-
# @File    : demo.py
# @Time    : 2021/1/26 15:13
# @Author  : gq
# @Email   : qianguo@zjft.com
# @Software: PyCharm
# @Desc    : 
"""
    python如何实现单例模式?请写出两种实现方式?
"""
from functools import wraps


# 1.装饰器实现
def Singleton(cls):
    instance_dict = {}

    @synchronized
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instance_dict:
            instance_dict[cls] = cls(*args, **kwargs)
        return instance_dict[cls]

    return wrapper


# 第二种方法：使用基类 New 是真正创建实例对象的方法，所以重写基类的new 方法，
# 以此保证创建对象的时候只生成一个实例

class Singleton2:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super(Singleton2, cls).__new__(cls, *args, **kwargs)
        return cls._instance


"""
    线程安全的单例模式
"""
import threading


def synchronized(func):
    func.__lock__ = threading.Lock()

    def syn_func(*args, **kwargs):
        with func.__lock__:
            return func(*args, **kwargs)

    return syn_func

@Singleton
class Foo:
    pass


if __name__ == '__main__':
    f1 = Foo()
    f2 = Foo()
    print(f1 is f2)
