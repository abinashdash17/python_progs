def facto(x):
    if ( x == 1):
        return x
    else :
        return x * facto(x-1)
x = input("Enter a value:")
x = int(x)
print("factorial is",facto(x))
