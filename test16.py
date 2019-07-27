def f2(f,arr):
    return f(arr[-len(arr):-1])
def f3(f,arr):
    return arr[0]
def f1(l):
    lL = len(l)
    if lL != 1:
        return f2(f1,l)
    else :
        return f3(f1,l)

x = [x for x in range(8,12,3)]
print(f1(x))

