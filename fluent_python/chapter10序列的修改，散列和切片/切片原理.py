# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/20 0:02
# Description:


class MySeq:
    def __getitem__(self, index):
        return index


if __name__ == '__main__':
    # s = MySeq()
    # print(s[1])  # 1
    # print(s[1:4])  # slice(1, 4, None)
    # print(s[1:4:2])  # slice(1, 4, 2)
    # print(s[1:4:2, 9])  # (slice(1, 4, 2), 9)
    # print(s[1:4:2, 7:9])  # (slice(1, 4, 2), slice(7, 9, None))
    #
    # print(dir(slice))

    # print(help(slice.indices))

    print(slice(None, 5, 2).indices(5))  # (0, 5, 2)
    print(slice(-3, None, None).indices(5))  # (2, 5, 1)
