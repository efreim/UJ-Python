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

    def is_empty(self):
        return self.head == self.tail

    def is_full(self):
        return (self.head + self.n - 1) % self.n == self.tail

    def put(self, data):
        try:
            if self.is_full():
                raise IndexError
            else:
                self.items[self.tail] = data
                self.tail = (self.tail + 1) % self.n
        except IndexError:
            print "Kolejka pelna, nie mozna niczego dodac!"

    def get(self):
        try:
            if self.is_empty():
                raise IndexError
            else:
                data = self.items[self.head]
                self.items[self.head] = None  # usuwam referencję
                self.head = (self.head + 1) % self.n
                return data
        except IndexError:
            print "Kolejka pusta, nie mozna niczego usunac"

    def print_queue(self):
        for item in range(self.head, self.n):
            if self.items[item] is not None:
                print self.items[item]
            elif self.is_empty():
                print "Kolejka pusta"
                return


que = Queue()
que.put(4)
que.put(2)
que.get()

que.put(1)
que.put(6)
que.put(3)

que.print_queue()
print
print "Dodaje wartosc wykraczajaca poza rozmiar kolejki"
que.put(9)
que.put(10)

print
print "Usuwam wartosc z pustej kolejki"
new_que = Queue()
new_que.get()
