hg= []
for i in range(6):
    hg.append([1 for x in range(6)])
x = hg
x[0][0] = 2
a = []
for i in range(1,5):
    for j in range(1,5):
        sum = 0
        l = x[i-1][j-1:j+2]
        m = [0,x[i][j],0]
        n = x[i+1][j-1:j+2]
        whole = [l,m,n]
        for arr in whole:
            for y in arr:
                sum+=y
        a.append(sum)
max_loc = 0
max_val = a[0]
for (index,num) in enumerate(a):
    if num >= max_val:
        max_loc = index
r = 1+int(max_loc/4)
c = 1+(max_loc%4)
ans = [x[r-1][c-1:c+2],x[r][c-1:c+2],x[r+1][c-1:c+2]]

for (indr,arr) in enumerate(ans):
    for (indc,i) in enumerate(arr):
        if indr == 1 and (indc == 0 or indc == 2):
            print(' ',end=' ')
        else:
            print(i,end=' ')
    print()
