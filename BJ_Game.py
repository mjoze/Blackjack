import BJ_Player
import BJ_Dealer
import BJ_Deck
import Player


class BJ_Game(object):
    def __init__(self, names):
        self.players = []

        for name in names:
            player = BJ_Player.BJ_Player(name)
            self.players.append(player)

        self.dealer = BJ_Dealer.BJ_Dealer("Rozdający")
        self.deck = BJ_Deck.BJ_Deck()
        self.deck.populate()
        self.deck.shuffle()

    @property
    def still_playing(self):
        sp = []
        for player in self.players:
            if not player.is_busted():
                sp.append(player)
        return sp

    def __additional_cards(self, player):
        while not player.is_busted() and player.is_hitting():
            self.deck.deal([player])
            print(player)
            if player.is_busted():
                player.bust()

    def play(self):
        self.deck.deal(self.players + [self.dealer], per_hand=2)
        self.dealer.flip_first_card()
        for player in self.players:
            print(player)
        print(self.dealer)
        for player in self.players:
            self.__additional_cards(player)
        self.dealer.flip_first_card()
        if not self.still_playing:
            print(self.dealer)
        else:
            print(self.dealer)
            self.__additional_cards(self.dealer)
            if self.dealer.is_busted():
                for player in self.still_playing:
                    player.win()
            else:
                for player in self.still_playing:
                    if player.total > self.dealer.total:
                        player.win()
                    elif player.total < self.dealer.total:
                        player.lose()
                    else:
                        player.push()
        for player in self.players:
            player.clear()
        self.dealer.clear()


def main():
    print("\t\tWitaj w grze 'Blackjack'! \n")
    names = []
    number = Player.Player.ask_number(question="Podaj liczbę graczy (1 - 7): ", low=1, high=8)
    for i in range(number):
        name = input("Wprowadź nazwę gracza: ")
        names.append(name)
    print()

    game = BJ_Game(names)

    again = None
    while again != "n":
        game.play()
        again = Player.Player.ask_yes_no("\nCzy chcesz zagrać ponownie?: ")


if __name__ == '__main__':
    main()
    input("\n\nAby zakończyć program, naciśnij klawisz Enter")