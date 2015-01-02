# coding=utf-8

"""
Poprawić implementację tablicową stosu tak, aby korzystała
z wyjątków w przypadku pojawienia się błędu. Metoda pop() ma
zgłaszać błąd w przypadku pustego stosu. Metoda push() ma
zgłaszać błąd w przypadku przepełnienia stosu. Napisać kod
testujący stos.
"""


class Stack:
    def __init__(self, size=6):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów na stosie
        self.size = size

    def __str__(self):
        return self.items

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        if self.is_full():
            raise IndexError("Stos przepelniony, nie mozna niczego dodac")
        else:
            self.items[self.n] = data
            self.n += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Stos pusty, nie mozna niczego usunac")
        else:
            self.n -= 1
            data = self.items[self.n]
            self.items[self.n] = None  # usuwam referencję
            return data
        print "Stos pusty, nie mozna niczego usunac"

    def print_stack(self):
        for item in range(0, self.n):
            print self.items[item]

