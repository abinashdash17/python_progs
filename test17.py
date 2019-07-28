def checkSize(s,e):
    if s == e :
        if n == arr[s]:
            return s
        else :
            return "not found"
    else :
        if (e-s) % 2 == 0:
            return sizeOdd(checkSize,s,e)
        else :
            return sizeEven(checkSize,s,e)
def sizeEven(f,s,e):
    l = (e-s)+1
    mp = (arr[s+int(l/2)-1] + arr[s+int(l/2)])/2
    if n == mp :
        return "not found"
    elif n < mp :
        return f(s,int(l/2)-1)
    else :
        return f(s+int(l/2),e)
def sizeOdd(f,s,e):
    l = e-s+1
    mp = s + int(l/2)
    if n == arr[mp]:
        return mp
    elif n < arr[mp]:
        return f(s,mp-1)
    else :
        return f(mp+1,e)

arr = [x for x in range(0,25)]
n = 8
print(checkSize(0,len(arr)-1))
