def f(x):
    if x == 0:
        print(0)
    else:
        print(x)
        f(x-1)

f(6)
