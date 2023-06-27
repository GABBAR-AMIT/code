class stack:
    def __init__(self):
        self.stack=[]
        
    def push(self,item):
        self.stack.append(item)
        
    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        else:
            print("Stack is empty")
            
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            print("Stack is Empty!")
            
    def is_empty(self):
        return len(self.stack)==0
    
    def size(self):
        return len(self.stack)
    
stack=stack()
stack.push(1)
stack.push(2)
