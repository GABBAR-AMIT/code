class tree():
    def __init__(self,data):
        self.left = None
        self.right=None
        self.data = data
        
    def printree(self):
        print(self.data) 
        
node=tree(10)
node.printree()
