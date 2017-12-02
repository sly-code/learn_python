# and,or,not
or_ret=2 or 3
print(or_ret,bool(or_ret))
or_ret=[] or 3
print(or_ret,bool(or_ret))
or_ret=[] or None
print(or_ret,bool(or_ret))
and_ret=2 and 3
print(and_ret,bool(and_ret))
and_ret=2 and {}
print(and_ret,bool(and_ret))
not_ret=not 2
print(not_ret)

X=0;Y=1;Z=2
print(Y if X else Z)
print((X and Y) or Z)
print([Z,Y][bool(X)])

for ((a,b),c) in [((1,2),3),((4,5),6)]:
    print(a,b,c)
for(a,*b,c) in [(1,2,3,4),(5,6,7,8)]:
    print(a,b,c)

L1=[1,2,3,4,5]
L2=[5,6,7,8,9]
print(list(zip(L1,L2)))
for (x,y) in zip(L1,L2):
    print(x,y,'--',x*y)

S="spam"
for (offset,item) in enumerate(S):
    print(item,"appears at offset",offset)
E=enumerate(S)
print(next(E))
print(next(E))
print(next(E))
print(next(E))


