from random import randint



class Products:
    products = []

    def __init__(self, name, minprice, maxprice):
        self.city_products = []
        self.name = name
        self.minprice = minprice
        self.maxprice = maxprice
        self.price = randint(self.minprice, self.maxprice)
        self.product_quantity = 0

        # Products.products.append(self)

    @classmethod
    def create_products(cls):
        Products.products.append(Products('Basic Goods', 10, 25))
        Products.products.append(Products('Arms', 95, 180))
        Products.products.append(Products('Opium', 5000, 12000))
        Products.products.append(Products('Silk', 1250, 3300))



class CityProduct(Products):
    def __init__(self, city, product, name, minprice, maxprice):
        super().__init__(name, minprice, maxprice)
        self.city = city
        self.product = product
        self.price_pick()

    def price_pick(self):
        self.price = randint(self.minprice, self.maxprice)
        return self.price

    def display_products_prices(self):
        i = 1
        for product in self.products:
            print('{}. {}: Price: {}  //'.format(i, product.name, self.price_pick(product)), end="")

            i += 1

    def display_products_in_stock(self):
        i = 1
        for product in self.products:
            print('    {} {}-- Stock: {}'.format(i, product.name, product.product_quantity))
            i += 1

