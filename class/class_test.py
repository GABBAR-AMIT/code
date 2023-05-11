class person:
    def __init__(self):
        self.name = "John"
        self.age = 35
        self.height = 180
        self.weight = 70
        
    def talk(self):
        print("hi i am ",self.name)
        
    def vote(self):
        if self.age<18 :
            print("i am not enegiable to vote")
        else:
            print("i am eligible to vote")

obj=person
person.talk(obj)
person.vote(obj)