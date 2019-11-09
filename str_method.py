name="Swaroop"
if name.startswith("Swa"):
    print("Yes, the string starts with 'Swa'")
if 'a' in name:
    print("Yes, it contains the letter 'a'")
if name.find("war")!=-1:
    print("yes ,it contains the word 'war'")
delimiter="_*_"
mylist=["Brazil","Russia","India","China","South Africa"]
print(delimiter.join(mylist))

line="example,of,\nstring, method\n"
print(line.rstrip())
print(line.split(','))

print(ord('a'))
import sys
print("My {1[spam]} runs {0.platform}".format(sys,{"spam":"laptop"}))
print("my {config[spam]} runs {_sys.platform}".format(_sys=sys,config={"spam":"laptop"}))

somelist = list("spam")
print("first={0[0]},third={0[2]}".format(somelist))
# complete grammar formation:{fieldname!conversionflag:formatspec}
# fieldname: number or keyword, can be followed by .name or [index]
# conversionflag=r,s,a, represent for repr, str, ascii respectively
# formatspec: [[fill]align][sign][#][0][width][.precision][typecode]
print("{0:10}={1:15}".format("spam",123.45678))
print("{0:>10}={1:<15}".format("spam",123.45678))
x=31.415926
print("{0:e},{1:.3e},{2:g}".format(x,x,x))
print("{0:f},{1:.2f},{2:06.2f}".format(x,x,x))
print("{0:X},{1:o},{2:b}".format(255,255,255))
print("{0:.{1}f}".format(1/3.0,4))

for ch in "a\nb\x1f\000d":
    print(ord(ch),end=' ')
print()
for ch in r"a\nb\x1f\000d":
    print(ord(ch),end=' ')
