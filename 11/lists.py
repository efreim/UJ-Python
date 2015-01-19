# coding=utf-8
import random
import math


def random_list(n):
    my_list = []
    for item in range(0, n):
        my_list.insert(random.randint(0, n - 1), item)
    return my_list


def almost_sorted_list(n):
    my_list = []
    for item in range(0, n):
        if item % 3 == 0:
            my_list.insert(item, item)
            tmp = my_list[item]
            my_list[item] = my_list[item - 1]
            my_list[item - 1] = tmp
        else:
            my_list.insert(item, item)
    return my_list


def almost_sorted_reversed_list(n):
    my_list = []
    for item in range(0, n):
        if item % 3 == 0:
            my_list.insert(item, item)
            tmp = my_list[item]
            my_list[item] = my_list[item - 1]
            my_list[item - 1] = tmp
        else:
            my_list.insert(item, item)
    reversed_list = my_list[::-1]
    return reversed_list


def gauss_list(n):
    my_list = []
    for item in range(0, n):
        my_list.append(int(random.gauss(2, 4)))
    return my_list


def random_repeated_list(n):
    my_list = []
    k = int(math.sqrt(n))
    for item in range(0, n):
        my_list.append(random.randint(0, k))
    return my_list
