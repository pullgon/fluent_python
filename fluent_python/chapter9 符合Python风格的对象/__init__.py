# -*-coding:utf-8-*-
# Author: gq
# CreatDate: 2021/1/7 22:09
# Description:
import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    """扑克牌"""

    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, item):
        return self._cards[item]
