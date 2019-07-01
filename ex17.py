net_amount = 0
while (True) :
    x = input("input data")
    if (x) :
        y = x.split(" ")
        if y[0] == 'D' :
            net_amount += int(y[1])
        elif y[0] == 'W' :
            net_amount -= int(y[1])
    else :
        break
print("net amount is {}".format(net_amount))

