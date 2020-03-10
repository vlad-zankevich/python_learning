__author__ = 'vlad'


def test_number():
    assert 2 + 2 == 4


def addition_calculating(x, y):
    result = x + y
    return result


def test_addition_calculating():
    assert addition_calculating(2, 2) == 4


string = "Hello World!"


def test_string_name():
    assert string == "Hello World!"


def string_concatenation(string_1, string_2):
    result = string_1 + string_2
    return result


def test_string_concatenation():
    assert string_concatenation("Hello ", "World!") == "Hello World!"

