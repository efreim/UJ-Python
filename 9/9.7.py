# coding=utf-8

"""
Mamy drzewo binarne bez klasy Binary Napisać funkcję count_leafs(top),
która liczy liście drzewa binarnego. Liście to węzły, które nie mają
potomków. Można podać rozwiązanie rekurencyjne lub rozwiązanie iteracyjne,
które jawnie korzysta ze stosu.

Załóżmy, że drzewo binarne przechowuje liczby. Napisać funkcję
calc_total(top), która podaje sumę liczb przechowywanych w drzewie.
"""


class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)


def print_btree_indented(top, level=0):
    if top is None: return
    print_btree_indented(top.right, level + 1)
    print "%s* %s" % ('   ' * level, top)
    print_btree_indented(top.left, level + 1)


def count_leafs(top):
    if (top.right or top.left) is None:
        return 1
    else:
        return count_leafs(top.left) + count_leafs(top.right)


def count_total(top):
    if top is None:
        return 0
    else:
        return top.data + count_total(top.left) + count_total(top.right)


root = None
root = Node("start")
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print
print_btree_indented(root, level=0)
print
print "Ilosc lisci drzewa binarnego: ", count_leafs(root)
print "Suma liczb przechowywanych w drzewie: ", count_total(root)


