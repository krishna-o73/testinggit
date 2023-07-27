def merge(a,b):
    c=[]
    i=0
    j=0
    while i+j<len(a)+len(b):
        if i==len(a):
            c.append(b[j])
            j=j+1
        elif j==len(b):
            c.append(a[i])
            i=i+1
        elif a[i]>b[j]:
            c.append(b[j])
            j=j+1
        elif a[i]<b[j]:
            c.append(a[i])
            i=i+1
    return c
def mergesort(a,l,r):
    if r-l<=1:
        return(a[l:r])
    if r-l>1:
        mid=(l+r)//2
        L=mergesort(a,l,mid)
        R=mergesort(a,mid,r)
        return(merge(L,R))
l1=[19,6,3,23,55,17,36,42]
print(mergesort(l1,0,len(l1)))
