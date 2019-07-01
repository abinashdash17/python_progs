x = input("Enter a sentence")
data = { "UPPER" : 0 , "LOWER" : 0 }
for ch in x :
    if ch.isupper() :
        data["UPPER"]+=1
    elif ch.islower() :
        data["LOWER"]+=1
print(data)
