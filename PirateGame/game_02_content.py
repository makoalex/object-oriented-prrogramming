import datetime
from Cities import City
# cities = (
#     {'name': 'Hong Kong', 'has_bank': True, 'has_warehouse': True},
#     {'name': 'Sanghai', 'has_bank': False, 'has_warehouse': True},
#     {'name': 'Taiwan', 'has_bank': False, 'has_warehouse': False}
# )


def leave_port(city_list, date):
    i = 1
    for city in city_list:
        print('{}. {}'.format(i, city.name))
        i += 1
    selected_city = input('Where to matey?\n')
    date = date + datetime.timedelta(days=1)
    return city_list[int(selected_city) - 1], date


def sell():
    input('what would you like to sell?\n')


def buy():
    input('what would you like to buy\n')


def transfer_warehouse():
    pass


def visit_bank():
    pass

#
# def current_city(name):
#     current_city = {'has_bank': True, 'has_warehouse': True, name: True}
