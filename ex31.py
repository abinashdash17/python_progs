def eoo(a):
    if a % 2 == 0 :
        return "even"
    else :
        return "odd"

x = 6
print("{} is {}".format(x,eoo(x)))
