x  = int(input())
y = bin(x)
max_num = 1
for i in range(len(y),1,-1):
    if y.find(i*'1') != -1:
        max_num = i

print(max_num)
