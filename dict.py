ab={"Swaroop":"Swaroop@swaroopch.com",
    "Larry":"larry@wall.org",
    "Spammer":"spammer@hotmail.com",
    'Matsumoto':	'matz@ruby-lang.org'}
print("there are {} contacts in the address book".format(len(ab)))
print("Swaroop's address is",ab["Swaroop"])
for name,address in ab.items():
    print("contact {} at {}".format(name,address))
ab["Guido"]="guido@qq.com"
print(sorted(ab))
print(list(ab.keys()))
print(list(ab.values()))
print(list(ab.items()))

#three ways to index by key that might not exist
#1: get method
print(ab.get("Guido","key not exists"))
print(ab.get("Alan","key not exists"))
#2: if test
if "Guido" in ab:
    print("\nGuido's address is",ab["Guido"])
#3: try and except
try:
    print("\nGuido's address is",ab["Alan"])
except KeyError:
    print("{} not exists".format("Alan"))

# remove keys
print(ab.pop("Spammer"))
print(ab)

#other ways to creat dict
D=dict(Alan=1,Luke=2,Harry=3,Green=4)
print(D)
D=dict(zip(['a','b','c'],[1,2,3]))
print(D)
D={k:v for (k,v) in zip(['a','b','c'],[10,12,13])}
print(D)
D=dict.fromkeys(['w','x','y','z'],0)
print(D)
