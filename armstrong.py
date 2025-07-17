n=int(input("enter any number="))
sum=0
m=n
while n>0:
    l=n%10
    sum=sum+l*l*l
    n=n//10
if(sum ==m):
    print("number is armstrong")
else:
    print("number is not armstrong") 
