# coding=utf-8
import math


def heron(a, b, c):
    """Obliczanie pola powierzchni trójkąta za pomocą wzoru
    Herona. Długości boków trójkąta wynoszą a, b, c."""
    if (a + b) < c or (a + c) < b or (b + c) < a:
        raise ValueError('Dlugosci bokow nie spelnianiaja warunku trojkata')
    else:
        print math.sqrt((a + b + c) * (a + b - c) * (a - b + c) * (-a + b + c)) / 4.0


heron(4, 5, 6)
heron(3,3,3)