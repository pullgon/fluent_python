# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2020/12/24 1:20
# Description:


def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    return sum([item.total() * 0.1 for item in order.cart if item.quantity >= 20])


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    return order.total() * 0.07 if len([item.product for item in order.cart]) >= 10 else 0
