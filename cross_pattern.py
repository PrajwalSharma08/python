for i in range(1,6):
    for j in range(1,6):
        if i==j:
            print('x',end="\t")
        elif 6-i==j:
            print('x',end="\t")
        else:
            print('',end="\t")
    print()
