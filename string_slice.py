x = int(input())
s = [ ]
for i in range(x):
    str1 = input()
    s.append(str1)
for j in s:
    for k in range(len(j)):
        if k%2 == 0:
            print(j[k],end='')
    print(' ',end='')
    for k in range(len(j)):
        if k%2 == 1:
            print(j[k],end='')
    print()
