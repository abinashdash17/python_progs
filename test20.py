def bsa(arr,n,s,e):
    mp = int((s+e)/2)
    if n == arr[mp]:
        return mp
    elif n < arr[mp]:
        if mp-1 < s :
            return "not found"
        else :
            return bsa(arr,n,s,mp-1)
    else :
        if mp+1 > e :
            return "not found"
        else :
            return bsa(arr,n,mp+1,e)

x = [i for i in range(0,100,5)]
n = 95
print(bsa(x,n,0,len(x)-1))
