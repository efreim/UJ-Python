# coding=utf-8
"""Poprawić metodę get(), aby w przypadku pustej kolejki zwracała
wyjątek. Poprawić metodę put() w tablicowej implementacji kolejki,
aby w przypadku przepełnienia kolejki zwracała wyjątek. Napisać kod
testujący kolejkę."""


class Queue:
    def __init__(self, size=5):
        self.n = size + 1  # faktyczny rozmiar tablicy
        self.items = self.n * [None]
        self.head = 0  # pierwszy do pobrania
        self.tail = 0  # pierwsze wolne


    def __str__(self):
        return self.items


    def is_empty(self):
        return self.head == self.tail


    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail


    def put(self, data):
        if self.is_full():
            raise IndexError("Kolejka pelna, nie mozna niczego dodac!")
        else:
            self.items[self.tail] = data
            self.tail = (self.tail + 1) % self.n


    def get(self):
        if self.is_empty():
            raise IndexError("Kolejka pusta, nie mozna niczego usunac")
        else:
            data = self.items[self.head]
            self.items[self.head] = None  # usuwam referencję
            self.head = (self.head + 1) % self.n
            return data


    def print_queue(self):
        for item in range(self.head, self.n):
            if self.items[item] is not None:
                print self.items[item]
            elif self.is_empty():
                print "Kolejka pusta"
                return

