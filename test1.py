class abc: # base / parent class
    a = "hello"
    b = " world"
    c = a+b
        

class xyz(abc): # child class
    def ert(self):
        print("1+2",abc.c)
        
class ghj(xyz):
    def ert1(self):
        print("inside the function of 2nd child class",abc.c)
obj =ghj()

obj.ert1()