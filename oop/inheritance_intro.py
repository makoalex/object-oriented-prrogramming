class Decimal:
    def __init__(self, number, places):
        self.number = number
        self.places = places

    def __repr__(self):
        return '{:.{prec}f}'.format(self.number, prec=self.places)

    """as seen on https://pyformat.info/#number"""
    """return '%.2f' % self.number"""


# the 2f = the number of decimal places to follow the decimal point
# the % symbol is for getting the floating point
class Currency(Decimal):
    def __init__(self, country, symbol, number, places):
        super().__init__(number, places)
        self.country = country
        self.symbol = symbol

    def __repr__(self):
        """return '{:.{prec}f}{} {}'.format(self.number,  self.symbol, self.country, prec= self.places)"""
        return '{}{}: {}'.format(super().__repr__(), self.symbol, self.country)

print(Currency('UK','£', 23.567, 2))


# the Currency inherits from the Decimal class, but we  have to call the Parent class with all the parameters
#
print(Decimal(12.3473, 2))
