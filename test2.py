def reverse(n):
    i = 0
    while i<n:
        j=i
        if j%7==0:
            yield j
        i=i+1
for i in reverse(36):
    print(i)
