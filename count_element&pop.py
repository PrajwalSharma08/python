s=list(input("enter a list="))
x=input("enter a element=")
print(s)
k=s.count(x)
if k==0:
    print("nhi mila")
else:
    print("pehla mil gaya.... miracle!! miracle!!",s.index(x))
print("itne  bar mila hai bhaiya",k)




k=len(s)
for i in range(0,k,2):
    s.pop(0)
print(s)


