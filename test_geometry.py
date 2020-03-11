from geometry import Point
from geometry import Square
from geometry import Circle
from geometry import Rectangle
from pytest import approx


def test_square_constructor():
    s = Square(1, 5, 2, 12)

    assert s.x == 1
    assert s.y == 5
    assert s.a == 2
    assert s.angle == 12


def test_square_area():
    s = Square(1, 5, 2, 12)

    assert s.area() == 16


def test_circle_area():
    my_circle = Circle(5, 11, 3)

    assert my_circle.area() == approx(28.273, abs=0.001)


def test_rectangle_area():
    rect_s = Rectangle(7, -2, 3, 2, 0)

    assert rect_s.area() == 24


def test_negative_rectangle_area():
    negative_rect_s = Rectangle(15, 17, -5, 4, 0)

    assert negative_rect_s.area() == 80


def zero_circle_area():
    zero_circle = Circle(-7, -9, 0)

    assert zero_circle.area() == 0


def test_circle_perimeter():
    circle_p = Circle(2, 11, 5)

    assert circle_p.perimeter() == approx(31.415, abs=0.001)


def test_square_perimeter():
    square_p = Square(4, 20, 4, 0)

    assert square_p.perimeter() == 32


def test_rectangle_perimeter():
    rect_p = Rectangle(4, 20, 4, 6, 0)

    assert rect_p.perimeter() == 40


