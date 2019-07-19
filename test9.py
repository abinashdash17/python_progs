from re import findall 
str1 = "filename 445"
pat = "\w+\s\d\d*"
print(findall(pat,str1))
