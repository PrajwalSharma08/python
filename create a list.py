l=[]
x=1
while x==1:
    print('enter your choice','\n','1-add elements','2-remove elements','3-show list')
    a=int(input("enter you choice="))
    z=len(l)
    if a==1:
        a=int(input("enter the elements="))
        l.append(a)
        print("updated list")
    elif a==2:
        if z==0:
            print("pehle add karo")
        else:
            l.pop()
            print("list updated")
    elif a==3:
        print(l)
    x=int(input("wapas se kuch krna h 1-ha  2-na"))
