from re import findall 
str1 = "abinash"
str2 = "ayush"
pat = "a+(yu|bina)(sh)+"
print(findall(pat,str1))
print(findall(pat,str2))
