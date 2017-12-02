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
#index and slice
L=[1,2,3,4,5]
L[1]=[];print(L)
L[1:2]=[];print(L)
del L[2:];print(L)

#concatenate
L=[1,2];M=L
L=L+[3,4]   #concatenation makes a new object
print("using concatenation: ",L,M)
L=[1,2];M=L
L+=[3,4]    #in-place extend
print("using +=: ",L,M)
#assignment mechanism
X=[1,2,3]
L=['a',X,'b']
D={'x':X,'y':2}
print("before change X:\n",L,'\n',D)
X[1]='surprise'
print("after change X:\n",L,'\n',D)
import  sys
print(sys.getrefcount(X))
X="spam";Y="eggs"
X,Y=Y,X
print("X={} Y={}".format(X,Y))
#compare, equality
L1=["python programming",1,('a',3)]
L2=["python programming",1,('a',3)]
print("initial individually: ",L1==L2,L1 is L2,L1[0] is L2[0],sys.getrefcount(L1),sys.getrefcount(L1[2]))
L3=L1
print("by =: ",L1==L3,L1 is L3,L1[0] is L3[0],sys.getrefcount(L1),sys.getrefcount(L1[2]))
L4=L1.copy()
print("by copy(): ",L1==L4,L1 is L4,L1[0] is L4[0],sys.getrefcount(L1),sys.getrefcount(L1[2]))
import  copy
L5=copy.deepcopy(L1)
print("by deepcopy(): ",L1==L5,L1 is L5,L1[0] is L5[0],sys.getrefcount(L1),sys.getrefcount(L1[2]))
t=copy.copy(L1[2]);print(t is L1[2],sys.getrefcount(t))
s1='spam'
s2='spam'
print(s1==s2, s1 is s2)
s1='a much longer string. it is a sentence'
s2='a much longer string. it is a sentence'
print(s1==s2,s1 is s2)
