import random

from Products import Products


class City:
    cities = []

    def __init__(self, name, has_bank, has_warehouse):
        self.name = name
        self.has_bank = has_bank
        self.has_warehouse = has_warehouse
        # City.cities.update({'name': self.name, 'has_bank': self.has_bank, 'has_warehouse': self.has_warehouse})

    @classmethod
    def create_cities(cls):
        cls.cities.append(City('>Hong Kong<', True, True))
        cls.cities.append(City('>Shanghai<', False, False))
        cls.cities.append(City('>Taipei<', False, False))




class CityProduct:
    def __init__(self, city, product):
        self.city = city
        self.product = product
        self.random_price_generator()

    def random_price_generator(self):
        self.price = random.randint(self.product.minprice, self.product.maxprice)

# City.create_cities()
