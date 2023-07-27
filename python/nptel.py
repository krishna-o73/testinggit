def average(l):
    l2=[]
    l3=[]
    for i in range(0,len(l)):
        if l[i][0] not in l3:
            l3.append(l[i][0])
            a=l[i][0]
            f=l[i][1]
            count=1
            for j in range(0,len(l)):
                if a==l[j][0] and i!=j:
                    f=f+l[j][1]
                    count=count+1
            t=(a,f/count)
            l2.append(t)
    return sorted(l2, key = lambda x: x[0])
l4=average([('Bombay',848),('Madras',103),('Bombay',923),('Bangalore',201),('Madras',128)])
print(l4)
    
