import datetime
import os

from Cities import City
from Products import Products

MENU_SEPARATOR = '---------------------------'
GAME_START = 'Let the games begin!!'


class GameManager:
    def __init__(self, cash, debt, guns, shiphold):
        self.firm_name
        self.cash = cash
        self.debt = debt
        self.guns = guns
        self.bank = 0
        self.cost=0
        self.shiphold = 60
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
        date = date + datetime.timedelta(days=30)
        return city_list[int(selected_city) - 1], date

    def sell(self):
        input('what would you like to sell?\n')

    def buy(self):
        selection_buy = input('What would you like to buy 1-{}/ C)ancel\n'.format(str(len(Products.products))))
        product_to_buy = Products.products[int(selection_buy) - 1]
        print('you can afford {}'.format(self.balance_cash(product_to_buy.price)))
        if selection_buy == 'C':
            return
        if product_to_buy == 3 or product_to_buy == 4:
            quantity = input('How much {} would you like?\n'.format(product_to_buy.name))
        else:
            quantity = input('How many {} would you like\n'.format(product_to_buy.name))
        self.cost = product_to_buy.price * int(quantity)
        print('it will cost {}'.format(self.cost))

        answer = input('buy? y/n\n')
        if answer == 'y' or answer == 'Y':
            self.account_withdrawl(quantity)

    def account_withdrawl(self, quantity):
            self.cash =self.cash - self.cost
            self.shiphold= self.shiphold- int(quantity)



    def balance_cash(self, product):
        balance = self.cash // product
        return balance

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
            print('Hold: {}'.format(self.shiphold))
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
                print('LEAVING PORT')
            elif new_option == 'S'.lower():
                self.sell()
            elif new_option == 'B'.lower():
                self.buy()
                # self.account_withdrawl()
            elif new_option == 'V'.lower() and game.current_city.has_bank:
                self.visit_bank()
            elif new_option == 'T'.lower():
                self.transfer_warehouse()
            elif new_option == 'Q'.lower():
                print('See you around')
                game_running = False


game = GameManager(400, 1000, 5, 100)
