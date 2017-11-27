poem="""\
programming is fun
when the work is done
if you wanna make your work also fun:
    use Python!"""
f=open("poem.txt",'w')
f.write(poem)
f.close()

f=open('poem.txt')
while True:
    '''f.readline() reads a single line from the file; 
    a newline character (\n) is left at the end of the string, 
    and is only omitted on the last line of the file if the file doesn’t end in a newline. 
    This makes the return value unambiguous; 
    if f.readline() returns an empty string, 
    the end of the file has been reached, 
    while a blank line is represented by '\n', 
    a string containing only a single newline.'''
    line=f.readline()
    if len(line)==0:
        break
    print(repr(line))   #as poem.txt doesn't end in a newline,
                        #the return of readline() doesn't contain a '\n' on the  last line of the file

print("the type of f is:",type(f))
f.seek(0)
for line in f:
    print(line,end=' ')
print()
f.close()

import os
os.remove("poem.txt")

with open("binary.bin","wb") as f:
    f.write(os.urandom(20))
with open("binary.bin",'rb') as f:
    bstring=f.read()
    print(repr(bstring))
for byte in bstring:
    print(byte,end=' ')
print()
os.remove("binary.bin")

import pickle
shoplist=["apple","mango","carrot","banana"]
f=open("shoplist.pkl","wb")
pickle.dump(shoplist,f)
f.close()
del shoplist
with open("shoplist.pkl","rb") as f:
    storedlist=pickle.load(f)
    print(storedlist)
    f.seek(0)
    print(f.read())
os.remove("shoplist.pkl")
