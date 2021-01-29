# -*- encoding: utf-8 -*-
# @File    : demo1.py
# @Time    : 2021/1/26 10:44
# @Author  : gq
# @Email   : qianguo@zjft.com
# @Software: PyCharm
# @Desc    : 
"""
    输入日期， 判断这一天是这一年的第几天？
"""
import datetime


def day_of_year(format_date):
    """
    :param format_date: 2021-01-11 11:00:00
    :return: str
    """
    year = int(format_date[:4])
    month = int(format_date[format_date.index("-") + 1:format_date.rindex("-")])
    day = int(format_date[format_date.rindex("-") + 1:format_date.index(" ")])
    print(year, month, day)
    date1 = datetime.date(year=year, month=month, day=day)
    date2 = datetime.date(year=year, month=1, day=1)
    return (date1 - date2).days + 1

if __name__ == '__main__':
    date = '2021-02-18 12:00:00'
    days = day_of_year(date)
    print(days)