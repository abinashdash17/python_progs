import re
str1 = "abinashdash17@gmail.com"
pat = "\w+"
test = re.findall(pat,str1)
print(test)
