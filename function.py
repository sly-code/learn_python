x = 5  # x is a global variable


def func1(x):
    print('x is',x)
    x = 2  # this x is a local
    print('changed local x to',x)


func1(x)
print('x is still',x)


def func2():
    global x
    global y
    y = 10 ; x = 6


func2()
print("after func2: x={},y={}".format(x, y))


def factor(n):
    if n == 1:
        return 1
    else:
        return n*factor(n-1)


print("{}! ={}".format(x,factor(x)))


def tester(start):
    state = start

    def nested(label):
        """this is a nested function defined inside a function"""
        nonlocal state
        print(label,state)
        state += 1  # allow to change it if nonlocal
    return nested


F = tester(0)
print(F.__doc__)
F("spam")
F("eggs")
F("python")


class Tester:
    """class implementation equivalent to tester...nested function"""
    def __init__(self,start):
        self.state = start

    def nested(self,label):
        print(label,self.state)
        self.state += 1

    def __call__(self, label):
        """call operator overload"""
        print(label, self.state)
        self.state += 1


print(Tester.__doc__)
F = Tester(10)
F.nested("spam")
F.nested("eggs")
F("spider")


def func3(i, lst):
    i += 1
    lst[0]="changed"

x=1
L=[1, 2, 3, 4]
func3(x, L)
print(x, L)

"""parameter match
function call: func(value),func(name=value),func(*sequence),func(**dict)
function def: func(name),func(name=value),func(*name),func(**name),func(*args,name),func(*,name=value)"""


def func4(spam, eggs, toast=13, ham=14):
    """a mixed use of keyword parameter and default parameter"""
    print((spam,eggs,toast,ham))


print(func4.__doc__)
func4(1,2)
func4(1,ham=2,eggs=3)
func4(spam=1,eggs=2)
func4(toast=1,eggs=2,spam=3)
func4(1,2,3,4)
print("* parameters unpack in function call:")
args = (5, 6, 7, 8)
func4(*args)
print("** parameters unpack in function call:")
args={"eggs":10,"toast":11,"spam":9,"ham":12}
func4(**args)


def saver(lst=[]):
    """function with mutable default argument"""
    lst.append(1)
    print(lst)


print(saver.__doc__)
saver([2])  # default not used
saver()     # default used
saver()     # default grows on each call
saver()     # in this case, the default acts like a static variable in C language


def saver1(lst=None):
    if lst is None:     # what if x = x or [] ?
        lst = []
    lst.append(1)
    print(lst)


saver1([2])
saver1()
saver1()


def func5(x, *pargs, **kargs):
    """arbitrary number of parameters"""
    print(x,pargs,kargs)


print(func5.__doc__)
func5(1, 2, 3, u=4, v=5)


def tracer(func, *pargs, **kargs):
    print("calling:",func.__name__)
    return func(*pargs, **kargs)


def _sum(w, x, y, z):
    return w+x+y+z


print(tracer(_sum, 1, 2, y=3, z=4))


def kwonly_1(x, *y, z):   # x can be passed by name or position, z must by name, and y collects any other parameters
    """this is a keyword-only parameter function"""
    print(x,y,z)


print(kwonly_1.__doc__)
kwonly_1(1, 2, 3, z=4)
kwonly_1(x=1, z=4)


def kwonly_2(x, *, y=1, z=2):   # x can be passed by name or position, y and z must be name and it takes only one positional argument
    """keyword only function with default arguments"""
    print(x,y,z)


print(kwonly_2.__doc__)
kwonly_2(11, z=13, y=12)
kwonly_2(z=23, x=21, y=22)
kwonly_2(31)
kwonly_2(41, y=42)


def kwonly_3(w, *x, y=2, **z):  # notice: keyword-only parameter must appears after *args and before **args
    print(w, x, y, z)


kwonly_3(1, 2, 3, spam=4, eggs=5)
kwonly_3(1, 2, 3, spam=4, eggs=5, y=6)


def sumtree(L):
    """sum on arbitrarily nested sublists"""
    tot=0
    for x in L:
        if not isinstance(x, list):
            tot += x
        else:
            tot += sumtree(x)
    return tot


L = [1, [2, [3, 4], 5], 6, [7, 8]]
print(sumtree.__doc__)
print("sum of all integers in list L is:",sumtree(L))


def echo(msg: str, times: int =1):  # str and int are annotations attached on parameter msg and times respectively
    print(msg*times)


print(echo.__annotations__)
schedule = [(echo, "spam!", 2), (echo, "ham!", 3)]   # function is also an object and can be treated like an integer or a string
for (func, *arg) in schedule:
    print(arg, end=' --> ')
    func(*arg)   # call functions embedded in containers
echo1 = echo     # echo1 and echo are references of a same function object
print("echo1 is echo:", echo1 is echo)
echo1("spider", 3)

"""anonymous function:lambda
grammar formation: lambda arg1, arg2, ..., argn :expression using args
lambda is an expression, not a statement while def is a statement
lambda body must be a single expression instead of a code block
this means lambda can appear in positions where def can't appear such as list or function args"""
L=[lambda x: x**2, lambda x: x**3, lambda x: x**4]
for f in L:
    print(f(2), end=' ')
print()

"""examples of map, filter and reduce"""
print(list(map((lambda x: x + 3),[1,2,3,4])))
print(list(map(pow, [1, 2, 3], [4, 5, 6])))  # 1^2, 2^5, 3^6
print(list(filter((lambda x: x>0), range(-5, 5))))
from functools import reduce
print(reduce((lambda x, y: x + y), [1, 2, 3, 4]))
