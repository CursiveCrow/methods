"""Exact rational author calculations; not a manuscript regression suite."""
from fractions import Fraction as F

def nearest(value, base, precision):
    value = F(value)
    if not value:
        return value
    sign = 1 if value > 0 else -1
    value = abs(value)
    exponent = 0
    while value >= base:
        value /= base
        exponent += 1
    while value < 1:
        value *= base
        exponent -= 1
    scaled = value * base ** (precision - 1)
    integer = scaled.numerator // scaled.denominator
    remainder = scaled - integer
    integer += int(remainder > F(1, 2) or
                   (remainder == F(1, 2) and integer % 2))
    return sign * integer * F(base) ** (exponent - precision + 1)

if __name__ == '__main__':
    for base, precision in [(2, 3), (2, 4), (2, 5), (4, 3), (10, 3)]:
        failures = []
        for k in range(1, precision):
            multiplier = base ** k + 1
            for x in range(base ** (precision - 1), base ** precision):
                t = nearest(multiplier * x, base, precision)
                s = nearest(t - x, base, precision)
                hi = nearest(t - s, base, precision)
                target = nearest(x, base, precision-k)
                if hi != target:
                    failures.append((k, x, t, s, hi, target))
                    break
        print('split', base, precision, failures[:4])
    u=F(1,200)
    print('triangle radicand factor', (1+2*u)**6*(1+u)**3,
          'bound', 1+16*u)
    print('area factor', (1+F(17,2)*u)*(1+u)**2, 'bound',1+11*u)
