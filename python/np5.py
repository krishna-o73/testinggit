def f(l):
    l1=[]
    if l==[]:
        return l1
    for x in l:
        if type(x) is list:
            l1=l1+f(x)
        else:
            l1.append(x)
    return l1
print(f([[[]]]))
            
