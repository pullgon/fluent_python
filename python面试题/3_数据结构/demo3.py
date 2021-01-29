# -*- encoding: utf-8 -*-
# @File    : demo3.py
# @Time    : 2021/1/26 13:58
# @Author  : gq
# @Email   : qianguo@zjft.com
# @Software: PyCharm
# @Desc    : 
"""
    字典推导式
"""
# d = {k: v for (k, v) in iterable}

"""
    字符串反转
"""
# print(a[::-1])

"""
    8.将字符串 "k:1 |k1:2|k2:3|k3:4"，处理成字典 {k:1,k1:2,...}
"""
# if __name__ == '__main__':
#     s = "k:1 |k1:2|k2:3|k3:4"
#     d = {k: v for e in s.split("|") for k, v in (e.split(":"),)}
#     print(d)

"""
    请按alist中元素的age由大到小排序
"""
# if __name__ == '__main__':
#     alist = [{'name': 'a', 'age': 20}, {'name': 'b', 'age': 30}, {'name': 'c', 'age': 25}]
#     a = sorted(alist, key=lambda x: x["age"], reverse=True)
#     print(alist)
#     print(a)

"""
    下面代码的输出结果将是什么？
"""
# if __name__ == '__main__':
#     list = ['a', 'b', 'c', 'd', 'e']
#     print(list[10:])


"""
    写一个列表生成式，产生一个公差为11的等差数列
"""
# if __name__ == '__main__':
#     a = [e * 11 for e in range(10)]
#     print(a)

"""
    给定两个列表，怎么找出他们相同的元素和不同的元素？
"""
# if __name__ == '__main__':
#     list1 = [1, 2, 3]
#     list2 = [3, 4, 5]
#     set1 = set(list1)
#     set2 = set(list2)
#     print(set1 & set2)
#     print(set1 ^ set2)

"""
    请写出一段python代码实现删除list里面的重复元素？
"""
# if __name__ == '__main__':
#     a = [1, 2, 3, 3, 4]
#     a = list(set(a))
#     print(a)

"""
    python中内置的数据结构有几种？
    a. 整型 int、 长整型 long、浮点型 float、 复数 complex
    b. 字符串 str、 列表 list、 元祖 tuple
    c. 字典 dict 、 集合 set
    d. Python3 中没有 long，只有无限精度的 int
"""

"""
    反转一个整数，例如-123 --> -321
"""

# def int_reversed(a):
#     if -2147483648 < a < 2147483647:
#         a_str = str(a)
#         if a_str[0] == '-':
#             a_str = a_str[1:][::-1]
#             return int(a_str) * -1
#         else:
#             a_str = a_str[::-1]
#             return int(a_str)
#     else:
#         return 0
#
#
# if __name__ == '__main__':
#     a = 10
#     print(int_reversed(a))

"""
    一行代码实现1-100之和
"""
# from functools import reduce

# if __name__ == '__main__':
    # a = reduce(lambda x, y: x + y, range(101))
    # a = sum(range(101))
    # print(a)
