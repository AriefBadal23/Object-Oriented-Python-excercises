class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color = 'black'
        # some more methods


class PointWithSlots():
    # Defines slots for only two instances variables
    __slots__ = ['x', 'y']

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.color= 'black'
        print(x, y)


point1 = Point(10,10)
point2 = PointWithSlots(10,10)
