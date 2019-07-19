from re import findall

str1 = "regex"
pat = "r(\w)g\\1x"
print(findall(pat,str1))
