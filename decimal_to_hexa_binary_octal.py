def dth(D):
    hd=" "
    h="0123456789abcdef"
    while D>0:
        r=D%16
        hd+=h[r]
        D//=16
    return hd
a=int(input("enter a number to change in a hexadecimal"))
print("decimal to hexadecimal",dth(a))
print(hex(a))

def dtb(D):
    hd=" "
    h="01"
    while D>0:
        r=D%2
        hd+=h[r]
        D//=2
    return hd
a=int(input("enter a number to change in a binary"))
print("decimal to binary",dtb(a))
print(bin(a))

def dto(D):
    hd=" "
    h="01234567"
    while D>0:
        r=D%8
        hd+=h[r]
        D//=8
    return hd
a=int(input("enter a number to change in a octal"))
print("decimal to octal",dto(a))
print(oct(a))


