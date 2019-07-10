class Rect:
    def __init__(self,l,b):
        self.l = l
        self.b = b
    def area(self):
        return self.l * self.b

x = input("Enter length and breadth: ")
x = x.split(",")
a = x[0]
b = x[1]
r1 = Rect(int(a),int(b))
print("Area of rectangle is {}".format(r1.area()))
