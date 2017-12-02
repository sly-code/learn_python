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
dir_result = os.popen("dir")
for line in dir_result:
    print(line,end=' ')

lines=[line.rstrip() for line in open("readme")]
print(lines[0],lines[1])

L=[x+y for x in "abc" for y in "lmn"]
print(L)
L=[(x,y) for x in range(5) if x % 2 == 0 for y in range(5) if y %2 == 1]
print(L)
print(list(enumerate(open("readme"))))

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

