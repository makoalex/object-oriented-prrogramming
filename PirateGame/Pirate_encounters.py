import random

import pyfiglet
import termcolor
from art import *


class Pirate:
    def __init__(self, game):
        self.game = game
        self.pirate_risk = 80
        self.pirate_strength = 10
        self.escape_chance = 35
        self.pirate_number = random.randint(1, self.pirate_strength)
        self.check_for_pirates()

    def check_for_pirates(self):
        result = random.randint(1, 101)
        if result <= self.pirate_risk:
            self.pirates_attack()

    def pirates_attack(self):
        print('******************')
        art_text =pyfiglet.figlet_format('PIRATES!!!', font='starwars')
        text = termcolor.colored(art_text, color='magenta', on_color='on_yellow', attrs=['blink'])

        print(text)
        fightingPirates = True
        while fightingPirates:
            print('There are {} prirates on our tail sir!'.format(self.pirate_number))
            print('We have {} cannons and our ship health is {} :'.format(self.game.guns, self.game.ship_health))
            print("")
            attack_option = input('What do you wish to do? : F)ight or R)un\n')
            if attack_option.lower() == 'r':
                if self.run():
                    fightingPirates = False
            if attack_option.lower() == 'f':
                self.fight()
            print('Press any key to continue')

    def run(self):
        answer = termcolor.colored('You try to run', color='green', on_color=None, attrs=None)
        print(answer)
        result = random.randint(1, 71)
        if result <= self.escape_chance:
            print(termcolor.colored('You escaped', color='green', on_color=None, attrs=None))
            return True
        else:
            print(termcolor.colored("You didnt't get away!", color='green', on_color=None, attrs=None))
            return False
    def fight(self):
        pass
