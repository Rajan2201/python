class Node:
    def __init__(self,data):
        self.data=data
        self.nxt=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertatbeg(self,data):
        newnode=Node(data)
        newnode.nxt=self.head
        self.head=newnode
    
    def delete(self):
        tmp=self.head
        self.head=self.head.nxt
        tmp.nxt=None
    def printlist(self):
        tmp=self.head
        while tmp:
            print(tmp.data,"==>",end='')
            tmp=tmp.nxt
obj=LinkedList()
ch=0
while ch!=4:
    print("\n Linked List Implementation \n 1.insertatbeg 2.deletion 3.print 4.exit")
    ch=int(input())
    if ch==1:
        print("enter the data:")
        data=input()
        obj.insertatbeg(data)
        obj.printlist()
    elif ch==2:
        obj.delete()
        obj.printlist()
    elif ch==3:
        obj.printlist()
    else:
        print("nothing will happen")
        
