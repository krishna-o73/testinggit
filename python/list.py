l=[2,7,5,3]
def sq(x):
    return ((x*x)%2)==0
l=list(map(lambda x:sq(x),l))
print(l)
