import BJ_Hand


class BJ_Dealer(BJ_Hand.BJ_Hand):
    def is_hitting(self):
        return self.total < 17

    def bust(self):
        print(self.name, "ma furę.")

    def flip_first_card(self):
        first_card = self.cards[0]
        first_card.flip()

