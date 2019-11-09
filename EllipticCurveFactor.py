from numtheory import *


class EllipticCurve:
    """elliptic curve y^2 = x^3 + ax + b over field Zp"""
    def __init__(self, a, b, p):
        assert gcd(4 * a ** 3 + 27 * b * b, p) != p and p % 2 and p % 3
        self.a = a
        self.b = b
        self.p = p

    def add(self, P, Q):    # P=(x1, y1), Q=(x2, y2)
        if P == ():
            return Q
        if Q == ():
            return P
        d = gcd(P[0] - Q[0], self.p)
        if d == 1:  # x1 != x2 (mod p)
            k = (P[1] - Q[1]) * ModRev(P[0] - Q[0], self.p) % self.p
            x = (k * k - P[0] - Q[0]) % self.p
            y = (k * (P[0] - x)- P[1]) % self.p
            return x, y
        elif d < self.p:    # d is a non-trivial factor of p
            print("%d = %d * %d" % (self.p, d, self.p//d))
            return None
        else:   # d = p, that is, x1 = x2 (mod p)
            d = gcd(P[1] + Q[1], self.p)
            if d == 1:  # y1 != -y2
                k = (3 * P[0] ** 2 + self.a) * ModRev(P[1] + Q[1], self.p)% self.p
                x = (k * k - P[0] - Q[0]) % self.p
                y = (k * (P[0] - x)- P[1]) % self.p
                return x, y
            elif d < self.p:  # d is a non-trivial factor of p
                print("%d = %d * %d" % (self.p, d, self.p//d))
                return None
            else:   # y1 = -y2
                return ()


ec = EllipticCurve(59, -59, 199843247)
P = (1, 1)
ret = ()
k = 16296
c, s = 1, 0
while k > 0:
    if k % 2:
        ret = ec.add(ret, P)
        s += c
        print("%dP=" % s, ret)
    k //= 2
    c = c * 2
    P = ec.add(P, P)
    #print("%dP=" % c, P)
    if ret is None or P is None:
        break
