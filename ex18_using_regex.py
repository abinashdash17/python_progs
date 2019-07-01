import re
x = input("Enter paswwords :")
res = []
for passwd in x.split(",") :
    if len(passwd) < 6 or len(passwd) > 12 :
        continue
    elif not re.search("[a-z]",passwd) :
        continue
    elif not re.search("[0-9]",passwd) :
        continue
    elif not re.search("[A-Z]",passwd) :
        continue
    elif not re.search("[$#@]",passwd) :
        continue
    elif re.search("\s",passwd) :
        continue
    res.append(passwd)
print(",".join(res))

