D = [i for i in range(6,0,-1)]
d = [i/D[0] for i in D]
x = [1,1,1,1,1]
y = []
if D[5] < 1 :
    for i in range(0,4):
        for j in range(0,4-i):
            x[j] = (d[j] - d[4-i] * d[4-i-j-1]) / (1- d[4-i]^2)
        for j in range(0,4-i):
            d[j] = x[j]
        y.append(d[3-i]^2)
print(y)

