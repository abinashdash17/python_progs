x = input("Enter series of words")
lst = x.split(" ")
l2 = list(set(lst))
l2.sort()
print(" ".join(l2))