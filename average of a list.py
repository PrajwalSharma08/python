def av(lst):
    return sum(lst)/len(lst)
def l():
    ls=[]
    for i in range(5):
        a=int(input("enter a number"))
        ls.append(a)
    return ls
print("average",av(l()))
        
