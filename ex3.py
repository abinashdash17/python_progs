x = input('Enter the upper limit of square')
x = int(x)
sqr_dict = {}
for i in range(1,x+1):
    sqr_dict[i] = i*i
print(sqr_dict)
