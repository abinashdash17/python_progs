def single(arr,n):
    if arr[0] == n:
        return "Found"
    else :
        return "not found"
def more(f,arr):
    arrLen = len(arr)
def bsa(arr,n):
    length = len(arr)
    if length != 1:
        return more(bsa,arr)
    else :
        return single(arr,n)
    
x = input("Enter a num: ")
l1 = [i for i in range(0,30,3)]
print(bsa([5],6))
