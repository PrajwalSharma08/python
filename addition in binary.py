x=int(input("no. of lines="))
f=open("calc.text","a+")
for i in range(x):
    a=int(input("first no.="))
    b=int(input("second no.="))
    c=a+b
    z=str(a)+"+"+str(b)+"="+str(c)
    f.write(z)
    f.write("\n")
f.close()
