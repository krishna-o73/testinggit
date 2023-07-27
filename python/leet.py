def relativeSortArray(arr1, arr2):
    l=[]
    for x in arr2:
        count=arr1.count(x)
        while count>0:
            l.append(x)
            count=count-1
    arr1.sort()
    print(arr1)
    for x in arr1:
        if x not in arr2:
            l.append(x)
            print(x)
    return l
print(relativeSortArray([28,6,22,8,44,17],[22,8,28,6]))
