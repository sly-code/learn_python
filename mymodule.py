if __name__=="__main__":
    print("This	program	is	being	run	by	itself")
else:
    print("'I	am	being	imported	from another module")

import  sys
print("the command line arguments are:")
for i in sys.argv:
    print(i)
print("\n\nthe Python path is:\n",sys.path)
import  os
print('\n',os.getcwd())
from math import sqrt
print("the square root of 3 is", sqrt(3))

import function
print(function.x, function.factor(4))
dir(str)

