import fractions
class Frac:

    def __init__(self, x=0, y=1):
        self.x = x
        self.y = y
        # Sprawdzamy, czy y=0.


    def __str__(self):
        if self.y == 1:
            return self.x
        else:
            return self.x/self.y

    def __repr__(self):        # zwraca "Frac(x, y)"
        return "Frac(%s, %s)" % (self.x, self.y)

    def com_den(self, other):
        common_denominator = (self.y * other.y) / fractions.gcd(self.y, other.y)
        self.x = self.x * (common_denominator / self.y)
        self.y = common_denominator
        other.x = other.x * (common_denominator / other.y)
        other.y = common_denominator


    def __cmp__(self, other):
        Frac.com_den(self, other)
        if self.x == other.x:
            return 0
        elif self.x > other.x:
            return 1
        else:
            return -1

    def __add__(self, other):
        # frac1+frac2, frac+int
        Frac.com_den(self, other)
        b = self.y
        a = self.x + other.x
        return Frac(a, b)

  #  __radd__ = __add__              # int+frac

    def __sub__(self, other):
        Frac.com_den(self, other)
        b = self.y
        a = self.x - other.x
        return Frac(a, b)

    def __rsub__(self, other):      # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(self.y * other - self.x, self.y)

    def __mul__(self, other):
        a = self.x * other.x
        b = self.y * other.y
        return Frac(a, b)

    __rmul__ = __mul__              # int*frac

    def __div__(self, other):
        a = self.x * other.y
        b = self.y * other.x
        return Frac(a, b)

    def __rdiv__(self, other): pass # int/frac

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