from math import sqrt
x = input("enter comma sep numbers")
C = 50
H = 30
D = x.split(',')
for d in D:
    q = sqrt(2*C*int(d)/H)
    print(int(q),end=',')
