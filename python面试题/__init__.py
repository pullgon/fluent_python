# -*- encoding: utf-8 -*-
# @File    : __init__.py.py
# @Time    : 2021/1/26 9:39
# @Author  : gq
# @Email   : qianguo@zjft.com
# @Software: PyCharm
# @Desc    :
import weakref
import objgraph


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients

    def __repr__(self):
        return f'Pizza({self.ingredients!r})'

    @classmethod
    def margherita(cls):
        return cls(['mozzarella', 'tomatoes'])

    @classmethod
    def prosciutto(cls):
        return cls(['mozzarella', 'tomatoes', 'ham'])


if __name__ == '__main__':
    pass
