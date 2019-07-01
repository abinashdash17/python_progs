x = input("Enter 2 nums:")
x_list = x.split(",")
y = []
for i in x_list:
    y.append(int(i))

arr = []
for i in range(0,y[0] ):
    temp =[]
    for j in range(0,y[1] ):
        temp.append(i*j) 
    arr.append(temp)
#l1 = [[j*i for j in range(0,y[1])] for i in range(0,y[0])]## one liner to achieve the same result
print(arr)
#print(l1)
