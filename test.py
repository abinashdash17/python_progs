def gennum() :
    i = 0
    while True :
        yield i
        i += 1
x = gennum()
y = gennum()
for i in x :
    if i%3 == 0:
        next(y)
    print(x,y)
    if i == 23 :
        break

