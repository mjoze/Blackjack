class Card:
    RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]

    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


card1 = Card('A', "c")
card2 = Card('5', "d")
card3 = Card('4', "h")
card4 = Card('3', "h")
card5 = Card('2', "s")

print(card1)
print(card2)
print(card3)
print(card4)
print(card5)