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
    def inserction(self, j):
        a=self.n1
        n_node=node(j)
        n_node.addr=a
    
    def del1(self,30):
        

node1=l_list()
node1.n1=node(10)
node2=node(20)
node1.n1.addr=node2
node3=node(30)
node2.addr=node3
node4=node(40)
node3.addr=node4
node5=node(50)
node4.addr=node5
node6=node(60)
node5.addr=node6
node7=node(70)
node6.addr=node7
node8=node(80)
node7.addr=node8
node9=node(90)
node8.addr=node9
node10=node(100)
node9.addr=node10
node1.p_rint()