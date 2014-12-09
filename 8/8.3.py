# coding=utf-8
import math
import random

def calc_pi(n=100000):
    """Obliczanie liczby pi metodą Monte Carlo.
    n oznacza liczbę losowanych punktów."""
    inside = 0
    outside = 0
    for item in range(1, n):
        d = math.hypot(random.random(), random.random())
        if d <= 1:
            inside += 1
        outside += 1

    print 4.0* inside/outside

calc_pi()
