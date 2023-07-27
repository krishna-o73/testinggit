from collections import Counter
s="aab"
res = Counter(s)
l=[]
for x in res:
    l.append(res[x])
l.sort()
count=0
b=4
while(b):
    l.sort()
    for i in range(0,len(l)-1):
        if(l[i]==l[i+1]):
            break
    if(i==len(l)):
        print(count)
    i=i+1
    l[i]=l[i]-1
    count=count+1
    b=b-1
print(b)
print(count)
