class coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def distance(self, other):
        x_diff = self.x - other.x
        y_diff = self.y - other.y
        return (x_diff - y_diff)
    def __str__(self):
        return "<" + str(self.x) + "," + str(self.y) + ">"

c = coordinate(4, 3)
one = coordinate(4, 1)
print(c)
print(c.x)
print(c.distance(one))