def fib():
    a=0
    b=1
    print(a,'\n',b)
    while a<200:
        c=a+b
        print(c)
        a,b=b,c
fib()
 
