class Dog():
    def __init__(self):
        self.legs = 4
    def getName(self,str):
        self.name = str
    def printName(self):
        print("{} has {} legs.".format(self.name.upper(),self.legs))

x = input("Enter name your dog:")
dog1 = Dog()
dog1.getName(x)
dog1.printName()
