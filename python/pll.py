class Node:
    def __init__(self,v=None):
        self.val=v
        self.next=None
        return
    def isempty(self):
        if self.val==None:
            return True
        else:
            return False
    def append(self,v):
        if self.isempty()==True:
            self.val=v
            return
        temp=self
        while temp.next!=None:
            temp=temp.next
        newnode=Node(v)
        temp.next=newnode
        return
    def insert(self,v):
        if self.isempty()==True:
            self.val=v
            return
        temp=self
        newnode=Node(v)
        (temp.val,newnode.val)=(newnode.val,temp.val)
        (temp.next,newnode.next)=(newnode,temp.next)
        return
    def delete(self,v):
        if self.isempty()==True:
            return
        if self.val==v:
            self.val=None
            if self.next != None:
                self.val = self.next.val
                self.next = self.next.next
            return
        temp=self
        while temp.next!=None:
            if temp.next.val==v:
                temp.next=temp.next.next
                return
            else:
                temp=temp.next
        return
    def __str__(self):
        selflist=[]
        if self.val==None:
            return(str(selflist))
        temp=self
        selflist.append(temp.val)
        while temp.next!=None:
            temp=temp.next
            selflist.append(temp.val)
        return str(selflist)
n=Node(78)
print(n)
n.append(12)
print(n)
n.append(34)
print(n)
n.insert(84)
print(n)
n.insert(54)
print(n)
n.insert(54)
print(n)
n.delete(54)
print(n)
n.delete(12)
print(n)
n.delete(76)
print(n)
