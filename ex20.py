def numgen(n) :
    i = 0
    while i <= n :
        if i % 7 == 0 :
            yield str(i)
        i += 1


x = input("Enter range :")
mynumgen = numgen(int(x))
l1 = list(mynumgen)
print(",".join(l1))
