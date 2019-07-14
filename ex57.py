import re
x = input("Enter your email id:")
pat = "\w+"
str1 = x
res = re.findall(pat,str1)
print(res[1])
