x = input("enter a number: ")
n = int(x)
def recur(m):
    if m == 1:
        return 1/2
    else :
        return (m/m+1) + recur(m-1)
