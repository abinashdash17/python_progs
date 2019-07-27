def ret(arr):
    arrLen = len(arr)
    if arrLen != 1 :
        return ret(arr[-arrLen:-1]) 
    else :
        return arr[0]

x =[ i for i in range(5,9)]
print(ret(x))
