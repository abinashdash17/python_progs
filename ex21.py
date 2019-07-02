from math import sqrt
pos={ 'x' : 0 , 'y' : 0}
while True :
    s = input("Enter movement details: ")
    if not s :
        break
    tup = tuple(s.split(" "))
    if tup[0] == 'UP' :
        pos['y'] = pos['y'] + int(tup[1])
    elif tup[0] == 'DOWN' :
        pos['y'] = pos['y'] - int(tup[1])
    elif tup[0] == 'LEFT' :
        pos['x'] = pos['x'] - int(tup[1])
    elif tup[0] == 'RIGHT' :
        pos['x'] = pos['x'] + int(tup[1])


dis =sqrt(pos['x']**2 + pos['y']**2)
print(round(dis))
