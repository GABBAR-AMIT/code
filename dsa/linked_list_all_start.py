class node:
    def __init__(self,data):
        self.data = data
        self.next=None
        
    def __repr__(self):
        return self.head
    
class linkedlist:
    def __init__(self):
        self.head=None
        
    def __repr__(self):
        node=self.head
        nodes=[]
        while node is not None:
            nodes.append(node.data)
            node=node.next
        nodes.append("None")
        return "->".join(nodes)
        
    def __iter__(self):
        node=self.head
        while node is not None:
            yield node
            node=node.next
            
    def add(self,node):
        node.next=self.head
        self.head=node
        
    def add_last(self,node):
        if self.head is None:
            self.head=node
            return
        for current_node in self:
            pass
        current_node.next=node
        
llist = linkedlist()
print(llist)
llist.add(node("A"))
llist.add_last(node("Z"))
print(llist)
