def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return fib(n-1) + fib(n-2)

x = int(input("enter a num: "))
l1 = []
for i in range(0,x+1):
    l1.append(str(fib(i)))

print(",".join(l1))
