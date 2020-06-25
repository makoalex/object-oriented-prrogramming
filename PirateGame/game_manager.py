import datetime
import os

from Cities import City
from Products import Products, CityProduct

MENU_SEPARATOR = '---------------------------'
GAME_START = 'Let the games begin!!'


class GameManager:
    def __init__(self, cash, debt, guns, shiphold):
        self.firm_name
        self.cash = cash
        self.debt = debt
        self.guns = guns
        self.bank = 0
        self.cost = 0
        self.shiphold = 60
        self.current_shiphold = 0
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
        sell_selection = input('what would you like to sell?1- {} or C)ancel\n'.format(str(len(Products.products))))

        if sell_selection == 'C':
            return
        product_to_sell = Products.products[int(sell_selection) - 1]
        quantity_sell = int(input('How many pieces of {} would you like to sell?'.format(product_to_sell.name)))
        print('you can sell {}'.format(product_to_sell.product_quantity))
        if quantity_sell > product_to_sell.product_quantity:
            print(' You said {}. Not enough units in hold'.format(quantity_sell))
        else:
            self.sell_shiphold(product_to_sell, quantity_sell)
        self.stock_after_sell(product_to_sell, quantity_sell)

    def sell_shiphold(self, product_sell, quantity):
        total = product_sell.price * quantity
        self.cash += total
        print('Your transaction of {}'.format(total))
        self.shiphold += quantity

    def stock_after_sell(self, product, quantity):
        product.product_quantity -= quantity

    def buy(self):
        selection_buy = input('What would you like to buy? 1-{}/ C)ancel\n'.format(str(len(Products.products))))
        product_to_buy = Products.products[int(selection_buy) - 1]
        print('you can afford {}'.format(self.balance_cash(product_to_buy.price)))
        if selection_buy == 'C':
            return
        if product_to_buy == 3 or product_to_buy == 4:
            quantity = input('How much {} would you like?\n'.format(product_to_buy.name))
        else:
            quantity = input('How many {} would you like\n'.format(product_to_buy.name))

        available_space = self.check_freespace_in_shiphold(quantity)
        if available_space != quantity:
            print("Whooops! You don't have space for that much. You can buy: {}".format(available_space))

        self.cost = product_to_buy.price * int(available_space)
        print('it will cost {}'.format(self.cost))
        answer1 = input('buy? y/n\n')
        if answer1 == 'y' or answer1 == 'Y':
            self.account_withdrawl(available_space)
            self.stock(available_space, product_to_buy)

    def account_withdrawl(self, quantity):
        if self.cost > self.cash:
            print('Sorry not enough money')
            reply = (input('would you like to sell?\n y/n\n'))
            if reply == 'y':
                print(self.sell())
                answer = (input('Would you like to repurchase? y/N\n'))
                if answer == 'y':
                    print(self.buy())
        else:
            self.cash = self.cash - self.cost
            self.shiphold = self.shiphold - int(quantity)

    def debt_interest(self):
        interest_rate = 25 * self.debt // 100
        self.debt = self.debt + interest_rate
        return self.debt

    def check_freespace_in_shiphold(self, quantity):
        if self.current_shiphold + int(quantity) <= self.shiphold:
            return quantity
        else:
            return self.shiphold - self.current_shiphold

    def stock(self, quantity, product_bought):
        product_bought.product_quantity += int(quantity)
        for product in Products.products:
            print('{} {}'.format(product.name, product.product_quantity))

    def balance_cash(self, product):
        balance = self.cash // product
        return balance

    def transfer_warehouse(self):
        pass

    def visit_bank(self):
        pass

    # def pirate_bribe(self):
    #     if new_option == 'L' and

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
            CityProduct.display_products_in_stock(CityProduct)

            print('City Goods')
            CityProduct.display_products_prices(CityProduct)

            print(MENU_SEPARATOR)

            has_bank = ''
            if game.current_city.has_bank:
                has_bank = 'V)isit Bank'
                print('WHAT WILL YOU CHOSE NEXT?\nL)eave Port\nS)ell\n{}\nB)uy\nT)ransfer Bank\nQ)uit'.format(has_bank))
            else:
                print('WHAT WILL YOU CHOSE NEXT?\nL)eave Port\nS)ell\nB)uy\nT)ransfer Bank\nQ)uit')
            print(MENU_SEPARATOR)
            print('New prices available{}. Check the Market'.format(MENU_SEPARATOR))
            new_option = input('enter the next step of your journey\n')
            if new_option == 'L'.lower():
                game.current_city, game.date = self.leave_port(City.cities, game.date)
                self.debt_interest()
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


game = GameManager(1000, 1000, 5, 100)
