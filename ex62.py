def recur(m):
    if m == 1:
        return 1/2
    else :
        return (m/m+1) + recur(m-1)
x = input("enter a number: ")
n = int(x)
print(recur(n))
