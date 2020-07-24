class City:
    cities = []

    def __init__(self, name, has_bank, has_warehouse):
        self.name = name
        self.has_bank = has_bank
        self.has_warehouse = has_warehouse
        self.warehouse = 10000


    @classmethod
    def create_cities(cls):
        cls.cities.append(City('>Hong Kong<', True, True))
        cls.cities.append(City('>Shanghai<', False, False))
        cls.cities.append(City('>Taipei<', False, False))


