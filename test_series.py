from series import fibonacci, lucas, sum_series


def test_fibonacci_input0():
    actual = fibonacci(0)
    expected = 0
    assert actual == expected


def test_fibonacci_input1():
    actual = fibonacci(1)
    expected = 1
    assert actual == expected


def test_fibonacci_input7():
    actual = fibonacci(7)
    expected = 13
    assert actual == expected


def test_lucas_input0():
    actual = lucas(0)
    expected = 2
    assert actual == expected


def test_lucas_input1():
    actual = lucas(1)
    expected = 1
    assert actual == expected


def test_lucas_input7():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_sum_series_fibonacci():
    actual = sum_series(6, 0, 1)
    expected = 8
    assert actual == expected


def test_sum_series_lucas():
    actual = sum_series(7, 2, 1)
    expected = 29
    assert actual == expected
