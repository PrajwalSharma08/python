try:
    a=int(input("enter a no="))
    b=int(input("enter a no="))
    c=a/b
    print(c)
except ZeroDivisionError:
    print("b can't be Zero")
except ValueError:
    print("wrong input")
