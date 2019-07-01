x = input("Enter binary numbers: ")
res = []
for i in x.split(",") :
    num = int(i,2)
    if num % 5 ==0 :
        res.append(i)
print(",".join(res))
