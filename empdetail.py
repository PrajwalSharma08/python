import pickle
f=open("empl.dat",'wb')
n=int(input("how many employee"))
a={}
for i in range(n):
    i_d=input("id ka name de=")
    n=input("name bhar")
    s=input("salary kitni hai")
    j=input("addhar no. daal")
    a[Empid]=i_d
    a[name]=n
    a[salary]=s
    a[addhar]=j
    pickle.dump(a,f)
f.close()
