def factor(n):
    l=[]
    for i in range(1,n+1):
        if n%i==0:
            l=l+[i]
    return l
def isprime(n):
    return ([1,n]==factor(n))
print(factor(18))
print(isprime(17))
def primeup(n):
    l=[]
    for i in range(1,n+1):
        if isprime(i)==True:
            l=l+[i]
    return l
print(primeup(10))
print(list(range(1,10,3)))
