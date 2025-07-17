n=int(input("no. of lines="))
f=open("tb.text","w")
for i in range(1,11):
    c=n*i
    z=str(n)+"*"+str(i)+"="+str(c)
    f.write(z)
    f.write("\n")
f.close()
