def swap(a,b):
    return [b,a]
n  = int(input())
x  = input().split(' ')
x  = [int(i) for i in x]
num_swaps = 0

print(x)
for i in range(n-1):
    for j in range(0,n-1-i):
        if x[j] > x[j+1]:
            x[j],x[j+1] = x[j+1],x[j]
            num_swaps+=1

print(x)
print(num_swaps)
