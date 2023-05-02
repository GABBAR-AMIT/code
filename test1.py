class node:
    def __init__(self,data):
        self.data=data
        self.next=None
        
class llist:
    def __init__(self):
        self.head=None
        
    def printt(self):
        a=self.head
        while a:
            print(a.data)
            a=a.next
no1=llist()
no1.head=node(20)
no2=node(40)
no1.head.next=no2
no3=node(60)
no2.next=no3
no1.printt()
#how to make a linklist ?