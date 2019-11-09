if __name__ == "__main__":
    print("This program is being run by itself")
else:
    print("'I am being imported from another module")

import sys
print("the command line arguments are:")
for i in sys.argv:
    print(i)
print("\nthe Python module search path is:")
for pth in sys.path:
    print(pth)
import os
print("current work directory is:", os.getcwd())

import mydict   # first import, run codes in mydict.py
print("\nfirst import, the D in mydict.py is:", mydict.D)
mydict.D['w'] += 1
print("after change, the D in mydict.py is:", mydict.D)
import mydict   # import again, but codes in mydict.py won't run again
print("import again, the D in mydict.py is:", mydict.D)

from number import x, L     # copy two names out. Equivalent statement: import number; x = number.x; L = number.L; del number
print("\nx in mymodule is {}, L in mymodule is {}".format(x, L))
x = 42      # change local x only
L[0] = 43   # change shared mutable in-place
import number
print("x in number.py is {}, L in number.py is {}".format(number.x, number.L))

