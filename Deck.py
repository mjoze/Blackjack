import Card
import Hand
import random


class Deck(Hand.Hand):

    def populate(self):
        for suit in Card.Card.SUITS:
            for rank in Card.Card.RANKS:
                self.add(Card.Card(rank, suit))

    def shuffle(self):
        random.shuffle(self.cards)

    def deal(self, hands, per_hand=1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    print("Nie mogę dalej rozdawać. Zabrakło kart!")


