def say(message,times=1):
    print(message*times)


def print_max(a, b):
    """print the maximuum of two numbers.
    The two values must be integers"""
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


x=50
def func(x):
    print('x is',x)
    x=2
    print('changed local x to',x)

def factor(n):
    if n==1:
        return 1
    else:
        return n*factor(n-1)


say('hello')
say("world",5)
a = 5
b = 9
print_max(a, b)
func(x)
print(print_max.__doc__)
print('x is still',x)
print(factor(a))
help(print_max)
