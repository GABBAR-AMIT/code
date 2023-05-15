class person:
    def __init__(self,name,age,height,weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        
    def talk(self):
        print("hi i am ",self.name)
        
    def vote(self):
        if self.age<18 :
            print("i am not enegiable to vote")
        else:
            print("i am eligible to vote")

obj=person('john',23,5.9,50)
obj1=person('abc',25,30,50)
obj1.talk()
obj.talk()
obj.vote()
obj1.vote()
