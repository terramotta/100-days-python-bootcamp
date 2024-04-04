# BlackJack Game

import random
import os
from art import logo

############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.

##############################################################


class Player():
    def __init__(self, name):
        self.hand = []
        self.score = 0
        self.name = name

    def auto_play(self):
        while self.score < 17:
            self.get_card()

    def get_card(self, num_cards=1):
        for _ in range(num_cards):
            card = random.choice([11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10])
            self.hand.append(card)
            self.score += card
            self.check_ace()

    def reset(self):
        self.hand = []
        self.score = 0

    def check_over_21(self):
        if self.score > 21:
            return True
        else:
            return False

    def check_under_21(self):
        if self.score < 21:
            return True
        else:
            return False

    def check_ace(self):
        if 11 in self.hand and self.check_under_21():
            self.hand[self.hand.index(11)] = 1
            self.score -= 10
            return True
        else:
            return False

    def show_hand(self):
        return self.hand

    def show_score(self):
        return self.score

    def __str__(self):
        return f"Sua mão: {self.show_hand()},\nPontuação: {self.show_score()}"


def get_input(prompt, input_list):
    while True:
        try:
            user_input = input(prompt).lower()
        except ValueError:
            print("Invalid input. Please try again.")
            continue
        if user_input in input_list:
            return user_input
        else:
            print("Invalid input. Please try again.")
            continue


def main():
    os.system('clear')
    print(logo)
    start_game = get_input(
        'Do you want to play a game of Blackjack? Type "y" or "n": ', ['y', 'n'])
    if start_game == 'n':
        exit("Goodbye!")

    os.system('clear')
    user_name = input("Enter your username: ").capitalize()

    player1 = Player(user_name)
    computer = Player('Computer')

    player1.get_card(2)

    computer.get_card(2)
    computer.auto_play()

    print(player1)
    print(f"Primeira carta do computador: {computer.show_hand()[0]}")

    while (get_input("\nDigite 'y' para receber outra carta, digite 'n' para parar: \n", ["y", "n"]) == 'y'):
        os.system('clear')
        player1.get_card()

        if player1.check_over_21() == True:
            break
        elif player1.check_under_21() == True:
            print(player1, '\n')
            continue
        else:
            break

    if player1.check_over_21():
        print(f"Você estourou!")
        print(player1, '\n')
        print(f"Computador: {computer.show_score()}")
        print("Computador venceu!")
    else:
        while computer.show_score() < 17:
            computer.get_card()
        print(f"\nVocê: {player1.show_score()}")
        print(f"Computador: {computer.show_score()}")
        if computer.check_over_21() or player1.show_score() > computer.show_score():
            print("\nVocê venceu!")
        elif player1.show_score() == computer.show_score():
            print("Empate!")
        else:
            print("\nComputador venceu!")


if __name__ == "__main__":
    main()
