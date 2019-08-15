class Node:
    def __init__(self,data):
        self.data=data
        self.address=None
class LinkedList:
    def __init__(self):
        self.head=None
    
    def insertatbeg(self,data):
        newnode=Node(data)
        newnode.address=self.head
        self.head=newnode
    
    def anyposition(self,data,pos):
        tmp=self.head
        while tmp.data!=pos:
            tmp=tmp.address
        if tmp.data==pos:
            new=Node(data)
            new.address=tmp.address
            tmp.address=new
    
    def insertatlast(self,data):
        new=Node(data)
        tmp=self.head
        while tmp.address!=None:
            tmp=tmp.address
        
        tmp.address=new
           
    def deleteatbeg(self):
        tmp=self.head
        self.head=self.head.address
        tmp.address=None
    
    def deleteatmiddle(self,pos):
        tmp=self.head
        while tmp.address!=pos:
            tmp=tmp.address
        if tmp.address==pos:
            tmp.address=tmp.address.address
            tmp.address=None
            
    def deleteatlast(self):
        tmp=self.head
        while tmp.address!=None:
            tmp=tmp.address
        tmp.address=None
        
    
    def printlist(self):
        tmp=self.head
        while tmp:
            print(tmp.data,"==>",end="")
            tmp=tmp.address
obj=LinkedList()
ch=0
while ch!=4:
    print("linked list implementation \n 1.insertatbeg 2.delete 3.print 4.anyposition 5.insertatlast 6.deleteatmiddle 7.deleteatlast 8.exit")
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
        print("wrong choice")

