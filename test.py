class mobile():
    def __init__(self, name, ram, an):
        self.name= name
    #name="oneplus"
        self.cpu="xyz"
        self.ram=ram
        self.x=an
    
m=mobile('samsung', '10gb', '12') # object or instance
n=mobile("htc", '8gb', '50')
print(n.name, n.cpu, n.ram, n.x)