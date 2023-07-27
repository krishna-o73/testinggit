class Node:
    def __init__(self,val=None):
        self.value=val
        self.next=None
        return
    
    def isempty(self):
        if self.value==None:
            return True
        else:
            return False
    def append(self,val):
        if self.isempty():
            self.value=val
        elif self.next==None:
            newnode=Node(val)
            self.next=newnode
        else:
            self.next.append(val)
        return
    def insert(self,val):
        if self.value==None:
            self.value=val
            return
        newnode=Node(val)
        (self.value,newnode.value)=(newnode.value,self.value)
        (self.next,newnode.next)=(newnode,self.next)
        return
    
    def delete(self,val):
        if self.value==None:
            return
        if self.value==val:
            self.value=None
            if self.next!=None:
                self.value=self.next.value
                self.next=self.next.next
                return
        else:
            if self.next!=None:
                self.next.delete(val)
                if self.next.value==None:
                    self.next=None
        return
n=Node(78)
n.append(12)
n.append(34)
n.insert(84)
n.insert(54)
n.insert(54)
n.delete(54)
n.delete(12)
n.delete(76)
            
