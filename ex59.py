import re
x = input("Enter words: ")
str1 = x
pat = "\d"
res = re.findall(pat,str1)
print(res)
