import math


class Circle:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r

    def Area(self):
        return math.pi * self.r * self.r
