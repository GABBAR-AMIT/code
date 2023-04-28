class node:
    def __init__(self,data):
        self.head=data
        self.addr=None

class l_list:
    def __init__(self):
        self.n1=None
    
    def p_rint(self):
        a=self.n1
        while a:
            print(a.head)
            a=a.addr

node1=l_list()
node1.n1=node(10)
node2=node(20)
node1.n1.addr=node2
node3=node(30)
node2.addr=node3
node4=node(40)
node3.addr=node4

node1.p_rint()
