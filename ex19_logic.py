print("Enter data: ")
l = []
while True :
    s = input()
    if s :
        l.append(tuple(s.split(",")))
    else :
        break
l1 = sorted(l)
print(l1)
