# coding=utf-8

"""
Poprawić implementację tablicową stosu tak, aby korzystała
z wyjątków w przypadku pojawienia się błędu. Metoda pop() ma
zgłaszać błąd w przypadku pustego stosu. Metoda push() ma
zgłaszać błąd w przypadku przepełnienia stosu. Napisać kod
testujący stos.
"""


class Stack:
    def __init__(self, size=10):
        self.items = size * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów na stosie
        self.size = size

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def push(self, data):
        try:
            if self.is_full():
                raise IndexError
            else:
                self.items[self.n] = data
                self.n += 1
        except IndexError:
            print "Stos przepelniony, nie mozna niczego dodac"

    def pop(self):
        try:
            if self.is_empty():
                raise IndexError
            else:
                self.n -= 1
                data = self.items[self.n]
                self.items[self.n] = None  # usuwam referencję
                return data
        except IndexError:
            print "Stos pusty, nie mozna niczego usunac"

    def print_stack(self):
        for item in range(0, self.n):
            print self.items[item]


stack = Stack()
stack.push(4)
stack.push(7)
stack.push(3)
stack.push(5)
stack.push(4)
stack.push(7)
stack.push(3)
stack.push(5)
stack.push(4)
stack.push(1)
stack.print_stack()
print
print "Dodaje wartosc wykraczajaca poza rozmiar stosu"
stack.push(2)

print
print "Usuwam wartosc z pustego stosu"
new_stack = Stack()
new_stack.pop()
