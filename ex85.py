x = [i for i in range(101)]
y = [j for (i,j) in enumerate(x) if i % 2 ==0]
print(y)
