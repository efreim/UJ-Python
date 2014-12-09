# coding=utf-8

def solve1(a, b, c):
    """Rozwiązywanie równania liniowego a x + b y + c = 0."""
    if a == 0:
        if b == 0:
            if c == 0:
                print "Rownanie tozsamosciowe"
            elif c != 0:
                print "Rownanie sprzeczne"
        elif b != 0:
                print "y = %s" % (float(-c/b))
    elif a != 0:
        if b != 0:
            print "y = %sx + (%s)" % (float(-a/b), float(-c/b))
        elif b == 0:
            print "x = %s" % (float(-c/a))


solve1(0.0,0.0,0.0)

solve1(0.0,0.0,3.0)

solve1(0.0,-2.0,5.0)
solve1(0.0,2.0,5.0)
solve1(0.0,-2.0,0.0)


solve1(3.0,-2.0,5.0)
solve1(3.0,2.0,5.0)
solve1(3.0,0.0,5.0)