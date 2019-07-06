x = input("Enter two num: ")
x = x.split(",")
l = int(x[0])
u = int(x[1])
li = [ i for i in range(l,u+1)]
fi = filter(lambda i : i%2==0,li)
mapped = map(lambda i : i* i,fi)
print(list(mapped))
