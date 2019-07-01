x = input("enter some numbers:")
l1 = x.split(",")
l2 = [int(i) for i in l1]
l3 = [ str(j*j) for j in l2 if j % 2!= 0]
print(",".join(l3))
