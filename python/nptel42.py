l1=[]
def simple(l):
    for element in l:
        if type(element)==type([]):
            simple(element)
        else:
            l1.append(element)
    return l1
print(simple([[[]]]))