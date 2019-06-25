x = input("Enter 2 nums:")
x_list = x.split(",")
y = []
for i in x_list:
    y.append(int(i))

arr = []
for i in range(0,y[0] ):
    for j in range(0,y[1] ):
        arr[i][j] = i*j

print(arr)
