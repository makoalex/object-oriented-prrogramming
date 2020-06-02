from random import randint


class Products:
    products = []

    def __init__(self, name, minprice, maxprice):
        self.name = name
        self.minprice = minprice
        self.maxprice = maxprice
        self.price = randint(self.minprice, self.maxprice)
        # Products.products.append(self)

    @classmethod
    def create_products(cls):
        Products.products.append(Products(' Basic Good', 5, 20))
        Products.products.append(Products(' Arms', 30, 105))

    def display_products(self):
        for product in self.products:
            print('Product name: {}-- Product price: {}--'.format(product.name, product.price))


