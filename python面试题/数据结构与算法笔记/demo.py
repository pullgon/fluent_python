# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/2/23 0:23
# Description:

"""
    变位词问题：写一个bool函数，以两个词作为参数，返回这两个词是否为变位词
"""


def anagram_solution1(a, b):
    """逐字检查法 0(n)"""
    if len(a) != len(b) or not a or not b:
        return False
    temp = list(b)
    for i in a:
        try:
            temp.remove(i)
        except ValueError:
            return False
    return True


def anagram_solution2(a, b):
    """先排序后比较 o(nlogn)"""
    if len(a) != len(b) or not a or not b:
        return False
    if sorted(a) == sorted(b):  # 排序时间复杂度 o(nlogn)
        return True
    else:
        return False


if __name__ == '__main__':
    print(anagram_solution2('python', 'typhon'))
    a = 'python'
    print(sorted(a))
