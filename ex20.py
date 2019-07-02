def div_7(n):
    for i in range(0,n+1):
        j = i
        i+=1
        if j % 7 == 0 :
            yield j

x = input("enter a num:")
for i in div_7(int(x)):
    print(i)
