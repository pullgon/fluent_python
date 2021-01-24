# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/24 23:53
# Description:


class Vector2d:
    """Vector2d 类的第二版，x 和 y 是只读属性"""

    def __init__(self, x, y):
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    def __iter__(self):
        return (i for i in (self.x, self.y))

    ...


if __name__ == '__main__':
    a = Vector2d(1, 2)
    print(a.x)
