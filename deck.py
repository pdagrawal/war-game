from card import Card
import random

class Deck:
    def __init__(self):
        self.all_cards = []
        for suit in Card.suits:
            for rank in Card.ranks:
                self.all_cards.append(Card(suit, rank))

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()
