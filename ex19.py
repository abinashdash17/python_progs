from operator import itemgetter,attrgetter
l = []
while (True): 
    s = input("Enter data: ")
    if (s) :
        l.append(tuple(s.split(',')))
    else :
        break
res = sorted(l,key=itemgetter(0,1,2))
print(res)

