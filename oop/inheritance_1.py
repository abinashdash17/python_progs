class Animal:
    def __init__(self,leg):
        self.leg = leg
    def intro(self):
        print(f'I have {self.leg} legs.')
class Dog(Animal):
    def __init__(self,name):
        Animal.__init__(self,4)
        self.name = name
    def make_sound(self):
        print(f'{self.name} says I have {self.leg} legs.')

dog = Animal(4)
human = Animal(2)
dog.intro()
human.intro()
dog1 = Dog('Jacky')
dog1.make_sound()
dog1.intro()