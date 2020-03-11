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

    def area(self):
        result = 3.1415 * self.r * self.r
        return result

    def perimeter(self):
        abs_r = abs(self.r)
        result = 2 * 3.1415 * abs_r
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
        result = (2 * self.a) * (2 * self.a)
        return result

    def perimeter(self):
        abs_a = abs(self.a)
        result = abs_a * 8
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

    def area(self):
        abs_a = abs(self.a)
        abs_b = abs(self.b)
        result = (2 * abs_a) * (2 * abs_b)
        return result

    def perimeter(self):
        abs_a = abs(self.a)
        abs_b = abs(self.b)
        result = (abs_a + abs_b) * 4
        return result


