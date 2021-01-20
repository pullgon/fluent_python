# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2020/12/24 22:41
# Description:

import time
from clock_demo import clock
from functools import lru_cache


@clock
def snooze(seconds):
    time.sleep(seconds)


@clock
def factorial(n):
    """n!"""
    return 1 if n < 2 else n * factorial(n - 1)


@lru_cache()
@clock
def fibonacci(n):
    """第 n 个斐波纳契数"""
    return n if n < 2 else fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    # print('*' * 40, 'Calling snooze(.123)')
    # snooze(0.123)
    # print('*' * 40, 'Calling factorial(6)')
    # print('6! =', factorial(6))
    # print(factorial.__name__, factorial.__doc__)
    print(fibonacci(10))
    # [0.00000030s] fibonacci(0) -> 0
    # [0.00000030s] fibonacci(1) -> 1
    # [0.00002620s] fibonacci(2) -> 1
    # [0.00000060s] fibonacci(3) -> 2
    # [0.00003850s] fibonacci(4) -> 3
    # [0.00000040s] fibonacci(5) -> 5
    # [0.00005040s] fibonacci(6) -> 8
    # [0.00000050s] fibonacci(7) -> 13
    # [0.00006270s] fibonacci(8) -> 21
    # [0.00000050s] fibonacci(9) -> 34
    # [0.00007570s] fibonacci(10) -> 55
    # 55
