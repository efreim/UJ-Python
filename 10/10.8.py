# coding=utf-8
"""Stworzyć ADT w postaci kolejki losowej, z której elementy
będą pobierane w losowej kolejności. Zadbać o to, aby każda
operacja była wykonywana w stałym czasie, niezależnie od liczby
elementów w kolejce."""
from random import randrange


class RandomQueue:
    def __init__(self, size):
        self.items = (size + 1) * [None]  # utworzenie tablicy
        self.n = 0  # liczba elementów
        self.size = (size + 1)

    def insert(self, data):
        if self.is_full():
            raise IndexError("Kolejka przepelniona, nie mozna niczego dodac")
        else:
            self.items[self.n] = data
            self.n += 1

    def remove(self):  # zwraca losowy element
        if self.is_empty():
            raise IndexError("Kolejka pusta, nie mozna niczego usunac")
        else:
            random_index = randrange(0, self.n)
            print "\nWylosowany element: ", random_index
            self.items[random_index] = None
         #   self.clean_queue(random_index)

#    def clean_queue(self, data):
#        for item in range(data, self.n):
#            self.items[item] = self.items[item + 1]
#        self.n -= 1

    def is_empty(self):
        return self.n == 0

    def is_full(self):
        return self.size == self.n

    def print_stack(self):
        print
        for item in range(0, self.n):
            print "Indeks: %s  Wartosc: %s " % (item, self.items[item])


rQueue = RandomQueue(10)
for i in range(0, 10):
    rQueue.insert(i)

rQueue.print_stack()
rQueue.remove()
rQueue.print_stack()
