# generic node class 
class node:
    def __init__(self,datavalue):# datavalue that is storing in the node.
        self.head = datavalue
        self.next = None

class l_list:
    def __init__(self) -> None:
        self.n1=None
    
    def print_l(self):#
        temp = self.n1
        while temp:
            print(temp.head)
            temp=temp.next
            
o1 = l_list()
o1.n1= node(4)
o2 = node(5)
o1.n1.next=o2 # we are linking the node1(o1.n1) to node 2 (o2)
o3 = node(8)
o2.next=o3

o1.print_l()