s='computer'
m=len(s)
for i in range(m,-1,-1):
    for j in range(i):
        print(' ',end='')
    for k in range(m-i):
        print(s[k],end=' ')
    print()
