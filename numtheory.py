"""this module contains some common number theory functions"""


def ModExpo(a, k, n):
    """return a^k mod n"""
    ret = 1
    while k > 0:
        if k % 2:
            ret = ret * a % n
        k //= 2
        a = (a * a) % n
    return ret


def isQuadRes(n, p):
    """return whether n is a quadratic residue modulo prime p or not"""
    if ModExpo(n, (p-1)//2, p) == 1:
        return True
    else:
        return False


def ModSqrt(a, p):
    """return the smaller square root of a modulo prime p"""
    a = a % p
    for x in range(p // 2 + 1):
        if x * x % p == a:
            return x
    return None


def gcd(a, b):
    """return gcd of two integers"""
    if b < 0:
        b = -b
    r = a % b
    while r:
        a = b
        b = r
        r = a % b
    return b


def ModRev(a, n):
    """return the reverse of a modulo n"""
    _n = n
    r = a % _n
    Q = []
    while r:
        Q.append(a // _n)
        a = _n
        _n = r
        r = a % _n
    if _n != 1:
        return None
    x, y = 0, 1
    while Q:
        t = x
        x = y
        y = t - Q.pop() * y
    return x % n

n = 65
L = []
for i in range(1, n):
    a = i * i % n
    if a not in L:
        L.append(a)
L.sort()
print(L)
print(L.__len__())

