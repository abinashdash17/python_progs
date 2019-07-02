def gene(x):
    i = 0
    while i<x+1 :
        j = i
        i+=1
        yield str(j)
x = gene(5)
print(type(x))
print(list(x))
