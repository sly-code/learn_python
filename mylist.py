shoplist=["apple","mango","carrot","banana"]
print("I have",len(shoplist),"items to purchase")
print("these items are:",end=' ')
for item in shoplist:
    print(item, end=' ')

shoplist.append("rice")
print('\n',shoplist)

shoplist.insert(1,"tomato")
print('\n',shoplist)

shoplist.sort()
print('\n',shoplist)
shoplist.sort(reverse=True)
print('\n',shoplist)

del shoplist[0]
print('\n',shoplist[0:-1])
L=[1,2]
L.append(L)
print(L,L[2],L[2][2])
