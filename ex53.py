class Shape:
    def __init__(self):
        pass
    def calcArea(self):
        return 0
class Square(Shape):
    def __init__(self,l):
        Shape.__init__(self)
        self.l = l
    def calcArea(self):
        return self.l ** 2 

r1 = Square(8)
print(r1.calcArea())
