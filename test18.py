import re
x = input()
str1 = x
pat = "^test1\d*"
res = re.findall(pat,str1)
print(res)
