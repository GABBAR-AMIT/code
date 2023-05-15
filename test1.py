class node:
    def __init__(self,data):
        self.head=data
        self.next=None
        
class listt:
    def __init__(self):
        self.n1=None
    def printt(self):
        a=self.n1
        while a :
            print(a.head)
            a=a.next
    def insert_l(self,j):
        new=node(j)
        new.next=self.n1
        self.n1=new
node1=listt()
node1.n1=node(10)
node2=node(15)
node1.n1.next=node2
node1.insert_l(5)
node1.printt()