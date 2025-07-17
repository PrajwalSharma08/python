import csv
f=open("cs.csv","w")
a=csv.writer(f)
n=int(input("enter a no."))
for i in range(1,11):
    y=n*i
    l=[n,"X",i,"=",y]
    a.writerow(l)
f.close()
