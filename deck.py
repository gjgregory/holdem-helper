# Imports
from card import Card

# Class
class Deck:
    'Class containing information for contents of a card deck'
    cards = []

    def __init__(self):
        for i in range(0,13):
            for j in range(0,4):
                self.cards.append(Card(i, j))


