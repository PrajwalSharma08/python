a=list(input("enter elements of list" ))
b=list(input("enter elements of second list"))
c=max(a)
print("maximam number of first list",c)
d=max(b)
print("maximum number of second list ",d)
if c>d:
    print("maximum value in both list is",c)
    print("index of maximum value is",a.index(c))
else:
    print("maximum value in both list is ",d)
    print("index of maximum value is ",b.index(d))
      
