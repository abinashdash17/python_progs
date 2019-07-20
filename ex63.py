def f(n):
    if n == 0 :
        return 1
    else :
        return f(n-1)+100

x = int(input("enter a number: "))
print(f(x))
