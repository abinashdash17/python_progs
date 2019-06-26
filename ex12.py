def is_even_dig(a):
    if int(a) % 2 == 0 :
        return True
    else :
        return False

res = []
for i in range(1000,3000 + 1):
    str1 = str(i)
    var = True
    for j in str1 :
        if (is_even_dig(j) == False):
                var = False
                break
    if (var):
        res.append(str1)
print(','.join(res))


