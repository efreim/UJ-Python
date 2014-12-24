# coding=utf-8
"""Mamy listę jednokierunkową bez klasy SingleList.
Napisać funkcje find_max() i find_min(), które
znajdują odpowiednio element największy i najmniejszy
na liście, a następnie zwracają ten element.
"""
import sys

class Node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)


def print_list(node):
    next = node.next
    print node.data
    if next is not None:
        print_list(next)


def find_max(node):
    n_max = -sys.maxint
    current = node
    while current is not None:
        next = current.next
        val = current.data
        current = next
        if n_max < val:
            n_max = val

    return n_max

def find_min(node):
    n_min = sys.maxint
    current = node
    while current is not None:
        next = current.next
        val = current.data
        current = next
        if n_min > val:
            n_min = val

    return n_min

head = None                   # [], pusta lista
head = Node(3, head)          # [3]
head = Node(2, head)          # [2, 3]
head = Node(4, head)          # [4, 2, 3]
head = Node(9, head)          # [9, 4, 2, 3]
head = Node(5, head)          # [5, 9, 4, 2, 3]


print_list(head)
print "max ", find_max(head)
print "min ", find_min(head)