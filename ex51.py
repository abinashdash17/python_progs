class circ:
    def __init__(self,r):
        self.rad = r
    def area(self):
        ar = 2 * 3.1415926535 * self.rad
        return ar

c = circ(5)
print("Area is {}".format(c.area()))
