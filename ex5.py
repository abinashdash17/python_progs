class Dog():
    dog_count = 0
    def __init__(self):
        self.legs = 4
        Dog.dog_count = Dog.dog_count + 1
    def getName(self,str):
        self.name = str
    def printName(self):
        print("{} has {} legs.".format(self.name.upper(),self.legs))

x = input("Enter name your dog:")
dog1 = Dog()
dog1.getName(x)
dog1.printName()

x = input("Enter name your dog:")
dog2 = Dog()
dog2.getName(x)
dog2.printName()
print(Dog.dog_count)
