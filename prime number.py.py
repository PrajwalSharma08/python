for i in range(1,101):
    if i==1:
        print(i , 'is not prime number')
    elif i>1:
        for j in range(2,i):
            if i%j==0:
                print(i,' not prime number')
                break
        else:
            print(i,'is prime')

