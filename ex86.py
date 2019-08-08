x = [i for i in range(101)]
y = [j for (i,j) in enumerate(x) if i in [k for k in range(101) if k%5==0]]
print(y)
