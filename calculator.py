def sum(a,b):
    print(a+b)
def sub(a,b):
    print(a-b)
def mult(a,b):
    print(a*b)
def divi(a,b):
    print(a/b)
def exp(a,b):
    print(a**b)
def quo(a,b):
    print(a//b)
def remi(a,b):
    print(a%b)
ch=1
while ch==1:
    print("1-add \n 2-sub \n 3-multiply \n 4-divide \n 5-exponent \n 6-quotient \n 7-reminder")
    e=int(input("enter your choice"))
    c=int(input("enter a first number="))
    d=int(input("enter a second number="))
    if e==1:
        sum(c,d)
    elif e==2:
        sub(c,d)
    elif e==3:
        mult(c,d)
    elif e==4:
        if d==0:
            print("Error!!!divisor can't be zero")
        else:
            divi(c,d)
    elif e==5:
        exp(c,d)
    elif e==6:
        quo(c,d)
    elif e==7:
        remi(c,d)
    ch=int(input('do you want to continue?1-yes 2-no'))
    if ch==2:
        print("Dhanyawad❤️❤️")
    

