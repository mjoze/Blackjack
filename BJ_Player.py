import BJ_Hand
import Player


class BJ_Player(BJ_Hand.BJ_Hand):
    def is_hitting(self):
        response = Player.Player.ask_yes_no('\n' + self.name + ", chcesz dobrać kartę? (T/N)")
        return response == 't'

    def bust(self):
        print(self.name, 'ma furę.')
        self.lose()

    def lose(self):
        print(self.name, 'przegrywa.')

    def win(self):
        print(self.name, 'wygrywa')

    def push(self):
        print(self.name, 'remisuje')