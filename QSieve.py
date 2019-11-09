from numtheory import *

pL = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
FB = []
N = 1059691
sqrt_N = int(N ** 0.5) + 1
print(sqrt_N)
for p in pL:
    if isQuadRes(N, p):
        FB.append(p)
print(FB)

A = 500
X = [(x + sqrt_N)**2 - N for x in range(A)]
print(X)
for p in FB:
    y = ModSqrt(N, p)
    x = (y - sqrt_N) % p
    for i in range(x, A, p):
        while X[i] %p == 0:
            X[i] //= p
    if p > 2:
         x = (-y - sqrt_N) % p
         for i in range(x, A, p):
             while X[i] %p == 0:
                 X[i] //= p
print(X)

Candidate = [(x + sqrt_N, (x + sqrt_N)**2-N) for x in range(A) if X[x] == 1]
print(Candidate)
for x in Candidate:
    y = x[1]
    print(y,end=':')
    for p in FB:
        i = 0
        while y % p == 0:
            i+=1
            y= y/p
        if i>0:
            print((p,i), end=' ')
    print()
