import re
pat = 'ma*n'
for str1 in ['abc','bcd','dab','maan']:
    if re.match(pat,str1):
        print(str1)
