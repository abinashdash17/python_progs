x = [i for i in range(0,10,2)]
x.append(5)
for i in x:
    assert i%2 == 0
