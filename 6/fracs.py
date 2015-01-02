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
            return self.x / self.y

    def __repr__(self):  # zwraca "Frac(x, y)"
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
        if isinstance(other, Frac):
            Frac.com_den(self, other)
            return Frac(self.x + other.x, self.y)
        elif isinstance(other, int):
            return Frac(self.x + other * self.y, self.y)

    def __radd__(self, other):  # int+frac
        return Frac(other * self.y + self.x, self.y)


    def __sub__(self, other):
        if isinstance(other, Frac):
            Frac.com_den(self, other)
            return Frac(self.x - other.x, self.y)
        elif isinstance(other, int):  # frac - int
            return Frac(self.x - other * self.y, self.y)

    def __rsub__(self, other):  # int-frac
        # tutaj self jest frac, a other jest int!
        return Frac(other * self.y - self.x, self.y)

    def __mul__(self, other):
        if isinstance(other, Frac):
            return Frac(self.x * other.x, self.y * other.y)
        elif isinstance(other, int):
            return Frac(self.x * other, self.y)

    def __rmul__(self, other):  # int*frac
        return Frac(other * self.x, self.y)


    def __div__(self, other):

        if isinstance(other, Frac):
            if other.y == 0:
                raise ValueError("Nie dziel przez 0")
            return Frac(self.x * other.y, self.y * other.x)

        elif isinstance(other, int):
            if other == 0:
                raise ValueError("Nie dziel przez 0")
            return Frac(self.x, self.y * other)

    def __rdiv__(self, other):
        if self.x == 0:
            raise ValueError("Nie dziel przez 0")
        else:
            return Frac(other * self.y, self.x)


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