# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/3/7 2:56
# Description: Create your models here.

from django.db import models


class BookInfo(models.Model):
    """图书模型类"""

    title = models.CharField(max_length=20, help_text="图书名称")  # 字符串，最大长度为20
    pub_date = models.DateField(help_text="出版日期")

    def __str__(self):
        return self.title


class HeroInfo(models.Model):
    """英雄人物类"""

    name = models.CharField(max_length=50, help_text="英雄名")
    age = models.IntegerField(help_text="英雄性别")
    # 0 为女， 1 为 男
    gender = models.IntegerField(help_text="英雄性别")
    comment = models.CharField(max_length=255, help_text="备注")
    hero_book = models.ForeignKey(
        "BookInfo", on_delete=models.CASCADE, related_name="book"
    )

    def __str__(self):
        return self.name
