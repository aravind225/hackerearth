class Node():
    def __init__(self,val):
        self.data=val
        self.add=None
class ll():
    def __init__(self):
        self.head=None
        self.last=None
    def insert(self,val):
        nn=Node(val)
        if self.head==None:
            self.head=nn
            self.last=nn
        else:
            self.last.add=nn
            self.last=nn
    def delete(self):
        if self.head==None:
            print("empty list")
        elif self.head==self.last:
            self.head=None
            self.last=None
        else:
            self.temp=self.head
            while self.temp.add.add!=None:
                self.temp=self.temp.add
            self.temp.add=None
            del self.last
            self.last=self.temp
    def insert_at_start(self,val):
        nn=Node(val)
        if self.head==None:
            self.last=nn
        nn.add=self.head
        self.head=nn
    def insert_by_pos(self,pos,val):
        self.p=1
        self.temp=self.head
        nn=Node(val)
        if self.head==None:
            self.insert(val)
        elif self.head==self.last:
            self.insert_at_start(val)
        else:
            while self.p!=pos-1 and self.temp.add!=None:
                self.temp=self.temp.add
                self.p+=1
            self.temp.add=nn
            nn.add=self.temp.add
    def display(self):
        if self.head==None:
            print("empty list")

        else:
            self.temp=self.head
            while self.temp!=None:
                print(self.temp.data,end="<-->")
                self.temp=self.temp.add
            print()
obj=ll()
while True:
    ch=int(input("1 insert 2 delete 3 display 4 display at start 5.display by pos"))
    if ch==1:
        val=int(input("enter the number"))
        obj.insert(val)
    elif ch==2:
        obj.delete()
    elif ch==3:
        obj.display()
    elif ch==4:
        val=int(input("enter the number"))
        obj.insert_at_start(val)
    elif ch==5:
        val=int(input("enter the number"))
        pos=int(input("required postion"))
        obj.insert_by_pos(pos,val)
    else:
        break
    
















        

    
