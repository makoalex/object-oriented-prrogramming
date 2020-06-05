from game_manager import game


# current_city = City.cities[0]


def welcome():
    print('Taipan! Welcome')


def start_option():
    starting_option = input(
        'would you like to start...\n    1) With cash (and a debt)\n>>or<<\n    2) Five guns and no cash...\n')

    if starting_option == '1':
        game.cash = game.cash
        game.debt = game.debt
        game.guns = 0

    else:
        game.cash =0
        game.guns = game.guns
        game.debt = 0
    return game.cash, game.debt, game.guns


# GAME START
welcome()
firm_name = game.firm_name()
start_option()
game.StartUp()

print('\n' * 10)
