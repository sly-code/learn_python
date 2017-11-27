x=2;y=3;z=5
print(x<y<z)
print(z/x,z//x)

inf=float("inf")
print(inf,x<inf)

x=1+2j;y=3+7j
print(x+y,x*y,x/y)

print([oct(64),hex(64),bin(64)])

x=eval("int")("123")
print(type(x),x)

x=1
print(x<<2,x|2,x&1)

import math
print(math.pi,math.e)

X=set("spam")
Y={'h','a','m'}
print(X & Y)
print(X | Y)
print(X-Y)
print(X^Y)
print(X>Y,X<Y)
Z={x**2 for x in [1,2,3,4]}
print(Z)
X={c*4 for c in "spamham"}
print(X)
L=[1,2,1,3,2,4,5]
X=set(L)
print(X)
X.add(6)
print(X)
X.add(6)
print(X)
