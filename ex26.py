x = input("enter 2 numbers sep by comma : ")
x = x.split(",")
res = lambda a,b : a+b
print("sum of {} and {} is {}".format(int(x[0]),int(x[1]),res(int(x[0]),int(x[1]))))
