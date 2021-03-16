# -*- coding: utf-8 -*-
# Register your models here.

from django.contrib import admin

from .models import BookInfo, HeroInfo


# 自定义模型类
class BookInfoAdmin(admin.ModelAdmin):
    """图书模型自定义管理类"""

    list_display = ["id", "title", "pub_date"]


class HeroInfoAdmin(admin.ModelAdmin):
    """图书模型自定义管理类"""

    list_display = ["id", "name", "age", "gender", "comment", "hero_book"]


# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
