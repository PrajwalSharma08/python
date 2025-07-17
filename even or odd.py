l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
e=[]
o=[]
x=[]
'''for i in range(len(l)):
    if i%2==0:
        o+=l[i]
    else:
        e+=l[i]
x=[o,e]
print(x)
'''
for i in range(len(l)):
    if i%2==0:
        o.append(l[i])
    else:
        e.append(l[i])
'''x.extend(o)
x.extend(e)
print(x)
'''
print(e)
print(o)

print(o+e)
o.extend(e)
'''print(e)
print(o)'''
