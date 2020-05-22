import datetime
import os

from game_02_content import visit_bank, leave_port, sell, buy, transfer_warehouse, cities, current_city

MENU_SEPARATOR = '---------------------------'
GAME_START = 'Let the games begin!!'
Date = datetime.date(1850, 4, 13)


def welcome():
    print('Taipan! Welcome')


def firm_name():
    firm_name = input('What will you name your firm? \n')
    return firm_name


def start_option():
    starting_option = input(
        'would you like to start...\n 1) With cash (and a debt)\n >>or<<\n 2) Five guns and no cash...\n')

    if starting_option == '1':
        cash = 400
        debt = cash
        guns = 0

    else:
        cash = 0
        guns = 5
        debt = cash
    return cash, debt, guns


# GAME START
welcome()
firm_name = firm_name()
cash, debt, guns = start_option()
print('\n' * 10)
while True:
    os.system('cls')
    # MAIN GAME INTERFACE
    print(MENU_SEPARATOR)
    print(GAME_START)
    print(MENU_SEPARATOR)

    print('Firm: {}'.format(firm_name))
    print('Date: {}'.format(Date))
    print(current_city['name'])
    print('cash: {}\ndebt: {}\nguns: {}'.format(cash, debt, guns))
    print(MENU_SEPARATOR)

    has_bank = ''
    if current_city['has_bank']:
        has_bank = 'V)isit Bank'
        print('WHAT WILL YOU CHOSE NEXT?\nL)eave Port\nS)ell\n{}\nB)uy\nT)ransfer Bank\nQ)uit'.format(has_bank))
    else:
        print('WHAT WILL YOU CHOSE NEXT?\nL)eave Port\nS)ell\nV)isit Bank\nB)uy\nT)ransfer Bank\nQ)uit')
    print(MENU_SEPARATOR)
    new_option = input('enter the next step of your journey\n')

    if new_option == 'L'.lower():
        current_city = leave_port(cities)
    elif new_option == 'S'.lower():
        sell()
    elif new_option == 'B'.lower():
        buy()
    elif new_option == 'V'.lower() and current_city['has bank']:
        visit_bank()
    elif new_option == 'T'.lower():
        transfer_warehouse()
    elif new_option == 'Q'.lower():
        print('See you around')
        break

