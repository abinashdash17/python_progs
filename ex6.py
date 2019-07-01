from math import sqrt
x = input("enter comma sep numbers")
C = 50
H = 30
D = x.split(',')
result=[]
for d in D:
    q = sqrt(2*C*int(d)/H)
    result.append(str(int(q)))
print(','.join(result))

