import csv
f=open("cs.csv",newline="\r\n")
a=csv.reader(f)
for i in a:
    l=len(i)
    for j in range(-1,-l-1,-1):
        print(i[j],end="")
    print()
f.close()
