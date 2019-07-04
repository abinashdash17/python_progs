x = [ i for i in range(1,11) ]
tup_x = tuple(x)
li = []
for i in tup_x :
    if i % 2 == 0 :
        li.append(i)

res = tuple(li)
print(res)
