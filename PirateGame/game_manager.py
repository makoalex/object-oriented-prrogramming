import datetime
import os

from Cities import City
from Products import Products

MENU_SEPARATOR = '---------------------------'
GAME_START = 'Let the games begin!!'


class GameManager:
    def __init__(self, cash, guns, shiphold):
        self.firm_name
        self.cash = cash
        self.debt = cash
        self.guns = guns
        self.bank = 0
        self.shiphold = shiphold
        City.create_cities()
        Products.create_products()
        self.current_city = City.cities[0]
        self.date = datetime.datetime(1850, 4, 13)

    def firm_name(self):
        self.firm_name = input('What will you name your firm? \n')
        return self.firm_name

    def leave_port(self, city_list, date):
        i = 1
        for city in city_list:
            print('{}. {}'.format(i, city.name))
            i += 1
        selected_city = input('Where to matey?\n')
        date = date + datetime.timedelta(days=1)
        return city_list[int(selected_city) - 1], date

    def sell(self):
        input('what would you like to sell?\n')

    def buy(self):
        input('what would you like to buy\n')

    def transfer_warehouse(self):
        pass

    def visit_bank(self):
        pass

    def StartUp(self):
        game_running = True

        while game_running:
            os.system('cls')
            # MAIN GAME INTERFACE
            print(MENU_SEPARATOR)
            print(GAME_START)
            print(MENU_SEPARATOR)

            print('Firm: {}'.format(self.firm_name))
            print('Date: {:%B %d, %Y}'.format(game.date))
            print(game.current_city.name)
            print('cash: {}\ndebt: {}\nguns: {}'.format(game.cash, game.debt, game.guns))
            print('City Goods')
            Products.display_products(Products)

            print(MENU_SEPARATOR)

            has_bank = ''
            if game.current_city.has_bank:
                has_bank = 'V)isit Bank'
                print('WHAT WILL YOU CHOSE NEXT?\nL)eave Port\nS)ell\n{}\nB)uy\nT)ransfer Bank\nQ)uit'.format(has_bank))
            else:
                print('WHAT WILL YOU CHOSE NEXT?\nL)eave Port\nS)ell\nB)uy\nT)ransfer Bank\nQ)uit')
            print(MENU_SEPARATOR)
            new_option = input('enter the next step of your journey\n')
            if new_option == 'L'.lower():
                game.current_city, game.date = self.leave_port(City.cities, game.date)
            elif new_option == 'S'.lower():
                self.sell()
            elif new_option == 'B'.lower():
                self.buy()
            elif new_option == 'V'.lower() and game.current_city.has_bank:
                self.visit_bank()
            elif new_option == 'T'.lower():
                self.transfer_warehouse()
            elif new_option == 'Q'.lower():
                print('See you around')
                game_running = False


game = GameManager(400, 5, 100)
