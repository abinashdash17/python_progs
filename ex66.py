def ev(n):
    for i in range(0,n+1):
        if i % 2 == 0:
            yield str(i)

x = int(input("Enter a number"))
ev1 = ev(x)
l1 = list(ev1)
print(",".join(l1))
