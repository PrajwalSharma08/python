c1='COMPUTER'
c=len(c1)

for i in range(0,6):
    for j in range(6,i,-1):
        print(' ',end='')
    print(i*' x')


for k in range(c,-1,-1):
    for h in range(k):
        print(c1[h],end='')
    print()
