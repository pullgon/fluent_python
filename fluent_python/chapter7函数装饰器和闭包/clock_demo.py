# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2020/12/24 22:35
# Description:

import time

DEFAULT_FMT = '[{elapsed:0.8f}s] {name}({args}) -> {result}'


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*args, **kwargs):
            t0 = time.perf_counter()
            result = func(*args, **kwargs)
            elapsed = time.perf_counter() - t0
            name = func.__name__
            arg_lst = []
            if args:
                arg_lst.append(', '.join(repr(arg) for arg in args))
            if kwargs:
                pairs = ['{}={}'.format(k, v) for k, v in sorted(kwargs.items())]
                arg_lst.append(', '.join(pairs))
            arg_str = ', '.join(arg_lst)
            # 这里使用 **locals() 是为了在 fmt 中引用 clocked 的局部变量。
            print(fmt.format(**locals()))
            # print('[%0.8fs] %s(%s) -> %r' % (elapsed, name, arg_str, result))
            return result

        return clocked

    return decorate


@clock(fmt='{name}({args}) dt={elapsed:0.3f}s')
def snooze(seconds):
    time.sleep(seconds)


if __name__ == '__main__':
    for i in range(3):
        snooze(0.123)
        # snooze((0.123,)) dt=0.123s
        # snooze((0.123,)) dt=0.123s
        # snooze((0.123,)) dt=0.123s
