"""expresses a has realtionship between a class known as a COMPOSITE- cometais an objct of another class known as a
COMPONENT """


# the composite class doesn't inherit the component's class interface but it can inherit its implementation

class Leg:
    pass


class Back:
    pass


class Chair:
    def __init__(self, num_legs):
        self.legs = [Leg() for leg in range(num_legs)]
        self.Back = Back()

    def __repr__(self):
        return 'i have {} legs and one  back'.format(self.legs)


print(Chair(5))
