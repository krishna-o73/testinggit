def matched(s):
    count=0
    for i in range(0,len(s)):
        if s[i]=='(':
            count=count+1
        if s[i]==')':
            count=count-1
        if count<0:
            return False
    if count==0:
        return True
    else:
        return False
print(matched("15ababa.agaga[][[["))
