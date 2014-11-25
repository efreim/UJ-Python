import fractions
class Frac:

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y

    def __str__(self):
        if self.y == 1:
            return self.x
        else:
            return self.x/self.y

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac(%s, %s)" % (self.x, self.y)

    @staticmethod
    def com_den(self, other):
        common_denominator = (self.y * other.y) / fractions.gcd(self.y, other.y)
        self.x = self.x * (common_denominator / self.y)
        self.y = common_denominator
        other.x = other.x * (common_denominator / other.y)
        other.y = common_denominator


    def __cmp__(self, other):
        self.com_den(self, other)
        if self.x == other.x:
            return 0
        elif self.x > other.x:
            return 1
        else:
            return -1

    def __add__(self, other):
        self.com_den(self, other)
        b = self.y
        a = self.x + other.x
        return Frac(a, b)

    def __sub__(self, other):
        self.com_den(self, other)
        b = self.y
        a = self.x - other.x
        return Frac(a, b)

    def __mul__(self, other):
        a = self.x * other.x
        b = self.y * other.y
        return Frac(a, b)

    def __div__(self, other):
        a = self.x * other.y
        b = self.y * other.x
        return Frac(a, b)

    def __pos__(self):
        return self

    def __neg__(self):
        return Frac(-self.x, self.y)

    def __invert__(self):
        return Frac(self.y, self.x)

    def is_positive(self):
        if (self.x > 0) & (self.y > 0) or (self.x < 0) & (self.y < 0):
            return True
        else:
            return False

    def is_zero(self):
        if self.x == 0:
            return True
        else:
            return False

    def frac2float(self):
        return float(self.x) / float(self.y)