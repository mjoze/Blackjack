import Card


class Hand:
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ""
            for card in self.cards:
                rep += str(card) + " "
        else:
            rep = '<pusta>'
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)


my_hand = Hand()
print("\nWyświetlam zawartość mojej ręki przed dodaniem jakichkoliwek kart:")
print(my_hand)
my_hand.add(Card.card1)
my_hand.add(Card.card2)
my_hand.add(Card.card3)
my_hand.add(Card.card4)
my_hand.add(Card.card5)
print(my_hand)

your_hand = Hand()
my_hand.give(Card.card1, your_hand)
my_hand.give(Card.card2, your_hand)
print("\nPrzekazuje pierwsze dwie karty z mojej ręki do Twojej.")
print("--------------------------")
print("Twoja ręka:")
print(your_hand)
print("Moja ręka:")
print(my_hand)

my_hand.clear()
print("\nMoja ręka po usunięciu z niej kart:")
print(my_hand)
input("\n\nAby zakończyć program, naciśnij klawisz Enter")