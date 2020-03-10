from geometry import Square


def test_square_constructor():
	s = Square(1, 5, 2, 12)

	assert s.x == 1
	assert s.y == 5
	assert s.a == 2
	assert s.angle == 12


def test_square_area():
	s = Square(1, 5, 2, 12)

	assert s.area() == 4
