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
        cls.cities.append(City('>Shanghai<', False, True))
        cls.cities.append(City('>Taipei<', False, False))





City.create_cities()
