import re
str1 = "abinashdash17@gmail.com"
pat = "[a-z]+[0-9]+"
test = re.findall(pat,str1)
print(test)
