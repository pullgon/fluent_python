# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2020/12/24 0:16
# Description:
import inspect
import promotions
from collections import namedtuple

Customer = namedtuple('Customer', 'name fidelity')


class LineItem:
    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:
    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion
        self.__total = 0

    def total(self):
        self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        discount = 0 if self.promotion is None else self.promotion(self)
        return self.total() - discount

    def __repr__(self):
        fmt = '<Order total: {:.2f}> due: {:.2f}'
        return fmt.format(self.total(), self.due())


def fidelity_promo(order):
    """为积分为1000或以上的顾客提供5%折扣"""
    return order.total() * 0.05 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order):
    """单个商品为20个或以上时提供10%折扣"""
    return sum([item.total() * 0.1 for item in order.cart if item.quantity >= 20])


def large_order_promo(order):
    """订单中的不同商品达到10个或以上时提供7%折扣"""
    return order.total() * 0.07 if len([item.product for item in order.cart]) >= 10 else 0


# promos = [v for k, v in globals().items() if k.endswith("_promo") and k != 'best_promo']

promos = [func for name, func in inspect.getmembers(promotions, inspect.isfunction)]


def best_promo(order):
    """选择最佳折扣"""
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    if __name__ == '__main__':
        # 两个顾客：joe 的积分是 0，ann 的积分是 1100。
        joe = Customer('John Doe', 0)
        ann = Customer('Ann Smith', 1100)

        # 有三个商品的购物车
        cart = [
            LineItem('banana', 4, 0.5),
            LineItem('apple', 10, 1.5),
            LineItem('watermelon', 5, 5.0),
        ]

        # banana_cart 中有 30 把香蕉和 10 个苹果
        banana_cart = [
            LineItem('banana', 30, 0.5),
            LineItem('apple', 10, 1.5),
        ]

        # long_order 中有 10 个不同的商品，每个商品的价格为 1.00
        Long_order = [LineItem(str(item), 1, 1.0) for item in range(10)]

        # 使用促销策略1
        print(Order(joe, cart, fidelity_promo))
        print(Order(ann, cart, fidelity_promo))
        # <Order total: 42.00> due: 42.00
        # <Order total: 42.00> due: 39.90

        # 使用促销策略2
        print(Order(joe, banana_cart, bulk_item_promo))
        # <Order total: 30.00> due: 28.50

        # 使用促销策略3
        print(Order(joe, Long_order, large_order_promo))
        print(Order(joe, cart, large_order_promo))
        # <Order total: 10.00> due: 9.30
        # <Order total: 42.00> due: 42.00

        # 最佳策略模式
        print(Order(joe, Long_order, best_promo))
        print(Order(joe, banana_cart, best_promo))
        print(Order(ann, cart, best_promo))
        # <Order total: 10.00> due: 9.30
        # <Order total: 30.00> due: 28.50
        # <Order total: 42.00> due: 39.90
