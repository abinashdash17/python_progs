def add (a,b):
    return int(a)+int(b)

x = input("2 integers: ")
x = x.split(",")
a = x[0]
b = x[1]
print("{} + {} = {}".format(a,b,add(a,b)))
