import csv
f=open("detail.csv","w",newline="")
fw=csv.writer(f)
l=[]
for i in range(5):
    id=input("apni id daalo=")
    na=input("apna name batao=")
    dl=input("apna dl no. daal=")
    r=[id,na,dl]
    l.append(r)
fw.writerows(l)
f.close()
