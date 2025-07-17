def diffrentiation(x,n):
    if n==0:
        return 1
    elif n==1:
        return x
    else:
        return n*x**(n-1)
    
print(diffrentiation(5,6))

def diff_log(x):
    return 1/x
print(diff_log(5-1))
