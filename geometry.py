__author__ = 'vlad'


class Point:
    def __init__(self, x, y):
        """'x' and 'y' are point coordinates"""
        self.x = x
        self.y = y


class Circle:
    def __init__(self, x, y, r):
        """'x' and 'y' are circle center coordinates and 'r' is a radius of a circle"""
        self.x = x
        self.y = y
        self.r = r

    def area(self, r):
        result = 3.1415 * r * r
        return result


class Square:
    def __init__(self, x, y, a, angle):
        """'x' and 'y' are square center of gravity coordinates,
        'a' is a length of the perpendicular from the center of gravity to the square side
        'angle' is the angle of the square to the vertical"""
        self.x = x
        self.y = y
        self.a = a
        self.angle = angle

    def area(self):
        result = self.a * self.a
        return result


class Rectangle:
    def __init__(self, x, y, a, b, angle):
        """'x' and 'y' are rectangle center of gravity coordinates,
        'a' is a length of the perpendicular from the center of gravity to the vertical rectangle side
        'b' is a length of the perpendicular from the center of gravity to the horizontal rectangle side
        'angle' is the angle of the rectangle to the vertical"""
        self.x = x
        self.y = y
        self.a = a
        self.b = b
        self.angle = angle

    def area(self, a, b):
        result = (2 * a) * (2 * b)
        return result


