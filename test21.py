x = input()
s = []
for i in range(0,int(x)):
    y= input()
    s.append(y)

for i in range(0,int(x)):
    str1 = s[i]
    for j in range(0,len(str1)):
        if j%2 == 0:
            print(str1[j],end='')
    print(' ',end='')
    for j in range(0,len(str1)):
        if j%2 != 0:
            print(str1[j],end='')
    print()
