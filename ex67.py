def div_57(n):
    for i in range(0,n+1):
        if i % 35 == 0:
            yield str(i)

x = int(input("Enter a num: "))
l1 = list(div_57(x))
print(",".join(l1))
