def SI(p=10000,r=5,t=1):
    s=p*r*t/100
    return s
def CI(p=10000,r=5,t=1):
    a=p*((1+(r/100))**t)-p
    return a
pi=int(input(' enter principal amount'))
rt=int(input(' enter rate of interest'))
ti=int(input(' enter time period'))
print("simple interest will earn for the above given data",SI(pi,rt,ti))
print("compound interest will earn for the above given data",CI(pi,rt,ti))















