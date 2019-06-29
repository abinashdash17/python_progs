def crit1(passwd) :
    t = False
    for ch in passwd :
        if ch.isupper():
            t = True
            break
    return t
def crit2(passwd) :
    t = False
    for ch in passwd :
        if ch.isdigit():
            t = True
            break
    return t

def crit3(passwd) :
    t = False
    for ch in passwd :
        if ch.islower():
            t = True
            break
    return t
def crit4(passwd) :
    t = False
    for ch in passwd :
        if ch == '$' or ch == '@' or ch == '#':
            t = True
            break
    return t

def critLen(passwd) :
    t = False
    if len(passwd) <= 12 and len(passwd) >= 6 :
        t = True
    return t

x = input("Enter a list of pass: ")
l1=x.split(",")
res =[]
for passwd in l1:
    test = []
    test.append(crit1(passwd))
    test.append(crit2(passwd))
    test.append(crit3(passwd))
    test.append(crit4(passwd))
    test.append(critLen(passwd))
    if test[0] and test[1] and test[2] and test[3] and test[4] :
        res.append(passwd)
print(",".join(res))
