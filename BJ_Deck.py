import Deck
import BJ_Card


class BJ_Deck(Deck.Deck):
    def populate(self):
        for suit in BJ_Card.BJ_Card.SUITS:
            for rank in BJ_Card.BJ_Card.RANKS:
                self.cards.append(BJ_Card(rank, suit))
