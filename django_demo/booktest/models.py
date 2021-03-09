# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/3/7 2:56
# Description: Create your models here.

from django.db import models


class BookInfo(models.Model):
    """图书模型类"""
    # 图书名称
    title = models.CharField(max_length=20)  # 字符串，最大长度为20
    # 出版日期
    pub_date = models.DateField()
