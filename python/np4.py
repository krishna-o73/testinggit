def ra(l):
    l1=[]
    for x in l:
        a=x[0]
        s=0
        c=0
        s1=[]
        if x not in s1:
            s1.append(a)
            for y in l:
                if a==y[0]:
                    s=s+y[1]
                    c=c+1
            t=(a,(s/c))
            l1.append(t)
    s2=set(l1)
    l1=list(s2)
    return list(sorted((l1)))
print(ra([('Bombay',1848),('Bombay',923),('Bombay',201),('Bombay',128),('Bombay',103),('Bombay',948),('Bangalore',323)]))
