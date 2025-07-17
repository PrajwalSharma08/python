import csv
f=open("cs.csv",newline="\r\n")
a=csv.reader(f)
s=" "
for i in a:
    for j in range(len(i)):
        s+=str(i[j])
print(s)
f.close()
