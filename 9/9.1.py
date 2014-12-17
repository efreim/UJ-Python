# coding=utf-8
"""Mamy listę jednokierunkową bez klasy SingleList. Napisać funkcje remove_head()
 i remove_tail(), które usuwają początkowy lub końcowy węzeł. Funkcje powinny
 zwracać parę (new_head, data)."""

"""def remove_head(node): pass
def remove_tail(node): pass
# Zastosowanie.
while head:
    #head, data = remove_head(head)
    head, data = remove_tail(head)
    print "usuwam", data"""


class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)  # bardzo ogólnie

    def remove_head(self):  # algorytm klasy O(1)
        while head:
            head, data = remove_head(head)
            #head, data = remove_tail(head)
            print "usuwam", data


head = None
# pusta lista

head = Node("front")
# lista jednoelementowa

# Ręczne budowanie dłuższej listy.
head = None  # [], pusta lista
head = Node(3, head)  # [3]
print head
head = Node(2, head)  # [2, 3]
print head
head = Node(4, head)  # [4, 2, 3]
print head
head.remove_head()

"""
def remove_head(self):          # algorytm klasy O(1)
        if self.length == 0:
            raise ValueError("pusta lista")
        data = self.head.data
        self.head = self.head.next
        self.length = self.length - 1
        if self.length == 0:    # zabezpieczenie
            self.tail = None
        return data
        """