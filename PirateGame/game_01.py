import os

print('Taipan! Welcome')
firm_name = input('What will you name your firm? \n')
print('Firm: {}'.format(firm_name))
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
os.system('cls')
print('\n'*90)
print('---------------------------')
print('Let the games begin!!')
print('---------------------------')
print('cash: {}\ndebt: {}\nguns: {}'.format(cash, debt, guns))
