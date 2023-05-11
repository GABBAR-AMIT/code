class node:
    def __init__(self,data):
        self.head=data
        self.add=None

class l_list:
    def __init__(self):
        self.N1=None
        
    def p_rint(self):
        temp = self.N1
        while temp:
            print(temp.head)
            temp=temp.add
node1=l_list
node1.N1=node(4)
node2=node(8)
node1.N1.add=node2
node1.p_rint