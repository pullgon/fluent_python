# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/24 23:48
# Description:


class Vector2d:
    """Vector2d 类的第一版，x 和 y 是公开属性"""

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    ...
