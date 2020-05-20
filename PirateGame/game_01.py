MENU_SEPARATOR = '---------------------------'
GAME_START = 'Let the games begin!!'


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
# MENU START
print(MENU_SEPARATOR)
print(GAME_START)
print(MENU_SEPARATOR)

print('Firm: {}'.format(firm_name))
print('cash: {}\ndebt: {}\nguns: {}'.format(cash, debt, guns))
