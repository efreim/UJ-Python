# coding=utf-8
class Rectangle:
    def __init__(self, x1=0, y1=0, x2=0, y2=0):
        if x1 > x2 or y1 > y2:
                raise ValueError("Lewy dolny rog musi miec mniejsze wsplorzedne od prawego gornego rogu")
        else:
            self.pt1 = Point(x1, y1)
            self.pt2 = Point(x2, y2)

    def __str__(self):
        return "[(%s, %s),(%s, %s)]" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __repr__(self):
        return "Rectangle(%s, %s, %s, %s" % (self.pt1.x, self.pt1.y, self.pt2.x, self.pt2.y)

    def __eq__(self, other):
        return self.pt1 == other.pt1 and self.pt2 == other.pt2

    def __ne__(self, other):
        return not self == other

    def center(self):
        return Point(float(self.pt2.x + self.pt1.x) / 2, float(self.pt2.y + self.pt1.y) / 2).__str__()

    def area(self):
        return (self.pt2.x - self.pt1.x) * (self.pt2.y - self.pt1.y)

    def move(self, x, y):
        self.pt1.x += x
        self.pt1.y += y
        self.pt2.x += x
        self.pt2.y += y
        return self.__str__()

    def intersection(self, other):
        # część wspólna prostokątów
        if self == other:
            return self
        if self.pt1.x < other.pt1.x and self.pt1.y >= other.pt1.y and self.pt2.x < other.pt2.x and self.pt2.y >= other.pt2.y:
            return Rectangle(other.pt1.x, self.pt1.y, self.pt2.x, other.pt2.y)
        elif self.pt1.x <= other.pt1.x and self.pt1.y < other.pt1.y and self.pt2.x <= other.pt2.x and self.pt2.y < other.pt2.y:
            return Rectangle(other.pt1.x, other.pt1.y, self.pt2.x, self.pt2.y)
        elif self.pt1.x > other.pt1.x and self.pt1.y <= other.pt1.y and self.pt2.x > other.pt2.x and self.pt2.y <= other.pt2.y:
            return Rectangle(self.pt1.x, other.pt1.y, other.pt2.x, self.pt2.y)
        elif self.pt1.x >= other.pt1.x and self.pt1.y > other.pt1.y and self.pt2.x >= other.pt2.x and self.pt2.y > other.pt2.y:
            return Rectangle(self.pt1.x, self.pt1.y, other.pt2.x, other.pt2.y)

    def cover(self, other):
    # prostąkąt nakrywający oba
        if self == other:
            return self
        if self.pt1.x <= other.pt1.x and self.pt1.y <= other.pt1.y and self.pt2.x <= other.pt2.x and self.pt2.y <= other.pt2.y:
            return Rectangle(self.pt1.x, self.pt1.y, other.pt2.x, other.pt2.y)
        elif self.pt1.x >= other.pt1.x and self.pt1.y >= other.pt1.y and self.pt2.x >= other.pt2.x and self.pt2.y >= other.pt2.y:
            return Rectangle(other.pt1.x, other.pt1.y, self.pt2.x, self.pt2.y)

    def make4(self):
    # zwraca listę czterech mniejszych
        return [Rectangle(self.p1.x, self.p1.y, self.center().x, self.center().y),
                Rectangle(self.center().x, self.center().y, self.p2.x, self.p2.y),
                Rectangle(self.p1.x, self.center().y, self.center().x, self.p1.y),
                Rectangle(self.center().x, self.p1.y, self.p2.x, self.center().y)]

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return "(%s, %s)" % (self.x, self.y)

    def __repr__(self):
        return "Point(%s, %s)" % (self.x, self.y)

    def __eq__(self, other):
        return (self.x == other.x) and (self.y == other.y)

    def __ne__(self, other):
        return not self == other