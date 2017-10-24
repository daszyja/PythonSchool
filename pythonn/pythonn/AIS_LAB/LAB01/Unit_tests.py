import pytest
from LAB_01 import *


def triangle_number(n):
    'Triangle number: for example 1th = 1, 2th = 1+2, 3th = 1+2+3'
    return (n * (n + 1)) / 2


def silnia(n):
    if n == 0:
        return 1
    else:
        return n * silnia(n - 1)


def avg_arith(tab):
    return sum(tab) / len(tab)


def test_func_1():
    assert one_a(11) == triangle_number(10)


def test_func_2():
    assert one_b(4) == silnia(3)


def test_func_2():
    assert one_c(9) == avg_arith([1, 2, 3, 4, 5, 6, 7, 8, 9])
