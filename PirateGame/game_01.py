import datetime
import os
from game_02_content import leave_port, sell, buy, transfer_bank
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
    print('cash: {}\ndebt: {}\nguns: {}'.format(cash, debt, guns))
    print(MENU_SEPARATOR)
    print('WHAT WILL YOU CHOSE NOW?:\nL)eave Port\nS)ell\nB)uy\nV)isit the Money Lender\nT)ransfer Bank\nQ)uit')
    new_option = input('enter the next step of your journey')

    if new_option == 'L'.lower():
        leave_port()
    elif new_option == 'S'.lower():
        sell()
    elif new_option == 'B'.lower():
        buy()
    elif new_option == 'T'.lower():
        transfer_bank()
    elif new_option == 'Q'.lower():
        break
