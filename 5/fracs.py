import fractions


def com_den(frac1, frac2):
    common_denominator = (frac1[1] * frac2[1]) / fractions.gcd(frac1[1], frac2[1])
    frac1[0] = frac1[0] * (common_denominator / frac1[1])
    frac1[1] = common_denominator
    frac2[0] = frac2[0] * (common_denominator / frac2[1])
    frac2[1] = common_denominator


def add_frac(frac1, frac2):
    com_den(frac1, frac2)
    frac3 = [0, frac1[1]]
    frac3[0] = frac1[0] + frac2[0]
    return frac3


def sub_frac(frac1, frac2):
    com_den(frac1, frac2)
    frac3 = [0, frac1[1]]
    frac3[0] = frac1[0] - frac2[0]
    return frac3


def mul_frac(frac1, frac2):
    frac3 = [0, 0]
    frac3[0] = frac1[0] * frac2[0]
    frac3[1] = frac1[1] * frac2[1]
    return frac3


def div_frac(frac1, frac2):
    frac3 = [0, 0]
    frac3[0] = frac1[0] * frac2[1]
    frac3[1] = frac1[1] * frac2[0]
    return frac3


def cmp_frac(frac1, frac2):
    com_den(frac1, frac2)
    if frac1[0] > frac2[0]:
        return "+1"
    if frac1[0] < frac2[0]:
        return "-1"
    else:
        return "0"


def is_positive(frac):
    if (frac[0] > 0) & (frac[1] > 0) or (frac[0] < 0) & (frac[1] < 0):
        return True
    else:
        return False


def is_zero(frac):
    if frac[0] == 0:
        return True
    else:
        return False


def frac2float(frac):
    return float(frac[0]) / float(frac[1])