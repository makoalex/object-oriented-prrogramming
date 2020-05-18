"""refers to information hiding, giving access to only specific information to the user """


# reduces system complexity1 and increases robustness
class Base:
    def __private(self):
        print('private base method')

    def _protected(self):
        print('protected base method only')

    def public(self):
        print('public method ')
        self.__private()
        self._protected()


class Derived(Base):
    def __private(self):
        print('private derived method')

    def _protected(self):
        print('protected derived method')
        """the second _protected method, overrides the firs, because it is not private """


d = Derived()
d.public()
"""d.__private()
print(dir(d))
d._Derived__private()"""
# printing all of the above shows that private methods are protected from being overridden in the derived class
# this is called NAME MANGLING
