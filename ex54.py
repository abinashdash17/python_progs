def div(a,b):
    return int(a)/int(b)

try:
    print(div())
except ZeroDivisionError :
    print("division by zero")
except Exception :
    print("caught an exception")
finally :
    print("Some unknown error")
