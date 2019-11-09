"""iterator tools: for loop, list comprehension, in member test, range, filter, reduce,map
iterable object: list, string, tuple, file"""
L = [1, 2, 3, 4, 5]
for x in L:  # automatic iteration: obtains iter, calls __next__, catches exceptions
    print(x**2,end=' ')
print()
I = iter(L)
while True:
    try:
        x = next(I)
    except StopIteration:
        break
    print(x**2,end=' ')
print()
import os
dir_result = os.popen("dir /B")
for line in dir_result:
    print(line,end=' ')

lines=[line.rstrip() for line in open("readme.txt")]
print(lines)

L=[x+y for x in "abc" for y in "lmn"]
print(L)
L=[(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y %2 == 1]
print(L)
print(list(enumerate(open("readme.txt"))))

print(list(filter(bool,[1,0,2,None,3,'',4])))

print(any(['spam','','hi']))
print(all(["spam",'',"hi"]))
print("sum of [3,2,4,1,5] is:",sum([3,2,4,1,5]))
print("max of [3,2,5,1,4] is:",max([3,2,5,1,4]))
print("min of [3,2,5,1,4] is:",min([3,2,5,1,4]))

# range iterator
R=range(10)
print("about range:",len(R),R[0],R[-1])
I=iter(R)
print(I.__next__(),I.__next__())
print(list(range(10)))


def gensquares(N):
    """yield function"""
    for i in range(1,N):
        yield i**2


print(gensquares.__doc__)
gnr=gensquares(5)   # generator object
print(gnr.__next__(), end=',')
print(next(gnr))
G = (x**2 for x in range(1, 6))    # generator expression
print("iter(G) is G:", iter(G) is G)
print(next(G), end=',')
print(G.__next__())
H = G
print(H.__next__())  # H is at the same position as G
print(list(H))  # collect the rest of H's items. after execution, H and G are both exhausted
"""compare to iterator of builtin types"""
L = [1, 2, 3, 4]
it1 = iter(L)
it2 = iter(L)
print("iter(L) is L:", iter(L) is L)
print("next(it1):", next(it1))
print("next(it1):", next(it1))
print("next(it2):", next(it2))  # lists supports multiple iterators
