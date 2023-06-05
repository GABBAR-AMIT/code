class node:#tree node with three data(left,data,right)
    def __init__(self,data):
        self.left=None
        self.right=None
        self.data=data
        
    def show(self):#print function
        if self.left:
            self.left.show()
        print(self.data)
        if self.right:
            self.right.show()
        
root=node(1000)
r_left=node(99)
r_right=node(101)
root.left=r_left
root.right=r_right
root.show()